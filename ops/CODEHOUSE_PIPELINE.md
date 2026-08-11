# CodeHouse — Pipeline de Prospecção (Santa Maria / RS)

Dono: Pablo. Atende todos os segmentos (menos franquias). Vende site institucional,
CRM, ERP, automação de atendimento.

## Critério de qualificação (Pablo)
- **NÃO é "sem site".** É "tem site FEIO ou MUITO SIMPLES" → vender site institucional AGORA.
- **TODOS os não-qualificados** (site ok, sem site, franquia) são guardados em base
  separada para vender CRM/ERP/automação DEPOIS.
- Franquias excluídas (lista `FRANCHISE_HINTS` em leadsource.py).

## Apify — actor correto (descoberto na prática)
- ✅ `pimperp/apify-google-maps-scraper` — ÚNICO que retorna `phone` na conta.
  Campo de busca = `searchStrings` (array de strings). NÃO `searchStringsArray`.
- ❌ `compass/crawler-google-places` (default da conta) — NÃO retorna telefone.
- ❌ `apify/google-maps-scraper`, `tri_angle/...` — 404 na conta.
- ⚠️ Run frequentemente dá **TIMED-OUT (~280s)** mas devolve dataset PARCIAL.
  NÃO abortar: buscar o dataset mesmo assim (`_fetch_real` faz polling e baixa parcial).

## Pontuação de "feio/simples" (`score_site_ugliness` em leadsource.py)
Abre o `website` e pontua: google business.site (+5), sem CSS (+3), sem JS (+2),
html<15KB (+2), <2 imagens (+2). score>=5 => feio. Site que não abre => feio (90).
Manual: nomes em `manual_feio_names` forçam feio=True (ex.: "Bovinu's" apontado feio).

## WhatsApp — canal (DESBLOQUEADO, NÃO RESOLVIDO)
- Bridge estável no Windows = **Baileys** (`@whiskeysockets/baileys`), SEM Chrome.
  `whatsapp-web.js` 1.34 + Chrome 131/146 dá `TargetCloseError` / `Execution context destroyed`.
- QR: usar `qrcode-terminal` (ASCII no terminal). `qrcode.toFile` PNG sai CORROMPIDO.
- ❌ **PROBLEMA ABERTO:** conta de número pessoal com Baileys foi LIMITADA pelo WhatsApp
  (`sendMessage` trava/timeout, `stream error 515`, `conflict/replaced`). ToS violada.
  → Solução oficial: **Meta Cloud API** (business account + n8n webhook).
  `WHATSAPP_WEBHOOK_URL` no config.py já prevê isso.

## Regras do Pablo (obrigatórias)
1. Aprovar cada mensagem de PRIMEIRO CONTATO antes de enviar (modo confirmação).
2. Guardar TODOS os leads não-qualificados p/ venda futura de CRM/ERP/automação.
3. WhatsApp Web no número pessoal = risco de ban (já ocorreu limite) → usar Meta Cloud API.

## Estado atual (verificado)
- ✅ Pipeline corrigido (config.py + leadsource.py) — Apify real + filtro site feio.
- ✅ 4 leads qualificados salvos em `leads_qualificados_site.json`
  (Bella Trento, Bovinu's, Loja 7, Rafael Bortolaso).
- ✅ 11 leads não-qualificados salvos em `leads_base_crm_erp.json`.
- ✅ INTRO_MSG (Pablo, amigável, opt-out LGPD) em conversation.py.
- ✅ Google Agenda integrada (codehouse_book.py) — lê eventos OK.
- ❌ Envio WhatsApp travado (conta limitada). Aguarda destravar ou Meta Cloud API.

## Próximos passos
1. Migrar envio para Meta Cloud API (WHATSAPP_WEBHOOK_URL).
2. Quando canal OK, disparar os 4 qualificados com INTRO_MSG personalizado.
