"""
Prospecção real com loop contínuo:
1. Apify descobre 1 empresa qualificada (Google Maps)
2. Salva dados da empresa, mas contato_tel = WhatsApp da namorada (TEST_LEAD_TEL/LID)
3. LLM (Ollama) qualifica + redige 1o contato
4. Envia via bridge WhatsApp
5. Loop: a cada INTERVAL s, poll inbound e conduz (classifica -> link ou opt-out)

Uso: uv run python prospect.py
Env: APIFY_TOKEN, TEST_LEAD_TEL (5515991224498), TEST_LEAD_LID (opcional)
"""
import os
import time
from dotenv import load_dotenv
load_dotenv()

from src.config import Config
from src.db import Database, Lead, LeadStatus, Message, Event
from src.scraper import ApifyLeadSource
from src.scorer import LLMScorer
from src.sender import Sender
from src.scheduler import FakeCalendarBackend, Scheduler
from src.inbound import InboundHandler, DBInboundSource, classify_intent

INTERVAL = int(os.environ.get("PROSPECT_INTERVAL", "30"))


def discover_one(cfg, db):
    """Busca 1 empresa via Apify e salva com o telefone da namorada."""
    src = ApifyLeadSource(token=cfg.apify.token, dry_run=False)
    leads = src.discover(cfg.prospecting.segment, cfg.prospecting.city, 5)
    # pega a primeira valida
    raw = next((l for l in leads if l.is_valid()), None)
    if not raw:
        print("[prospect] nenhuma empresa valida encontrada")
        return None
    tel = os.environ.get("TEST_LEAD_TEL", "")
    if not tel:
        print("[prospect] defina TEST_LEAD_TEL (ex: 5555991224498)")
        return None
    # usa o telefone REAL da namorada como contato (bridge resolve LID no inbound)
    contact_tel = f"+{tel}"
    with db.session() as s:
        l = Lead(empresa=raw.empresa, contato_nome=raw.contato_nome or "Responsavel",
                 contato_tel=contact_tel, segmento=raw.segmento, site=raw.site,
                 rede_social=raw.rede_social, cnpj=raw.cnpj,
                 status=LeadStatus.NAO_CONTATADO)
        s.add(l); s.commit(); lid = l.id
    print(f"[prospect] empresa: {raw.empresa} | tel contato: {contact_tel}")
    return raw, lid


def main():
    cfg = Config.load("config.yaml")
    db = Database(cfg.db_url)
    db.init()

    # 1) descobrir
    disc = discover_one(cfg, db)
    if not disc:
        return
    raw, lid = disc

    # 2) qualificar (LLM Ollama) + estudar dores
    scorer = LLMScorer(cfg.llm.base_url, cfg.llm.api_key, cfg.llm.model, dry_run=False)
    enr = scorer.enrich(raw)
    print(f"[prospect] score={enr.score} dor={enr.dor_estimada}")

    # 3) 1o contato: Pablo apresenta Code House + dor do lead (LLM + humanizer)
    from src.conversation import first_contact
    text = first_contact(db, db.session().__enter__().get(Lead, lid), enr,
                         cfg.llm.base_url, cfg.llm.api_key, cfg.llm.model,
                         cfg.calendar.schedule_url)
    print(f"[prospect] 1a mensagem: {text[:120]}")

    # envia via bridge
    sender = Sender(db, None, cfg.n8n.outbound_webhook, dry_run=False,
                    whatsapp_bridge_url=cfg.n8n.whatsapp_bridge_url)
    ok = Sender._send_via_bridge(cfg.n8n.whatsapp_bridge_url,
                                 db.session().__enter__().get(Lead, lid).contato_tel, text)
    # grava no DB
    with db.session() as s:
        l = s.get(Lead, lid)
        l.status = LeadStatus.CONTATADO
        l.append_consent("abordagem enviada (Pablo/Code House)")
        s.add(Message(lead_id=l.id, direcao="out", conteudo=text,
                      canal="whatsapp", tipo="abordagem"))
        s.commit()
    print(f"[prospect] 1o contato enviado={ok}")

    # 4) loop: monitorar respostas
    handler = InboundHandler(db, DBInboundSource(db), cfg.calendar.schedule_url,
                             cfg.n8n.whatsapp_bridge_url)
    print(f"[prospect] loop ativo (poll a cada {INTERVAL}s). Aguardando resposta...")
    while True:
        try:
            n = handler.process_once()
            if n:
                print(f"[prospect] {n} msg processada(s). "
                      f"Status lead {lid}: {db.session().__enter__().get(Lead, lid).status.value}")
            time.sleep(INTERVAL)
        except KeyboardInterrupt:
            print("\n[prospect] encerrado.")
            break


if __name__ == "__main__":
    main()
