import tempfile
from datetime import datetime, timezone

from sqlalchemy import inspect

from src.db import (
    Database, Event, Lead, LeadStatus, Message, mask_pii,
)


def _db(tmp_path):
    db = Database(f"sqlite:///{tmp_path / 't.db'}")
    db.init()
    return db


def test_init_and_tables(tmp_path):
    db = _db(tmp_path)
    with db.session() as s:
        s.add(Lead(empresa="Clinica X"))
        s.commit()
    assert inspect(db.engine).has_table("leads")


def test_mask_pii_phone():
    assert mask_pii("+55 41 99999-1234") == "+5***34"
    assert "***" in mask_pii("Joao Silva")


def test_lead_lifecycle(tmp_path):
    db = _db(tmp_path)
    with db.session() as s:
        lead = Lead(
            empresa="Clinica ABC", segmento="clinicas", contato_tel="+55 41 98888-0000",
            score=80, motivo="sem site", status=LeadStatus.NAO_CONTATADO,
        )
        s.add(lead)
        s.commit()
        lid = lead.id

    with db.session() as s:
        lead = s.get(Lead, lid)
        lead.status = LeadStatus.CONTATADO
        lead.append_consent("abordagem enviada via n8n")
        s.commit()
        assert lead.status == LeadStatus.CONTATADO
        assert "abordagem enviada" in lead.consent_log
        # log sem PII
        log = lead.log_line()
        assert "+55 41 98888-0000" not in log
        assert "***" in log


def test_append_only_messages(tmp_path):
    db = _db(tmp_path)
    with db.session() as s:
        lead = Lead(empresa="Clinica Y")
        s.add(lead)
        s.commit()
        lid = lead.id
        s.add(Message(lead_id=lid, direcao="out", conteudo="Ola", tipo="abordagem"))
        s.add(Message(lead_id=lid, direcao="in", conteudo="Interessa", tipo="resposta"))
        s.commit()
    with db.session() as s:
        lead = s.get(Lead, lid)
        assert len(lead.messages) == 2
        assert lead.messages[0].direcao == "out"


def test_event_created_on_schedule(tmp_path):
    db = _db(tmp_path)
    with db.session() as s:
        lead = Lead(empresa="Clinica Z", status=LeadStatus.AGENDOU)
        s.add(lead)
        s.commit()
        lid = lead.id
        s.add(Event(lead_id=lid, google_event_id="evt_1",
                    start=datetime(2026, 9, 1, 10, 0, tzinfo=timezone.utc),
                    end=datetime(2026, 9, 1, 10, 30, tzinfo=timezone.utc)))
        s.commit()
    with db.session() as s:
        lead = s.get(Lead, lid)
        assert lead.events[0].google_event_id == "evt_1"
