"""Fábrica de pipeline por config (ponytail): escolhe fonte real ou fake.

Em dry_run: DryRunLeadSource + FakeScorer + FakeMessageWriter + FakeCalendar.
Em produção: Apify + LLM + webhook n8n + Google Calendar (não implementados no MVP).
"""
from __future__ import annotations

from src.config import Config
from src.db import Database
from src.inbound import FakeInboundSource, InboundHandler
from src.scraper import ApifyLeadSource, DryRunLeadSource
from src.scorer import FakeScorer, LLMScorer
from src.sender import FakeMessageWriter, LLMMessageWriter, Sender
from src.scheduler import FakeCalendarBackend, GoogleCalendarBackend, Scheduler


def build_pipeline(cfg: Config, db: Database) -> dict:
    if cfg.dry_run:
        source = DryRunLeadSource()
        scorer = FakeScorer()
        writer = FakeMessageWriter()
        backend = FakeCalendarBackend()
    else:
        source = ApifyLeadSource(token=cfg.apify.token, dry_run=False)
        scorer = LLMScorer(cfg.llm.base_url, cfg.llm.api_key, cfg.llm.model,
                           dry_run=False)
        writer = LLMMessageWriter(cfg.llm.base_url, cfg.llm.api_key, cfg.llm.model,
                                  dry_run=False)
        backend = GoogleCalendarBackend(cfg.calendar.token, cfg.calendar.calendar_id,
                                         dry_run=False)

    return {
        "source": source,
        "scorer": scorer,
        "sender": Sender(db, writer, cfg.n8n.outbound_webhook, cfg.dry_run),
        "scheduler": Scheduler(db, backend, cfg.calendar.schedule_url),
        "inbound": InboundHandler(db, FakeInboundSource(), cfg.calendar.schedule_url),
    }
