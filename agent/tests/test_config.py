import os
import tempfile
from pathlib import Path

import pytest

from src.config import Config


def _write_tmp_config(tmp_path: Path, body: str) -> str:
    p = tmp_path / "config.yaml"
    p.write_text(body, encoding="utf-8")
    return str(p)


def test_load_defaults(tmp_path):
    cfg_path = _write_tmp_config(tmp_path, "dry_run: true\n")
    cfg = Config.load(cfg_path)
    assert cfg.dry_run is True
    assert cfg.db_url == "sqlite:///./codehouse.db"
    assert cfg.prospecting.segment == "clinicas"


def test_env_var_resolution(tmp_path, monkeypatch):
    monkeypatch.setenv("N8N_WEBHOOK_URL", "https://n8n.test/hook")
    body = """
n8n:
  outbound_webhook: "${N8N_WEBHOOK_URL}"
dry_run: false
"""
    cfg = Config.load(_write_tmp_config(tmp_path, body))
    assert cfg.n8n.outbound_webhook == "https://n8n.test/hook"
    assert cfg.dry_run is False


def test_prospecting_and_min_score(tmp_path):
    body = """
prospecting:
  segment: "imobiliarias"
  city: "Sao Paulo"
  limit: 5
  min_score: 70
dry_run: true
"""
    cfg = Config.load(_write_tmp_config(tmp_path, body))
    assert cfg.prospecting.segment == "imobiliarias"
    assert cfg.prospecting.min_score == 70
