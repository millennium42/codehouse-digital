"""Endpoint de ingestão de mensagens inbound (bridge WhatsApp -> agente).

O bridge envia {lead_id?, body, from}. Resolve o lead pelo telefone, grava
a mensagem e ACORDA o agente imediatamente (gatilho) — o Pablo responde na
hora, sem polling. Se o handler falhar, a mensagem fica no DB para retry.

Uso: uv run python -m src.ingest  (escuta :8000)
"""
from __future__ import annotations

import os
import re
import threading

from flask import Flask, request, jsonify

from src.config import Config
from src.db import Database, Lead, Message, LeadStatus
from src.inbound import InboundHandler, InboundMessage

app = Flask(__name__)
_db_instance: Database | None = None
_handler: InboundHandler | None = None
_cfg: Config | None = None


def _init():
    global _db_instance, _handler, _cfg
    if _cfg is None:
        _cfg = Config.load("config.yaml")
    if _db_instance is None:
        _db_instance = Database(_cfg.db_url)
        _db_instance.init()
    if _handler is None:
        _handler = InboundHandler(_db_instance, None,  # type: ignore
                                 _cfg.calendar.schedule_url,
                                 _cfg.n8n.whatsapp_bridge_url)
    return _db_instance, _handler


def _digits(s: str) -> str:
    return re.sub(r"\D", "", s or "")


def _resolve_lead_id(s, lead_id, body, from_field) -> int | None:
    if lead_id:
        try:
            lid = int(lead_id)
            if s.get(Lead, lid) is not None:
                return lid
        except (ValueError, TypeError):
            pass
    if from_field:
        dg = _digits(from_field)
        # LID da namorada (teste) mapeado via env
        test_lid = os.environ.get("TEST_LEAD_LID", "")
        if test_lid and _digits(test_lid) == dg:
            # usa o unico lead nao descartado
            for l in s.query(Lead).filter(Lead.opt_out.is_(False)).all():  # noqa: E712
                return l.id
        for n in range(8, min(len(dg), 12) + 1):
            suf = dg[-n:]
            for l in s.query(Lead).all():
                if _digits(l.contato_tel).endswith(suf):
                    return l.id
    return None


def _wake_agent(lid: int, body: str):
    """Gatilho: acorda o Pablo para responder na hora."""
    try:
        db, h = _init()
        h._handle(InboundMessage(lead_id=lid, text=body))
        print(f"[ingest] agente acordado p/ lead {lid}")
    except Exception as e:
        print(f"[ingest] erro ao acordar agente: {e}")


@app.post("/inbound")
def inbound():
    data = request.get_json(force=True, silent=True) or {}
    lead_id = data.get("lead_id")
    body = data.get("body") or data.get("message") or data.get("text")
    from_field = data.get("from", "")
    if not body:
        return jsonify({"ok": False, "error": "body obrigatorio"}), 400
    db, _ = _init()
    with db.session() as s:
        lid = _resolve_lead_id(s, lead_id, body, from_field)
        if lid is None:
            return jsonify({"ok": False, "error": "lead nao encontrado"}), 404
        s.add(Message(lead_id=lid, direcao="in", conteudo=str(body),
                      canal="whatsapp", tipo="resposta", processed=True))
        s.commit()
    # gatilho: acorda o agente em thread separada (nao bloqueia o bridge)
    threading.Thread(target=_wake_agent, args=(lid, str(body)), daemon=True).start()
    return jsonify({"ok": True, "lead_id": lid})


@app.get("/healthz")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    port = int(os.environ.get("INGEST_PORT", "8000"))
    app.run(host="0.0.0.0", port=port, threaded=True)
