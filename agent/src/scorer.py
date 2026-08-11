"""Enriquecimento e pontuação de leads (scorer).

Recebe RawLead, faz enriquecimento (busca site/rede) e usa LLM para:
- detectar se já possui sistema (site, ERP, CRM, chat)
- estimar dor / oportunidade
- gerar score 0-100 + motivo

Em dev/testes usa `FakeScorer` (regras determinísticas, sem rede).
"""
from __future__ import annotations

import abc
import os
from dataclasses import dataclass

from src.llm_client import chat_completion_json
from src.scraper import RawLead


@dataclass
class Enrichment:
    site: str | None
    rede_social: str | None
    tem_sistema: bool | None
    dor_estimada: str | None
    score: int
    motivo: str


class Scorer(abc.ABC):
    @abc.abstractmethod
    def enrich(self, lead: RawLead) -> Enrichment:
        ...


class FakeScorer(Scorer):
    """Regras determinísticas: quanto menos presença digital, maior a dor."""

    def enrich(self, lead: RawLead) -> Enrichment:
        has_site = bool(lead.site)
        has_social = bool(lead.rede_social)
        tem_sistema = has_site  # heurística simples: site => provável presença
        # score: sem site = +40, sem rede = +25, teto 100
        score = 35
        if not has_site:
            score += 40
        if not has_social:
            score += 25
        score = min(score, 100)
        dor = []
        if not has_site:
            dor.append("sem presença digital / site institucional")
        if not has_social:
            dor.append("sem canal de aquisição em redes")
        if not dor:
            dor.append("pode querer evoluir ERP/CRM/chat")
        motivo = f"score={score}: " + "; ".join(dor)
        return Enrichment(
            site=lead.site,
            rede_social=lead.rede_social,
            tem_sistema=tem_sistema,
            dor_estimada="; ".join(dor),
            score=score,
            motivo=motivo,
        )


class LLMScorer(Scorer):
    """Scorer real via LLM (OpenAI-compatible). Requer credencial.

    Em dry_run levanta — use FakeScorer em dev. A chamada LLM fica isolada
    em `_call_llm`.
    """

    def __init__(self, base_url: str = "", api_key: str = "", model: str = "",
                 dry_run: bool = True) -> None:
        self.base_url = base_url
        self.api_key = api_key
        self.model = model
        self.dry_run = dry_run

    def enrich(self, lead: RawLead) -> Enrichment:
        if self.dry_run or not self.api_key:
            raise RuntimeError("LLMScorer requer api_key e dry_run=false.")
        resp = self._call_llm(lead)
        return Enrichment(
            site=lead.site,
            rede_social=lead.rede_social,
            tem_sistema=resp.get("tem_sistema"),
            dor_estimada=resp.get("dor_estimada"),
            score=int(resp.get("score", 0)),
            motivo=resp.get("motivo", ""),
        )

    def _call_llm(self, lead: RawLead) -> dict:
        system = (
            "Voce e um analista de prospeccao B2B. Receba dados de uma empresa e "
            "retorne JSON com: tem_sistema (bool), dor_estimada (string curta), "
            "score (0-100, quanto maior mais chance de vender software sob medida), "
            "motivo (string explicando o score). Responda apenas JSON."
        )
        user = (
            f"Empresa: {lead.empresa}\nSegmento: {lead.segmento}\n"
            f"Site: {lead.site or 'sem site'}\n"
            f"Rede social: {lead.rede_social or 'sem rede'}\n"
            f"Contato: {lead.contato_nome or 'desconhecido'}"
        )
        return chat_completion_json(
            self.base_url, self.api_key, self.model, system, user
        )
