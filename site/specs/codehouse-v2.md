# Code House — Landing Page v2 + Histórias Futuras
## Continuação do Ralph Loop após ship da v1

**Pré-requisito:** v1 (H-00 a H-18) aprovada no /review e deployed no Render.
**Data:** 2026-08-07

---

## V1 — Gaps descobertos na revisão

Estas histórias foram omitidas do spec v1 mas são necessárias antes ou imediatamente após o primeiro deploy.

---

### H-19 — Setup inicial do repositório
**Como** engenheiro, **quero** o repositório Git configurado corretamente desde o primeiro commit, **para** garantir rastreabilidade, colaboração e proteção do histórico.

**Critérios de aceitação:**
- [ ] Repositório criado no GitHub com nome `codehouse-landing`
- [ ] Branch padrão: `main`
- [ ] `.gitignore` cobrindo: `.DS_Store`, `node_modules/`, `*.log`, `.env`, `.env.local`
- [ ] `README.md` com: descrição do projeto, stack, como rodar localmente, como fazer deploy
- [ ] Branch protection em `main`: requer PR, pelo menos 1 aprovação (configurável depois se solo)
- [ ] Nenhum arquivo sensível (credenciais, números reais de WhatsApp, emails) no histórico Git
- [ ] Primeiro commit: apenas estrutura base, design system e `<head>` (H-00, H-15, H-12)
- [ ] Cada história subsequente = commit separado com mensagem descritiva

---

### H-20 — Substituição de placeholders antes do deploy
**Como** dono da Code House, **quero** que todos os dados reais estejam configurados antes da URL pública, **para** que nenhum visitante veja placeholder ou dado de teste.

**Critérios de aceitação:**
- [ ] Número do WhatsApp real substituído em H-07 e H-14 (buscar por `5500000000000`)
- [ ] Email de contato real no footer (H-08)
- [ ] URL canônica no `<link rel="canonical">` atualizada para o domínio real do Render
- [ ] OG image com URL real do domínio
- [ ] JSON-LD com URL e dados reais
- [ ] `sitemap.xml` com URL real
- [ ] Lighthouse rodado uma última vez após substituições para confirmar nada quebrou
- [ ] Checklist de "pronto para ship" assinado (um commit com mensagem `chore: substituir placeholders pré-deploy`)

---

## V2 — Funcionalidade e compliance

Fase após v1 estabilizada em produção.

---

### H-21 — Formulário com backend real (Formspree)
**Como** visitante que enviou o formulário, **quero** que minha mensagem chegue de verdade à Code House, **para** não depender de uma promessa de "em breve entraremos em contato" que nunca acontece.

**Critérios de aceitação:**
- [ ] Conta no Formspree criada com plano free (50 submits/mês)
- [ ] Endpoint do Formspree configurado no `action` do formulário
- [ ] Submit via `fetch` (POST JSON) — sem redirect, sem reload
- [ ] Estado de loading: botão desabilitado + label "Enviando..." durante o request
- [ ] Estado de sucesso: mensagem "Mensagem recebida! Em breve entraremos em contato." — igual à v1 mas agora com envio real
- [ ] Estado de erro de rede: mensagem "Não foi possível enviar. Tente pelo WhatsApp." com link direto
- [ ] Timeout de 10s: se o Formspree não responder, cai no estado de erro
- [ ] Email recebido no Formspree contém: Nome, Empresa, Mensagem, timestamp, IP (automático pelo Formspree)
- [ ] Sem exposição do endpoint Formspree no HTML público — usar variável de ambiente ou não importa (Formspree é público por design — aceitar)
- [ ] SPAM: Formspree tem proteção básica embutida — não implementar captcha adicional na v2
- [ ] Remoção do código de simulação de 800ms da v1

---

### H-22 — LGPD / Aviso de privacidade
**Como** visitante brasileiro, **quero** saber como meus dados são usados antes de preencher o formulário, **para** exercer meu direito à informação garantido pela LGPD (Lei 13.709/2018).

**Critérios de aceitação:**
- [ ] Banner de privacidade discreto no rodapé da página (não popup intrusivo):
  - [ ] Texto: "Ao usar este site e enviar formulários, você concorda com nossa [Política de Privacidade]."
  - [ ] Link para `/politica-de-privacidade` (H-23)
  - [ ] Botão "Entendi" que oculta o banner e persiste no `localStorage` (`ch-privacy-accepted`)
  - [ ] Banner não aparece se `ch-privacy-accepted = true`
- [ ] Abaixo do botão "Enviar mensagem" no formulário: texto pequeno "Seus dados são usados apenas para responder seu contato."
- [ ] Banner não bloqueia conteúdo — posição `sticky bottom` ou inline no footer
- [ ] Sem coleta de cookies de rastreamento na v2 (analytics ainda não instalado)

---

### H-23 — Página de política de privacidade
**Como** visitante preocupado com privacidade, **quero** ler como a Code House trata meus dados, **para** decidir se envio minhas informações de contato.

**Critérios de aceitação:**
- [ ] Arquivo `politica-de-privacidade.html` na raiz
- [ ] Mesmo design system da landing (design system importado ou inline)
- [ ] Nav simplificada: logo + link "Voltar ao início"
- [ ] Conteúdo obrigatório (simplificado, em linguagem humana):
  - [ ] Quais dados são coletados (nome, empresa, mensagem via formulário)
  - [ ] Para que são usados (apenas para responder o contato)
  - [ ] Quanto tempo são guardados (enquanto necessário para atendimento)
  - [ ] Com quem são compartilhados (Formspree para entrega do email — nomear)
  - [ ] Como exercer direitos: email de contato para `solicitar exclusão ou correção`
  - [ ] Data de última atualização
- [ ] `<title>`: "Política de Privacidade — Code House"
- [ ] `sitemap.xml` atualizado para incluir esta URL
- [ ] Rota adicionada no `render.yaml` se necessário

---

### H-24 — Analytics privado com Plausible
**Como** dono da Code House, **quero** entender como os visitantes interagem com a landing, **para** tomar decisões sobre o que melhorar sem rastrear ninguém com cookies.

**Critérios de aceitação:**
- [ ] Conta no Plausible criada (free trial 30 dias, depois pago ou self-hosted)
- [ ] Script do Plausible adicionado ao `<head>` com `defer` — 1KB, sem cookies
- [ ] Eventos customizados rastreados:
  - [ ] Clique em "Falar com a gente" (hero e nav)
  - [ ] Clique no botão WhatsApp flutuante
  - [ ] Clique no link WhatsApp da seção de contato
  - [ ] Submit bem-sucedido do formulário
  - [ ] Clique em "Ver exemplos"
- [ ] Sem rastreamento de dados pessoais (Plausible não rastreia por design)
- [ ] Banner LGPD (H-22) NÃO precisa mencionar analytics pois Plausible é cookieless
- [ ] Dashboard do Plausible configurado como público ou privado (decisão do dono)
- [ ] Script bloqueado em `localhost` — não polui dados com acessos de desenvolvimento
- [ ] Performance: script Plausible não bloqueia render (já vem com `defer` por padrão)

---

### H-25 — Menu hamburger mobile
**Como** visitante mobile, **quero** acessar todos os links de navegação em uma tela pequena, **para** não precisar rolar a página para encontrar as seções.

**Critérios de aceitação:**
- [ ] Botão hamburger (3 linhas SVG) visível em mobile (< 900px) à direita do logo
- [ ] Clique no hamburger: abre drawer ou dropdown com todos os links de navegação
- [ ] Links no menu: Serviços / Processo / Exemplos / Falar com a gente
- [ ] Clique em qualquer link do menu: fecha o menu e navega para a seção
- [ ] Clique fora do menu (no overlay): fecha o menu
- [ ] Tecla `Escape`: fecha o menu
- [ ] Foco armadilhado no menu quando aberto (acessibilidade — foco não sai do drawer)
- [ ] `aria-expanded` no botão hamburger: `true`/`false` conforme estado
- [ ] `aria-label="Abrir menu"` / `"Fechar menu"` no botão
- [ ] Animação de abertura: slide down ou fade — respeita `prefers-reduced-motion`
- [ ] Menu não empurra o conteúdo da página — `position: fixed` ou `absolute`
- [ ] Z-index acima de tudo exceto modais

---

### H-26 — GitHub Actions CI
**Como** engenheiro, **quero** que cada PR e merge na `main` passe por validações automáticas, **para** não fazer ship de código com erros regressivos sem perceber.

**Critérios de aceitação:**
- [ ] Arquivo `.github/workflows/ci.yml` criado
- [ ] Trigger: `push` e `pull_request` na branch `main`
- [ ] Jobs do workflow:
  - [ ] **validate-html**: executar `html-validate` ou `htmlhint` no `index.html` e `404.html`
  - [ ] **lighthouse-ci**: rodar Lighthouse CI e verificar thresholds (Performance ≥ 90, A11y ≥ 90, SEO ≥ 90)
  - [ ] **link-check**: verificar âncoras internas quebradas (IDs referenciados existem)
- [ ] Falha em qualquer job bloqueia merge no PR (se branch protection ativa)
- [ ] Lighthouse CI configurado com `lighthouserc.json` na raiz com thresholds explícitos
- [ ] Workflow tem `timeout-minutes: 10` para não consumir Actions desnecessariamente
- [ ] Resultado do Lighthouse CI postado como comentário no PR (opcional mas recomendado)

---

## V3 — Crescimento e expansão

Fase após v2 estabilizada. Prioridade definida pelo tráfego e conversões reais.

---

### H-27 — Depoimentos reais de clientes
**Como** visitante avaliando a Code House, **quero** ler o que clientes reais acharam do trabalho, **para** ter prova social antes de contratar.

**Pré-requisito:** Existir pelo menos 2 depoimentos reais com autorização por escrito do cliente.

**Critérios de aceitação:**
- [ ] Seção entre H-06 (exemplos) e H-07 (contato)
- [ ] Eyebrow: `// o que dizem nossos clientes`
- [ ] Grid de cards: foto (opcional, com permissão), nome, cargo, empresa, texto do depoimento
- [ ] Sem foto inventada ou stock photo — campo é omitido se não tiver foto real
- [ ] Texto do depoimento: exatamente o que o cliente escreveu (sem edição de conteúdo)
- [ ] Máximo 3 cards na v3 — expansão com paginação ou slider na v4
- [ ] Autorização documentada internamente (não precisa estar no código)

---

### H-28 — Portfólio / Cases de sucesso
**Como** visitante técnico ou gestor, **quero** ver casos reais de sistemas entregues pela Code House, **para** avaliar a capacidade de execução antes de contratar.

**Pré-requisito:** Ter pelo menos 1 case documentado com autorização do cliente.

**Critérios de aceitação:**
- [ ] Página `/cases` ou `/portfolio` separada
- [ ] Link "Ver cases" adicionado na nav e no footer
- [ ] Cada case: nome do projeto (anonimizado se necessário), setor, problema, solução, resultado mensurável
- [ ] Screenshots reais do sistema (ou mockups se cliente não autorizou screenshot)
- [ ] Tags de tecnologia usada
- [ ] Link de volta para a landing
- [ ] SEO da página de cases: title, description, OG

---

### H-29 — Domínio customizado e DNS
**Como** dono da Code House, **quero** a landing acessível em `codehouse.com.br` (ou equivalente), **para** ter identidade profissional e não depender de URL do Render.

**Critérios de aceitação:**
- [ ] Domínio adquirido e configurado no Registro.br ou similar
- [ ] DNS apontado para os IPs/CNAME do Render
- [ ] HTTPS automático funcionando no domínio customizado (Render provisiona via Let's Encrypt)
- [ ] Redirect `www.codehouse.com.br` → `codehouse.com.br` (ou vice-versa — escolher canonical)
- [ ] `<link rel="canonical">`, OG, JSON-LD e `sitemap.xml` atualizados com o novo domínio
- [ ] `render.yaml` atualizado com o domínio
- [ ] Redirect do domínio temporário do Render para o domínio real (301)

---

### H-30 — Dados legais no footer
**Como** visitante que precisa validar a empresa antes de contratar, **quero** ver os dados legais da Code House no rodapé, **para** ter confiança de que é uma empresa formal.

**Pré-requisito:** CNPJ formalizado (MEI, LTDA ou equivalente).

**Critérios de aceitação:**
- [ ] CNPJ no footer em monospace faint
- [ ] Razão social (se diferente do nome fantasia)
- [ ] Estado/cidade de atuação
- [ ] Link para a política de privacidade (H-23) no footer
- [ ] Não incluir endereço completo se trabalho for remoto (opcional)

---

### H-31 — Testes E2E com Playwright
**Como** engenheiro, **quero** testes automatizados cobrindo os fluxos críticos da landing, **para** detectar regressões antes de qualquer deploy.

**Critérios de aceitação:**
- [ ] Playwright instalado como devDependency
- [ ] Script `npm test` ou `npx playwright test` executa os testes
- [ ] Testes críticos:
  - [ ] Navegação: clicar em cada link da nav ancora na seção correta
  - [ ] Formulário — caminho feliz: preencher nome + mensagem + submeter → ver mensagem de sucesso
  - [ ] Formulário — erro: submeter vazio → ver mensagens de erro nos campos obrigatórios
  - [ ] Dark mode: clicar no toggle → verificar `data-theme="dark"` no `<html>`
  - [ ] WhatsApp button: verificar que o link tem `href` contendo `wa.me`
  - [ ] Mobile 375px: verificar que links da nav estão ocultos
- [ ] Testes rodam no CI (H-26 atualizado para incluir `playwright test`)
- [ ] Screenshots de falha salvas como artifacts no CI
- [ ] Sem testes frágeis que dependem de texto exato de UI que muda frequentemente

---

## Critérios de rejeição — v2 e v3

### P0
- Backend do formulário (H-21) envia mensagem para email errado
- Política de privacidade (H-23) não menciona o Formspree como processador de dados
- Domínio customizado (H-29) sem HTTPS

### P1
- Analytics (H-24) rastreia antes do banner LGPD ser aceito
- Menu hamburger (H-25) sem foco armadilhado (foco sai do drawer sem fechar)
- CI (H-26) falha silenciosamente sem bloquear merge
- Depoimentos (H-27) com foto sem autorização documentada

---

## Ordem de implementação — v2

1. **H-19** — Setup do repositório (se não feito)
2. **H-20** — Substituição de placeholders
3. **H-21** — Formulário com Formspree
4. **H-22** — Aviso LGPD
5. **H-23** — Política de privacidade
6. **H-24** — Plausible analytics
7. **H-25** — Menu hamburger
8. **H-26** — GitHub Actions CI

## Ordem de implementação — v3 (prioridade por impacto real)

1. **H-29** — Domínio customizado (impacto de credibilidade imediato)
2. **H-27** — Depoimentos reais (quando existirem)
3. **H-30** — Dados legais (quando CNPJ formalizado)
4. **H-28** — Cases/portfólio (quando tiver cases documentados)
5. **H-31** — Testes E2E (quando CI estiver ativo)
