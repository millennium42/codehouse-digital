"""Agendamento de reunião/demo via Google Calendar (scheduler).

R5: ao aceite de horário, cria evento e envia invite. Em dry_run cria evento
fake (sem rede). Persiste Event no DB e marca lead AGENDOU. Recusa se opt_out.
"""
from __future__ import annotations

import abc
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

from src.db import Database, Event, Lead, LeadStatus


@dataclass
class Slot:
    start: datetime
    end: datetime


class CalendarBackend(abc.ABC):
    @abc.abstractmethod
    def create(self, lead: Lead, slot: Slot) -> str:
        """Retorna google_event_id."""


class FakeCalendarBackend(CalendarBackend):
    def __init__(self) -> None:
        self._n = 0

    def create(self, lead: Lead, slot: Slot) -> str:
        self._n += 1
        return f"fake_event_{self._n}"


class GoogleCalendarBackend(CalendarBackend):
    def __init__(self, token: str = "", calendar_id: str = "primary",
                 dry_run: bool = True) -> None:
        self.token = token
        self.calendar_id = calendar_id
        self.dry_run = dry_run

    def create(self, lead: Lead, slot: Slot) -> str:
        if self.dry_run or not self.token:
            raise RuntimeError("GoogleCalendarBackend requer token e dry_run=false.")
        raise NotImplementedError("chamada Google Calendar API isolada")


def default_slots(base: datetime | None = None) -> list[Slot]:
    base = base or datetime.now(timezone.utc) + timedelta(days=1)
    base = base.replace(hour=10, minute=0, second=0, microsecond=0)
    return [
        Slot(base, base + timedelta(minutes=30)),
        Slot(base.replace(hour=14), base.replace(hour=14) + timedelta(minutes=30)),
        Slot(base.replace(hour=16), base.replace(hour=16) + timedelta(minutes=30)),
    ]


class Scheduler:
    def __init__(self, db: Database, backend: CalendarBackend) -> None:
        self.db = db
        self.backend = backend

    def schedule(self, lead_id: int, slot: Slot) -> Event | None:
        with self.db.session() as s:
            lead = s.get(Lead, lead_id)
            if lead is None or lead.opt_out:
                return None
            event_id = self.backend.create(lead, slot)
            lead.status = LeadStatus.AGENDOU
            lead.append_consent(f"evento agendado {event_id}")
            ev = Event(lead_id=lead.id, google_event_id=event_id,
                       start=slot.start, end=slot.end)
            s.add(ev)
            s.commit()
            return ev
