"""CodeHouse — persistência de estado de conversa em Postgres.

Pure-Python (pg8000), sem libpq. Guarda o estado de cada lead entre
webhooks inbound, para o ConversationManager retomar de onde parou.

Se o Postgres não estiver disponível, cai para um store em-memória
(avisa, mas não quebra o loop). Em produção o Postgres é obrigatório.
"""
import os
import json
import pg8000.native  # pure-python driver


class PostgresStore:
    def __init__(self, dsn=None):
        self.dsn = dsn or os.environ.get(
            "CODEHOUSE_DATABASE_URL",
            "postgresql://codehouse:codehouse@127.0.0.1:5432/codehouse",
        )
        self._mem = {}
        self.conn = None
        self._connect()

    def _parse(self):
        s = self.dsn.split("://", 1)[1]
        creds, rest = s.split("@", 1)
        user, password = creds.split(":", 1)
        hostport, db = rest.split("/", 1)
        host, port = (hostport.split(":", 1) + ["5432"])[:2]
        return {"user": user, "password": password,
                "host": host, "port": int(port), "database": db}

    def _connect(self):
        try:
            u = self._parse()
            self.conn = pg8000.native.Connection(
                user=u["user"], password=u["password"],
                host=u["host"], port=u["port"], database=u["database"],
            )
            self._init_schema()
        except Exception as e:
            print(f"[store] Postgres indisponível, usando memória: {e}")
            self.conn = None

    def _init_schema(self):
        self.conn.run("""
            CREATE TABLE IF NOT EXISTS lead_state (
                lead_id TEXT PRIMARY KEY,
                stage TEXT NOT NULL,
                data JSONB NOT NULL DEFAULT '{}'::jsonb,
                updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
            )
        """)

    def available(self):
        return self.conn is not None

    def get(self, lead_id):
        if not self.conn:
            return self._mem.get(lead_id)
        rows = self.conn.run(
            "SELECT stage, data FROM lead_state WHERE lead_id = :id",
            id=lead_id,
        )
        if not rows:
            return None
        stage, data = rows[0]
        return {"stage": stage, "data": data}

    def set(self, lead_id, stage, data):
        if not self.conn:
            self._mem[lead_id] = {"stage": stage, "data": data}
            return
        self.conn.run(
            """INSERT INTO lead_state (lead_id, stage, data)
               VALUES (:id, :stage, :data)
               ON CONFLICT (lead_id) DO UPDATE
                 SET stage = :stage, data = :data, updated_at = now()""",
            id=lead_id, stage=stage, data=json.dumps(data),
        )
