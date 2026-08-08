# Code House — Landing Page
**Objetivo:** Landing page de apresentação da Code House para pequenas empresas.
**Deploy:** Render (static site)
**Data:** 2026-08-07
**Definição de "concluído":** Página publicada no Render, responsiva, dark/light mode, formulário funcional, Core Web Vitals no green, sem bug P0/P1.

## Personas
- **Pedro** — dono de loja física, nunca contratou sistema, quer saber "o que vocês fazem e como começo"
- **Marina** — gerente de PME, já usou ERP engessado, busca flexibilidade e sistema que entenda o negócio dela
- **Thiago** — gestor de e-commerce pequeno, quer loja virtual com identidade própria e gestão de pedidos

## Histórias de usuário

### H-00 — Design system e tokens CSS
**Como** engenheiro implementando a landing, **quero** um sistema de tokens CSS definido antes de qualquer componente, **para** garantir consistência visual em toda a página e facilitar dark/light mode.
- [x] Paleta definida em variáveis `:root`:
  - `--bg`: `#F0F4F8`
  - `--surface`: `#E2EBF4`
  - `--surface-raised`: `#FAFCFE`
  - `--cloud`: `#3E82AB`
  - `--cloud-hover`: `#2E6E95`
  - `--cloud-light`: `#6AAFD6`
  - `--cloud-faint`: `#C0D8EC`
  - `--ink`: `#17232E`
  - `--ink-muted`: `#4A6275`
  - `--ink-faint`: `#7A9AAF`
  - `--border`: `#B4CCE0`
  - `--border-strong`: `#7AADC8`
- [x] Tipografia definida em variáveis: `--font-sans` e `--font-mono`
- [x] Escala de espaçamento baseada em múltiplos de 4px
- [x] Border-radius padrão: 2px (brutalista leve)
- [x] Nenhum componente usa cor ou fonte hardcoded fora dos tokens
- [x] Arquivo CSS organizado: tokens → reset → utilitários → componentes → layout → responsividade

### H-01 — Navegação global
**Como** visitante, **quero** uma barra de navegação fixa com links para as seções, **para** acessar qualquer parte da página sem perder contexto de onde estou.
- [x] Logo `CODE.HOUSE` em monospace à esquerda; ponto separador na cor `--cloud`
- [x] Clique no logo ancora ao topo da página
- [x] Links: Serviços / Processo / Exemplos / "Falar com a gente"
- [x] CTA "Falar com a gente": borda azul nuvem; hover → preenchimento sólido azul, texto fundo
- [x] Barra `position: sticky; top: 0`
- [x] `background: var(--bg)` + `border-bottom: 1px solid var(--border)`
- [x] `z-index` acima de todos
- [x] Em mobile (< 900px): apenas logo + botão CTA; demais links ocultados
- [x] Focus visível (outline)
- [x] Links são âncoras HTML
- [x] Cada seção destino tem `id` correspondente

### H-02 — Hero — mensagem principal
**Como** visitante que chegou pela primeira vez, **quero** entender em 5 segundos o que a Code House faz e para quem, **para** decidir se vale continuar lendo.
- [x] Layout em 2 colunas (desktop)
- [x] Eyebrow monospace: "Soluções Personalizadas em TI"
- [x] Headline H1: "Sistemas feitos para o *seu* jeito de trabalhar." ("seu" em `--cloud`)
- [x] H1 único na página
- [x] Subtítulo (1 parágrafo)
- [x] Dois botões em linha: "Falar com a gente" (sólido, `#contato`) + "Ver exemplos" (outline, `#exemplos`)
- [x] Fade-in suave no mockup (sem reduced-motion)
- [x] Em mobile (< 900px): layout em 1 coluna; mockup antes do texto
- [x] Padding top do hero acomoda a nav sticky

### H-03 — Hero mockup — preview CRM
**Como** visitante, **quero** ver um preview visual real de como um sistema CRM da Code House parece, **para** sentir a qualidade concretamente.
- [x] `aria-hidden="true"`
- [x] Janela de app com barra de título, dots macOS style, "CRM — Clientes"
- [x] Sidebar com 5 itens; Clientes ativo com `--cloud-faint` e borda esquerda `--cloud`
- [x] Área de conteúdo com Header, badge 42 registros
- [x] Grid de 3 stat cards
- [x] Tabela com 4 linhas, fonte em escala reduzida
- [x] Apenas tokens; ok em dark mode
- [x] Bordas em `--border`, max `border-radius: 4px`
- [x] Mobile: mockup reduzido proporcionalmente, sem scroll-x

### H-04 — Seção de serviços
**Como** visitante, **quero** ver as soluções que a Code House oferece com descrição clara, **para** identificar se têm o que eu preciso.
- [x] Eyebrow monospace: `// serviços`
- [x] Título H2: "O que a Code House entrega"
- [x] Grid 5 colunas, `border: 1px solid var(--border)`
- [x] Card: ícone SVG inline + nome em monospace + descrição
- [x] Hover sutil: `background: var(--surface)`
- [x] Ícones SVG: stroke `currentColor`, 16x16
- [x] Mobile < 900px: 2 colunas, `border-bottom`
- [x] Mobile < 600px: 1 coluna
- [x] `id="servicos"`

### H-05 — Seção de processo
**Como** visitante, **quero** entender como funciona o processo de trabalho da Code House, **para** saber o que esperar.
- [x] Eyebrow monospace: `// como funciona`
- [x] Título H2: "Do problema à solução em três etapas"
- [x] Grid 3 colunas, mesmo padrão visual dos serviços (com borders)
- [x] Etapas numeradas "Etapa 01", etc. (monospace faint)
- [x] Mobile: 1 coluna com `border-bottom` (via gap)
- [x] Textos aplicados conforme spec
- [x] `id="processo"`

### H-06 — Seção de exemplos de sistemas
**Como** visitante, **quero** ver previews visuais dos sistemas que a Code House constrói, **para** ter confiança na qualidade.
- [ ] Eyebrow monospace: `// exemplos de sistemas`
- [ ] Título H2: "O que sistemas feitos assim parecem"
- [ ] Grid 2x2, 4 cards
- [ ] CRM / ERP / E-shop / Site Institucional (com mockups CSS puro em cada)
- [ ] Apenas variáveis CSS
- [ ] `aria-hidden="true"` em mockups
- [ ] Mobile: 1 coluna; mockups com `overflow-x: auto`
- [ ] `id="exemplos"`

### H-07 — Seção de contato
**Como** visitante interessado, **quero** entrar em contato com a Code House, **para** iniciar o projeto.
- [x] Fundo `var(--surface)`
- [x] Layout 2 colunas (desktop): copy + form
- [x] Eyebrow, H2, Subtítulo, Link WhatsApp abaixo
- [x] Formulário com Nome, Empresa (opcional), Necessidade (textarea)
- [x] Labels em monospace uppercase
- [x] `border-color: var(--cloud)` ao focus
- [x] Validação de submit (erro inline, "Informe seu nome...") sem envio real
- [x] Sucesso: delay 800ms, form substituído por "Mensagem recebida..."
- [x] Proteção XSS via `textContent`
- [x] Mobile: 1 coluna
- [x] `id="contato"`

### H-08 — Footer
**Como** visitante, **quero** um rodapé com informações básicas da empresa e links, **para** referência.
- [ ] `border-top: 1px solid var(--border)`
- [ ] Layout 2 colunas
- [ ] Esquerda: Logo, Tagline, WhatsApp, Email
- [ ] Direita: Links (Serviços / Processo / Exemplos / Contato)
- [ ] Linha final copyright
- [ ] Mobile: coluna única
- [ ] Sem dados legais (v1)

### H-09 — Dark mode e Light mode
**Como** visitante, **quero** que a página respeite minha preferência de tema do sistema e permita troca manual, **para** ter conforto visual em qualquer ambiente.
- [x] Tokens CSS em `:root` (light mode — padrão)
- [x] Override via `@media (prefers-color-scheme: dark)` redefinindo apenas os tokens
- [x] Override via `:root[data-theme="dark"]` e `:root[data-theme="light"]` — toggle manual vence o media query em ambas direções
- [x] `data-theme` aplicado no elemento `<html>`, não em `<body>`
- [x] Toggle (botão sol/lua) visível na nav em desktop — ícone SVG, sem texto
- [x] Ao clicar no toggle: alterna o atributo `data-theme` no `<html>` e persiste no `localStorage` com key `ch-theme`
- [x] Ao carregar a página: lê `localStorage` e aplica o tema salvo antes do primeiro render (script inline no `<head>` para evitar flash)
- [x] Dark mode não é inversão: azul nuvem `--cloud` levemente mais claro no dark para manter legibilidade em fundo escuro
- [x] Contraste verificado em ambos os temas (critério H-11)
- [x] Nenhum elemento usa cor hardcoded fora dos tokens (exceto cores semânticas das tags de status)
- [x] Mockups CSS dos exemplos funcionam em ambos os temas sem CSS duplicado

### H-10 — Responsividade
**Como** visitante mobile, **quero** que a página seja utilizável em qualquer tamanho de tela.
- [ ] Breakpoints 900px e 600px
- [ ] Nenhum `overflow-x` no body
- [ ] Botões e inputs `min-height: 44px`
- [ ] Texto >= 14px em mobile
- [ ] Testado em SE portrait/landscape, tablet, desktop
- [ ] Imagens/mockups `max-width: 100%`

### H-11 — Acessibilidade e performance
**Como** visitante, **quero** página acessível e rápida.
- [ ] Focus visível
- [ ] `prefers-reduced-motion` desabilita animações/smooth-scroll
- [ ] Contraste WCAG AA
- [ ] `aria-hidden` ou `aria-label` adequados para SVGs
- [ ] Formulário com labels semânticos
- [ ] `<html lang="pt-BR">`
- [ ] LCP < 2.5s, CLS < 0.1, INP < 200ms
- [ ] Sem JS bloqueante, CSS inline ou bloco único

### H-12 — SEO e metadados
**Como** dono da Code House, **quero** metadados completos.
- [x] Meta e Open Graph completos (title, description, image, url)
- [x] Twitter card
- [x] JSON-LD LocalBusiness
- [x] H1 único, hierarquia ok
- [x] robots.txt e sitemap.xml

### H-13 — Deploy no Render
**Como** dono, **quero** landing publicada no Render rastreável como código.
- [ ] `index.html` e `render.yaml` (static site)
- [ ] Headers HTTP configurados em `_headers`
- [ ] Rota fallback para 404
- [ ] Rollback possível via Render

### H-14 — CTA flutuante WhatsApp
**Como** visitante, **quero** botão flutuante rápido para o WhatsApp.
- [ ] Botão fixo inferior direito (52x52px)
- [ ] Ícone SVG `#25D366`
- [ ] Tooltip em CSS puro "Falar pelo WhatsApp"
- [ ] Z-index correto
- [ ] Número placeholder `5500000000000`

### H-15 — Favicon e assets básicos
**Como** visitante, **quero** aba identificável.
- [x] Favicon SVG inline (letra "C" + fundo `--cloud`)
- [x] `<meta name="theme-color">`
- [x] Imagem estática `og-image.png` (fundo + CODE.HOUSE)

### H-16 — Seção de credibilidade
**Como** visitante, **quero** indicadores de confiança.
- [ ] Seção baseada apenas em dados reais (ou diferenciais objetivos)
- [ ] Layout grid, 3-4 itens (icon/número + texto curto)
- [ ] Sem falsos depoimentos

### H-17 — Página 404 customizada
**Como** visitante, **quero** 404 customizada.
- [ ] `404.html`
- [ ] Mesmo design system
- [ ] "Esta página não existe. Mas a solução que você precisa, a gente constrói."

### H-18 — Performance — Core Web Vitals
**Como** dono, **quero** página em threshold green no Google.
- [ ] Lighthouse scores >= 90
- [ ] JS inline de tema no `<head>`, resto no final do `<body>` ou com defer

## Critérios de rejeição
- **P0**: Erro de load, Scroll-x no body, H1 duplicado/ausente, link quebrado (404 interno), XSS em formulário, CSS sem token, `render.yaml` erro.
- **P1**: Contraste inadequado, flash de tema, submit ignorando erro, mockup overflow, animação em reduced-motion, Lighthouse perf < 90, focus oculto, SVG polutivo, OG image ausente.

## Fora de escopo (v1)
Backend real, blog/cases, multi-idioma, animações complexas, CMS, analytics, login, menu hamburger, dados legais, depoimentos.

## Ordem de implementação
1. H-00
2. H-15
3. H-12
4. H-01
5. H-09
6. H-02
7. H-03
8. H-04
9. H-05
10. H-16
11. H-06
12. H-07
13. H-14
14. H-08
15. H-17
16. H-10
17. H-11
18. H-18
19. H-13
