"""
Teste ponta a ponta: 1 lead fake -> LLM(Ollama) qualifica -> bridge WhatsApp envia.
O numero do "cliente" (namorada) vem de TEST_LEAD_TEL no .env (formato 5511999999999).
O bridge deve estar rodando em WHATSAPP_BRIDGE_URL e o QR escaneado.
"""
import os
from dotenv import load_dotenv
load_dotenv()

from src.config import Config
from src.db import Database, Lead, LeadStatus
from src.scanner_factory import build_pipeline
from src.scraper import DryRunLeadSource, RawLead


def main():
    cfg = Config.load("config.yaml")
    db = Database(cfg.db_url)
    db.init()
    pipe = build_pipeline(cfg, db)

    tel = os.environ.get("TEST_LEAD_TEL", "")
    lid_contact = os.environ.get("TEST_LEAD_LID", "")  # ex: 105223007813876@lid
    if not tel:
        print("ERRO: defina TEST_LEAD_TEL no .env (ex: 5511999999999)")
        return

    # 1 lead fake determinístico
    # contato_tel usa o LID real (visto no bridge) para o mapeamento inbound funcionar
    contact_tel = lid_contact or f"+{tel}"
    raw = RawLead(
        empresa="Clinica Teste Namorada", contato_nome="Namorada",
        contato_tel=contact_tel, segmento="clinicas", site=None,
        rede_social=None, source="teste",
    )
    # salva lead
    with db.session() as s:
        l = Lead(empresa=raw.empresa, contato_nome=raw.contato_nome,
                 contato_tel=contact_tel, segmento=raw.segmento,
                 status=LeadStatus.NAO_CONTATADO)
        s.add(l); s.commit(); lid = l.id

    print(f"[teste] lead {lid} criado: {raw.empresa} {raw.contato_tel}")

    # qualifica com LLM
    enr = pipe["scorer"].enrich(raw)
    print(f"[teste] score={enr.score} dor={enr.dor_estimada}")

    # envia via bridge
    res = pipe["sender"].send_first_contact(db.session().__enter__().get(Lead, lid), enr)
    print(f"[teste] enviado={res.sent} dry={res.dry_run}")
    print(f"[teste] mensagem: {res.message}")
    print("\nAguarde a mensagem no WhatsApp. Responda como cliente (ex: 'sim, quero').")
    print("O bridge encaminha ao ingest e o agente manda o link de agendamento.")


if __name__ == "__main__":
    main()
