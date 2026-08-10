"""Tratamento de respostas inbound e condução até o agendamento (inbound).

R4: agente mantém a conversa. Faz poll de respostas (via n8n → DB, ou fonte
fake em dev) e conduz: qualifica interesse, propõe horários, detecta aceite
ou opt-out. Append-only: grava Message(in). Atualiza status.

Estados de condução por lead (campo `status`):
  CONTATADO -> RESPONDEU -> (AGENDOU | DESCARTADO)
Opt-out a qualquer momento para DESCARTADO + opt_out=True.
"""
from __future__ import annotations

import abc
from dataclasses import dataclass

from src.db import Database, Lead, LeadStatus, Message


@dataclass
class InboundMessage:
    lead_id: int
    text: str


class InboundSource(abc.ABC):
    @abc.abstractmethod
    def poll(self) -> list[InboundMessage]:
        ...


class FakeInboundSource(InboundSource):
    """Fonte fake: respostas pré-definidas por lead_id (ciclo determinístico)."""

    def __init__(self, script: dict[int, list[str]] | None = None) -> None:
        self.script = script or {}
        self._idx: dict[int, int] = {}

    def poll(self) -> list[InboundMessage]:
        out: list[InboundMessage] = []
        for lid, lines in self.script.items():
            i = self._idx.get(lid, 0)
            if i < len(lines):
                out.append(InboundMessage(lead_id=lid, text=lines[i]))
                self._idx[lid] = i + 1
        return out


def classify_intent(text: str) -> str:
    t = text.strip().lower()
    if any(w in t for w in ["sair", "nao", "não", "pare", "descadastrar", "remove"]):
        return "opt_out"
    if any(w in t for w in ["horario", "agenda", "reuniao", "reunião", "demo", "demonstracao", "disponivel"]):
        return "schedule"
    if any(w in t for w in ["sim", "interessa", "quero", "pode", "ok", "topo"]):
        return "accept"
    return "neutral"


PROPOSAL = (
    "Ótimo! Sugiro 3 horários para uma demonstração de 30min: "
    "ter 10h, qua 14h ou qui 16h. Qual funciona?"
)


class InboundHandler:
    def __init__(self, db: Database, source: InboundSource) -> None:
        self.db = db
        self.source = source

    def process_once(self) -> int:
        processed = 0
        for msg in self.source.poll():
            self._handle(msg)
            processed += 1
        return processed

    def _handle(self, msg: InboundMessage) -> None:
        with self.db.session() as s:
            lead = s.get(Lead, msg.lead_id)
            if lead is None:
                return
            intent = classify_intent(msg.text)
            s.add(Message(lead_id=lead.id, direcao="in", conteudo=msg.text,
                          canal="whatsapp", tipo="resposta"))
            if intent == "opt_out":
                lead.opt_out = True
                lead.status = LeadStatus.DESCARTADO
                lead.append_consent("opt-out recebido; não contactar novamente")
                s.commit()
                return
            if lead.status == LeadStatus.CONTATADO:
                lead.status = LeadStatus.RESPONDEU
            if intent in ("accept", "schedule"):
                lead.status = LeadStatus.AGENDOU
                s.add(Message(lead_id=lead.id, direcao="out",
                              conteudo=PROPOSAL, canal="whatsapp",
                              tipo="proposta_agendamento"))
            s.commit()
