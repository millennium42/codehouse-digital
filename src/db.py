"""Camada de persistência PostgreSQL (SQLAlchemy).

Estado de leads / mensagens / eventos. Append-only em mensagens e consent_log.
Sem PII em logs (mascarar ao logar). Trata lead como dado pessoal (LGPD).
"""
from __future__ import annotations

import re
from datetime import datetime, timezone
from enum import Enum
from typing import Optional

from sqlalchemy import (
    DateTime, Enum as SQLEnum, ForeignKey, Integer, String, Text, create_engine,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker


class LeadStatus(str, Enum):
    NAO_CONTATADO = "nao_contatado"
    CONTATADO = "contatado"
    RESPONDEU = "respondeu"
    AGENDOU = "agendou"
    DESCARTADO = "descartado"


def _now() -> datetime:
    return datetime.now(timezone.utc)


def mask_pii(value: Optional[str]) -> str:
    """Mascara telefone/nome para logs (LGPD: zero PII em log)."""
    if not value:
        return ""
    v = value.strip()
    if re.fullmatch(r"\+?\d[\d\s()-]{6,}", v):
        prefix = "" if not v.startswith("+") else "+"
        digits = re.sub(r"\D", "", v)
        if len(digits) >= 4:
            return f"{prefix}{digits[:1]}***{digits[-2:]}"
    if " " in v:
        parts = v.split(" ")
        if len(parts) > 1:
            return f"{parts[0][:1]}***"
    if len(v) > 2:
        return f"{v[:1]}***"
    return "***"


class Base(DeclarativeBase):
    pass


class Lead(Base):
    __tablename__ = "leads"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    empresa: Mapped[str] = mapped_column(String(200), nullable=False)
    cnpj: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    contato_nome: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    contato_tel: Mapped[Optional[str]] = mapped_column(String(40), nullable=True)
    segmento: Mapped[Optional[str]] = mapped_column(String(80), nullable=True)
    rede_social: Mapped[Optional[str]] = mapped_column(String(300), nullable=True)
    site: Mapped[Optional[str]] = mapped_column(String(300), nullable=True)
    tem_sistema: Mapped[Optional[bool]] = mapped_column(nullable=True)
    dor_estimada: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    score: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    motivo: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    status: Mapped[LeadStatus] = mapped_column(
        SQLEnum(LeadStatus), default=LeadStatus.NAO_CONTATADO, nullable=False
    )
    opt_out: Mapped[bool] = mapped_column(default=False, nullable=False)
    consent_log: Mapped[str] = mapped_column(Text, default="", nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=_now)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=_now, onupdate=_now
    )

    messages: Mapped[list["Message"]] = relationship(
        back_populates="lead", cascade="all, delete-orphan"
    )
    events: Mapped[list["Event"]] = relationship(
        back_populates="lead", cascade="all, delete-orphan"
    )

    def append_consent(self, entry: str) -> None:
        ts = _now().isoformat()
        self.consent_log = (self.consent_log + f"\n[{ts}] {entry}").strip()

    def log_line(self) -> str:
        """Linha segura para log (sem PII)."""
        return (
            f"Lead(id={self.id}, empresa={self.empresa}, seg={self.segmento}, "
            f"status={self.status.value}, score={self.score}, "
            f"tel={mask_pii(self.contato_tel)})"
        )


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    lead_id: Mapped[int] = mapped_column(ForeignKey("leads.id"), nullable=False)
    direcao: Mapped[str] = mapped_column(String(4), nullable=False)  # out/in
    conteudo: Mapped[str] = mapped_column(Text, nullable=False)
    canal: Mapped[str] = mapped_column(String(20), default="whatsapp", nullable=False)
    tipo: Mapped[str] = mapped_column(String(30), default="abordagem", nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=_now)

    lead: Mapped[Lead] = relationship(back_populates="messages")


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    lead_id: Mapped[int] = mapped_column(ForeignKey("leads.id"), nullable=False)
    google_event_id: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    start: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    end: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    lead: Mapped[Lead] = relationship(back_populates="events")


class Database:
    def __init__(self, url: str) -> None:
        self.engine = create_engine(url, future=True)
        self._session_factory = sessionmaker(bind=self.engine, expire_on_commit=False)

    def init(self) -> None:
        Base.metadata.create_all(self.engine)

    def reset(self) -> None:
        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)

    def session(self):
        return self._session_factory()
