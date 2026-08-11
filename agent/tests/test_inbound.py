from src.db import Database, Lead, LeadStatus
from src.inbound import FakeInboundSource, InboundHandler, classify_intent
from src.scheduler import FakeCalendarBackend, Scheduler


def _seed(db, status=LeadStatus.CONTATADO):
    with db.session() as s:
        l = Lead(empresa="Clinica I", contato_tel="+55 41 90000-1111")
        l.status = status
        s.add(l)
        s.commit()
        return l.id


def test_classify_intent():
    assert classify_intent("sim, interessa") == "accept"
    assert classify_intent("quero horario") == "schedule"
    assert classify_intent("sair") == "opt_out"
    assert classify_intent("tudo bem, obrigado") == "neutral"


def test_inbound_accept_moves_to_agendou(tmp_path, monkeypatch):
    def fake_reply(db, lead, enr, text, *a, **k):
        return f"Combinado! LINK_AGENDA: https://calendar.google.com/XYZ"

    monkeypatch.setattr("src.conversation.reply", fake_reply)
    db = Database(f"sqlite:///{tmp_path / 'i.db'}")
    db.init()
    lid = _seed(db)
    src = FakeInboundSource({lid: ["sim, quero demo"]})
    InboundHandler(db, src, schedule_url="https://calendar.google.com/XYZ").process_once()
    with db.session() as s:
        l = s.get(Lead, lid)
        assert l.status == LeadStatus.AGENDOU
        types = [m.tipo for m in l.messages]
        assert "resposta" in types
        assert "resposta_agente" in types
        assert "https://calendar.google.com/XYZ" in l.consent_log


def test_inbound_proposal_includes_schedule_link(tmp_path, monkeypatch):
    def fake_reply(db, lead, enr, text, *a, **k):
        return f"Otimo! LINK_AGENDA: https://calendar.google.com/XYZ"

    monkeypatch.setattr("src.conversation.reply", fake_reply)
    db = Database(f"sqlite:///{tmp_path / 'p.db'}")
    db.init()
    lid = _seed(db)
    src = FakeInboundSource({lid: ["sim, quero demo"]})
    h = InboundHandler(db, src, schedule_url="https://calendar.google.com/XYZ")
    h.process_once()
    with db.session() as s:
        l = s.get(Lead, lid)
        assert l.status == LeadStatus.AGENDOU
        assert "https://calendar.google.com/XYZ" in l.consent_log


def test_scheduler_marks_link_sent(tmp_path):
    db = Database(f"sqlite:///{tmp_path / 'sl.db'}")
    db.init()
    with db.session() as s:
        l = Lead(empresa="Clinica L", contato_tel="+55 41 90000-4444")
        s.add(l); s.commit(); lid = l.id
    ev = Scheduler(db, FakeCalendarBackend(), schedule_url="https://cal/X").schedule(lid)
    assert ev is None
    with db.session() as s:
        l = s.get(Lead, lid)
        assert l.status == LeadStatus.AGENDOU
        assert "link de agendamento" in l.consent_log


def test_inbound_opt_out_blocks(tmp_path):
    db = Database(f"sqlite:///{tmp_path / 'o.db'}")
    db.init()
    lid = _seed(db)
    src = FakeInboundSource({lid: ["sair por favor"]})
    InboundHandler(db, src).process_once()
    with db.session() as s:
        l = s.get(Lead, lid)
        assert l.opt_out is True
        assert l.status == LeadStatus.DESCARTADO
        assert "opt-out" in l.consent_log

