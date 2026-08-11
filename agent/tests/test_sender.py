from src.db import Database, Lead, LeadStatus
from src.scorer import Enrichment
from src.sender import FakeMessageWriter, Sender


def _make_lead(db):
    with db.session() as s:
        l = Lead(empresa="Clinica Teste", contato_nome="Maria",
                 contato_tel="+55 41 90000-9999", segmento="clinicas")
        s.add(l)
        s.commit()
        return l.id


def test_send_dry_run_no_webhook(tmp_path):
    db = Database(f"sqlite:///{tmp_path / 's.db'}")
    db.init()
    lid = _make_lead(db)
    with db.session() as s:
        lead = s.get(Lead, lid)
        enr = Enrichment(site=None, rede_social=None, tem_sistema=False,
                         dor_estimada="sem site", score=100, motivo="x")
        res = Sender(db, FakeMessageWriter(), webhook_url="", dry_run=True)\
            .send_first_contact(lead, enr)
    assert res.dry_run is True
    assert res.sent is False
    assert "CodeHouse" in res.message
    assert "sair" in res.message  # opt-out LGPD
    with db.session() as s:
        l = s.get(Lead, lid)
        assert l.status == LeadStatus.CONTATADO
        assert len(l.messages) == 1
        assert l.messages[0].direcao == "out"


def test_send_respects_opt_out(tmp_path):
    db = Database(f"sqlite:///{tmp_path / 'o.db'}")
    db.init()
    lid = _make_lead(db)
    with db.session() as s:
        l = s.get(Lead, lid)
        l.opt_out = True
        s.commit()
    with db.session() as s:
        lead = s.get(Lead, lid)
        res = Sender(db, FakeMessageWriter())\
            .send_first_contact(lead, Enrichment(None, None, False, "", 50, "x"))
    assert res.message == ""
    assert res.sent is False
