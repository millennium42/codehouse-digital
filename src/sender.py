"""Redação da abordagem e envio via webhook n8n (sender).

R3: LLM redige 1ª mensagem de abordagem (identifica empresa + via de opt-out
LGPD) e dispara via webhook n8n. Em dry_run, não envia — só redige e loga
mascarado. Append-only: grava Message(out) no DB.
"""
from __future__ import annotations

import abc
import json
import os
from dataclasses import dataclass

import requests

from src.db import Database, Lead, LeadStatus, Message
from src.scorer import Enrichment


@dataclass
class SendResult:
    message: str
    sent: bool
    dry_run: bool


class MessageWriter(abc.ABC):
    @abc.abstractmethod
    def write(self, lead: Lead, enrichment: Enrichment) -> str:
        ...


class FakeMessageWriter(MessageWriter):
    """Redação determinística em PT-BR, com opt-out LGPD embutido."""

    def write(self, lead: Lead, enrichment: Enrichment) -> str:
        nome = lead.contato_nome or "responsável"
        dor = enrichment.dor_estimada or "evoluir operação com software sob medida"
        return (
            f"Olá {nome}, sou da CodeHouse (desenvolvimento de software "
            f"personalizado). Notei que a {lead.empresa} pode se beneficiar com "
            f"{dor}. Criamos páginas, ERPs, CRMs e automação de chat sob medida. "
            f"Posso enviar uma proposta rápida? Se preferir não receber, "
            f"responda 'sair' e não contactarei novamente."
        )


class LLMMessageWriter(MessageWriter):
    def __init__(self, base_url: str = "", api_key: str = "", model: str = "",
                 dry_run: bool = True) -> None:
        self.base_url = base_url
        self.api_key = api_key
        self.model = model
        self.dry_run = dry_run

    def write(self, lead: Lead, enrichment: Enrichment) -> str:
        if self.dry_run or not self.api_key:
            raise RuntimeError("LLMMessageWriter requer api_key e dry_run=false.")
        raise NotImplementedError("chamada LLM isolada")


class Sender:
    def __init__(self, db: Database, writer: MessageWriter,
                 webhook_url: str = "", dry_run: bool = True) -> None:
        self.db = db
        self.writer = writer
        self.webhook_url = webhook_url or os.environ.get("N8N_WEBHOOK_URL", "")
        self.dry_run = dry_run
        self.meta_token = os.environ.get("WHATSAPP_TOKEN", "")
        self.meta_phone_id = os.environ.get("WHATSAPP_PHONE_ID", "")

    def send_first_contact(self, lead: Lead, enrichment: Enrichment) -> SendResult:
        if lead.opt_out:
            return SendResult("", False, self.dry_run)
        text = self.writer.write(lead, enrichment)
        sent = False
        if not self.dry_run:
            if self.webhook_url:
                requests.post(self.webhook_url, json={
                    "to": lead.contato_tel, "message": text,
                    "lead_id": lead.id,
                }, timeout=10)
                sent = True
            elif self.meta_token and self.meta_phone_id:
                # Fallback: Meta Cloud API direto (sem n8n)
                url = f"https://graph.facebook.com/v19.0/{self.meta_phone_id}/messages"
                requests.post(url, json={
                    "messaging_product": "whatsapp", "to": lead.contato_tel,
                    "type": "text", "text": {"body": text},
                }, headers={"Authorization": f"Bearer {self.meta_token}"}, timeout=10)
                sent = True
        with self.db.session() as s:
            l = s.get(Lead, lead.id)
            l.status = LeadStatus.CONTATADO
            l.append_consent(f"abordagem enviada{' (dry_run)' if self.dry_run else ''}")
            s.add(Message(lead_id=l.id, direcao="out", conteudo=text,
                          canal="whatsapp", tipo="abordagem"))
            s.commit()
            lead.status = l.status
        return SendResult(message=text, sent=sent, dry_run=self.dry_run)
