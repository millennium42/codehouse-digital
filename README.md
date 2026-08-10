# CodeHouse Prospecting Agent

Agente de prospecção comercial para a **CodeHouse** (desenvolvimento de software
personalizado: páginas, ERPs, CRMs, automação de chat).

O **Hermes** orquestra o ciclo; o **n8n** é apenas a ponte de WhatsApp (Meta
Cloud API); o estado vive em **PostgreSQL**. Respeita **LGPD** (opt-out,
consent_log append-only, zero PII em logs).

## Ciclo (R9)
`discover → enrich → qualify → send → poll inbound → schedule`

1. **discover** — Apify MCP (Google Maps / IG / LinkedIn) por segmento+cidade.
2. **enrich** — LLM busca site/rede, detecta sistema atual, estima dor.
3. **qualify** — score 0-100 + motivo; só `>= min_score` recebe abordagem.
4. **send** — LLM redige 1ª mensagem (com opt-out LGPD) → webhook n8n.
5. **poll inbound** — n8n grava resposta; agente conduz até agendar/opt-out.
6. **schedule** — Google Calendar cria evento + invite no aceite.

## Stack
- Python 3.11 + SQLAlchemy (PostgreSQL)
- Módulos: `scraper`, `scorer`, `sender`, `inbound`, `scheduler`, `orchestrator`
- dry-run: fontes fake determinísticas (sem rede, sem credencial)

## Setup
```bash
uv venv && uv pip install -e ".[dev]"
cp .env.example .env   # preencha credenciais reais em produção
# dev/demo (sem credenciais):
uv run python -m src.cli --config config.dryrun.yaml --limit 8
# testes:
uv run pytest
```

## Configuração
`config.yaml` (ou `config.dryrun.yaml`):
- `prospecting`: segment, city, limit, min_score
- `n8n.outbound_webhook`: URL do webhook n8n (envia WhatsApp)
- `llm`: base_url / api_key / model (OpenAI-compatible)
- `calendar`: token Google Calendar
- `apify`: token Apify
- `db.url`: PostgreSQL (ou sqlite em dev)
- `dry_run`: true = não envia nada, usa fontes fake

## LGPD
- Lead tratado como dado pessoal.
- `opt_out` por lead bloqueia envio.
- `consent_log` append-only (abordagem / opt-out / agendamento).
- **Zero PII em logs** — telefone/nome mascarados (`mask_pii`).

## Status MVP
R1–R10 entregues (dry-run). Fontes reais (Apify/LLM/Google Calendar) isoladas
atrás de interfaces e bloqueadas em dry_run — plugar credenciais para produção.
