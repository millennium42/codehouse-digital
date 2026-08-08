# Code House — Landing Page
## Spec completo para o Ralph Loop — v2

**Objetivo:** Landing page de apresentação da Code House para pequenas empresas.
**Deploy:** Render (static site)
**Data:** 2026-08-07
**Definição de "concluído":** Página publicada no Render, responsiva, dark/light mode, formulário funcional, Core Web Vitals no green, sem bug P0/P1.

---

## Contexto do produto

A Code House entrega soluções de TI personalizadas para pequenas empresas (CRM, ERP, site institucional, e-shop e sob medida). O diferencial é adaptar o sistema ao fluxo e linguagem do cliente — não impor um template genérico. A marca fala por si: sem rosto de fundador, sem foto pessoal. O que convence é a identidade visual e os exemplos de sistemas que a empresa pode construir.

---

## Personas

- **Pedro** — dono de loja física, nunca contratou sistema, quer saber "o que vocês fazem e como começo"
- **Marina** — gerente de PME, já usou ERP engessado, busca flexibilidade e sistema que entenda o negócio dela
- **Thiago** — gestor de e-commerce pequeno, quer loja virtual com identidade própria e gestão de pedidos

---

## Histórias de usuário

---

### H-00 — Design system e tokens CSS
**Como** engenheiro implementando a landing, **quero** um sistema de tokens CSS definido antes de qualquer componente, **para** garantir consistência visual em toda a página e facilitar dark/light mode.

**Critérios de aceitação:**
- [ ] Paleta definida em variáveis `:root`:
  - `--bg`: `#F0F4F8` — fundo principal (off-white com bias azul)
  - `--surface`: `#E2EBF4` — superfícies elevadas
  - `--surface-raised`: `#FAFCFE` — cards e mockups
  - `--cloud`: `#3E82AB` — accent principal (azul nuvem)
  - `--cloud-hover`: `#2E6E95` — estado hover do accent
  - `--cloud-light`: `#6AAFD6` — accent claro
  - `--cloud-faint`: `#C0D8EC` — accent muito suave (backgrounds de destaque)
  - `--ink`: `#17232E` — texto principal
  - `--ink-muted`: `#4A6275` — texto secundário
  - `--ink-faint`: `#7A9AAF` — texto terciário / labels
  - `--border`: `#B4CCE0` — bordas padrão
  - `--border-strong`: `#7AADC8` — bordas de destaque
- [ ] Tipografia definida em variáveis:
  - `--font-sans`: `system-ui, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif`
  - `--font-mono`: `'Courier New', 'Courier', monospace`
- [ ] Escala de espaçamento baseada em múltiplos de 4px (0.25rem)
- [ ] Border-radius padrão: 2px (brutalista leve)
- [ ] Nenhum componente usa cor ou fonte hardcoded fora dos tokens (exceto tags de status que têm semântica própria)
- [ ] Arquivo CSS organizado: tokens → reset → utilitários → componentes → layout → responsividade

---

### H-01 — Navegação global
**Como** visitante, **quero** uma barra de navegação fixa com links para as seções, **para** acessar qualquer parte da página sem perder contexto de onde estou.

**Critérios de aceitação:**
- [ ] Logo `CODE.HOUSE` em monospace à esquerda; ponto separador na cor `--cloud`
- [ ] Clique no logo ancora ao topo da página (`#top` ou `href="#"`)
- [ ] Links de navegação: Serviços / Processo / Exemplos / "Falar com a gente"
- [ ] "Falar com a gente" estilizado como CTA: borda azul nuvem; hover → preenchimento sólido azul, texto fundo
- [ ] Barra `position: sticky; top: 0` — segue o scroll sem sobrepor conteúdo
- [ ] `background: var(--bg)` + `border-bottom: 1px solid var(--border)`
- [ ] `z-index` suficiente para ficar acima de todos os elementos da página
- [ ] Em mobile (< 900px): apenas logo + botão "Falar com a gente"; demais links ocultados
- [ ] Focus visível (outline) em todos os itens — navegação por teclado funcional
- [ ] Links são âncoras HTML (`<a href="#id-da-secao">`) — não JS puro
- [ ] Cada seção destino tem `id` correspondente ao link da nav

---

### H-02 — Hero — mensagem principal
**Como** visitante que chegou pela primeira vez, **quero** entender em 5 segundos o que a Code House faz e para quem, **para** decidir se vale continuar lendo.

**Critérios de aceitação:**
- [ ] Layout em duas colunas (desktop): texto à esquerda (proporção 1.1), mockup à direita (proporção 0.9)
- [ ] Eyebrow em monospace uppercase com traço decorativo: "Soluções Personalizadas em TI"
- [ ] Headline H1: "Sistemas feitos para o *seu* jeito de trabalhar." — "seu" em `var(--cloud)`
- [ ] H1 é único em toda a página
- [ ] Subtítulo (1 parágrafo): menciona CRM, ERP, lojas virtuais e sites; reforça personalização vs template genérico
- [ ] Dois botões em linha: "Falar com a gente" (sólido) + "Ver exemplos" (outline)
- [ ] Botão "Falar com a gente" ancora para `#contato`
- [ ] Botão "Ver exemplos" ancora para `#exemplos`
- [ ] Fade-in suave no mockup ao carregar (apenas se `prefers-reduced-motion: no-preference`)
- [ ] Em mobile (< 900px): layout em coluna única; mockup aparece antes do texto (impacto visual imediato)
- [ ] Padding top do hero leva em conta a altura da nav sticky (sem sobreposição)

---

### H-03 — Hero mockup — preview CRM
**Como** visitante, **quero** ver um preview visual real de como um sistema CRM da Code House parece, **para** sentir a qualidade concretamente antes de ler mais.

**Critérios de aceitação:**
- [ ] Elemento decorativo (não clicável, não interativo) — `aria-hidden="true"`
- [ ] "Janela de app" com barra de título: dots coloridos (vermelho/amarelo/verde) + label "CRM — Clientes" em monospace
- [ ] Sidebar esquerda com 5 itens: Clientes (ativo), Negócios, Tarefas, Relatórios, Config
- [ ] Item ativo: fundo `--cloud-faint`, texto `--cloud`, borda lateral esquerda 2px `--cloud`
- [ ] Área de conteúdo com:
  - [ ] Header "Clientes ativos" + badge "42 registros"
  - [ ] Grid de 3 stat cards: Total 42 (accent) / Novos 7 / Taxa 94%
  - [ ] Tabela com 4 linhas: Nome / Empresa / Status (tag "Ativo" em verde-água / "Proposta" em azul)
  - [ ] Texto da tabela em escala reduzida (0.6–0.65rem)
- [ ] Mockup usa exclusivamente variáveis de token — funciona em dark e light mode
- [ ] Bordas do mockup em `--border`, sem `border-radius` maior que 4px
- [ ] Em mobile: mockup é reduzido para caber na largura (não causa scroll horizontal)

---

### H-04 — Seção de serviços
**Como** visitante, **quero** ver as soluções que a Code House oferece com descrição clara de cada uma, **para** identificar se têm o que eu preciso sem ter que ligar ou perguntar.

**Critérios de aceitação:**
- [ ] Eyebrow monospace: `// serviços`
- [ ] Título H2: "O que a Code House entrega"
- [ ] Grid horizontal com 5 colunas separadas por `border: 1px solid var(--border)` — sem shadow, `border-radius: 2px`
- [ ] Cada card: ícone SVG inline próprio (não icon-font) + nome em monospace uppercase + descrição curta
- [ ] Serviços e descrições exatas:
  1. **CRM** — "Gestão de clientes, funil de vendas e histórico de relacionamento."
  2. **ERP** — "Controle integrado de estoque, financeiro, compras e operações."
  3. **Site Institucional** — "Presença digital com identidade visual e conteúdo da sua empresa."
  4. **E-shop** — "Loja virtual com catálogo, pagamentos e gestão de pedidos."
  5. **Sob Medida** — "Qualquer solução de TI adaptada ao seu processo, do zero."
- [ ] Hover sutil: `background: var(--surface)` — sem transformações ou sombras
- [ ] Ícones SVG: stroke `currentColor`, sem fill sólido, tamanho 16×16
- [ ] Em mobile < 900px: grid 2 colunas com `border-bottom` entre linhas
- [ ] Em mobile < 600px: grid 1 coluna
- [ ] Seção tem `id="servicos"` para âncora da nav

---

### H-05 — Seção de processo
**Como** visitante, **quero** entender como funciona o processo de trabalho da Code House, **para** saber o que esperar ao contratar — sem surpresas.

**Critérios de aceitação:**
- [ ] Eyebrow monospace: `// como funciona`
- [ ] Título H2: "Do problema à solução em três etapas"
- [ ] Grid de 3 colunas separadas por `border` — mesmo padrão visual dos serviços
- [ ] Cada etapa: número em monospace faint (texto "Etapa 01") + título H3 + parágrafo descritivo
- [ ] Etapas exatas:
  1. **Entendemos seu negócio** — conversamos sobre fluxo, gargalos e o que você quer automatizar ou organizar melhor
  2. **Construímos a solução** — sistema personalizado com a sua linguagem, seu fluxo e suas regras; não um template com funcionalidades genéricas
  3. **Acompanhamos o crescimento** — suporte contínuo, melhorias conforme o negócio evolui e novas necessidades aparecem
- [ ] Numeração como informação ("Etapa 01"), não como ornamento visual
- [ ] Em mobile: 1 coluna com `border-bottom` entre etapas; última sem border
- [ ] Seção tem `id="processo"` para âncora da nav

---

### H-06 — Seção de exemplos de sistemas
**Como** visitante, **quero** ver previews visuais dos sistemas que a Code House constrói, **para** ter confiança na qualidade e na capacidade técnica antes de entrar em contato.

**Critérios de aceitação:**
- [ ] Eyebrow monospace: `// exemplos de sistemas`
- [ ] Título H2: "O que sistemas feitos assim parecem"
- [ ] Grid 2×2 com 4 cards de exemplo
- [ ] Cada card: header (nome + badge "Personalizado"/"Sob medida") + área de preview com mockup CSS puro
- [ ] **Card 1 — CRM / Funil de vendas:**
  - Tabela: Cliente / Etapa / Valor / Status
  - 5 linhas de dados com valores reais (nomes fictícios de empresas brasileiras)
  - Tags de status com cores semânticas (aguardando/fechado)
- [ ] **Card 2 — ERP / Painel operacional:**
  - Gráfico de barras CSS (6 meses, Jan–Jun) com barras do período atual em destaque `--cloud`
  - Row de 3 stat cards: Estoque / Pedidos (accent) / Saldo
- [ ] **Card 3 — E-shop / Catálogo:**
  - Grid 3×2 de mini cards de produto (placeholder gradiente + nome + preço em monospace)
  - Último item com borda tracejada e label "+ item" (simula estado vazio)
- [ ] **Card 4 — Site institucional:**
  - Mini navbar escura + bloco hero com texto + linhas de conteúdo + par de botões (solid/outline)
- [ ] Todos os mockups: variáveis de token apenas, nenhuma cor hardcoded
- [ ] Nenhum mockup clicável ou interativo — todos `aria-hidden="true"`
- [ ] Em mobile: grid 1 coluna; mockups com `overflow-x: auto` se necessário
- [ ] Seção tem `id="exemplos"` para âncora da nav e botão do hero

---

### H-07 — Seção de contato
**Como** visitante interessado, **quero** entrar em contato com a Code House pela forma que preferir (formulário ou WhatsApp), **para** iniciar o projeto sem atrito.

**Critérios de aceitação:**
- [ ] Seção com fundo `var(--surface)` — diferenciação visual clara do restante
- [ ] Layout 2 colunas (desktop): copy à esquerda + formulário à direita
- [ ] Copy à esquerda:
  - [ ] Eyebrow: "Vamos conversar"
  - [ ] Headline H2: "Seu sistema ainda não existe. A gente constrói."
  - [ ] Subtítulo: convida a descrever o negócio; reforça personalização
  - [ ] Link WhatsApp abaixo do subtítulo: ícone SVG + "Prefere pelo WhatsApp?" → abre `https://wa.me/[número]` em nova aba
- [ ] Formulário:
  - [ ] Campo Nome (obrigatório)
  - [ ] Campo Empresa (opcional)
  - [ ] Campo Textarea "O que você precisa?" (obrigatório)
  - [ ] Labels em monospace uppercase acima dos campos
  - [ ] `border-color: var(--cloud)` ao `:focus` em todos os inputs
  - [ ] Placeholder text em `var(--ink-faint)`
  - [ ] Botão "Enviar mensagem" — sólido azul nuvem, largura auto (não full-width)
- [ ] Validação de submit:
  - [ ] Campos obrigatórios vazios: exibe mensagem de erro inline abaixo do campo
  - [ ] Mensagens de erro em linguagem simples: "Informe seu nome para continuarmos"
  - [ ] Sem validação excessiva (empresa é opcional — nunca bloqueia)
- [ ] Estado de sucesso: exibe mensagem inline "Mensagem recebida! Em breve entraremos em contato." sem reload
  - [ ] Formulário some ou é substituído pela mensagem de sucesso (não fica visível por baixo)
- [ ] Submit sem backend — sem chamada real de rede; simula sucesso após 800ms para dar sensação de processamento
- [ ] Inputs: sem XSS — `textContent` para exibir qualquer valor lido do form, nunca `innerHTML`
- [ ] Em mobile: layout coluna única; link WhatsApp em destaque acima do formulário
- [ ] Seção tem `id="contato"` para âncoras da nav e botão do hero

---

### H-08 — Footer
**Como** visitante, **quero** um rodapé com informações básicas da empresa e links de navegação, **para** ter referência e credibilidade ao final da leitura.

**Critérios de aceitação:**
- [ ] `border-top: 1px solid var(--border)` separando do conteúdo
- [ ] Layout 2 colunas: esquerda (identidade) e direita (links)
- [ ] Esquerda:
  - [ ] Logo `CODE.HOUSE` em monospace
  - [ ] Tagline curta: "Soluções de TI para quem precisa de resultado, não de planilha."
  - [ ] Link WhatsApp em monospace faint
  - [ ] Email de contato em monospace faint (sem `mailto:` se ainda não definido — usar placeholder)
- [ ] Direita:
  - [ ] Links de navegação: Serviços / Processo / Exemplos / Contato
  - [ ] Todos em monospace uppercase faint com hover `--cloud`
- [ ] Linha final (abaixo de tudo): "© 2026 Code House — Soluções em TI" centralizado ou à esquerda
- [ ] Em mobile: coluna única; identidade acima, links abaixo, copyright por último
- [ ] Sem CNPJ ou dados legais por enquanto (fora de escopo v1) — lista na seção "Fora de escopo"

---

### H-09 — Dark mode e Light mode
**Como** visitante, **quero** que a página respeite minha preferência de tema do sistema e permita troca manual, **para** ter conforto visual em qualquer ambiente.

**Critérios de aceitação:**
- [ ] Tokens CSS em `:root` (light mode — padrão)
- [ ] Override via `@media (prefers-color-scheme: dark)` redefinindo apenas os tokens
- [ ] Override via `:root[data-theme="dark"]` e `:root[data-theme="light"]` — toggle manual vence o media query em ambas direções
- [ ] `data-theme` aplicado no elemento `<html>`, não em `<body>`
- [ ] Toggle (botão sol/lua) visível na nav em desktop — ícone SVG, sem texto
- [ ] Ao clicar no toggle: alterna o atributo `data-theme` no `<html>` e persiste no `localStorage` com key `ch-theme`
- [ ] Ao carregar a página: lê `localStorage` e aplica o tema salvo antes do primeiro render (script inline no `<head>` para evitar flash)
- [ ] Dark mode não é inversão: azul nuvem `--cloud` levemente mais claro no dark para manter legibilidade em fundo escuro
- [ ] Contraste verificado em ambos os temas (critério H-11)
- [ ] Nenhum elemento usa cor hardcoded fora dos tokens (exceto cores semânticas das tags de status)
- [ ] Mockups CSS dos exemplos funcionam em ambos os temas sem CSS duplicado

---

### H-10 — Responsividade
**Como** visitante mobile, **quero** que a página seja completamente utilizável em qualquer tamanho de tela, **para** não precisar dar zoom ou scrollar horizontalmente.

**Critérios de aceitação:**
- [ ] Breakpoints definidos:
  - `900px`: colapsa grids de 2+ colunas; nav simplificada
  - `600px`: colapsa grid de serviços para 1 coluna
- [ ] Nenhum elemento causa `overflow-x` no body em nenhum breakpoint
- [ ] Wide content (tabelas, mockups) com `overflow-x: auto` no próprio container
- [ ] Hero: coluna única em mobile; mockup antes do texto
- [ ] Todos os botões e inputs: `min-height: 44px` (toque adequado — iOS HIG)
- [ ] Links de navegação mobile: apenas logo + CTA (sem menu hamburger — fora de escopo v1)
- [ ] Texto: sem `font-size` menor que 14px em mobile
- [ ] Testado e verificado em:
  - [ ] 375×667px — iPhone SE (portrait)
  - [ ] 375×812px — iPhone SE (landscape) — sem scroll horizontal
  - [ ] 768×1024px — tablet portrait
  - [ ] 1280×800px — desktop
- [ ] Imagens e mockups com `max-width: 100%` — nunca estouram o container

---

### H-11 — Acessibilidade e performance
**Como** visitante com necessidades específicas ou conexão lenta, **quero** que a página seja acessível e carregue rápido, **para** ter boa experiência independente do dispositivo ou condição.

**Acessibilidade:**
- [ ] Focus visível em todos os elementos interativos (nav, botões, inputs, links, toggle de tema)
- [ ] `prefers-reduced-motion`: fade-in e `scroll-behavior: smooth` desabilitados; sem outras animações
- [ ] Contraste WCAG AA: ≥ 4.5:1 para texto normal, ≥ 3:1 para texto grande (≥ 18px/bold ou ≥ 24px)
- [ ] Verificar contraste em ambos os temas (light e dark)
- [ ] SVGs decorativos: `aria-hidden="true"`
- [ ] SVGs informativos: `role="img"` + `aria-label`
- [ ] Botões que só têm ícone (toggle de tema): `aria-label` descritivo
- [ ] Mockups de app: `aria-hidden="true"` (decorativos)
- [ ] Formulário: cada input tem `<label>` associado via `for`/`id` — sem `placeholder` como substituto de label
- [ ] `<html lang="pt-BR">`
- [ ] Estrutura de headings: H1 único → H2 por seção → H3 dentro de seção

**Performance (Core Web Vitals — thresholds green):**
- [ ] LCP (Largest Contentful Paint): < 2.5s
- [ ] CLS (Cumulative Layout Shift): < 0.1
- [ ] INP (Interaction to Next Paint): < 200ms
- [ ] Sem JavaScript de terceiros no caminho crítico
- [ ] CSS inline no `<head>` ou `<style>` único — sem `@import` externo
- [ ] Sem fontes externas (CDN bloqueado) — apenas system fonts
- [ ] Página funcional sem JavaScript (formulário: fallback para `mailto:` link ou mensagem)
- [ ] Imagens (se houver): formato WebP, `loading="lazy"` fora do hero

---

### H-12 — SEO e metadados
**Como** dono da Code House, **quero** que a página tenha metadados completos, **para** que Google e redes sociais indexem e compartilhem corretamente.

**Critérios de aceitação:**
- [ ] `<meta charset="utf-8">`
- [ ] `<meta name="viewport" content="width=device-width, initial-scale=1">`
- [ ] `<title>`: "Code House — Soluções Personalizadas em TI para Pequenas Empresas"
- [ ] `<meta name="description">`: até 160 caracteres — menciona CRM, ERP, e-shop, site institucional, personalizado
- [ ] `<link rel="canonical" href="[URL da página]">`
- [ ] Open Graph:
  - `og:type`: `website`
  - `og:title`: mesmo do `<title>`
  - `og:description`: mesmo do description
  - `og:url`: URL canônica
  - `og:image`: placeholder `1200×630px` — imagem da marca (criar asset simples)
  - `og:locale`: `pt_BR`
  - `og:site_name`: `Code House`
- [ ] Twitter Card:
  - `twitter:card`: `summary_large_image`
  - `twitter:title`, `twitter:description`, `twitter:image`
- [ ] JSON-LD (structured data) no `<head>`:
  ```json
  {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Code House",
    "description": "...",
    "url": "...",
    "serviceType": ["CRM", "ERP", "E-commerce", "Site Institucional"]
  }
  ```
- [ ] H1 único, hierarquia de headings correta (H1 → H2 → H3), sem saltos
- [ ] `robots.txt` na raiz: permite indexação de tudo
- [ ] `sitemap.xml` na raiz: uma URL (a própria landing)

---

### H-13 — Deploy no Render
**Como** dono da Code House, **quero** a landing publicada no Render com configuração rastreável como código, **para** ter URL pública, HTTPS e auto-deploy confiável.

**Critérios de aceitação:**
- [ ] `index.html` na raiz do repositório Git
- [ ] `render.yaml` na raiz definindo o serviço:
  ```yaml
  services:
    - type: web
      name: codehouse-landing
      env: static
      staticPublishPath: .
      buildCommand: ""
      routes:
        - type: rewrite
          source: /404
          destination: /404.html
  ```
- [ ] Branch de deploy: `main`
- [ ] Auto-deploy ativo a cada push na `main`
- [ ] HTTPS ativo (padrão Render — verificar após primeiro deploy)
- [ ] Headers HTTP configurados via `_headers` file na raiz:
  ```
  /*
    X-Frame-Options: DENY
    X-Content-Type-Options: nosniff
    Referrer-Policy: strict-origin-when-cross-origin
    Cache-Control: public, max-age=3600
  /index.html
    Cache-Control: no-cache
  ```
- [ ] URL de health check: raiz `/` retorna 200
- [ ] Rollback: qualquer deploy anterior acessível via histórico de deploys do Render
- [ ] Domínio customizado: configurar se disponível (fora de escopo v1 se não houver domínio)

---

### H-14 — CTA flutuante WhatsApp
**Como** visitante em qualquer ponto da página, **quero** um botão de acesso rápido ao WhatsApp sempre visível, **para** entrar em contato sem precisar rolar até a seção de contato.

**Critérios de aceitação:**
- [ ] Botão fixo `position: fixed`, canto inferior direito, `bottom: 1.5rem; right: 1.5rem`
- [ ] Ícone SVG do WhatsApp (verde `#25D366`) + fundo branco/escuro dependendo do tema
- [ ] `width: 52px; height: 52px; border-radius: 50%`
- [ ] `box-shadow` sutil para destacar do conteúdo
- [ ] Link `href="https://wa.me/[número]"` com `target="_blank" rel="noopener noreferrer"`
- [ ] `aria-label="Conversar pelo WhatsApp"`
- [ ] Tooltip ao hover: "Falar pelo WhatsApp" — CSS puro, sem biblioteca
- [ ] Não cobre conteúdo importante em mobile (testar nas posições de scroll)
- [ ] `z-index` acima de todo conteúdo mas abaixo de modais (se houver)
- [ ] Número do WhatsApp: placeholder `5500000000000` — substituir antes do deploy

---

### H-15 — Favicon e assets básicos
**Como** visitante, **quero** que a aba do browser mostre ícone e nome da Code House, **para** identificar a aba facilmente entre outras abertas.

**Critérios de aceitação:**
- [ ] Favicon SVG inline no `<head>` usando `data:` URI: fundo azul nuvem (`--cloud`) + letra "C" em branco em monospace
- [ ] `<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,...">`
- [ ] Fallback PNG 32×32 (opcional, se SVG não for suportado)
- [ ] `<link rel="apple-touch-icon">` 180×180 (placeholder aceitável na v1)
- [ ] `<meta name="theme-color" content="#3E82AB">` — cor da barra do browser em mobile
- [ ] OG image (para H-12): imagem estática simples `og-image.png` — fundo azul nuvem + "CODE.HOUSE" em branco; gerada e commitada no repositório

---

### H-16 — Seção de credibilidade
**Como** visitante avaliando a Code House, **quero** ver indicadores de que a empresa é confiável e experiente, **para** ter segurança ao entrar em contato.

**Critérios de aceitação:**
- [ ] Seção entre processo e exemplos (ou após os exemplos — decidir na implementação)
- [ ] Sem fotos de pessoas, sem depoimentos falsos, sem logos inventados de clientes
- [ ] Conteúdo permitido (apenas o que for verdadeiro):
  - [ ] Número de projetos entregues (ex: "Mais de X sistemas entregues" — se verdadeiro)
  - [ ] Áreas de atuação (ex: "Projetos em varejo, saúde, serviços e educação")
  - [ ] Comprometimento com entrega (ex: "Cada sistema é único. Sem templates.")
  - [ ] Garantia de suporte (ex: "Acompanhamos após o lançamento")
- [ ] Layout: 3–4 itens em grid horizontal, cada um com número/icon + texto curto
- [ ] Se não houver dados reais suficientes, substituir por 3 diferenciais objetivos da Code House (personalização, flexibilidade, acompanhamento)
- [ ] **Regra:** nada nessa seção pode ser inverídico. Em caso de dúvida, omitir o dado.

---

### H-17 — Página 404 customizada
**Como** visitante que acessou uma URL inexistente, **quero** ver uma página 404 da Code House, **para** não me perder e poder voltar ao conteúdo.

**Critérios de aceitação:**
- [ ] Arquivo `404.html` na raiz do repositório
- [ ] Mesmo design system da landing (CSS compartilhado ou inline)
- [ ] Conteúdo: logo + mensagem amigável + link de volta para a home
- [ ] Sem nav completa — apenas logo e um botão "Voltar para o início"
- [ ] Configurado no `render.yaml` (H-13 já inclui a rota)
- [ ] `<title>`: "Página não encontrada — Code House"
- [ ] Mensagem sugerida: "Esta página não existe. Mas a solução que você precisa, a gente constrói."

---

### H-18 — Performance — Core Web Vitals
**Como** dono da Code House, **quero** que a página atinja os thresholds green do Google, **para** ter boa pontuação de SEO e experiência rápida para todos os visitantes.

**Critérios de aceitação:**
- [ ] LCP < 2.5s medido no Lighthouse (mobile e desktop)
- [ ] CLS < 0.1 — sem layout shift após carregamento
- [ ] INP < 200ms — interações respondem rápido
- [ ] Lighthouse Performance Score ≥ 90 (mobile)
- [ ] Lighthouse Accessibility Score ≥ 90
- [ ] Lighthouse SEO Score ≥ 90
- [ ] Lighthouse Best Practices Score ≥ 90
- [ ] Sem JavaScript blocante no `<head>`
- [ ] Script de toggle de tema: inline no `<head>` (pequeno, crítico para evitar flash de tema)
- [ ] Demais scripts: no final do `<body>` ou com `defer`
- [ ] CSS: único arquivo ou `<style>` inline — sem múltiplos requests
- [ ] Sem recursos de terceiros (CDN de fontes, analytics, scripts externos) no caminho crítico

---

## Critérios de rejeição (bloqueia ship)

### P0 — Crítico (page-breaking)
- Página não carrega (erro HTTP, JS error que quebra o render)
- Scroll horizontal no body em qualquer breakpoint testado
- H1 ausente ou duplicado
- Link âncora da nav aponta para `id` inexistente (404 interno)
- Formulário exibe dados de input via `innerHTML` (XSS)
- CSS usa cor hardcoded em vez de token (inconsistência visual em dark mode)
- `render.yaml` ausente ou mal configurado (auto-deploy falha)

### P1 — Alto (experiência quebrada)
- Dark mode com contraste < 4.5:1 em qualquer texto normal
- Toggle de tema causa flash de tema no reload (localStorage não lido antes do render)
- Formulário submete com campos obrigatórios vazios sem feedback de erro
- Mockups causam overflow em mobile
- `prefers-reduced-motion` ignorado (animações em quem pediu para não ter)
- Lighthouse Performance Score < 90 em mobile
- Focus ausente em algum elemento interativo
- SVG decorativo sem `aria-hidden` (polui árvore de acessibilidade)
- OG image ausente (compartilhamento social sem preview)

---

## Fora de escopo (v1)

- Backend real para o formulário (email, webhook, banco)
- Blog ou área de cases
- Multi-idioma (pt-BR apenas)
- Animações pesadas (Three.js, GSAP, Framer Motion)
- Sistema de CMS ou geração de conteúdo dinâmico
- Analytics (v2: Plausible)
- Área de cliente / login
- Menu hamburger em mobile (v2 se nav crescer)
- CNPJ e dados legais (v2 quando formalizado)
- Depoimentos de clientes reais (v2)
- Domínio customizado (v2 se não disponível agora)

---

## Ordem de implementação

1. **H-00** — Design system / tokens CSS (fundação)
2. **H-15** — Favicon e OG image (assets antes de qualquer HTML)
3. **H-12** — `<head>` completo: meta, OG, Twitter Card, JSON-LD
4. **H-01** — Nav + toggle de tema (com H-09 integrado)
5. **H-09** — Dark/light mode completo (localStorage + flash prevention)
6. **H-02** — Hero texto
7. **H-03** — Hero mockup CRM
8. **H-04** — Seção de serviços
9. **H-05** — Seção de processo
10. **H-16** — Seção de credibilidade
11. **H-06** — Exemplos de sistemas (4 mockups)
12. **H-07** — Seção de contato + formulário
13. **H-14** — CTA flutuante WhatsApp
14. **H-08** — Footer
15. **H-17** — Página 404
16. **H-10** — Revisão de responsividade end-to-end
17. **H-11** — Acessibilidade end-to-end
18. **H-18** — Performance / Lighthouse audit
19. **H-13** — Deploy Render + `_headers` + verificação pós-deploy
