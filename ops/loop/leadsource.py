"""CodeHouse — fontes de leads.

- LocalLeadSource: JSON fixo p/ teste/dev.
- ApifyLeadSource: fetch REAL na Apify (actor pimperp/apify-google-maps-scraper).
  Retorna telefone + website. Filtra franquias e pontua "site feio/simples".

Criterio CodeHouse (Pablo): leads qualificados = tem site FEIO/SIMPLIES
(para vender site institucional AGORA). Nao-qualificados (site ok, sem site,
franquia) sao guardados em base separada para vender CRM/ERP/automacao depois.
"""
import json
import os
import time
import ssl
import urllib.request
import urllib.error

BASE = os.environ.get("APIFY_BASE", "https://api.apify.com/v2")

# substrings que indicam franquia/cadeia (excluir)
FRANCHISE_HINTS = (
    "franquia", "franquias", "mc donalds", "mcdonald", "burger king", "subway",
    "telefonica", "vivo", "claro", "oi ", "renner", "riachuelo", "cacau show",
    "habib", "giraffas", "outback", "starbucks", "mcdonalds", "rede", "matriz",
    "filial", "pizza hut",
)


def normalize_phone(p):
    if not p:
        return ""
    digits = "".join(c for c in p if c.isdigit())
    if digits.startswith("55") and len(digits) >= 11:
        return "+" + digits
    if len(digits) in (10, 11):
        return "+55" + digits
    return ""


def is_franchise(name, cat):
    n = (name or "").lower()
    c = (cat or "").lower()
    return any(h in n or h in c for h in FRANCHISE_HINTS)


def score_site_ugliness(url, manual_feio=None):
    """Retorna (feio: bool, score: int, detalhe: str).

    Heuristica: site morto (nao abre), google business.site, sem CSS, sem JS,
    pouco conteudo, poucas imagens = feio/simples.
    manual_feio forca feio=True (ex.: Bovinu's apontado como visualmente feio).
    """
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    if manual_feio:
        return True, 99, "marcado manualmente como feio"
    if not url:
        return False, 0, "sem site (nao qualifica para site institucional)"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15, context=ctx) as r:
            html = r.read().decode("utf-8", "ignore")
            final_url = r.geturl()
        size = len(html)
        has_css = bool(__import__("re").search(r"<link[^>]+stylesheet|style=", html, __import__("re").I))
        has_js = bool("script" in html.lower())
        imgs = html.lower().count("<img")
        gsite = "negocio.site" in final_url or "sites.google" in final_url or "business.site" in final_url
        score = 0
        if gsite:
            score += 5
        if not has_css:
            score += 3
        if not has_js:
            score += 2
        if size < 15000:
            score += 2
        if imgs < 2:
            score += 2
        feio = score >= 5
        return feio, score, f"size={size} css={has_css} js={has_js} imgs={imgs} gsite={gsite}"
    except Exception as e:
        return True, 90, f"site nao abre: {str(e)[:50]}"


class LocalLeadSource:
    def __init__(self, path):
        self.path = path

    def fetch(self, max_n=50):
        if not os.path.exists(self.path):
            return []
        with open(self.path, encoding="utf-8") as f:
            data = json.load(f)
        return data[:max_n]


def _parse_items(items, manual_feio_names=()):
    """Classifica leads: qualificados (site feio) + nao-qualificados (base CRM/ERP)."""
    qualificados = []
    nao_qualificados = []
    seen = set()
    for it in items:
        name = it.get("title") or it.get("name") or "Desconhecido"
        web = (it.get("website") or "").strip()
        pn = it.get("phoneNumbers") or it.get("phone")
        phone = normalize_phone(pn[0] if isinstance(pn, list) and pn else (pn if isinstance(pn, str) else ""))
        cat = it.get("categoryName", "") or ""
        key = (phone or name).lower()
        if key in seen:
            continue
        seen.add(key)
        franquia = is_franchise(name, cat)
        manual = any(m.lower() in name.lower() for m in manual_feio_names)
        feio, sc, det = score_site_ugliness(web, manual_feio=manual)
        lead = {
            "id": "apify_" + str(it.get("placeId") or name).replace(" ", "_"),
            "name": name,
            "company": name,
            "role": "Dono",
            "sector": cat,
            "company_size": 0,
            "phone": phone,
            "email": "",
            "website": web,
            "address": it.get("address", ""),
            "source": "apify",
            "site_feio": feio,
            "franquia": franquia,
            "site_score": sc,
            "site_detail": det,
        }
        if franquia:
            lead["motivo"] = "franquia (excluido)"
            nao_qualificados.append(lead)
        elif feio:
            lead["motivo"] = "site feio/simples -> vender site institucional"
            qualificados.append(lead)
        else:
            lead["motivo"] = "site ok / sem site -> base CRM/ERP/automacao"
            nao_qualificados.append(lead)
    return qualificados, nao_qualificados


class ApifyLeadSource:
    """Adapter p/ Apify. Requer APIFY_API_KEY. Actor: pimperp/apify-google-maps-scraper."""

    def __init__(self, api_key, actor=None, run_input=None, mock=False, base=None):
        self.api_key = api_key
        self.actor = actor or os.environ.get("APIFY_ACTOR", "pimperp/apify-google-maps-scraper")
        self.run_input = run_input or json.loads(os.environ.get("APIFY_RUN_INPUT", "{}"))
        self.mock = mock or (not api_key)
        if base:
            self.BASE = base

    def fetch(self, max_n=50, manual_feio_names=()):
        if self.mock:
            return self._fetch_mock(max_n)
        return self._fetch_real(max_n, manual_feio_names)

    def _run_status(self, run_id):
        url = f"{self.BASE}/actor-runs/{run_id}?token={self.api_key}"
        with urllib.request.urlopen(url, timeout=30) as r:
            return json.load(r)["data"].get("status")

    def _fetch_real(self, max_n, manual_feio_names):
        # 1) inicia o run
        url = f"{self.BASE}/acts/{self.actor}/runs?token={self.api_key}"
        req = urllib.request.Request(
            url,
            data=json.dumps(self.run_input).encode(),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=30) as r:
            run = json.load(r)["data"]
        run_id = run["id"]
        ds_id = run.get("defaultDatasetId")
        # 2) polling — NAO aborta em TIMED-OUT: busca dataset parcial mesmo assim
        for _ in range(40):
            st = self._run_status(run_id)
            if st in ("SUCCEEDED", "FAILED"):
                break
            time.sleep(10)
        # 3) baixa dataset (mesmo se TIMED-OUT veio parcial)
        if not ds_id:
            return [], []
        ds_url = (
            f"{self.BASE}/datasets/{ds_id}/items?token={self.api_key}&limit={max_n}"
            f"&fields=title,name,phone,phoneNumbers,website,categoryName,address,placeId"
        )
        try:
            with urllib.request.urlopen(ds_url, timeout=30) as r:
                items = json.load(r)
        except Exception:
            items = []
        return _parse_items(items, manual_feio_names)

    def _fetch_mock(self, max_n):
        fake = [
            {"title": "Padaria Pao Quente", "categoryName": "Padaria",
             "phoneNumbers": ["+5555999990000"], "website": "https://padariafeia.blogspot.com",
             "placeId": "abc123"},
            {"title": "Clinica Bem Estar", "categoryName": "Saude",
             "phoneNumbers": ["+5555999991111"], "website": "", "placeId": "def456"},
        ]
        return _parse_items(fake)
