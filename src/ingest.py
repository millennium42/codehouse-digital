"""Endpoint de ingestão de mensagens inbound (n8n -> agente).

O n8n recebe o callback do Meta e faz POST aqui; este serviço grava a
mensagem na tabela `messages` do Postgres (append-only, processed=false).
O orquestrador do agente faz poll desta tabela (DBInboundSource).

Uso: uv run python -m src.ingest  (escuta :8000)
"""
from __future__ import annotations

import os

from flask import Flask, request, jsonify  # ponytail: flask leve p/ endpoint unico

from src.config import Config
from src.db import Database, Message

app = Flask(__name__)
_db_instance: Database | None = None


def _db() -> Database:
    global _db_instance
    if _db_instance is None:
        cfg = Config.load("config.yaml")
        _db_instance = Database(cfg.db_url)
        _db_instance.init()
    return _db_instance


@app.post("/inbound")
def inbound():
    data = request.get_json(force=True, silent=True) or {}
    lead_id = data.get("lead_id")
    body = data.get("body") or data.get("message") or data.get("text")
    if not lead_id or not body:
        return jsonify({"ok": False, "error": "lead_id e body obrigatórios"}), 400
    db = _db()
    with db.session() as s:
        s.add(Message(lead_id=int(lead_id), direcao="in", conteudo=str(body),
                      canal="whatsapp", tipo="resposta", processed=False))
        s.commit()
    return jsonify({"ok": True})


@app.get("/healthz")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    port = int(os.environ.get("INGEST_PORT", "8000"))
    app.run(host="0.0.0.0", port=port)
