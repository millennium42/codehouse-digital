"""Cliente LLM OpenAI-compatible (ponytail).

Usado por LLMScorer e LLMMessageWriter. Qualquer endpoint compatível
serve (OpenAI, OpenRouter, Ollama local). Respeita timeout e erro claro.
"""
from __future__ import annotations

import json
import os

import requests


def chat_completion(
    base_url: str,
    api_key: str,
    model: str,
    system: str,
    user: str,
    timeout: int = 30,
) -> str:
    """Retorna o texto da resposta do assistente."""
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
    resp = requests.post(url, headers=headers, json=payload, timeout=timeout)
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"]


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
