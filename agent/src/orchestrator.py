"""Orquestrador do ciclo de prospecção (R9).

Ciclo: discover -> enrich -> qualify -> send -> poll inbound -> schedule.
Hermes chama `run_cycle()`; n8n é ponte (webhook). Em dry_run usa fontes fake
e não toca redes externas. Append-only audit por lead (R10).
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone

from src.config import Config
from src.db import Database, Lead, LeadStatus
from src.inbound import FakeInboundSource, InboundHandler
from src.scanner_factory import build_pipeline  # ponytail: monta fontes por config


@dataclass
class CycleStats:
    discovered: int = 0
    qualified: int = 0
    sent: int = 0
    replied: int = 0
    scheduled: int = 0
    discarded: int = 0

    def summary(self) -> str:
        return (
            f"descobertos={self.discovered} qualificados={self.qualified} "
            f"enviados={self.sent} responderam={self.replied} "
            f"agendados={self.scheduled} descartados={self.discarded}"
        )


class ProspectingAgent:
    def __init__(self, cfg: Config, db: Database) -> None:
        self.cfg = cfg
        self.db = db
        pipeline = build_pipeline(cfg, db)
        self.source = pipeline["source"]
        self.scorer = pipeline["scorer"]
        self.sender = pipeline["sender"]
        self.scheduler = pipeline["scheduler"]

    def run_cycle(self, inbound_script: dict[int, list[str]] | None = None) -> CycleStats:
        stats = CycleStats()
        self.db.init()

        # 1) discover
        raws = self.source.discover(
            self.cfg.prospecting.segment,
            self.cfg.prospecting.city,
            self.cfg.prospecting.limit,
        )
        stats.discovered = len(raws)
        valid_ids: list[int] = []
        with self.db.session() as s:
            for r in raws:
                if not r.is_valid():
                    continue
                lead = Lead(
                    empresa=r.empresa, cnpj=r.cnpj, contato_nome=r.contato_nome,
                    contato_tel=r.contato_tel, segmento=r.segmento,
                    rede_social=r.rede_social, site=r.site, status=LeadStatus.NAO_CONTATADO,
                )
                s.add(lead)
                s.commit()
                valid_ids.append(lead.id)

        # 2) enrich + 3) qualify + 4) send
        for lid in valid_ids:
            with self.db.session() as s:
                lead = s.get(Lead, lid)
                raw = _raw_from_lead(lead)
                enr = self.scorer.enrich(raw)
                lead.site = enr.site
                lead.rede_social = enr.rede_social
                lead.tem_sistema = enr.tem_sistema
                lead.dor_estimada = enr.dor_estimada
                lead.score = enr.score
                lead.motivo = enr.motivo
                s.commit()

                if lead.score is not None and lead.score >= self.cfg.prospecting.min_score:
                    stats.qualified += 1
                    res = self.sender.send_first_contact(lead, enr)
                    if res.message:
                        stats.sent += 1
                else:
                    lead.status = LeadStatus.DESCARTADO
                    lead.append_consent(f"score baixo ({lead.score}) descartado")
                    stats.discarded += 1
                    s.commit()

        # 5) poll inbound + 6) schedule (condução two-way)
        handler = InboundHandler(
            self.db, FakeInboundSource(inbound_script or {}),
            schedule_url=self.cfg.calendar.schedule_url,
        )
        stats.replied = handler.process_once()
        # agenda leads que aceitaram (status AGENDOU via inbound)
        from src.scheduler import default_slots
        for lid in self._accepted_leads():
            slot = default_slots(datetime(2026, 9, 1, tzinfo=timezone.utc))[0]
            ev = self.scheduler.schedule(lid, slot)
            if ev:
                stats.scheduled += 1
        return stats

    def _accepted_leads(self) -> list[int]:
        with self.db.session() as s:
            rows = s.query(Lead).filter(
                Lead.status == LeadStatus.AGENDOU,
                Lead.opt_out.is_(False),
            ).all()
            return [r.id for r in rows]


def _raw_from_lead(lead: Lead):
    from src.scraper import RawLead
    return RawLead(
        empresa=lead.empresa, contato_nome=lead.contato_nome,
        contato_tel=lead.contato_tel, segmento=lead.segmento,
        rede_social=lead.rede_social, site=lead.site, cnpj=lead.cnpj,
        source="db",
    )
