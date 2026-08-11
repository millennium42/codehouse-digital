# Code House — Redesign v3
## Spec completa para Ralph Loop — NÃO EXECUTAR AGORA

**Data:** 2026-08-07
**Status:** Aguardando aprovação → /build

---

## Diagnóstico do v2 (por que reescrever)

| Problema | Impacto |
|---|---|
| Página é um único scroll linear sem abas | Sem interatividade, usuário não explora |
| Exemplos exibidos como 4 cards lado a lado | Mockups competem por espaço, ficam pequenos |
| Tipografia é system-ui genérica | Não tem identidade visual própria |
| Animações são apenas opacity/translateY | Sem personalidade de movimento |
| Sem JS de peso: nenhuma biblioteca frontend | Parece site de template de 2018 |
| Layout 2-col simétrico em tudo | Composição visual fraca, não guia o olho |
| Nenhuma sessão interativa (tabs, accordions) | Site passivo, não engaja |

---

## Decisões de arquitetura

### Modelo de navegação da página
- Seção **Exemplos** muda para sistema de 4 **abas clicáveis** (CRM / ERP / E-shop / Site)
- Um painel grande exibe o mockup ativo — 100% do espaço disponível
- Transição animada entre abas (slide horizontal suave com Anime.js)
- Seção **Serviços** muda para layout de lista com painel de detalhe à direita (hover activa, click fixa)
- Restante da página: scroll linear, mas enriquecido com GSAP ScrollTrigger

### Stack de bibliotecas frontend

| Biblioteca | Versão | Via | Uso |
|---|---|---|---|
| **GSAP** | 3.12.5 | CDN (cdnjs) | ScrollTrigger reveals, parallax, timeline de hero |
| **ScrollTrigger** | 3.12.5 | CDN (cdnjs) | Plugin do GSAP para animações na rolagem |
| **Anime.js** | 3.2.1 | CDN (cdnjs) | Contadores de stats, transições de abas, micro-animações |
| **Three.js** | r165 | CDN (cdnjs) | Canvas background no hero (partículas ou campo de pontos 3D) |

CSP no `_headers`: adicionar `script-src` e `connect-src` para `cdnjs.cloudflare.com`.

### Tipografia

| Papel | Família | Fonte | Via |
|---|---|---|---|
| Display / Headlines | **Syne** (Bold 700, ExtraBold 800) | Google Fonts | `<link>` no `<head>` |
| Body / Running text | **Inter** (400, 500) | Google Fonts | `<link>` no `<head>` |
| Mono / Labels / UI | **Space Mono** (400, 700) | Google Fonts | `<link>` no `<head>` |

- Syne é geométrica, arquitetural, levemente excêntrica — não está na lista de fontes AI-genéricas
- Space Mono para labels/badges tem personalidade code-heavy que reforça identidade tech

### Tokens de cor revisados

Manter base azul-nuvem mas com mais contraste e micro-detalhes:

```css
--bg: #F2F4F7          /* 2% menos frio que antes */
--surface: #E8ECF2
--surface-raised: #FBFCFE
--cloud: #2D74A0       /* ligeiramente mais escuro = mais contraste WCAG */
--cloud-hover: #1F5F88
--cloud-light: #5A9EC4
--cloud-faint: #C8DFF0
--ink: #111920          /* mais escuro */
--ink-muted: #405970
--ink-faint: #6E8CA4
--border: #C0D0E0
--border-strong: #7AADC8
--ok: #2E8B65
--warn: #B87B0A
--red: #B84040
```

Dark mode tokens: ajustados para ter mais profundidade (não é simples inversão).

---

## Histórias v3

---

### H-32 — Design system: tipografia + tokens revisados

**Como** visitante, **quero** sentir que a Code House tem identidade visual própria, **para** não confundir com qualquer outro site de TI genérico.

#### Critérios de aceitação granulares

**Fontes:**
- [ ] `<link rel="preconnect" href="https://fonts.googleapis.com">` e `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>` antes de qualquer `<link>` de font
- [ ] `<link>` carregando Syne (wght 700;800), Inter (wght 400;500) e Space Mono (wght 400;700)
- [ ] `font-display: swap` incluído na URL do Google Fonts (`&display=swap`)
- [ ] `--font-display: 'Syne', sans-serif` — para h1, h2, h3
- [ ] `--font-body: 'Inter', system-ui, sans-serif` — para body, p, label, input
- [ ] `--font-mono: 'Space Mono', 'Courier New', monospace` — para tags, badges, nav links, código
- [ ] Escala tipográfica definida como tokens CSS:
  - `--t-display: clamp(3rem, 6vw, 5rem)` — h1 hero
  - `--t-h2: clamp(1.8rem, 3vw, 2.5rem)` — section titles
  - `--t-h3: 1.1rem` — cards e sub-seções
  - `--t-body: 1rem` — parágrafo base
  - `--t-small: 0.875rem` — texto secundário
  - `--t-label: 0.65rem` — labels de seção, badges
  - `--t-mono: 0.7rem` — nav links, tags mono
- [ ] `letter-spacing: -.03em` em headings com Syne (corrige espaçamento excessivo de display)
- [ ] `letter-spacing: .12em` em labels/tags mono (Space Mono precisa de espaçamento extra)

**Tokens revisados:**
- [ ] Todos os 14 tokens de cor do diagrama acima implementados em `:root`
- [ ] Dark mode completo redefinido em `@media (prefers-color-scheme: dark)` E em `:root[data-theme="dark"]`
- [ ] Light mode explícito em `:root[data-theme="light"]`
- [ ] Tokens de sombra:
  - `--shadow-sm: 0 1px 3px rgba(14,30,50,.08), 0 1px 2px rgba(14,30,50,.06)`
  - `--shadow-md: 0 4px 12px rgba(14,30,50,.1), 0 2px 4px rgba(14,30,50,.06)`
  - `--shadow-lg: 0 12px 40px rgba(14,30,50,.12), 0 4px 8px rgba(14,30,50,.06)`
- [ ] Token de radius: `--r: 3px` (levemente mais arredondado que 2px, ainda brutalista)
- [ ] Token de transição: `--trans: 160ms cubic-bezier(.4,0,.2,1)`
- [ ] Lighthouse acessibilidade: todos os pares fg/bg passam WCAG AA (4.5:1 texto, 3:1 UI)

**Verificação:**
- [ ] Screenshot comparando v2 vs v3 tipografia — Syne em h1 deve ser visivelmente diferente
- [ ] Nenhum fallback de font aparece (carregar página sem internet = system-ui, esperado)

---

### H-33 — Hero v3: Three.js canvas + headline animada + layout diagonal

**Como** visitante que chega pela primeira vez, **quero** ter uma primeira impressão forte e distinta, **para** sentir que a Code House tem personalidade e não é mais um site de agência genérico.

#### Critérios de aceitação granulares

**Layout:**
- [ ] Hero ocupa `min-height: 100svh` (tela inteira, não apenas 70%)
- [ ] Layout: 55% texto (esquerda), 45% canvas/visual (direita)
- [ ] Linha diagonal separando as colunas: `clip-path` no container direito, criando ângulo de 4° — não retilíneo
- [ ] Padding: `padding: 0 4rem 0 6rem` no lado esquerdo, para criar assimetria intencional

**Three.js canvas (background visual):**
- [ ] `<canvas id="heroCanvas">` ocupando 100% do container direito, com `border-radius` 0 (flush)
- [ ] Three.js r165 carregado via CDN: `cdnjs.cloudflare.com/ajax/libs/three.js/r165/three.min.js`
- [ ] Cena: campo de pontos (PointsMaterial) com ~600 pontos distribuídos em volume 3D
- [ ] Cor dos pontos: `var(--cloud)` lida do CSS (via `getComputedStyle`)
- [ ] Animação: rotação lenta automática em eixo Y (`mesh.rotation.y += 0.001` por frame)
- [ ] Mouse move: rotação do campo responde sutilmente ao cursor (parallax 3D suave) — `mousemove` listener, fator 0.05
- [ ] `requestAnimationFrame` loop — cancelado no unload via `cancelAnimationFrame`
- [ ] Resize handler: canvas se redimensiona ao mudar tamanho da janela, câmera atualiza `aspect`
- [ ] `prefers-reduced-motion`: se ativo, canvas fica estático (rotação = 0, sem responsividade ao mouse)
- [ ] Mobile (< 900px): canvas reduz para apenas background no topo, não divide layout

**Headline animada (GSAP):**
- [ ] GSAP 3.12.5 carregado via CDN com `defer`
- [ ] `DOMContentLoaded`: headline aparece com timeline GSAP:
  - `t=0`: eyebrow slide em de baixo (opacity 0→1, y: 20→0, duration: 0.5s)
  - `t=0.25`: h1 palavra por palavra, stagger de 0.08s por palavra
  - `t=0.6`: subtítulo fade in
  - `t=0.85`: botões fade in com slide-up
  - `t=1.0`: stat badges abaixo dos botões aparecem
- [ ] Palavras do h1 são quebradas em `<span>` individualmente por JS antes da animação
- [ ] `prefers-reduced-motion`: GSAP animações definidas com `gsap.defaults({duration:0})` — instantâneas mas presentes
- [ ] `will-change: transform, opacity` adicionado nos elementos animados, removido após animação completar

**Copy da headline:**
- [ ] H1: `"Sistemas feitos\npara o seu\nmodo de operar."` — 3 linhas, Syne ExtraBold 800
- [ ] Palavra `"seu"` em `<em>` com `font-style:normal; color: var(--cloud)`
- [ ] Subtítulo (Inter 400, 1.05rem, 1.75 line-height, max-width: 46ch):
  `"A Code House entende como sua empresa funciona de verdade — e constrói o sistema que acompanha esse ritmo, sem templates e sem engessamento."`
- [ ] Eyebrow (Space Mono, uppercase, 0.62rem): `"// soluções personalizadas em TI"`
- [ ] Stat inline abaixo dos botões: `38+ projetos · 22 clientes · 5 anos`
  - Fonte: Space Mono 0.58rem, cor: `var(--ink-f)`
  - Separados por `·` com `margin: 0 .5rem`

**Hero CRM mockup (lado direito, dentro do canvas area):**
- [ ] Canvas é background; o mockup CRM flutua sobre ele como overlay com `position: absolute`
- [ ] Mockup reduz para 360px de largura (era window.app-win)
- [ ] Adicionar 2 notificações "toast" que aparecem dentro do mockup:
  - Toast 1: "✓ Negócio fechado — Ana Lima · R$ 4.200" (aparece 1.5s após load, desaparece em 4s)
  - Toast 2: "📅 Lembrete: reunião às 14h com FerroMax" (aparece 5s após load, desaparece em 8s)
  - Animação dos toasts: slide-in de baixo via Anime.js (translateY 20px→0, opacity 0→1, 250ms)
- [ ] Dados do mockup mais ricos: 5 linhas na tabela, não 4

---

### H-34 — Navegação sticky com indicador de seção ativa

**Como** visitante scrollando a página, **quero** saber onde estou e acessar qualquer seção rapidamente, **para** não me perder no conteúdo.

#### Critérios de aceitação granulares

**Indicador ativo:**
- [ ] IntersectionObserver com `threshold: 0.4` em cada `<section id="...">` principal
- [ ] A seção com maior área visível determina o link ativo na nav
- [ ] Link ativo: `color: var(--cloud)` + `::after` com linha de 2px abaixo, animado via transition
- [ ] `aria-current="page"` adicionado/removido dinamicamente no link ativo

**Barra de progresso:**
- [ ] Linha de 2px na parte superior da nav (acima da borda inferior existente)
- [ ] Width: porcentagem do scroll total da página
- [ ] Background: `linear-gradient(90deg, var(--cloud-faint), var(--cloud))`
- [ ] Atualizada via `scroll` event com `requestAnimationFrame` throttle
- [ ] Não aparece quando scroll < 100px (hero ainda visível)

**Nav scroll-away:**
- [ ] Quando scroll desce > 80px: nav minimiza (font-size reduz 10%, padding vertical reduz)
- [ ] Quando scroll sobe após ter descido: nav reaparece instantaneamente
- [ ] Transição: `height: 60px → 48px`, `transition: height 200ms ease`

**Logo:**
- [ ] Em desktop: "CODE.HOUSE" em Space Mono 700
- [ ] Ao passar o cursor: o ponto entre CODE e HOUSE pulsa (scale 1→1.3→1, via CSS keyframe)
- [ ] Click no logo: `scrollTo({top:0, behavior:'smooth'})`

---

### H-35 — Stats section com Anime.js countup

**Como** visitante avaliando credibilidade, **quero** ver números reais de forma impressionante, **para** perceber a experiência da Code House rapidamente.

#### Critérios de aceitação granulares

**Layout:**
- [ ] 4 itens em row de 4 colunas — separados por bordas verticais `1px solid var(--border)`
- [ ] Background: `var(--surface)` com borda top e bottom
- [ ] Sem grid assimétrico — todos os 4 com mesmo peso visual
- [ ] Padding: `3.5rem 0` (mais generoso que antes)

**Cada stat item:**
- [ ] Número grande: Syne 800, `font-size: clamp(2.8rem, 5vw, 4rem)`, `color: var(--cloud)`
- [ ] Label abaixo: Space Mono 0.6rem, uppercase, `var(--ink-f)`
- [ ] Ícone SVG acima do número: 24px, `stroke: var(--cloud)`, `stroke-width: 1.2`
- [ ] Sufixo "+": `font-size: 1.8rem` em `<sup>`, `color: var(--cloud-light)` — menor que o número

**Countup com Anime.js:**
- [ ] Anime.js 3.2.1 carregado via CDN com `defer`
- [ ] IntersectionObserver dispara a animação quando o stat strip entra na viewport
- [ ] `anime({targets: el, innerHTML: [0, finalValue], round: 1, easing: 'easeOutExpo', duration: 1800})`
- [ ] Animação roda uma única vez (observer desconectado após disparar)
- [ ] `prefers-reduced-motion`: mostra valor final direto, sem contagem

**Valores dos stats:**
- [ ] 38+ Projetos entregues
- [ ] 22+ Clientes ativos
- [ ] 5 Anos no mercado
- [ ] 100% Suporte pós-lançamento (sem countup, exibe direto como "100%")

---

### H-36 — Seção de serviços: layout lista + painel de detalhe

**Como** visitante querendo entender os serviços, **quero** ver mais detalhes de cada um sem perder o contexto geral, **para** avaliar o que é relevante para mim sem rolar a página inteira.

#### Critérios de aceitação granulares

**Layout:**
- [ ] Grid de 2 colunas: `300px 1fr` (lista fixa à esquerda, detalhe dinâmico à direita)
- [ ] Lista da esquerda: 5 itens de serviço, empilhados verticalmente
- [ ] Painel direito: detalhe do serviço selecionado — ocupa todo o espaço disponível
- [ ] Painel direito tem `min-height: 360px` — não muda de altura ao trocar serviço

**Lista de serviços (esquerda):**
- [ ] Cada item: `padding: 1.25rem 1.5rem`, `border-bottom: 1px solid var(--border)`
- [ ] Estado inativo: fundo `transparent`, texto `var(--ink-m)`
- [ ] Estado hover: fundo `var(--cloud-faint)`, texto `var(--ink)`
- [ ] Estado ativo (selecionado): fundo `var(--cloud-faint)`, borda esquerda `3px solid var(--cloud)`, texto `var(--cloud)`
- [ ] Nome do serviço em Space Mono 0.62rem uppercase
- [ ] Sub-tag abaixo: Inter 0.8rem, `var(--ink-f)` — "CRM / funil / automação" etc.
- [ ] Ícone SVG 18px à esquerda do nome — mesmo ícone do v2 mas 18px

**Painel de detalhe (direita):**
- [ ] Ao selecionar um serviço: conteúdo anterior fade out (opacity 0, 100ms), novo conteúdo fade in (opacity 1, 200ms) via Anime.js
- [ ] Conteúdo do painel:
  - Eyebrow: tag do serviço
  - H3: título descritivo (diferente do nome curto da lista)
  - Parágrafo: 3-4 linhas explicando o valor e o que diferencia da Code House
  - Lista de features: 5-6 bullets com ícones checkmark (SVG inline)
  - CTA inline: `"→ Ver um exemplo deste sistema"` que ativa a aba correspondente em H-37

**Conteúdo para cada serviço (completo e definitivo):**

CRM — "Gestão de clientes que acompanha seu processo de vendas"
> Não é um CRM genérico de prateleira — é construído em cima de como você já trabalha. Funil de vendas configurado do seu jeito, campos que fazem sentido para o seu negócio, histórico de cada cliente ao alcance.
> ✓ Pipeline de negócios personalizado / ✓ Histórico de interações / ✓ Alertas e lembretes / ✓ Relatórios do que importa / ✓ Integração com WhatsApp (opcional)

ERP — "Operação integrada sem planilhas paralelas"
> Estoque, compras, faturamento e financeiro em um só lugar. O ERP da Code House conecta os setores que já existem na sua empresa — não força você a mudar de processo, apenas organiza o que já acontece.
> ✓ Controle de estoque em tempo real / ✓ Fluxo de caixa e contas / ✓ Pedidos de compra / ✓ Dashboard operacional / ✓ Alertas de ruptura de estoque

E-shop — "Loja virtual que vende, não que parece"
> Site, catálogo, carrinho, pagamento e gestão de pedidos integrados. Feito para funcionar no mobile, carregar rápido e converter — não para ganhar prêmio de design.
> ✓ Catálogo com filtros / ✓ Checkout com Pix e cartão / ✓ Gestão de pedidos / ✓ Cálculo de frete / ✓ Dashboard de vendas

Site Institucional — "Presença digital que representa quem você é"
> Não é um template com as cores da sua empresa. É um site construído a partir da identidade visual, da linguagem e do que seus clientes precisam encontrar.
> ✓ Design personalizado / ✓ Mobile-first / ✓ SEO técnico incluso / ✓ Performance Core Web Vitals / ✓ CMS simples para atualizar conteúdo

Sob Medida — "Qualquer sistema que o seu negócio precise"
> Automação de processo, sistema de agendamento, painel de gestão, aplicativo interno — se existe um processo manual recorrente que trava a sua equipe, a Code House constrói a solução.
> ✓ Levantamento de requisitos incluso / ✓ Prototipagem antes do desenvolvimento / ✓ Tecnologia adequada ao problema / ✓ Documentação entregue / ✓ Suporte pós-lançamento

**Interatividade:**
- [ ] Estado inicial: primeiro serviço (CRM) ativo ao carregar
- [ ] Click na lista: muda o ativo + anima o painel
- [ ] Keyboard: tab entre itens da lista, Enter/Space ativa o serviço (acessibilidade)
- [ ] `role="tablist"` na lista, `role="tab"` nos itens, `role="tabpanel"` no painel, `aria-selected` dinâmico

---

### H-37 — Seção de Exemplos: sistema de 4 abas com mockups full-size

**Como** visitante curioso sobre o que a Code House produz, **quero** explorar exemplos completos e realistas de cada tipo de sistema, **para** visualizar como ficaria o meu sistema antes de contratar.

> **Esta é a historia mais crítica do redesign.** Transforma 4 cards comprimidos em 4 experiências completas intercambiáveis.

#### Critérios de aceitação granulares

**Estrutura de abas:**
- [ ] 4 abas: CRM · ERP · E-shop · Site
- [ ] Barra de abas: `display: flex`, estilo pill/tab, `border-bottom: 2px solid var(--border)`
- [ ] Aba ativa: `background: var(--cloud-faint)`, `border-bottom: 2px solid var(--cloud)`, texto `var(--cloud)` em Space Mono
- [ ] Aba inativa: fundo transparent, texto `var(--ink-m)`
- [ ] Hover em aba inativa: `background: var(--surface)`, texto `var(--ink)`
- [ ] Transição de hover: `var(--trans)` em background e color
- [ ] Painel de conteúdo: `min-height: 520px`, `border: 1px solid var(--border)`, `border-radius: 0 0 var(--r) var(--r)`
- [ ] Borda superior: começa logo abaixo da aba ativa (sem gap)

**Transição de painel (Anime.js):**
- [ ] Ao clicar em aba diferente:
  1. Painel atual: `translateX(0 → -20px)`, `opacity(1 → 0)`, 120ms
  2. Painel novo: `translateX(20px → 0)`, `opacity(0 → 1)`, 180ms, começa após step 1
- [ ] Direção da translação: depende se a aba nova está à esquerda ou à direita da aba atual
  - Se aba nova está à direita do ativo atual: saída para -20px, entrada de +20px
  - Se aba nova está à esquerda: saída para +20px, entrada de -20px
- [ ] `prefers-reduced-motion`: sem translate, apenas opacity

**Acessibilidade das abas:**
- [ ] `role="tablist"` no container das abas
- [ ] `role="tab"` em cada aba, `id="tab-{nome}"`, `aria-controls="panel-{nome}"`, `aria-selected="true/false"`, `tabindex="0/-1"`
- [ ] `role="tabpanel"` em cada painel, `id="panel-{nome}"`, `aria-labelledby="tab-{nome}"`, `hidden` quando não ativo
- [ ] Keyboard: setas ← → movem entre abas (rotatório), Enter/Space ativa, Home/End vai para primeira/última
- [ ] Focus visível nas abas (outline: `2px solid var(--cloud)`, offset: `2px`)

---

#### H-37a — Aba CRM: Pipeline interativo

**Conteúdo:**
- [ ] Layout: 2 colunas dentro do painel — `340px` (KPIs + pipeline) e `1fr` (lista de negócios + atividade)
- [ ] Separador vertical: `1px solid var(--border)`

**Coluna esquerda (funil):**
- [ ] 4 KPIs no topo: Total negócios, Pipeline total (R$), Fechados este mês (R$), Taxa de conversão (%)
- [ ] KPIs em grid 2x2 com separadores de borda fina
- [ ] Cada KPI: número grande (Syne 700), label abaixo (Space Mono), cor do número varia (cloud, ok, ink)
- [ ] Pipeline visual (funil de barras): 4 estágios empilhados verticalmente
  - [ ] Nome do estágio à esquerda (80px, Space Mono, 0.5rem, uppercase)
  - [ ] Barra de largura relativa ao número de negócios (não ao valor)
  - [ ] Cores das barras: progresso de saturação — `--cloud-faint` (Prospecção) → `--cloud-light` → `--cloud` → `--ok` (Fechado)
  - [ ] Ao lado da barra: número de negócios + valor em R$
  - [ ] Barras animadas ao entrar na viewport (width: 0 → final, 800ms, easing: easeOutCubic, via Anime.js)
  - [ ] Barras re-animam ao ativar a aba se ainda não foram vistas

**Coluna direita (negócios):**
- [ ] Tabela de negócios: 6 linhas de dados
- [ ] Colunas: Cliente / Empresa / Valor / Etapa / Responsável / Último contato
- [ ] Coluna Etapa: chip colorido (mesmas cores do funil)
- [ ] Linha ativa (hover): `background: var(--cloud-faint)`, cursor: pointer
- [ ] Header da tabela: Space Mono 0.44rem uppercase, `var(--ink-f)`
- [ ] Células: Inter 0.56rem, primeira coluna em `var(--ink)` 500, demais em `var(--ink-m)`
- [ ] Linha piscando sutilmente (keyframe opacity .8→1) na linha mais recente — indica live
- [ ] Abaixo da tabela: feed de atividade recente (3 itens com dot animado no primeiro)

**Dados concretos (realistas):**
```
Ana Lima     | MerceTex Ind.   | R$ 4.200  | Ativo    | João | Hoje 09:14
Bruno Dias   | LojaTech Sul    | R$ 8.700  | Proposta | Maria | Ontem
Carla Mota   | Studio CM       | R$ 2.800  | Negoc.   | João | 3 dias
Diego Ramos  | FerroMax Ltda   | R$ 12.500 | Ativo    | Maria | Hoje 11:40
Elisa Cunha  | Padaria Doce    | R$ 1.900  | Prospec. | João | 5 dias
Felipe Silva | TecnoFretes     | R$ 6.300  | Proposta | Maria | 2 dias
```

---

#### H-37b — Aba ERP: Dashboard com SVG chart animado

**Conteúdo:**
- [ ] Layout: coluna única, sem divisão — conteúdo empilhado verticalmente
- [ ] 4 KPIs topo com trend arrows (▲▼), grid 4 colunas

**KPIs (valores e dados):**
- [ ] Receita / Mês: R$ 96.400 ▲ vs. mês anterior (+12%)
- [ ] Itens em estoque: 284 unidades ▲ (+18 vs. semana passada)
- [ ] Pedidos / Dia: 17 pedidos ▼ (-3 vs. ontem)
- [ ] Satisfação clientes: 4.8/5 ▲

**Gráfico de linha SVG:**
- [ ] ViewBox: `0 0 600 120`, 100% de largura, `height: 120px`
- [ ] 12 pontos (Jan-Dez), valores: `45,52,38,61,58,74,68,82,79,88,72,96` (em k)
- [ ] `<polyline>` com `stroke: var(--cloud)`, `stroke-width: 2`, `fill: none`
- [ ] Área de fill (`<path>`) com `fill: url(#areaGrad)` — gradiente linear de cloud/25% → cloud/0%
- [ ] Animação na ativação da aba: `stroke-dasharray: [comprimento real]`, `stroke-dashoffset: comprimento → 0` via Anime.js, 1.6s easeInOutSine
- [ ] Área (fill) aparece após a linha terminar de desenhar (delay de 1.2s, opacity 0→1 em 0.6s)
- [ ] Ponto de destaque no último data point (Dez): `<circle cx="..." cy="0" r="5" fill="var(--cloud)">` com pulse animation
- [ ] Labels no eixo X: Jan Fev Mar Abr Mai Jun Jul Ago Set Out Nov Dez — Space Mono 0.4rem
- [ ] Labels no eixo Y: 0 / 25k / 50k / 75k / 100k — linhas horizontais tracejadas com `stroke-dasharray: 4 4`, `stroke: var(--border)`, `opacity: .6`
- [ ] Tooltip ao hover sobre ponto: `<div>` posicionado absolutamente, mostra mês e valor, fade in 100ms

**Lista de pedidos recentes:**
- [ ] 5 pedidos, colunas: Nº pedido / Cliente / Itens / Valor / Status / Hora
- [ ] Status como chips: Entregue (ok-bg/ok), Em rota (warn-bg/warn), Separando (cloud-f/cloud), Aguardando (surface/ink-m)
- [ ] Primeira linha pisca (pulse dot) para indicar live

**Mini mini-painel de estoque crítico:**
- [ ] 3 itens com estoque abaixo do mínimo: nome, estoque atual vs. mínimo, barra de progresso vermelha
- [ ] Título: "⚠ Ruptura iminente" em Space Mono 0.52rem vermelho

---

#### H-37c — Aba E-shop: Catálogo interativo

**Conteúdo:**
- [ ] Layout: 2 colunas — `1fr` catálogo (esquerda), `260px` carrinho (direita)
- [ ] Painel fixo: carrinho não scroll com a lista de produtos

**Catálogo (coluna esquerda):**
- [ ] Filtros por categoria: row de pills clicáveis — Todos / Roupas / Calçados / Bolsas / Acessórios
- [ ] Pill ativa: `background: var(--cloud)`, texto branco
- [ ] Ao trocar pill: produtos filtram com Anime.js (esconder com `scale(0.95) opacity(0)`, revelar `scale(1) opacity(1)`, 200ms)
- [ ] Grid de produtos: `grid-template-columns: repeat(3, 1fr)`, `gap: .75rem`
- [ ] Cada card de produto:
  - [ ] Imagem-placeholder: SVG inline representando o produto (não retângulo colorido) — silhueta reconhecível
  - [ ] Badge "Oferta" em vermelho se aplicável — posição `absolute` no canto superior esquerdo da imagem
  - [ ] Badge "Novo" em `--cloud` se adicionado há < 7 dias simulados
  - [ ] Nome do produto: Inter 500, 0.7rem
  - [ ] Categoria: Space Mono 0.42rem, `var(--ink-f)`
  - [ ] Rating: estrelas SVG preenchidas proporcionalmente (não emoji), tamanho 9px, cor `var(--warn)`
  - [ ] Preço: Syne 700, 0.8rem, `var(--cloud)`
  - [ ] Botão "Adicionar": Space Mono 0.45rem, `background: var(--cloud)`, width 100%, hover: `var(--cloud-hover)`
  - [ ] Ao clicar Adicionar: botão exibe "✓ Adicionado!" por 1.5s via Anime.js, depois volta ao texto original
  - [ ] Ao adicionar, número do carrinho (badge no ícone do carrinho) incrementa com mini bounce

**Produtos definidos (completo):**
```
1. Camiseta Premium    | Roupas     | R$89,90  | ★★★★☆ (4.0) | SVG: silhueta camiseta
2. Tênis Esporte Run   | Calçados   | R$129,90 | ★★★★★ (4.8) | SVG: silhueta tênis | OFERTA
3. Bolsa Couro Natural | Bolsas     | R$249,00 | ★★★★☆ (4.2) | SVG: silhueta bolsa
4. Mochila Urban 25L   | Acessórios | R$139,90 | ★★★☆☆ (3.5) | SVG: silhueta mochila | NOVO
5. Boné Classic Brim   | Roupas     | R$49,90  | ★★★★☆ (4.0) | SVG: silhueta boné
6. Carteira Slim       | Acessórios | R$79,90  | ★★★★★ (4.9) | SVG: silhueta carteira
```

**Carrinho (coluna direita):**
- [ ] Header: "Carrinho" em Space Mono + badge de quantidade
- [ ] Lista de itens adicionados: nome, quantidade (±), preço unitário, preço total
- [ ] Botão de remover item: ×, hover vermelho
- [ ] Total: Syne 700, grande, `var(--cloud)`
- [ ] Botão "Finalizar compra": `btn-solid`, largura total
- [ ] Carrinho inicia com 2 produtos pré-carregados para demonstração (estado não vazio é mais rico visualmente)
- [ ] Ao adicionar produto: item aparece no carrinho com slide-in + total atualiza com Anime.js (countup de 300ms)
- [ ] Carrinho vazio: mensagem "Nenhum item. Clique em + Adicionar no catálogo." com ícone

**Campo de busca:**
- [ ] Input de busca acima dos filtros: `placeholder="Buscar produto..."`, Space Mono 0.65rem
- [ ] Ao digitar: filtra produtos em tempo real (debounce 200ms), sem submit, sem request
- [ ] Se nenhum resultado: mensagem "Nenhum produto encontrado para '[termo]'."

---

#### H-37d — Aba Site Institucional: wireframe funcional com interação

**Conceito:** não é um wireframe estático — é uma prévia interativa do tipo de site que a Code House entrega.

**Conteúdo:**
- [ ] Layout: miniatura do site (scale simulada, não CSS scale — dimensionada para caber no painel)
- [ ] Elementos interativos dentro da prévia (cursor: pointer, hover effects) para demonstrar responsividade

**Elementos do site simulado:**
- [ ] Navbar: logo + links + CTA button
  - [ ] Hover nos links: underline animada (width 0→100% via CSS transition)
  - [ ] CTA button: hover muda background (cloud → cloud-hover)
- [ ] Hero section: título grande (Syne), subtítulo, 2 botões, shape decoration à direita
  - [ ] Shape decoration: `<svg>` abstrato com círculo e retângulo sobrepostos, cor cloud-faint
  - [ ] Botão primário: hover com sombra
- [ ] Feature cards (3): ícone + título + texto, em row
  - [ ] Hover: card sobe `translateY(-4px)` com `box-shadow` intensificado
- [ ] Testimonial: foto avatar (círculo colorido + inicial) + texto + nome/cargo
- [ ] Footer: logo + links + texto de copyright

**Painel lateral (fora da prévia):**
- [ ] Ao lado direito do wireframe (240px): "Funcionalidades incluídas"
  - [ ] Lista de 8 items com ícones: Performance 90+, Mobile-first, SEO técnico, Dark mode, Animações GSAP, Formulário de contato, Domínio configurado, Suporte 6 meses
  - [ ] Stack tecnológica: "Next.js + TypeScript + Tailwind" ou "HTML + CSS + JS puro" (mostrar que flexibilidade)
- [ ] CTA: "Quero um site assim →" — link âncora para `#contato`

---

### H-38 — Seção Processo: scroll horizontal com GSAP ScrollTrigger

**Como** visitante, **quero** entender as etapas de trabalho de forma que guia o olho, **para** confiar no processo antes de contratar.

#### Critérios de aceitação granulares

**Layout:**
- [ ] Container com `overflow: hidden` e largura limitada ao viewport
- [ ] 3 cards de etapa em row, mas revelados sequencialmente conforme o scroll
- [ ] Não é scroll horizontal do usuário — é o GSAP que move conforme scroll vertical

**Implementação GSAP ScrollTrigger:**
- [ ] Plugin ScrollTrigger registrado: `gsap.registerPlugin(ScrollTrigger)`
- [ ] Timeline: `gsap.timeline({ scrollTrigger: { trigger: ".process-section", start: "top center", end: "bottom center", scrub: 1 } })`
- [ ] Cards 2 e 3 iniciam fora da tela (`x: "100%"`) e deslizam para dentro conforme scroll
- [ ] Número grande de fundo (01/02/03) anima em paralelo: `opacity: 0 → 1`, `y: 20 → 0`
- [ ] Connector line entre os cards: `<line>` SVG com `stroke-dashoffset` animado pelo scrub — a linha "desenha" entre os cards conforme scroll
- [ ] Fallback: `@media (prefers-reduced-motion)` → cards todos visíveis, sem animação de scroll

**Conteúdo de cada etapa (mais detalhado que antes):**
- Etapa 01 — **Diagnóstico**: "Reunião para mapear como o negócio funciona — o que trava, o que é manual e o que já funciona bem. Saímos com um documento de requisitos validado."
- Etapa 02 — **Construção**: "Desenvolvimento em sprints curtos com entregas visíveis. Você acompanha cada etapa e valida antes de seguir para a próxima."
- Etapa 03 — **Entrega e suporte**: "Deploy em produção, treinamento da equipe e suporte contínuo. O sistema evolui junto com o negócio."

**Visual:**
- [ ] Número de fundo: Syne 800, `font-size: 8rem`, `var(--border)`, `opacity: 0.4`, `pointer-events: none`
- [ ] Ícone em cada step: SVG 28px inline, `stroke: var(--cloud)`
- [ ] Borda superior esquerda no step card: `3px solid var(--cloud)` (detalhe brutalista)

---

### H-39 — GSAP ScrollTrigger: reveals de seção

**Como** visitante scrollando, **quero** que o conteúdo apareça com propósito, **para** que a página tenha ritmo visual e não pareça que tudo foi despejado de uma vez.

#### Critérios de aceitação granulares

**Revelações por seção:**
- [ ] **Eyebrow/tag de seção**: translateX(-20px) + opacity 0 → 0,1, 0.4s ease — aparece antes do título
- [ ] **H2 da seção**: translateY(20px) + opacity 0 → 0, 0.5s ease, delay 0.1s
- [ ] **Cards em grid**: stagger com intervalo de 0.1s por card, translateY(16px) + opacity 0 → 0
- [ ] **Barras de progresso** (pipeline): width 0 → valor final, stagger 0.15s
- [ ] **SVG chart** (ERP): stroke-dashoffset animado ao entrar na viewport da aba ativa
- [ ] Stats: countup via Anime.js, disparado pelo ScrollTrigger ao entrar a seção

**Configuração do ScrollTrigger:**
- [ ] `start: "top 80%"` (dispara quando topo do elemento está a 80% da viewport)
- [ ] `toggleClass: "is-visible"` — a classe adiciona os estilos finais (opacity 1, translate 0)
- [ ] Transitions definidas no CSS para `.is-visible` — ScrollTrigger só adiciona a classe
- [ ] Isso é mais performático que `gsap.to` individual para cada elemento

**Performance:**
- [ ] `ScrollTrigger.refresh()` chamado após font-display:swap terminar (evitar CLS de layout)
- [ ] Todos os elementos animados têm `will-change: transform, opacity` antes da animação
- [ ] `will-change` removido após a animação completar (não deixar will-change permanente)

---

### H-40 — Seção de Contato: form com validação inline + micro-interações

**Como** visitante preenchendo o formulário, **quero** feedback imediato sobre o que estou digitando, **para** não submeter dados incorretos e receber confirmação de que a mensagem foi enviada.

#### Critérios de aceitação granulares

**Layout:**
- [ ] 2 colunas: `1fr 1fr`
- [ ] Coluna esquerda: copy, "porque falar com a Code House", lista de motivos, alternativa WhatsApp
- [ ] Coluna direita: formulário

**Validação inline:**
- [ ] Nome: obrigatório, mínimo 2 caracteres — validado `onblur`
- [ ] Email: obrigatório, formato válido (regex simples) — validado `onblur`
- [ ] Mensagem: obrigatório, mínimo 20 caracteres — validado `onblur`
- [ ] Empresa: opcional — sem validação
- [ ] Ao falhar validação: borda `2px solid var(--red)`, mensagem de erro abaixo do campo com slide-down (Anime.js 0.2s)
- [ ] Ao corrigir: erro desaparece com fade-out, borda volta para `var(--cloud)` (indicando preenchimento correto)
- [ ] Botão submit: desabilitado se qualquer campo obrigatório vazio ou com erro

**Labels animadas:**
- [ ] Labels "flutuantes": ao focar o campo, label sobe e reduz (como Material UI) — `position: absolute`, `transform: translateY(-18px) scale(0.75)`, `color: var(--cloud)`
- [ ] Quando o campo perde foco e está vazio: label volta à posição original
- [ ] Animação de label: CSS transition 0.15s cubic-bezier(.4,0,.2,1)

**Submissão (simulada no v3 — real em H-21):**
- [ ] Botão em loading: spinner SVG animado (rotate 360° infinito via CSS animation) + "Enviando..."
- [ ] Após 900ms: forma do formulário desaparece (slide up + opacity 0, 300ms)
- [ ] Mensagem de sucesso aparece: slide up + opacity 1
- [ ] Mensagem de sucesso: ícone checkmark SVG com animation de stroke-dashoffset (desenha o check), texto "Mensagem recebida! Em breve entraremos em contato."

**Copy da coluna esquerda:**
- [ ] Eyebrow: `"// vamos conversar"`
- [ ] H2: `"Sua ideia merece um sistema à altura."`
- [ ] Parágrafo: "Conta o que você precisa. A Code House analisa, propõe e só avança quando você sentir que a solução faz sentido para o seu negócio."
- [ ] Lista de razões para contatar (3 bullets com ícones):
  - "Diagnóstico sem compromisso — entendemos antes de propor"
  - "Orçamento claro — sem surpresas no meio do projeto"
  - "Entrega acompanhada — você aprova cada etapa"
- [ ] Link WhatsApp: inter 0.85rem, `var(--ink-m)`, com ícone WhatsApp SVG 16px + "Prefere resposta imediata? WhatsApp"

---

### H-41 — Footer e WhatsApp float

**Como** visitante chegando ao fim da página, **quero** ter acesso fácil às informações de contato e links de navegação, **para** sair da página com os dados que preciso.

#### Critérios de aceitação granulares

**Layout do footer:**
- [ ] 3 colunas: `Brand (1fr) / Links (auto) / Contato (auto)`
- [ ] `padding: 4rem 6rem` — mais espaçoso
- [ ] `border-top: 1px solid var(--border)`
- [ ] Background: `var(--surface)` (levemente diferente do `--bg`)

**Coluna Brand:**
- [ ] Logo CODE.HOUSE em Space Mono 700
- [ ] Tagline: "Sistemas que funcionam do jeito que você trabalha."
- [ ] Tag "Soluções em TI · Personalizado · Desde 2021" em Space Mono 0.55rem, `var(--ink-f)`

**Coluna Links:**
- [ ] Header: "Navegação" em Space Mono 0.55rem uppercase, `var(--ink-f)`
- [ ] Links: Serviços / Processo / Exemplos / Contato
- [ ] Hover: `color: var(--cloud)` + `translateX(4px)` (leve slide para direita via `transition: transform`)

**Coluna Contato:**
- [ ] Header: "Fale com a gente" em Space Mono 0.55rem uppercase
- [ ] Email: `contato@codehouse.dev`
- [ ] WhatsApp: número formatado "(00) 00000-0000" + ícone
- [ ] Ambos como links (`mailto:` e `https://wa.me/...`)

**Footer bottom:**
- [ ] `border-top: 1px solid var(--border)`
- [ ] `padding: 1.25rem 6rem`
- [ ] Esquerda: "© 2026 Code House — CNPJ: XX.XXX.XXX/0001-XX" — placeholder até H-30
- [ ] Direita: "Política de Privacidade" (link → H-23) + "Desenvolvido pela Code House"

**WhatsApp float:**
- [ ] `position: fixed; bottom: 2rem; right: 2rem; z-index: 200`
- [ ] Círculo 56px, background `#25D366`, `box-shadow: 0 4px 20px rgba(37,211,102,.4)`
- [ ] SVG WhatsApp branco 26px
- [ ] Hover: `transform: scale(1.08)`, sombra intensificada, transition 200ms
- [ ] Tooltip ao hover (aparece à esquerda): "Falar pelo WhatsApp" — fade in 150ms
- [ ] Label "pulse" effect (ring de animação que expande e some) — `::after` com scale 1→1.6, opacity 1→0, 2s infinite
- [ ] Aparece apenas após scroll > 300px (não compete com hero)
- [ ] `aria-label="Abrir conversa no WhatsApp"`, `target="_blank" rel="noopener noreferrer"`

---

### H-42 — Responsivo e mobile: hamburger + layout adaptado

**Como** visitante mobile, **quero** a experiência completa do site em tela pequena, **para** não perder funcionalidade ou ter que dar zoom.

#### Critérios de aceitação granulares

**Breakpoints:**
- [ ] `--bp-md: 900px` — principal breakpoint de layout
- [ ] `--bp-sm: 600px` — ajustes finos mobile

**Nav mobile (< 900px):**
- [ ] Links da nav ocultos
- [ ] Botão hamburger visível: 3 barras SVG `20×14px`, `stroke: var(--ink)`, `stroke-width: 1.8`
- [ ] Ao abrir: barras transformam em X (via CSS transform + transition, não trocar SVG)
- [ ] Menu: `position: fixed; top: 60px; left: 0; right: 0; z-index: 99`
- [ ] Background do menu: `var(--bg)` com `backdrop-filter: blur(12px)` e `border-bottom: 1px solid var(--border)`
- [ ] Abrir: `translateY(-100%) → 0`, `opacity: 0 → 1`, 250ms ease via Anime.js
- [ ] Fechar: ação reversa
- [ ] Foco armadilhado quando aberto (`Tab` navega entre links, `Escape` fecha)
- [ ] `aria-expanded` no botão, `aria-label` dinâmico ("Abrir menu" / "Fechar menu")

**Hero mobile:**
- [ ] Coluna única — canvas Three.js fica como `height: 200px` de background acima do texto
- [ ] H1 reduz: `clamp(2rem, 8vw, 3rem)`
- [ ] Botões em coluna, 100% de largura

**Services mobile:**
- [ ] Lista + painel de detalhe colapsam para accordion
- [ ] Cada serviço: click expande painel de detalhe abaixo do item (slideDown via Anime.js)
- [ ] Apenas um expandido por vez

**Exemplos mobile:**
- [ ] Abas scrolláveis horizontalmente (não quebram linha)
- [ ] `overflow-x: auto`, `-webkit-overflow-scrolling: touch`
- [ ] Painel de aba: layout interno adaptado (1 coluna, scroll vertical)
- [ ] Tabelas: `overflow-x: auto` com scroll horizontal indicado por sombra na borda

**Stats mobile:**
- [ ] Grid 2×2 (não 4×1)

**Process mobile:**
- [ ] Cards em coluna, sem animação de scroll horizontal — apenas fade-in normal

---

### H-43 — Performance e CSP

**Como** dono da Code House, **quero** que a landing carregue rapidamente e com segurança, **para** não perder visitas nem ter vulnerabilidades.

#### Critérios de aceitação granulares

**CSP no `_headers` (Render):**
```
/*
  Content-Security-Policy: default-src 'self'; script-src 'self' https://cdnjs.cloudflare.com https://fonts.googleapis.com 'unsafe-inline'; style-src 'self' https://fonts.googleapis.com 'unsafe-inline'; font-src 'self' https://fonts.gstatic.com; img-src 'self' data:; connect-src 'none'; frame-src 'none'; object-src 'none'
```
- [ ] `'unsafe-inline'` em script-src: necessário para o anti-flash inline de tema (alternativa: nonce, mais complexo para static)
- [ ] cdnjs.cloudflare.com autorizado para GSAP, Anime.js, Three.js
- [ ] fonts.googleapis.com e fonts.gstatic.com autorizados
- [ ] `frame-src: 'none'` — não iframeável (clickjacking protection)
- [ ] `object-src: 'none'` — sem Flash/plugins

**Performance:**
- [ ] GSAP/Anime.js/Three.js carregados com `defer` — não bloqueiam render
- [ ] Google Fonts: `<link rel="preconnect">` antes do `<link>` de font
- [ ] Imagens/SVGs otimizados: nenhum SVG inline desnecessariamente grande
- [ ] `font-display: swap` nas Google Fonts
- [ ] `requestAnimationFrame` no scroll handler (não `scroll` diretamente para cálculos pesados)
- [ ] Three.js canvas: `antialias: false` em mobile (detectado via `window.innerWidth < 900`) para economizar GPU
- [ ] Lighthouse Performance ≥ 90, A11y ≥ 95, SEO ≥ 95, Best Practices ≥ 90

**Outras headers Render:**
```
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
```

---

## Ordem de implementação v3

```
H-32  Design system: tokens + tipografia
H-33  Hero v3: Three.js + GSAP timeline
H-34  Nav sticky com indicador de seção
H-35  Stats: Anime.js countup
H-36  Services: layout lista + painel de detalhe
H-37  Abas de exemplos (container + sistema de tabs)
H-37a   └─ Aba CRM
H-37b   └─ Aba ERP
H-37c   └─ Aba E-shop
H-37d   └─ Aba Site
H-38  Processo: ScrollTrigger horizontal
H-39  Reveals ScrollTrigger: todas as seções
H-40  Contato: validação inline + micro-animações
H-41  Footer + WPP float
H-42  Responsivo: hamburger + mobile adapts
H-43  CSP + headers + performance final
```

---

## Critérios de rejeição v3

### P0
- Qualquer elemento sem visibilidade: conteúdo sumindo por z-index, overflow hidden, opacity stuck em 0
- Three.js crash em mobile causando tela em branco
- Abas sem estado ARIA correto (leitor de tela não consegue navegar)
- Lighthouse Performance < 80 por culpa das bibliotecas (reavaliação de carregamento)
- Animação disparando fora de ordem causando flash ou salto de layout (CLS > 0.1)

### P1
- Hamburger menu sem foco armadilhado
- Countup animando mais de uma vez (observer não desconectado)
- Filtro do E-shop não funcionando corretamente (produto errado aparece em categoria errada)
- Tooltip do gráfico ERP fora da viewport em telas pequenas
- WhatsApp float aparecendo sobre o conteúdo do formulário em mobile

---

## Definição de Pronto (v3)

- [ ] Todos os critérios de H-32 a H-43 atendidos
- [ ] Lighthouse: Perf ≥ 90, A11y ≥ 95, SEO ≥ 95, BP ≥ 90
- [ ] Teste manual: Chrome, Firefox, Safari (desktop + mobile)
- [ ] Nenhum erro no console (0 erros, warnings aceitáveis apenas de third-party)
- [ ] `prefers-reduced-motion` testado: todas as animações GSAP/Anime param ou são instantâneas
- [ ] Dark mode testado: todos os elementos legíveis, nenhum contraste abaixo de 3:1
- [ ] Tabs de exemplos: toda troca de aba testada em keyboard (tab, setas, enter)
- [ ] Formulário: validação testada com campos em branco, email inválido, mensagem curta
- [ ] Three.js: testado em mobile (canvas renderizado corretamente, não está quebrando layout)
