"""CodeHouse — gerenciador da conversa inicial (máquina de estados).

Estados: intro -> waiting -> qualified -> scheduled | dead.
O estado de cada lead é persistido (PostgresStore) para retomar entre
webhooks inbound do n8n em produção.
"""
# Texto de primeiro contato — Pablo / Code House. Amigável, sem jargão, opt-out LGPD.
INTRO_MSG = (
    "Olá {name}, tudo bem? Aqui é o Pablo da Code House. A gente desenvolve "
    "site/página institucional, CRM, ERP e automação de atendimento pra "
    "restaurantes, clínicas, varejo e outros segmentos. Vi que a {company} "
    "ainda não tem uma página institucional e queria trocar uma ideia rápida "
    "sobre como ajudar a captar mais clientes. Teria uns 10–15 min pra uma "
    "reunião esta semana? Posso mandar uns horários. "
    "(Se não quiser receber mais mensagens, é só avisar que removo seu contato — LGPD.)"
)


class ConversationManager:
    def __init__(self, messenger_send, scheduler_book, store=None):
        self.send = messenger_send
        self.book = scheduler_book
        self.store = store

    def _load(self, lead_id):
        if self.store:
            return self.store.get(lead_id)
        return None

    def _save(self, lead_id, stage, data=None):
        if self.store:
            self.store.set(lead_id, stage, data or {})

    def start(self, lead):
        st = self._load(lead.get("id"))
        if st and st["stage"] in ("qualified", "scheduled", "dead"):
            return {"status": "noop", "stage": st["stage"]}
        text = INTRO_MSG.format(name=lead.get("name", "cliente"),
                                company=lead.get("company", "sua empresa"))
        res = self.send("whatsapp", lead.get("phone", ""), text)
        self._save(lead.get("id"), "intro")
        return res

    def handle_inbound(self, lead, message):
        m = (message or "").lower()
        if any(k in m for k in ["sim", "pode", "quero", "top", "ok", "manda", "horário"]):
            self._save(lead.get("id"), "qualified")
            return self.schedule(lead)
        if any(k in m for k in ["não", "nao", "obrigado", "descordo"]):
            self._save(lead.get("id"), "dead")
            return {"status": "closed", "reason": "recusa"}
        self.send("whatsapp", lead.get("phone", ""),
                  "Sem problema! Me diga um horário que te atende ou responda 'sim'.")
        self._save(lead.get("id"), "waiting")
        return {"status": "followup"}

    def schedule(self, lead):
        res = self.book(lead.get("name"), lead.get("email", ""), "Reunião inicial")
        self._save(lead.get("id"), "scheduled", {"event": res})
        return res
