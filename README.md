# CodeHouse Digital

A empresa digital da **CodeHouse** (Pablo) — monorepo unificado que reúne o
agente de prospecção comercial, o site institucional e o runtime operacional.

> Tudo é um único projeto. Três módulos sob um teto:

```
codehouse-digital/
├── agent/   # Pacote Python do agente de prospecção (discover→enrich→qualify→send→schedule)
├── site/    # Site institucional estático (HTML/CSS, build via build_site.py)
└── ops/     # Runtime operacional: loop de prospecção, scheduling (Google Agenda), WhatsApp bridge, base de leads
```

## Componentes

### `agent/` — Agente de Prospecção
Agente comercial em Python (SQLAlchemy + PostgreSQL). Ciclo R9:
`discover → enrich → qualify → send → poll inbound → schedule`.
Respeita LGPD (opt-out, consent_log append-only, zero PII em logs).
Detalhes em [`agent/README.md`](agent/README.md).

### `site/` — Site Institucional
Páginas estáticas (landing, 404, política de privacidade) + `build_site.py`.
Deploy via Render (ver `site/render.yaml`).

### `ops/` — Runtime Operacional
- `loop/` — pipeline de prospecção (Apify, scoring de "site feio", LLM).
- `scheduling/` — integração Google Calendar (`codehouse_book.py`).
- `whatsapp-bridge/` — bridge Baileys / WhatsApp Web (Windows).
- `leads_*.json` — base de leads qualificados e não-qualificados.
- `CODEHOUSE_PIPELINE.md` — playbook operacional e regras do Pablo.

## Setup rápido
```bash
# Agente
cd agent && uv venv && uv pip install -e ".[dev]"
cp .env.example .env   # preencha credenciais reais em produção

# Site (gerar/servir)
cd site && python build_site.py

# Ops loop
cd ops/loop && python pipeline.py   # dry-run por padrão
```

## Segurança / LGPD
- `.env`, `baileys_auth/`, `.wwebjs_auth/` e `qr.png` **não são versionados**.
- Telefone/nome mascarados (`mask_pii`); zero PII em logs.
- WhatsApp Web no número pessoal viola ToS → usar **Meta Cloud API** em produção.

## Status
MVP operando em dry-run. Fontes reais (Apify / LLM / Google Calendar / Meta)
isoladas atrás de interfaces e bloqueadas em dry-run — plugar credenciais p/ produção.
