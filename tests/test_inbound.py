from src.db import Database, Lead, LeadStatus
from src.inbound import FakeInboundSource, InboundHandler, classify_intent


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


def test_inbound_accept_moves_to_agendou(tmp_path):
    db = Database(f"sqlite:///{tmp_path / 'i.db'}")
    db.init()
    lid = _seed(db)
    src = FakeInboundSource({lid: ["sim, quero demo"]})
    InboundHandler(db, src).process_once()
    with db.session() as s:
        l = s.get(Lead, lid)
        assert l.status == LeadStatus.AGENDOU
        # 1 in + 1 out(proposta)
        types = [m.tipo for m in l.messages]
        assert "resposta" in types
        assert "proposta_agendamento" in types


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
