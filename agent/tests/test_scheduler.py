from datetime import datetime, timezone, timedelta

from src.db import Database, Lead, LeadStatus
from src.scheduler import (
    FakeCalendarBackend, Scheduler, default_slots,
)


def test_default_slots_three():
    slots = default_slots(datetime(2026, 9, 1, tzinfo=timezone.utc))
    assert len(slots) == 3
    assert slots[0].start.hour == 10


def test_schedule_creates_event(tmp_path):
    db = Database(f"sqlite:///{tmp_path / 'c.db'}")
    db.init()
    with db.session() as s:
        l = Lead(empresa="Clinica C", contato_tel="+55 41 90000-2222")
        s.add(l)
        s.commit()
        lid = l.id
    sched = Scheduler(db, FakeCalendarBackend())
    slot = default_slots(datetime(2026, 9, 1, tzinfo=timezone.utc))[0]
    ev = sched.schedule(lid, slot)
    assert ev is not None
    assert ev.google_event_id.startswith("fake_event_")
    with db.session() as s:
        l = s.get(Lead, lid)
        assert l.status == LeadStatus.AGENDOU
        assert "agendado" in l.consent_log


def test_schedule_respects_opt_out(tmp_path):
    db = Database(f"sqlite:///{tmp_path / 'co.db'}")
    db.init()
    with db.session() as s:
        l = Lead(empresa="Clinica O", contato_tel="+55 41 90000-3333", opt_out=True)
        s.add(l)
        s.commit()
        lid = l.id
    ev = Scheduler(db, FakeCalendarBackend())\
        .schedule(lid, default_slots(datetime(2026, 9, 1, tzinfo=timezone.utc))[0])
    assert ev is None
