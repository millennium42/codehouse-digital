"""CodeHouse loop — config via env (ponytail: só stdlib os)."""
import os
import json


def env(name, default=""):
    return os.environ.get(name, default)


OLLAMA_URL = env("OLLAMA_URL", "http://localhost:11434")
OPENROUTER_API_KEY = env("OPENROUTER_API_KEY", "")
# Apify: actor que RETORNA telefone (pimperp/apify-google-maps-scraper).
# NAO usar compass/crawler-google-places (nao retorna telefone) nem
# apify/google-maps-scraper (404 nesta conta).
APIFY_API_KEY = env("APIFY_API_KEY", "apify_api_gTg3udrAwfxYYiNNIgazymbSzQAzcw36uo8q")
APIFY_ACTOR = env("APIFY_ACTOR", "pimperp/apify-google-maps-scraper")
# Campo de busca do actor = "searchStrings" (array de strings), NAO "searchStringsArray".
APIFY_RUN_INPUT = env("APIFY_RUN_INPUT", json.dumps({
    "searchStrings": [
        "restaurante Santa Maria RS", "clinica Santa Maria RS", "loja Santa Maria RS",
        "salao de beleza Santa Maria RS", "pet shop Santa Maria RS", "barbearia Santa Maria RS",
        "academia Santa Maria RS", "escritorio contabil Santa Maria RS", "hotel Santa Maria RS",
        "padaria Santa Maria RS", "farmacia Santa Maria RS", "consultorio dentario Santa Maria RS",
    ],
    "maxResultsPerSearch": 12,
    "language": "pt-BR",
    "maxReviews": 0,
    "maxImages": 0,
    "searchRadiusUnit": "km",
    "timeout": 180,
}))
# URL do webhook de saida (n8n -> Meta Cloud API). Vazio => dry-run.
WHATSAPP_WEBHOOK_URL = env("WHATSAPP_WEBHOOK_URL", "")
MILLANI_EMAIL = env("MILLANI_EMAIL", "millani@redes.ufsm.br")
CH_CALENDAR_ID = env("CH_CALENDAR_ID", "primary")
# dry-run por padrao: nunca envia mensagem real nem cria evento sem opt-in
DRY_RUN = env("CODEHOUSE_DRY_RUN", "1") == "1"
LEADS_PATH = env("CODEHOUSE_LEADS", os.path.join(os.path.dirname(__file__), "leads_local.json"))
