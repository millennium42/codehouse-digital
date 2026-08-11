"""Humanizador leve de texto (pos-processamento de saida do LLM).

Remove marcadores de robô, suaviza tom, quebra frases longas.
Nao chama LLM — so texto. Para humanizacao profunda, use o skill 'humanizer'.
"""
from __future__ import annotations

import re

_ROBO = [
    r"\b(como uma IA|como um assistente virtual|sou um bot|sou uma IA)\b",
    r"\b(espero ter ajudado|estou aqui para ajudar)\b",
    r"^\s*[-\*]\s+",  # bullets soltos
]


def humanize(text: str) -> str:
    if not text:
        return text
    t = text.strip()
    # remove marcadores de robô
    for p in _ROBO:
        t = re.sub(p, "", t, flags=re.IGNORECASE)
    # remove linhas vazias duplas
    t = re.sub(r"\n{2,}", "\n", t)
    # quebra frases muito longas (>180 chars sem ponto) — corta em ; ou ,
    t = re.sub(r"([,;])\s*", r"\1\n", t)
    # remove espacos extras
    t = re.sub(r"[ \t]{2,}", " ", t)
    # capitaliza inicio
    t = t.strip()
    if t and t[0].islower():
        t = t[0].upper() + t[1:]
    return t.strip()
