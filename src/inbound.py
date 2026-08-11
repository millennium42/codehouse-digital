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
    if any(w in t for w in ["sair", "nao", "não", "pare", "descadastrar", "remove", "cancel"]):
        return "opt_out"
    if any(w in t for w in ["horario", "agenda", "reuniao", "reunião", "demo", "demonstracao", "disponivel", "link", "agendar"]):
        return "schedule"
    if any(w in t for w in ["sim", "interessa", "quero", "pode", "ok", "topo", "saber mais", "mais inform", "informacao", "informações", "detalhe", "detalhes", "como funciona"]):
        return "accept"
    return "neutral"


PROPOSAL = (
    "Ótimo! Para escolher o melhor horário para uma demonstração de 30min, "
    "use meu link de agendamento: {schedule_url}"
)


def build_proposal(schedule_url: str) -> str:
    return PROPOSAL.format(schedule_url=schedule_url or "<link de agendamento>")



class InboundHandler:
    def __init__(self, db: Database, source: InboundSource,
                 schedule_url: str = "", bridge_url: str = "") -> None:
        self.db = db
        self.source = source
        self.schedule_url = schedule_url
        self.bridge_url = bridge_url

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
                prop = build_proposal(self.schedule_url)
                s.add(Message(lead_id=lead.id, direcao="out",
                              conteudo=prop,
                              canal="whatsapp",
                              tipo="proposta_agendamento"))
                # envia a proposta via bridge WhatsApp (se configurado)
                if self.bridge_url:
                    from src.sender import Sender
                    Sender._send_via_bridge(
                        self.bridge_url,
                        Sender._phone_to_whatsapp(lead.contato_tel),
                        prop,
                    )
            s.commit()


class DBInboundSource(InboundSource):
    """Lê mensagens `in` não processadas do Postgres e marca como processadas."""

    def __init__(self, db: Database) -> None:
        self.db = db

    def poll(self) -> list[InboundMessage]:
        out: list[InboundMessage] = []
        with self.db.session() as s:
            rows = (
                s.query(Message)
                .filter(Message.direcao == "in", Message.processed == False)  # noqa: E712
                .order_by(Message.id)
                .all()
            )
            for r in rows:
                out.append(InboundMessage(lead_id=r.lead_id, text=r.conteudo))
                r.processed = True
            s.commit()
        return out
