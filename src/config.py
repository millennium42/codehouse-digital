"""Carregamento de configuração do agente CodeHouse.

Lê .env (python-dotenv) e config.yaml, resolvendo ${VAR} a partir do ambiente.
Suporta dry_run para dev/testes sem credenciais reais.
"""
from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv

_ENV_PATTERN = re.compile(r"\$\{([A-Z0-9_]+)\}")


def _resolve_env_vars(node: Any) -> Any:
    """Substitui ${VAR} por os.environ[VAR] recursivamente no YAML."""
    if isinstance(node, dict):
        return {k: _resolve_env_vars(v) for k, v in node.items()}
    if isinstance(node, list):
        return [_resolve_env_vars(v) for v in node]
    if isinstance(node, str):
        def repl(m: re.Match) -> str:
            return os.environ.get(m.group(1), "")
        return _ENV_PATTERN.sub(repl, node)
    return node


@dataclass
class ProspectingConfig:
    segment: str = "clinicas"
    city: str = "Curitiba"
    limit: int = 20
    min_score: int = 50


@dataclass
class N8NConfig:
    outbound_webhook: str = ""
    inbound_webhook: str = ""


@dataclass
class LLMConfig:
    base_url: str = ""
    api_key: str = ""
    model: str = "gpt-4o-mini"


@dataclass
class CalendarConfig:
    enabled: bool = False
    token: str = ""
    calendar_id: str = "primary"
    schedule_url: str = ""  # link público de agendamento (Google Calendar Appointment Scheduling)


@dataclass
class ApifyConfig:
    token: str = ""


@dataclass
class Config:
    db_url: str = "sqlite:///./codehouse.db"
    dry_run: bool = True
    prospecting: ProspectingConfig = field(default_factory=ProspectingConfig)
    n8n: N8NConfig = field(default_factory=N8NConfig)
    llm: LLMConfig = field(default_factory=LLMConfig)
    calendar: CalendarConfig = field(default_factory=CalendarConfig)
    apify: ApifyConfig = field(default_factory=ApifyConfig)

    @classmethod
    def load(cls, path: str | os.PathLike[str] = "config.yaml") -> "Config":
        load_dotenv()
        raw = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
        raw = _resolve_env_vars(raw)
        p = raw.get("prospecting", {})
        n = raw.get("n8n", {})
        l = raw.get("llm", {})
        c = raw.get("calendar", {})
        a = raw.get("apify", {})
        return cls(
            db_url=raw.get("db", {}).get("url", "sqlite:///./codehouse.db"),
            dry_run=str(raw.get("dry_run", "true")).lower() in ("1", "true", "yes"),
            prospecting=ProspectingConfig(
                segment=p.get("segment", "clinicas"),
                city=p.get("city", "Curitiba"),
                limit=int(p.get("limit", 20)),
                min_score=int(p.get("min_score", 50)),
            ),
            n8n=N8NConfig(
                outbound_webhook=n.get("outbound_webhook", ""),
                inbound_webhook=n.get("inbound_webhook", ""),
            ),
            llm=LLMConfig(
                base_url=l.get("base_url", ""),
                api_key=l.get("api_key", ""),
                model=l.get("model", "gpt-4o-mini"),
            ),
            calendar=CalendarConfig(
                enabled=str(c.get("enabled", "false")).lower() in ("1", "true", "yes"),
                token=c.get("token", ""),
                calendar_id=c.get("calendar_id", "primary"),
                schedule_url=c.get("schedule_url", ""),
            ),
            apify=ApifyConfig(token=a.get("token", "")),
        )
