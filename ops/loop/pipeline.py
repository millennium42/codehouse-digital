"""CodeHouse — orquestrador do loop end-to-end.

Fluxo: discover -> score -> (hot/warm) contact -> converse -> schedule.
Loop contínuo: roda N ciclos sobre a fila de leads; em --once para 1 passada.

Fontes: --source local (default) | apify (real, requer APIFY_API_KEY) |
        apify-mock (valida o parse sem chave).
"""
import sys
import json

from config import (OLLAMA_URL, DRY_RUN, WHATSAPP_WEBHOOK_URL, LEADS_PATH)
from leadsource import LocalLeadSource, ApifyLeadSource
from scorer import score
from messenger import send
from conversation import ConversationManager
from store import PostgresStore

sys.path.insert(0, r"C:\Users\Admin\codehouse\scheduling")
from codehouse_book import book as book_event  # noqa: E402


def build_pipeline(source="local", mock_apify=False):
    if source == "apify" or source == "apify-mock":
        import os as _os
        src = ApifyLeadSource(
            api_key=_os.environ.get("APIFY_API_KEY", "FAKEKEY"),
            mock=(source == "apify-mock"),
            base=_os.environ.get("APIFY_BASE"),
        )
    else:
        src = LocalLeadSource(LEADS_PATH)
    store = PostgresStore()
    cm = ConversationManager(
        lambda ch, to, text: send(ch, to, text, DRY_RUN, WHATSAPP_WEBHOOK_URL),
        lambda name, email, mtype: book_event(name, email, 30, mtype, dry_run=DRY_RUN),
        store=store,
    )
    return src, cm, store


def run(once=False, simulate_reply=True, source="local", mock_apify=False):
    src, cm, store = build_pipeline(source, mock_apify)
    leads = src.fetch()
    log = []
    for lead in leads:
        s = score(lead, OLLAMA_URL)
        entry = {"lead": lead.get("name"), "score": s}
        if s["tier"] == "cold":
            entry["action"] = "skip (cold)"
            log.append(entry)
            continue
        intro_res = cm.start(lead)
        entry["intro"] = intro_res.get("status")
        if simulate_reply:
            inbound = cm.handle_inbound(lead, "sim, pode mandar horário")
            entry["converse"] = inbound
        log.append(entry)
        if once:
            break
    return log


if __name__ == "__main__":
    once = "--once" in sys.argv
    sim = "--no-sim" not in sys.argv
    if "--source" in sys.argv:
        i = sys.argv.index("--source") + 1
        source = sys.argv[i]
    elif "--apify" in sys.argv:
        source = "apify"
    elif "--apify-mock" in sys.argv:
        source = "apify-mock"
    else:
        source = "local"
    out = run(once=once, simulate_reply=sim, source=source)
    print(json.dumps(out, indent=2, ensure_ascii=False))
