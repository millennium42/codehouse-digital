"""Endpoint de ingestão de mensagens inbound (bridge WhatsApp -> agente).

O bridge envia {lead_id?, body, from}. Se lead_id nao existir no DB,
resolve pelo telefone (ultimos digitos de `from` casam com contato_tel).
Grava na tabela `messages` (append-only, processed=false).
O orquestrador faz poll desta tabela.

Uso: uv run python -m src.ingest  (escuta :8000)
"""
from __future__ import annotations

import os
import re

from flask import Flask, request, jsonify

from src.config import Config
from src.db import Database, Lead, Message

app = Flask(__name__)
_db_instance: Database | None = None


def _db() -> Database:
    global _db_instance
    if _db_instance is None:
        cfg = Config.load("config.yaml")
        _db_instance = Database(cfg.db_url)
        _db_instance.init()
    return _db_instance


def _digits(s: str) -> str:
    return re.sub(r"\D", "", s or "")


def _resolve_lead_id(s, lead_id, body, from_field) -> int | None:
    # 1) lead_id explicito e existente
    if lead_id:
        try:
            lid = int(lead_id)
            if s.get(Lead, lid) is not None:
                return lid
        except (ValueError, TypeError):
            pass
    # 2) resolver pelo telefone (ultimos 8-11 digitos de `from`)
    if from_field:
        dg = _digits(from_field)
        # tenta sufixos de 8 a 11 digitos
        for n in range(8, min(len(dg), 12) + 1):
            suf = dg[-n:]
            for l in s.query(Lead).all():
                if _digits(l.contato_tel).endswith(suf):
                    return l.id
    return None


@app.post("/inbound")
def inbound():
    data = request.get_json(force=True, silent=True) or {}
    lead_id = data.get("lead_id")
    body = data.get("body") or data.get("message") or data.get("text")
    from_field = data.get("from", "")
    if not body:
        return jsonify({"ok": False, "error": "body obrigatorio"}), 400
    db = _db()
    with db.session() as s:
        lid = _resolve_lead_id(s, lead_id, body, from_field)
        if lid is None:
            return jsonify({"ok": False, "error": "lead nao encontrado"}), 404
        s.add(Message(lead_id=lid, direcao="in", conteudo=str(body),
                      canal="whatsapp", tipo="resposta", processed=False))
        s.commit()
    return jsonify({"ok": True, "lead_id": lid})


@app.get("/healthz")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    port = int(os.environ.get("INGEST_PORT", "8000"))
    app.run(host="0.0.0.0", port=port)
