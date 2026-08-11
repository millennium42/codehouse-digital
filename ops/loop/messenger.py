"""CodeHouse — envio de mensagens.

Por padrão dry-run (imprime, não envia). Em produção, aponta WHATSAPP_WEBHOOK_URL
para o n8n que dispara o WhatsApp (Meta Cloud API oficial recomendada).
"""
import json
import urllib.request
import urllib.error


def send(channel, to, text, dry_run=True, webhook_url=""):
    payload = {"channel": channel, "to": to, "text": text}
    if dry_run or not webhook_url:
        print(f"[DRY-RUN][{channel}] -> {to}: {text[:140]}")
        return {"status": "dry_sent", "payload": payload}
    body = json.dumps(payload).encode()
    try:
        req = urllib.request.Request(
            webhook_url, data=body,
            headers={"Content-Type": "application/json"}, method="POST",
        )
        with urllib.request.urlopen(req, timeout=10) as r:
            return {"status": "sent", "response": r.read().decode()[:200]}
    except urllib.error.URLError as e:
        return {"status": "error", "error": str(e), "payload": payload}
