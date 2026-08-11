"""CodeHouse — qualificação de lead.

Pipeline de scoring:
  1. Tenta LLM local (Ollama) se o servidor estiver de pé.
  2. Fallback heurístico (stdlib puro, determinístico) — funciona sem rede.

Retorna dict: {"score": 0-100, "tier": hot|warm|cold, "reason": str, "engine": str}
"""
import json
import urllib.request
import urllib.error
import os

DEFAULT_MODEL = os.environ.get("OLLAMA_MODEL", "")  # vazio => auto-detecta


def _list_models(url):
    try:
        with urllib.request.urlopen(url + "/api/tags", timeout=5) as r:
            data = json.load(r)
        return [m["name"] for m in data.get("models", [])]
    except Exception:
        return []


def _pick_model(url, preferred=DEFAULT_MODEL):
    if preferred:
        return preferred
    models = _list_models(url)
    if not models:
        return None
    # prefere o menor llama disponível (3b/1b) p/ latência; senão o primeiro
    llamas = [m for m in models if "llama" in m.lower()]
    if llamas:
        llamas.sort(key=lambda m: (".3b" in m, ".1b" in m, ".7b" in m, m))
        return llamas[0]
    return models[0]


def _parse_llm_json(text):
    text = (text or "").strip()
    # remove cercas ```json ... ```
    if "```" in text:
        text = text.split("```")[1]
        if text.lower().startswith("json"):
            text = text[4:]
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1:
        try:
            return json.loads(text[start:end + 1])
        except Exception:
            return None
    return None


def _ollama_score(lead, url):
    model = _pick_model(url)
    if not model:
        return None
    prompt = (
        "Você é o qualificador da CodeHouse (software sob medida). "
        "Pontue de 0 a 100 este lead e responda SOMENTE JSON "
        '{"score":int,"tier":"hot|warm|cold","reason":str}.\n'
        f"Lead: nome={lead.get('name')} empresa={lead.get('company')} "
        f"cargo={lead.get('role')} setor={lead.get('sector')} "
        f"mensagem={lead.get('message')}"
    )
    body = json.dumps(
        {"model": model, "prompt": prompt, "stream": False, "format": "json"}
    ).encode()
    try:
        req = urllib.request.Request(
            url + "/api/generate",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=30) as r:
            resp = json.load(r)
        parsed = _parse_llm_json(resp.get("response", ""))
        if isinstance(parsed.get("score"), int):
            parsed["engine"] = "ollama:" + model
            return parsed
    except Exception:
        return None
    return None


def _heuristic(lead):
    score = 0
    reasons = []
    msg = (lead.get("message") or "").lower()
    need_kw = ["preciso", "urgente", "orçamento", "orçamento", "sistema",
               "automatizar", "app", "site", "software", "gestão"]
    if any(k in msg for k in need_kw):
        score += 40
        reasons.append("sinal de necessidade")
    role = (lead.get("role") or "").lower()
    if role in ("dono", "ceo", "cfo", "fundador", "diretor", "gerente", "sócio"):
        score += 25
        reasons.append("perfil decisor")
    if (lead.get("company_size") or 0) >= 10:
        score += 20
        reasons.append("porte médio+")
    sector = (lead.get("sector") or "").lower()
    if sector in ("varejo", "serviços", "saúde", "indústria", "educação", "logística"):
        score += 15
        reasons.append("setor susceptível")
    tier = "hot" if score >= 70 else "warm" if score >= 40 else "cold"
    return {"score": min(score, 100), "tier": tier,
            "reason": "; ".join(reasons) or "sem sinais fortes",
            "engine": "heuristic"}


def score(lead, ollama_url):
    r = _ollama_score(lead, ollama_url)
    if r:
        return r
    return _heuristic(lead)
