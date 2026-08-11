from src.scraper import RawLead
from src.scorer import FakeScorer, LLMScorer


def test_fake_scorer_no_presence_high_score():
    lead = RawLead(empresa="X", contato_tel="+55 41 90000-0001", segmento="clinicas")
    e = FakeScorer().enrich(lead)
    assert e.score == 100
    assert e.tem_sistema is False
    assert "sem presença" in e.motivo


def test_fake_scorer_with_site_lower_score():
    lead = RawLead(empresa="Y", contato_tel="+55 41 90000-0002",
                   site="https://y.com", rede_social="https://ig/y")
    e = FakeScorer().enrich(lead)
    assert e.score == 35
    assert e.tem_sistema is True


def test_llm_scorer_blocked_in_dryrun():
    s = LLMScorer(api_key="", dry_run=True)
    try:
        s.enrich(RawLead(empresa="Z", contato_tel="+55 41 90000-0003"))
        assert False
    except RuntimeError:
        pass
