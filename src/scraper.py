"""Descoberta de leads via Apify MCP.

Abstrai a fonte de descoberta atrás de uma interface `LeadSource`.
Em produção usa Apify (Google Maps / IG / LinkedIn). Em dev/testes usa
`FakeLeadSource` (dados determinísticos) e `DryRunLeadSource` (sem credencial).
A normalização entrega um `RawLead` pronto para o scorer/db.
"""
from __future__ import annotations

import abc
import os
import time
from dataclasses import dataclass
from typing import Iterable

import requests


@dataclass
class RawLead:
    empresa: str
    contato_nome: str | None = None
    contato_tel: str | None = None
    segmento: str | None = None
    rede_social: str | None = None
    site: str | None = None
    cnpj: str | None = None
    source: str = "apify"

    def is_valid(self) -> bool:
        """Lead inválido se não tem telefone (não dá pra contatar via WhatsApp)."""
        return bool(self.contato_tel)


class LeadSource(abc.ABC):
    @abc.abstractmethod
    def discover(self, segment: str, city: str, limit: int) -> list[RawLead]:
        ...


class ApifyLeadSource(LeadSource):
    """Fonte real via Apify (Google Maps / Instagram / LinkedIn).

    Requer APIFY_TOKEN. Em dry_run levanta se chamado sem token — use
    DryRunLeadSource em dev. A chamada HTTP real fica isolada em `_run_actor`.
    """

    def __init__(self, token: str | None = None, dry_run: bool = False) -> None:
        self.token = token or os.environ.get("APIFY_TOKEN", "")
        self.dry_run = dry_run

    def discover(self, segment: str, city: str, limit: int) -> list[RawLead]:
        if self.dry_run or not self.token:
            raise RuntimeError(
                "ApifyLeadSource requer token e dry_run=false. Use DryRunLeadSource em dev."
            )
        rows = self._run_actor(segment, city, limit)
        return [self._normalize(r) for r in rows]

    def _run_actor(self, segment: str, city: str, limit: int) -> list[dict]:
        # Apify REST: start run -> poll -> fetch dataset
        actor_id = "lukassimko/google-maps-scraper"
        headers = {"Authorization": f"Bearer {self.token}"}
        start_url = (
            f"https://api.apify.com/v2/acts/{actor_id}/runs"
            f"?token={self.token}"
        )
        payload = {
            "searchString": f"{segment} em {city}",
            "maxCrawledPlaces": min(limit, 100),
            "language": "pt-BR",
        }
        r = requests.post(start_url, json=payload, headers=headers, timeout=30)
        r.raise_for_status()
        run_id = r.json()["data"]["id"]
        # poll until finished
        for _ in range(30):
            status = requests.get(
                f"https://api.apify.com/v2/actor-runs/{run_id}?token={self.token}",
                timeout=30,
            ).json()["data"]["status"]
            if status in ("SUCCEEDED", "FAILED", "ABORTED"):
                break
            time.sleep(5)
        if status != "SUCCEEDED":
            return []
        ds_id = requests.get(
            f"https://api.apify.com/v2/actor-runs/{run_id}?token={self.token}",
            timeout=30,
        ).json()["data"]["defaultDatasetId"]
        items = requests.get(
            f"https://api.apify.com/v2/datasets/{ds_id}/items?token={self.token}",
            timeout=30,
        ).json()
        return items

    def _normalize(self, row: dict) -> RawLead:
        return RawLead(
            empresa=row.get("title") or row.get("name") or "Desconhecido",
            contato_tel=row.get("phone") or row.get("telefone"),
            site=row.get("website"),
            rede_social=row.get("instagramUrl") or row.get("linkedinUrl"),
            segmento=row.get("categoryName") or "desconhecido",
            cnpj=row.get("cnpj"),
        )


class DryRunLeadSource(LeadSource):
    """Fonte fake determinística para dev/testes (sem rede, sem token)."""

    def __init__(self, seed: int = 0) -> None:
        self.seed = seed

    def discover(self, segment: str, city: str, limit: int) -> list[RawLead]:
        out: list[RawLead] = []
        for i in range(1, limit + 1):
            out.append(
                RawLead(
                    empresa=f"{segment.title()} {city} #{i}",
                    contato_nome=f"Responsavel {i}",
                    contato_tel=f"+55 41 90000-{i:04d}",
                    segmento=segment,
                    site=f"https://{segment}{i}.com.br" if i % 3 != 0 else None,
                    rede_social=f"https://instagram.com/{segment}{i}" if i % 2 == 0 else None,
                    cnpj=f"00000000000{i % 10}",
                    source="dryrun",
                )
            )
        return out
