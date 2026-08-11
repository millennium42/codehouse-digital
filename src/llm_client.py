"""Cliente LLM OpenAI-compatible (ponytail).

Usado por LLMScorer e LLMMessageWriter. Qualquer endpoint compatível
serve (OpenAI, OpenRouter, Ollama local). Respeita timeout e erro claro.
"""
from __future__ import annotations

import json
import os
import time

import requests


def chat_completion(
    base_url: str,
    api_key: str,
    model: str,
    system: str,
    user: str,
    timeout: int = 30,
    max_retries: int = 3,
) -> str:
    """Retorna o texto da resposta do assistente (com retry/backoff)."""
    url = base_url.rstrip("/") + "/chat/completions"
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": 0.3,
    }
    last_err = None
    for attempt in range(max_retries):
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=timeout)
            if resp.status_code == 429:
                wait = 2 ** attempt * 5
                time.sleep(wait)
                last_err = "429 rate limit"
                continue
            resp.raise_for_status()
            data = resp.json()
            return data["choices"][0]["message"]["content"]
        except requests.HTTPError as e:
            last_err = e
            if resp.status_code == 429:
                time.sleep(2 ** attempt * 5)
                continue
            raise
    raise RuntimeError(f"LLM falhou apos {max_retries} tentativas: {last_err}")


def chat_completion_json(
    base_url: str, api_key: str, model: str,
    system: str, user: str, timeout: int = 30,
) -> dict:
    """Igual a chat_completion mas faz parse de JSON da resposta."""
    text = chat_completion(base_url, api_key, model, system, user, timeout)
    # tolera markdown code fences
    clean = text.strip()
    if clean.startswith("```"):
        clean = clean.split("```")[1]
        if clean.startswith("json"):
            clean = clean[4:]
    return json.loads(clean)
