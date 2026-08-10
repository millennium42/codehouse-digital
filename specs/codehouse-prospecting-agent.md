# Spec — Agente de Prospecção CodeHouse

Status: aprovada (MVP) · Data: 2026-08-10

## Objetivo
Agente que descobre leads qualificados para a CodeHouse (dev de softwares
personalizados), faz contato inicial via WhatsApp (n8n + LLM) e agenda
reunião/demo. O agente Hermes orquestra o ciclo inteiro; o n8n é apenas a
ponte de envio/recebimento WhatsApp (Meta Cloud API).

## ICP (perfil de cliente ideal)
Multi-segmento — PMEs brasileiras que podem consumir:
- Páginas institucionais / presença digital
- ERPs sob medida
- CRMs
- Automação de chat / atendimento

Não restrito a um setor: clínicas, escritórios, consultorias, imobiliárias,
varejo, restaurantes, indústrias menores.

## Fonte de descoberta
- **Apify MCP** (Google Maps, Instagram, LinkedIn, etc.) acionado pelo agente.
- Entrada parametrizada: segmento + cidade + volume alvo.

## Qualificação (enriquecimento)
Módulo scorer com LLM:
- Busca site / rede social do lead.
- Detecta se já possui sistema (site, ERP, CRM, chat).
- Estima dor / oportunidade.
- Gera `score` 0-100 + `motivo` (justificativa da pontuação).
- Persiste enriquecimento e score no PostgreSQL.

## Contrato com n8n
- Agente roda o ciclo e **dispara via webhook n8n** a mensagem já redigida.
- n8n → Meta Cloud API (envio) e n8n → webhook inbound (resposta).
- Agente faz **poll** no estado (DB/caixa) para manter a conversa até agendar.

## Estado / persistência
- **PostgreSQL** (padrão Millani).
- Tabela `leads`: id, empresa, cnpj, contato (nome/telefone), segmento,
  rede_social, score, motivo, status, opt_out, consent_log, created_at,
  updated_at.
- Tabela `messages` (append-only): lead_id, direção (out/in), conteúdo,
  canal, timestamp, tipo (abordagem/resposta/agendamento).
- Tabela `events`: lead_id, google_event_id, start, end (quando agendado).
- Status: nao_contatado | contatado | respondeu | agendou | descartado.

## LGPD / conformidade
- Lead tratado como **dado pessoal**.
- `opt_out` por lead (bloqueia novo envio).
- `consent_log`: registro de abordagem e opt-out (append-only).
- **Zero PII em logs** (mascarar telefone/nome em logs de sistema).
- Mensagem de abordagem inclui identificação da empresa e via de opt-out.

## Respostas (loop two-way)
- Agente mantém a conversa: poll na caixa de entrada (via n8n → DB).
- Ao responder, qualifica interesse e conduz até o agendamento.
- Não desiste após 1ª mensagem; mantém até `agendou` ou `descartado`/opt-out.

## WhatsApp
- **Meta Cloud API** via n8n (envio e recebimento).
- Agente não fala direto com a Meta; consome/s grave estado no DB e o n8n
  faz a ponte.
- Ambiente: webhook n8n configurável por env (`N8N_WEBHOOK_URL`).

## Stack
- **Hermes** como orquestrador (CLI / cron / serviço).
- Módulos Python separados:
  - `scraper.py` — extração via Apify MCP.
  - `scorer.py` — enriquecimento + score LLM.
  - `sender.py` — redação da mensagem (LLM) + dispatch via webhook n8n.
  - `inbound.py` — poll de respostas + condução até agendamento.
  - `scheduler.py` — Google Calendar API (cria evento + invite).
  - `db.py` — camada PostgreSQL (SQLAlchemy ou psycopg).
- `.env.example` + `config.yaml` para segredos e parâmetros.

## Calendário
- **Google Calendar API**: ao aceite de horário, cria evento e envia invite
  por email/WhatsApp. (Simulável em dev sem credencial real.)

## Requisitos indispensáveis (R1–R10)
- R1. `scraper` extrai via Apify MCP por segmento+cidade → lead normalizado.
- R2. `scorer` enriquece (site/rede), detecta sistema atual, estima dor,
  score 0-100 + motivo; persiste.
- R3. `sender` redação LLM (1ª abordagem) + webhook n8n; marca `contatado`.
- R4. `inbound` poll + conduz conversa até agendar; qualifica interesse.
- R5. `scheduler` cria evento Google Calendar + invite no aceite.
- R6. Schema PostgreSQL: leads / messages / events conforme acima.
- R7. LGPD: opt-out, sem PII em log, consent_log append-only.
- R8. `.hermes.md` + documentação viva + `.env.example` + `config.yaml`.
- R9. Entrypoint Hermes/CLI que roda o ciclo:
  discover → enrich → qualify → send → poll → schedule.
- R10. Log de auditoria append-only de todo o ciclo (sem PII).

## Definição de "concluído" (MVP)
Um ciclo **ponta a ponta** roda num segmento (ex.: clínicas em cidade X):
extrai N leads → enriquece → qualifica → envia via webhook n8n (ou dry-run
simulado) → trata resposta → agenda no Google Calendar (ou dry-run) →
persiste em PostgreSQL → respeita LGPD/opt-out. CI verde, TDD desde o PR #1.

## Restrições
- Hermes orquestra; n8n é ponte, não orquestrador.
- Nunca enviar sem qualificação.
- LGPD/opt-out obrigatórios; sem PII em logs.
- Idioma: português.
- Padrão Millani: PostgreSQL, Python, TDD, CI P0/P1=0, auditável.
- Sem mocks em produção; dry-run explícito em dev.
