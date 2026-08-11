"""Testes dos stubs reais (Apify + LLM) com requests mockado (sem rede)."""
from __future__ import annotations

import json
from unittest import mock

from src.scraper import ApifyLeadSource
from src.scorer import LLMScorer
from src.sender import LLMMessageWriter
from src.scraper import RawLead


def _fake_resp(json_data, status=200):
    m = mock.Mock()
    m.status_code = status
    m.json.return_value = json_data
    m.raise_for_status.return_value = None
    return m


def test_apify_run_actor_normalizes():
    src = ApifyLeadSource(token="tok", dry_run=False)
    run_json = {"data": {"id": "run1", "status": "SUCCEEDED",
                         "defaultDatasetId": "ds1"}}
    items = [{"title": "Clinica X", "phone": "+55 41 90000-1111",
              "website": "https://x.com", "categoryName": "clinicas"}]
    with mock.patch("src.scraper.requests.post",
                    return_value=_fake_resp({"data": {"id": "run1"}})), \
         mock.patch("src.scraper.requests.get", side_effect=[
             _fake_resp(run_json),            # status poll
             _fake_resp(run_json),            # dataset id
             _fake_resp(items),               # items
         ]):
        rows = src._run_actor("clinicas", "Curitiba", 3)
    assert rows[0]["title"] == "Clinica X"
    lead = src._normalize(rows[0])
    assert lead.contato_tel == "+55 41 90000-1111"
    assert lead.is_valid()


def test_llm_scorer_parses_json():
    s = LLMScorer(base_url="http://llm", api_key="k", model="m", dry_run=False)
    llm_out = json.dumps({"tem_sistema": False, "dor_estimada": "sem site",
                          "score": 85, "motivo": "sem presenca"})
    with mock.patch("src.scorer.chat_completion_json", return_value=json.loads(llm_out)):
        e = s.enrich(RawLead(empresa="Y", segmento="clinicas"))
    assert e.score == 85
    assert e.tem_sistema is False
    assert "sem presenca" in e.motivo


def test_llm_message_writer_returns_text():
    w = LLMMessageWriter(base_url="http://llm", api_key="k", model="m", dry_run=False)
    with mock.patch("src.sender.chat_completion",
                    return_value="Olá Maria, sou da CodeHouse..."):
        from src.db import Lead, LeadStatus
        from src.scorer import Enrichment
        txt = w.write(Lead(empresa="Z", contato_nome="Maria"),
                      Enrichment(None, None, False, "sem site", 80, "x"))
    assert "CodeHouse" in txt
