from datetime import datetime, timezone

from src.config import Config
from src.db import Database, LeadStatus
from src.orchestrator import ProspectingAgent


def _cfg(tmp_path):
    p = tmp_path / "config.yaml"
    p.write_text(
        "prospecting:\n  segment: clinicas\n  city: Curitiba\n  limit: 6\n  min_score: 50\n"
        "dry_run: true\n",
        encoding="utf-8",
    )
    return Config.load(str(p))


def test_full_dry_run_cycle_accept(tmp_path, monkeypatch):
    def fake_reply(db, lead, enr, text, *a, **k):
        # simula Pablo enviando link de agenda
        return f"Combinado! LINK_AGENDA: https://calendar.google.com/XYZ"

    monkeypatch.setattr("src.conversation.reply", fake_reply)
    cfg = _cfg(tmp_path)
    cfg.db_url = f"sqlite:///{tmp_path / 'e2e.db'}"
    db = Database(cfg.db_url)
    agent = ProspectingAgent(cfg, db)

    # dryrun: a cada 3 sem site (+40) e a cada 2 sem rede (+25) => 4/6 sem site
    # nem todos qualificam (2 têm site+rede => score 35 < 50)
    stats = agent.run_cycle(inbound_script={1: ["sim, quero demo"], 2: ["sair"]})
    assert stats.discovered == 6
    assert stats.qualified == 4
    assert stats.sent == 4
    assert stats.replied == 2
    assert stats.scheduled >= 1
    assert stats.discarded == 2

    with db.session() as s:
        from src.db import Lead
        leads = s.query(Lead).all()
        by_id = {l.id: l for l in leads}
        assert by_id[1].status == LeadStatus.AGENDOU
        assert by_id[2].opt_out is True
        assert by_id[2].status == LeadStatus.DESCARTADO


def test_min_score_discards_low(tmp_path):
    cfg = _cfg(tmp_path)
    cfg.prospecting.min_score = 200  # ninguém passa (fake máx 100)
    cfg.db_url = f"sqlite:///{tmp_path / 'e2e2.db'}"
    db = Database(cfg.db_url)
    agent = ProspectingAgent(cfg, db)
    stats = agent.run_cycle()
    assert stats.qualified == 0
    assert stats.sent == 0
    assert stats.discarded == 6
