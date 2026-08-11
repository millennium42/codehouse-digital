from src.scraper import ApifyLeadSource, DryRunLeadSource, RawLead


def test_rawlead_valid_requires_phone():
    ok = RawLead(empresa="X", contato_tel="+55 41 90000-0001")
    assert ok.is_valid()
    bad = RawLead(empresa="Y", contato_tel=None)
    assert not bad.is_valid()


def test_dryrun_discover_returns_normalized():
    src = DryRunLeadSource(seed=1)
    leads = src.discover("clinicas", "Curitiba", 5)
    assert len(leads) == 5
    assert leads[0].empresa == "Clinicas Curitiba #1"
    assert leads[0].contato_tel.startswith("+55")
    # 1/3 sem site (i%3==0)
    assert leads[2].site is None


def test_apify_requires_token(monkeypatch):
    monkeypatch.setenv("APIFY_TOKEN", "")
    src = ApifyLeadSource(token="", dry_run=False)
    try:
        src.discover("clinicas", "Curitiba", 3)
        assert False, "deveria levantar sem token"
    except RuntimeError:
        pass


def test_apify_dryrun_blocked():
    src = ApifyLeadSource(token="abc", dry_run=True)
    try:
        src.discover("clinicas", "Curitiba", 3)
        assert False
    except RuntimeError:
        pass
