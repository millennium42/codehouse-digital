# Deploy Code House — Site v6

## Pré-requisitos (já feitos)

- [x] Repositório GitHub: `github.com/millennium42/codehouse-digital`
- [x] `render.yaml` configurado em `/site`
- [x] Formspree conectado (ID: `xaewbejg`)
- [x] Sem dados inventados, mockups demo
- [x] CSS responsivo, dark-first, FAQ accordion, WhatsApp flutuante

## Como fazer deploy (Pablo)

### Opção A: Render (Recomendado — tem `render.yaml`)

1. Acessar https://dashboard.render.com
2. Criar conta com GitHub (Login with GitHub)
3. New + → Web Service
4. Conectar repositório: `millennium42/codehouse-digital`
5. Configurar:
   - **Name**: `code-house-landing`
   - **Root Directory**: `site`
   - **Environment**: `Static`
   - **Build Command**: (vazio)
   - **Publish Directory**: `./`
6. Criar Web Service
7. Aguardar deploy (1-2 min)
8. Acessar: `https://code-house-landing.onrender.com`

### Opção B: Netlify Drop (mais rápido, sem automação)

1. Acessar https://app.netlify.com/drop
2. Arrastar a pasta `/site` para a página
3. Pronto! URL aleatória `https://[random].netlify.app`

### Opção C: GitHub Pages (manual via Actions)

1. GitHub → Settings → Pages
2. Source: Deploy from branch → `main` → `/site` folder
3. Save → aguardar 2-3 min
4. Acessar: `https://millennium42.github.io/codehouse-digital/site/`

## Pós-deploy

- [ ] Testar formulário (enviar mensagem, ver se chega no email do Pablo)
- [ ] Testar WhatsApp flutuante
- [ ] Testar dark/light toggle
- [ ] Testar responsivo (mobile)
- [ ] Atualizar `canonical` e `og:url` quando tiver domínio customizado

## Domínio customizado futuro

Quando registrar `codehouse.com.br`:

1. No Render: Settings → Custom Domain → `codehouse.com.br`
2. Atualizar DNS conforme instrução do Render
3. No site/index.html:
   - `<!-- canonical... -->` → `<link rel="canonical" href="https://codehouse.com.br">`
   - `<meta property="og:url" content="/">` → `<meta property="og:url" content="https://codehouse.com.br">`
   - `"url": "/"` → `"url": "https://codehouse.com.br"`
4. Commit + push → deploy automático
