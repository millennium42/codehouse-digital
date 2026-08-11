# Code House — Build Prompt Master v3
## Documento auto-suficiente para o Ralph Loop /build

**Data:** 2026-08-08  
**Entregável:** `index.html` — landing page profissional, dinâmica, pronta para deploy no Render  
**Executor:** Ler este documento inteiro antes de tocar em qualquer código  

---

## Visão geral

A Code House é uma empresa de soluções personalizadas em TI para pequenas empresas. O site deve comunicar:
- Que a empresa é técnica mas acessível
- Que os sistemas são feitos para o jeito que o cliente trabalha
- Que existe experiência real por trás (números, exemplos concretos)
- Que o processo é transparente e sem burocracia

**Estética:** minimalista brutalista leve — azul-nuvem, tipografia com personalidade, sem a cara de template lovable/AI. Cada detalhe deve parecer escolhido, não gerado.

---

## Stack de Bibliotecas

Todas via CDN com `defer`. Nunca bloquear o render.

```html
<!-- Smooth scroll -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/lenis/1.1.14/lenis.min.js" defer></script>

<!-- GSAP + plugins -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>

<!-- Anime.js -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js" defer></script>

<!-- Three.js -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r165/three.min.js" defer></script>

<!-- Splitting.js (char/word split para animações de texto) -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/splitting/1.0.6/splitting.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/splitting/1.0.6/splitting.min.js" defer></script>
```

**Ordem de execução:** Todo JS de animação dentro de `window.addEventListener('load', () => { ... })` para garantir que as libs CDN estejam disponíveis.

---

## Design Tokens — Implementação obrigatória

```css
:root {
  /* Cores */
  --bg:           #F1F4F8;
  --surface:      #E6ECF3;
  --surface-up:   #FAFCFF;
  --cloud:        #2D74A0;
  --cloud-h:      #1F5F88;
  --cloud-l:      #5A9EC4;
  --cloud-f:      #C5DEF0;
  --ink:          #101820;
  --ink-m:        #3D566E;
  --ink-f:        #6A8CA4;
  --border:       #C2D2E2;
  --border-s:     #7AADC8;
  --ok:           #2B8A5F;
  --ok-bg:        rgba(43,138,95,.12);
  --warn:         #B37C0A;
  --warn-bg:      rgba(179,124,10,.12);
  --red:          #B84040;
  --red-bg:       rgba(184,64,64,.1);
  --wpp:          #25D366;

  /* Tipografia */
  --f-display: 'Syne', sans-serif;
  --f-body:    'Inter', system-ui, sans-serif;
  --f-mono:    'Space Mono', 'Courier New', monospace;

  /* Escala */
  --t-hero:   clamp(3rem, 6.5vw, 5.2rem);
  --t-h2:     clamp(1.8rem, 3vw, 2.6rem);
  --t-h3:     1.1rem;
  --t-body:   1rem;
  --t-sm:     0.875rem;
  --t-label:  0.62rem;
  --t-mono:   0.68rem;

  /* Layout */
  --max-w:   1140px;
  --pad-x:   clamp(1.5rem, 5vw, 6rem);
  --pad-sec: clamp(4rem, 8vw, 8rem);
  --r:       3px;

  /* Sombras */
  --sh-sm: 0 1px 3px rgba(14,30,55,.07), 0 1px 2px rgba(14,30,55,.05);
  --sh-md: 0 4px 14px rgba(14,30,55,.09), 0 2px 4px rgba(14,30,55,.05);
  --sh-lg: 0 12px 40px rgba(14,30,55,.12), 0 4px 8px rgba(14,30,55,.06);

  /* Transição */
  --trans:    160ms cubic-bezier(.4,0,.2,1);
  --trans-md: 300ms cubic-bezier(.4,0,.2,1);
}

@media (prefers-color-scheme: dark) { :root {
  --bg:       #0C131C;
  --surface:  #121E2A;
  --surface-up: #18293A;
  --cloud:    #5898C0;
  --cloud-h:  #6AAFD6;
  --cloud-f:  #1A3550;
  --ink:      #D6E6F4;
  --ink-m:    #7A9AB4;
  --ink-f:    #486880;
  --border:   #1C3652;
  --border-s: #2C5070;
}}
:root[data-theme="dark"]  { /* mesmos tokens do dark acima */ }
:root[data-theme="light"] { /* mesmos tokens do :root original */ }
```

---

## Fontes Google

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Inter:wght@400;500&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
```

---

## Histórias — Implementação obrigatória

---

### H-50 — Preloader com logo animado

**O que é:** Tela de carregamento exibida enquanto as fontes e scripts CDN carregam. Desaparece com transição elegante.

**Critérios:**
- [ ] `<div id="preloader">` fixo, cobre toda a tela, `z-index: 9999`, `background: var(--bg)`
- [ ] Dentro: logo "CODE.HOUSE" em Space Mono 700, `font-size: 1.2rem`
- [ ] Animação do logo: cada caractere aparece com stagger via Anime.js — `translateY(8px → 0)`, `opacity(0 → 1)`, `duration: 400ms`, `delay: stagger(60ms)`
- [ ] Abaixo do logo: barra de progresso `2px × 120px` que anima de `width 0 → 120px` em 800ms
- [ ] Quando `window.load` disparar: preloader faz `opacity 1 → 0`, `scale(1 → 1.04)`, 400ms, depois `display: none`
- [ ] O resto da página fica com `visibility: hidden` enquanto preloader está ativo
- [ ] Após preloader sair: `visibility: visible`, GSAP hero timeline dispara
- [ ] Sem preloader se `prefers-reduced-motion` ativo — remover preloader instantaneamente

---

### H-51 — Cursor customizado

**O que é:** Substitui o cursor padrão por um cursor de círculo minimalista que acompanha o mouse com leve atraso (smooth follow).

**Critérios:**
- [ ] `<div id="cursor">` — círculo `16px × 16px`, `border: 1.5px solid var(--cloud)`, border-radius 50%, `position: fixed`, `pointer-events: none`, `z-index: 9998`
- [ ] `<div id="cursor-dot">` — ponto `4px × 4px`, `background: var(--cloud)`, border-radius 50%, `position: fixed`, `pointer-events: none`, `z-index: 9999`
- [ ] O círculo segue o mouse com `lerp` (interpolação linear suave): `currentX += (targetX - currentX) * 0.12` a cada frame
- [ ] O dot segue o mouse instantaneamente (sem lerp)
- [ ] Hover em links/buttons: cursor escala para `2.2×`, borda muda para `2px solid var(--cloud)`, `mix-blend-mode: multiply` ativado
- [ ] Hover em texto selecionável: cursor muda para modo "text" (alongado verticalmente via `scaleX(.3) scaleY(1.4)`)
- [ ] No hero canvas Three.js: cursor desaparece (`opacity: 0`) para não competir com o efeito 3D
- [ ] Mobile (`window.matchMedia('(pointer:coarse)')`): cursor customizado não inicializado
- [ ] `body { cursor: none }` aplicado apenas quando cursor custom inicializado com sucesso

---

### H-52 — Navegação sticky com scroll progress, indicador ativo e toggle de tema

**Critérios:**

*Estrutura:*
- [ ] `<nav>` com `position: sticky; top: 0; z-index: 100`
- [ ] `<div class="progress-bar">` — linha 2px na borda superior da nav, `width` = % de scroll da página, `background: linear-gradient(90deg, var(--cloud-f), var(--cloud))`
- [ ] Logo: "CODE.HOUSE" em Space Mono 700 — o ponto `.` tem `color: var(--cloud)` e pulsa (`scale 1→1.4→1, 2s infinite`)
- [ ] Links em Space Mono `var(--t-label)`, uppercase, `letter-spacing: .12em`
- [ ] Link ativo (via IntersectionObserver): underline animada via CSS `::after` (`width: 0→100%`, transition 200ms)
- [ ] Botão de tema (sol/lua SVG): toggle entre `data-theme="dark"` e `data-theme="light"` em `<html>`, persiste em `localStorage`
- [ ] CTA "Falar com a gente": border `1px solid var(--cloud)`, hover `background: var(--cloud)`, color `var(--bg)`

*Comportamento de scroll:*
- [ ] Scroll > 60px para baixo: nav height reduz (`60px → 48px`, transition 200ms), padding vertical diminui
- [ ] Scroll para cima em qualquer ponto: nav retorna ao tamanho normal
- [ ] Ao chegar no topo (scroll = 0): progress bar invisível

*Mobile:*
- [ ] Breakpoint 900px: links ocultos, botão hamburger aparece
- [ ] Hamburger: 3 barras que transformam em X via CSS (`transform: rotate`), transition 200ms
- [ ] Drawer mobile: `position: fixed`, slide-down via Anime.js 250ms, `backdrop-filter: blur(12px)`
- [ ] Foco armadilhado dentro do drawer quando aberto
- [ ] `aria-expanded`, `aria-label` dinâmicos no botão hamburger

---

### H-53 — Hero seção: Three.js + GSAP timeline + headline de impacto

**Critérios:**

*Layout:*
- [ ] `min-height: 100svh`, overflow hidden
- [ ] Grid 2 colunas desktop: `1.1fr 0.9fr`
- [ ] Coluna esquerda: texto, `padding: 0 var(--pad-x)`
- [ ] Coluna direita: `position: relative`, canvas Three.js + app mockup flutuando sobre

*Three.js canvas:*
- [ ] Canvas `100%` width e height da coluna direita
- [ ] Cena: ~500 partículas em campo 3D (`THREE.Points` com `THREE.PointsMaterial`)
- [ ] Cor das partículas: lida de `getComputedStyle(document.documentElement).getPropertyValue('--cloud')`
- [ ] Partículas distribuídas em esfera de raio 3 com `Math.random()` — não em grid
- [ ] Tamanho: `size: 0.035`, `sizeAttenuation: true`
- [ ] Rotação auto: `group.rotation.y += 0.0008` por frame
- [ ] Mouse move: rotação suave do campo em X e Y (fator 0.04), via `lerp` no mousemove
- [ ] Resize: renderer e câmera recalculam no `window.resize`
- [ ] Dark mode: ao trocar tema, cores das partículas se atualizam lendo novo valor de CSS var
- [ ] `prefers-reduced-motion`: rotação parada (0), sem resposta ao mouse
- [ ] Mobile (< 900px): canvas reduced para `height: 220px`, sem mouse-parallax

*Mockup CRM (flutuando sobre canvas):*
- [ ] `position: absolute`, `right: 2rem`, `bottom: 2rem`, `width: 340px`
- [ ] Card com app simulado (ver H-57 para conteúdo completo do mockup)
- [ ] `box-shadow: var(--sh-lg)`, `border: 1px solid var(--border)`, `border-radius: var(--r)`
- [ ] Hover no mockup: `translateY(-4px)`, sombra intensificada, transition 300ms
- [ ] Toast notifications que aparecem dentro do mockup:
  - Toast 1 (1.5s após load): "✓ Negócio fechado — Ana Lima · R$ 4.200" — slide-up 250ms, some em 4s
  - Toast 2 (5s após load): "📅 Reunião às 14h com FerroMax" — mesmo comportamento

*Headline animada (Splitting.js + GSAP):*
- [ ] `Splitting()` chamado no H1 para dividir em `<span class="char">`
- [ ] Timeline GSAP `DOMContentLoaded` (antes do preloader sair — timeline pausada, resume quando preloader encerra):
  - t=0.0s: eyebrow `opacity 0→1, translateY(10→0)`, 0.4s ease
  - t=0.2s: chars do H1, stagger 0.025s cada, `opacity 0→1, translateY(20→0) rotateX(40→0deg)`, transformOrigin "bottom center"
  - t=0.8s: parágrafo subtítulo, `opacity 0→1, translateY(12→0)`, 0.5s
  - t=1.0s: botões `opacity 0→1, translateY(8→0)`, stagger 0.1s
  - t=1.2s: stat strip abaixo dos botões, `opacity 0→1`, 0.3s
- [ ] Eyebrow: "// soluções personalizadas em TI" — Space Mono, `var(--t-label)`, uppercase, `var(--cloud)`
- [ ] H1: "Sistemas feitos para o seu modo de operar." — Syne 800, `var(--t-hero)`, `letter-spacing: -.03em`, `line-height: 1.06`
- [ ] Palavra "seu" em `<span style="color:var(--cloud)">seu</span>`
- [ ] Parágrafo: Inter 400, `1.05rem`, `1.75` line-height, `max-width: 46ch`, `var(--ink-m)`
- [ ] Texto: "A Code House entende como sua empresa funciona de verdade — e constrói o sistema que acompanha esse ritmo, sem templates e sem engessamento."
- [ ] Stat strip: "38+ projetos · 22 clientes · 5 anos" — Space Mono 0.58rem, `var(--ink-f)`

*Botões:*
- [ ] Botão primário "Falar com a gente": `background: var(--cloud)`, hover `var(--cloud-h)` + `translateY(-2px)` + sombra
- [ ] Botão secundário "Ver exemplos": outline `var(--border-s)`, hover `background: var(--cloud-f)`
- [ ] Magnetic effect no botão primário: ao mover o cursor próximo (< 80px), botão "atrai" o cursor levemente (`translateX/Y` até 8px via GSAP quickTo)

---

### H-54 — Marquee/ticker section (logos e tecnologias)

**O que é:** Faixa com desfile infinito de logos/nomes de tecnologias entre o hero e os stats.

**Critérios:**
- [ ] `background: var(--surface)`, `border-top: 1px solid var(--border)`, `border-bottom: 1px solid var(--border)`
- [ ] `padding: 1.25rem 0`, `overflow: hidden`
- [ ] Container duplo: conteúdo repetido 2× dentro de `.marquee-track`
- [ ] Animação: `@keyframes marquee { 0% { transform: translateX(0) } 100% { transform: translateX(-50%) } }` — CSS puro, sem JS
- [ ] `animation: marquee 24s linear infinite`, `animation-play-state: paused` ao hover
- [ ] Itens: logotipos texto de tecnologias que a Code House usa:
  - Node.js · PostgreSQL · React · TypeScript · Docker · Python · Next.js · Supabase · AWS · Linux · REST API · JWT Auth · GSAP · Figma · Render
- [ ] Cada item em Space Mono 0.62rem, uppercase, `var(--ink-f)`, separado por `·` decorativo
- [ ] Sem SVG logos externos (sem request) — apenas texto tech
- [ ] `prefers-reduced-motion`: `animation-play-state: paused` (stop animation)

---

### H-55 — Stats section com Anime.js countup

**Critérios:**
- [ ] 4 colunas, `background: var(--surface)`, border top e bottom
- [ ] Cada item: ícone SVG 24px (stroke `var(--cloud)`), número grande (Syne 800, `clamp(2.8rem,5vw,4rem)`, `var(--cloud)`), label (Space Mono 0.6rem uppercase, `var(--ink-f)`)
- [ ] Número `font-variant-numeric: tabular-nums`
- [ ] Sufixo "+": `<sup>` em font-size 50% do número, `var(--cloud-l)`
- [ ] Countup via Anime.js: `anime({ targets: el, innerHTML: [0, target], round: 1, duration: 1800, easing: 'easeOutExpo' })`
- [ ] Disparo: IntersectionObserver `threshold: 0.6`, desconectado após disparar
- [ ] `prefers-reduced-motion`: valor final direto, sem countup
- [ ] Ícones para cada stat: pasta SVG inline (nenhum request externo)
  - Projetos: ícone de code block `</>`, 2 linhas de código
  - Clientes: ícone de pessoas (2 círculos sobrepostos)
  - Anos: ícone de calendário
  - Suporte: ícone de escudo com check
- [ ] Valores: 38+ Projetos / 22+ Clientes / 5+ Anos / 100% Suporte

---

### H-56 — Seção Serviços: lista interativa + painel de detalhe com micro-animações

**Critérios:**

*Layout:*
- [ ] Grid `300px 1fr` — lista fixa esquerda, painel dinâmico direita
- [ ] Separador vertical: `1px solid var(--border)` com `height: 100%`
- [ ] Mobile: vira accordion (lista vertical, painel colapsa abaixo de cada item)

*Lista de serviços (esquerda):*
- [ ] 5 itens: CRM / ERP / E-shop / Site Institucional / Sob Medida
- [ ] Cada item: ícone SVG 18px + nome em Space Mono + subtag em Inter 0.8rem
- [ ] Hover: `background: var(--cloud-f)`, `translateX(4px)` no ícone (transition 150ms)
- [ ] Ativo: borda esquerda `3px solid var(--cloud)`, `background: var(--cloud-f)`, ícone `color: var(--cloud)`
- [ ] `role="tablist"`, `role="tab"` por item, `aria-selected`, navegação por teclado (setas ↑↓)

*Painel de detalhe (direita):*
- [ ] Ao trocar serviço: saída `opacity 0, translateX(-12px)` em 100ms, entrada `opacity 1, translateX(0)` em 200ms via Anime.js
- [ ] Conteúdo por serviço — completo e definitivo:

**CRM — "Gestão de clientes que acompanha seu funil de vendas"**
Texto: "Não é um CRM genérico — é construído em cima de como você já trabalha. Funil de vendas configurado do seu jeito, campos que fazem sentido para o negócio, histórico de cada cliente acessível em segundos."
Features: Pipeline personalizado / Histórico de interações / Alertas e lembretes / Relatórios do que importa / Integração com WhatsApp (opcional)

**ERP — "Operação integrada sem planilhas paralelas"**
Texto: "Estoque, compras, faturamento e financeiro em um só lugar. Conecta os setores que já existem na sua empresa — não força mudança de processo, apenas organiza o que já acontece."
Features: Controle de estoque em tempo real / Fluxo de caixa e contas / Pedidos de compra / Dashboard operacional / Alertas de ruptura de estoque

**E-shop — "Loja virtual que vende, não que parece"**
Texto: "Catálogo, carrinho, pagamentos e gestão de pedidos integrados. Feito para funcionar no mobile, carregar rápido e converter — não para ganhar prêmio de design."
Features: Catálogo com filtros / Checkout com Pix e cartão / Gestão de pedidos / Cálculo de frete / Dashboard de vendas

**Site Institucional — "Presença digital que representa quem você é"**
Texto: "Não é template com as cores da empresa — é um site construído a partir da identidade visual, da linguagem e do que os clientes precisam encontrar."
Features: Design único / Mobile-first / SEO técnico incluso / Performance Core Web Vitals / CMS para atualizar conteúdo

**Sob Medida — "Qualquer sistema que o negócio precise"**
Texto: "Automação de processo, sistema de agendamento, painel de gestão interno — se existe um processo manual recorrente que trava a equipe, a Code House constrói a solução."
Features: Levantamento de requisitos incluso / Prototipagem antes do dev / Tecnologia adequada ao problema / Documentação entregue / Suporte pós-lançamento

*Cada painel inclui:*
- [ ] Eyebrow (Space Mono, uppercase, `var(--cloud)`)
- [ ] H3 (Syne 700, `var(--t-h3)`)
- [ ] Parágrafo (Inter 400, `var(--t-body)`)
- [ ] Lista de features: cada item com SVG checkmark `var(--ok)` + texto Inter 0.9rem
- [ ] CTA inline: `"→ Ver exemplo deste sistema"` que ativa a aba correspondente em H-59

---

### H-57 — Mockup CRM do Hero (componente completo)

**Critérios do mockup (reutilizado em Hero e em aba CRM):**
- [ ] Window chrome: 3 dots (vermelho/amarelo/verde), label "CRM — Painel" em Space Mono
- [ ] Sidebar: 6 itens de navegação (Clientes ON, Negócios, Tarefas, Relatórios, Automações, Config)
- [ ] Item ativo com borda esquerda 2px azul
- [ ] Content area:
  - 3 KPI cards: Total clientes (42), Novos esta semana (7), Taxa de retenção (94%)
  - Tabela com 5 clientes: Nome / Empresa / Valor / Status (chip colorido) / Último contato
  - Feed de atividade recente: 3 itens com dot animado (pulse) no mais recente
- [ ] Status chips: "Ativo" (ok-bg/ok), "Proposta" (cloud-f/cloud), "Negociação" (warn-bg/warn)
- [ ] Dot pulsando no feed de atividade: `@keyframes pulse { 0%,100% {opacity:1;transform:scale(1)} 50% {opacity:.4;transform:scale(.7)} }`, 2s infinite

---

### H-58 — Seção Processo: GSAP ScrollTrigger horizontal scrub

**Critérios:**

*Layout:*
- [ ] 3 etapas em row, separadas por linha SVG animada (connector)
- [ ] Wrapper com `overflow: hidden`

*GSAP ScrollTrigger:*
- [ ] `gsap.registerPlugin(ScrollTrigger)` após libs carregarem
- [ ] Cards 2 e 3: iniciam `translateX(60px), opacity(0)`
- [ ] Timeline com `scrollTrigger: { trigger: '.process-section', start: 'top 70%', end: 'bottom 30%', scrub: 0.8 }`:
  - Card 2 entra: `translateX(0), opacity(1)` aos 33% do scrub
  - Card 3 entra: `translateX(0), opacity(1)` aos 66% do scrub
  - Connector line 1 (entre card 1 e 2): `stroke-dashoffset` vai de `comprimento → 0`
  - Connector line 2 (entre card 2 e 3): idem, com delay
- [ ] Número de fundo (01/02/03): Syne 800, `6rem`, `var(--border)`, `opacity:.35` — não animado
- [ ] Borda superior esquerda em cada card: `3px solid var(--cloud)` — detalhe brutalista

*Conteúdo:*
- 01: **Diagnóstico** — "Reunião para mapear como o negócio funciona. Saímos com um documento de requisitos validado pelo cliente."
- 02: **Construção** — "Desenvolvimento em sprints com entregas visíveis. O cliente valida cada etapa antes de avançar."
- 03: **Entrega e Suporte** — "Deploy em produção, treinamento da equipe e suporte contínuo. O sistema cresce junto com o negócio."

*Mobile:*
- [ ] Cards em coluna vertical, sem scrub — apenas fade-in normal (ScrollTrigger simples)

---

### H-59 — Exemplos: sistema de 4 abas com painéis full-size

**Estrutura geral:**
- [ ] Header da seção: eyebrow + H2 + parágrafo introdutório
- [ ] Barra de abas: 4 tabs — CRM · ERP · E-shop · Site
- [ ] Aba ativa: `background: var(--cloud-f)`, `border-bottom: 2px solid var(--cloud)`, texto `var(--cloud)` Space Mono
- [ ] Painel de conteúdo: `border: 1px solid var(--border)`, `min-height: 540px`, `border-radius: 0 0 var(--r) var(--r)`
- [ ] Transição entre painéis (Anime.js):
  - Saída: `translateX(0→-24px), opacity(1→0)`, 130ms
  - Entrada: `translateX(direção→0), opacity(0→1)`, 200ms, começa após saída
  - Direção: baseada na posição relativa da aba (esquerda → positivo, direita → negativo)
- [ ] `role="tablist/tab/tabpanel"`, `aria-selected`, `aria-controls`, navegação por teclado (setas ← →, Home/End)
- [ ] `hidden` attribute nos painéis inativos

---

#### H-59a — Aba CRM: Pipeline interativo

**Layout:** 2 colunas dentro do painel — `340px` (funil) | `1fr` (lista + atividade)

**Coluna funil (esquerda):**
- [ ] 4 KPIs em grid 2×2: Total negócios (19) · Pipeline (R$68k) · Fechados/mês (R$28k) · Conversão (41%)
- [ ] Funil de 4 estágios empilhados: Prospecção / Proposta / Negociação / Fechado ✓
- [ ] Cada estágio: label (Space Mono 0.48rem, uppercase, 80px) + track (barra) + valor
- [ ] Largura das barras relativa à quantidade de negócios: 100% / 66% / 48% / 26%
- [ ] Cores: `var(--cloud-f)` → `rgba(var(--cloud-l),.7)` → `var(--cloud)` → `var(--ok)` (saturação crescente)
- [ ] Barras animam `width: 0 → final` ao ativar a aba: Anime.js, `easing: 'easeOutCubic'`, `duration: 800ms`, stagger 150ms
- [ ] Rod de "reanimar" ao voltar para a aba (resetar width para 0 e reanimar)

**Coluna lista (direita):**
- [ ] Tabela: 6 negócios — Nome / Empresa / Valor / Etapa (chip) / Responsável / Últ. contato
- [ ] Linha 1 pisca sutilmente (pulse `@keyframes` na `background-color`) — "live"
- [ ] Feed de atividade (3 itens): dot + texto descritivo, primeiro com dot pulsando
- [ ] Footer do painel: "Atualizado há 2 min" (esquerda) + "Total fechado: R$ 28.500" verde (direita)

**Dados:**
```
Ana Lima     | MerceTex Ind.   | R$ 4.200  | Ativo      | João  | Hoje 09:14
Bruno Dias   | LojaTech Sul    | R$ 8.700  | Proposta   | Maria | Ontem
Carla Mota   | Studio CM       | R$ 2.800  | Negociação | João  | 3 dias
Diego Ramos  | FerroMax Ltda   | R$ 12.500 | Ativo      | Maria | Hoje 11:40
Elisa Cunha  | Padaria Doce    | R$ 1.900  | Prospecção | João  | 5 dias
Felipe Silva | TecnoFretes     | R$ 6.300  | Proposta   | Maria | 2 dias
```

---

#### H-59b — Aba ERP: Dashboard com SVG line chart animado

**Layout:** coluna única, elementos empilhados

**4 KPIs com trend arrows:**
- [ ] Receita/mês: R$96.400 ▲ +12% vs mês anterior
- [ ] Estoque: 284 itens ▲ +18 vs semana
- [ ] Pedidos/dia: 17 ▼ -3 vs ontem
- [ ] Satisfação: 4.8★ ▲

**SVG Line Chart (receita anual):**
- [ ] `viewBox="0 0 600 120"`, 100% largura, `height: 120px`
- [ ] 12 data points (Jan-Dez): `45,52,38,61,58,74,68,82,79,88,72,96` (em mil R$)
- [ ] Calcular coordenadas Y: `y = 100 - ((value - min) / (max - min)) * 90`
- [ ] Pontos X: distribuídos uniformemente em 0 a 600 (passo: 54.5)
- [ ] Linha: `<polyline>` `stroke: var(--cloud)`, `stroke-width: 2`, `fill: none`, `stroke-linecap: round`, `stroke-linejoin: round`
- [ ] Área fill: `<path>` com `fill: url(#areaGrad)` — gradiente linear vertical `var(--cloud)/30% → var(--cloud)/0`
- [ ] Animação ao ativar aba: `stroke-dasharray: [totalLength]`, `stroke-dashoffset: totalLength → 0`, Anime.js 1.6s `easeInOutSine`
- [ ] Área: `opacity 0 → 1` após 1.2s, 0.5s ease
- [ ] Ponto de destaque no último data point: `<circle r="5" fill="var(--cloud)">` com `box-shadow` via `filter: drop-shadow`
- [ ] Pulse no último ponto: `<circle r="5">` com animação de `r: 5→10` e `opacity: 1→0`, 2s infinite
- [ ] Grid horizontal: 5 linhas `stroke-dasharray: "4 4"`, `stroke: var(--border)`, `stroke-opacity: .6`
- [ ] Labels eixo X: Jan a Dez em Space Mono 0.4rem
- [ ] Labels eixo Y: 0 / 25k / 50k / 75k / 100k em Space Mono 0.4rem
- [ ] Tooltip: `<div>` posicionado absolutamente, mostra mês e valor, aparece no `mousemove` sobre o SVG — calcula data point mais próximo

**Tabela de pedidos recentes (5 pedidos):**
```
#4821 | Tecidos Mota    | 3 itens | R$ 3.240 | Entregue   | 09:14
#4820 | FerroMax Ltda   | 8 itens | R$ 8.700 | Separando  | 08:52
#4819 | Café do Bom     | 2 itens | R$ 1.560 | Em rota    | 08:30
#4818 | Studio CM       | 5 itens | R$ 4.100 | Entregue   | Ontem
#4817 | Padaria Doce    | 1 item  | R$ 890   | Entregue   | Ontem
```

**Painel de ruptura de estoque (mini, abaixo):**
- [ ] Header "⚠ Atenção: estoque crítico" em Space Mono 0.48rem, `var(--warn)`
- [ ] 3 itens: nome + atual vs mínimo + barra de progresso vermelha curta

---

#### H-59c — Aba E-shop: Catálogo interativo com filtros e carrinho

**Layout:** `1fr | 260px` (catálogo | carrinho)

**Catálogo (coluna esquerda):**
- [ ] Campo de busca: `placeholder="Buscar produto..."`, debounce 200ms, filtra inline
- [ ] Pills de categoria: Todos / Roupas / Calçados / Bolsas / Acessórios
- [ ] Pill ativa: `background: var(--cloud)`, texto branco
- [ ] Filtro: ao clicar pill, produtos inativos fazem `scale(.92) opacity 0` em 150ms via Anime.js, depois `display:none`; os ativos fazem `display:block` + `scale(1) opacity 1` com stagger 50ms
- [ ] Grid de produtos: 3 colunas, `gap: .75rem`
- [ ] Cada card:
  - Imagem: SVG inline representando o produto (não retângulo — silhueta reconhecível)
  - Badge "Oferta" vermelho ou "Novo" azul se aplicável
  - Categoria: Space Mono 0.4rem, `var(--ink-f)`
  - Nome: Inter 500, 0.72rem
  - Stars: SVG estrelas preenchidas proporcionalmente (clip-path polygon), `var(--warn)`, 9px
  - Preço: Syne 700, 0.85rem, `var(--cloud)`
  - Botão "+ Adicionar": Space Mono 0.44rem, `background: var(--cloud)`, 100% largura, hover escurece
  - Ao clicar: botão muda para "✓ Adicionado!" por 1.5s via Anime.js, badge do carrinho incrementa com bounce

**6 produtos com SVG silhuetas:**
1. Camiseta Premium | Roupas | R$89,90 | ★★★★☆ | SVG: forma T simples
2. Tênis Esporte Run | Calçados | R$129,90 | ★★★★★ | OFERTA | SVG: perfil de tênis
3. Bolsa Couro Natural | Bolsas | R$249,00 | ★★★★☆ | SVG: retângulo arredondado com alça
4. Mochila Urban 25L | Acessórios | R$139,90 | ★★★☆☆ | NOVO | SVG: retângulo com alças
5. Boné Classic Brim | Roupas | R$49,90 | ★★★★☆ | SVG: semicírculo com aba
6. Carteira Slim | Acessórios | R$79,90 | ★★★★★ | SVG: retângulo fino

**Carrinho (coluna direita):**
- [ ] Header: "Carrinho" + badge de quantidade (circle, `background: var(--cloud)`, cor branca)
- [ ] Lista de itens com ±quantidade e ×remover
- [ ] Ao adicionar: item aparece com `translateY(10px) opacity(0 → 1)` em 200ms
- [ ] Total: Syne 700, `1.2rem`, `var(--cloud)` — atualiza com mini countup Anime.js (300ms) a cada mudança
- [ ] Botão "Finalizar compra": `btn-solid`, largura 100%
- [ ] Estado pré-carregado: 2 produtos no carrinho (não iniciar vazio)
- [ ] Carrinho vazio: mensagem "Nenhum item. Adicione produtos." com ícone carrinho SVG

---

#### H-59d — Aba Site Institucional: prévia interativa

**Layout:** prévia simulada do site (esquerda, ~70%) + lista de features (direita, ~30%)

**Prévia simulada (miniatura funcional dentro do painel):**
- [ ] Navbar simulada: logo + links + CTA — hover nos links gera underline animada (CSS transition)
- [ ] Hero: headline grande + subtítulo + 2 botões + shape decoration SVG à direita
- [ ] Feature cards (3): ícone + título + texto, hover `translateY(-4px)` + sombra
- [ ] Testimonial: avatar (círculo com inicial) + quote + nome/cargo
- [ ] Footer mini: logo + copyright
- [ ] Todos os elementos são interativos dentro da prévia (cursor: pointer, hover states)
- [ ] CTA "Quero um site assim →" dentro do painel direito, link para `#contato`

**Lista de features incluídas (painel direito):**
- [ ] 8 itens com ícones: Perf ≥90 / Mobile-first / SEO / Dark mode / Animações / Formulário / Domínio / Suporte 6 meses

---

### H-60 — Seção "Por que a Code House?" (split-screen)

**O que é:** Seção de diferenciação com layout split — lado esquerdo texto, lado direito lista de contrastes "Genérico vs. Code House".

**Critérios:**
- [ ] Grid `1fr 1fr`, `align-items: center`
- [ ] Lado esquerdo: eyebrow + H2 + parágrafo
- [ ] Lado direito: tabela de comparação
  
**Tabela de comparação:**
- [ ] Header: "Template genérico" | "Code House"
- [ ] 5 linhas:
  | Template | Code House |
  |---|---|
  | Funcionalidades fixas | Fluxo do seu negócio |
  | Personalização limitada | Construído do zero |
  | Suporte por ticket | Suporte direto |
  | Você se adapta ao sistema | Sistema se adapta a você |
  | Deploy e tchau | Evoluímos juntos |
- [ ] Coluna esquerda: `var(--ink-f)`, tachar texto com `text-decoration: line-through` suave
- [ ] Coluna direita: `var(--ink)`, ícone checkmark `var(--ok)` antes do texto
- [ ] Reveal: ScrollTrigger — linhas entram com stagger `translateX(-12px) opacity(0 → 1)` 

---

### H-61 — Seção de Contato com validação inline e micro-animações

**Critérios:**

*Layout:*
- [ ] Grid `1fr 1fr`, `gap: 5rem`
- [ ] Esquerda: copy + lista de razões para contratar + link WhatsApp
- [ ] Direita: formulário

*Labels flutuantes:*
- [ ] Campos com `position: relative`, label `position: absolute`
- [ ] Ao focar ou campo ter valor: label sobe e reduz — `translateY(-22px) scale(.75)`, `color: var(--cloud)`, transition 150ms
- [ ] Quando perde foco e vazio: label retorna à posição original
- [ ] Ao focar campo: `border-color: var(--cloud)`

*Campos:*
- [ ] Nome (obrigatório, min 2 chars) + Email (obrigatório, regex) + Empresa (opcional) + Mensagem (obrigatório, min 20 chars)
- [ ] Validação `onblur`: erro com `border-color: var(--red)` + mensagem abaixo slide-down 200ms Anime.js
- [ ] Ao corrigir: erro some com fade-out, `border-color: var(--cloud)` (feedback positivo)
- [ ] Botão submit: desabilitado se campos obrigatórios inválidos

*Submit:*
- [ ] Loading: SVG spinner (rotate 360 via CSS animation) + "Enviando..."
- [ ] Sucesso (após 900ms): formulário faz `opacity 0, translateY(-8px)` em 300ms, depois desaparece; mensagem de sucesso aparece com checkmark SVG animado (`stroke-dashoffset`)
- [ ] Copy da mensagem: "✓ Mensagem recebida! Em breve entraremos em contato."

*Copy esquerda:*
- [ ] Eyebrow: `// vamos conversar`
- [ ] H2: "Sua ideia merece um sistema à altura."
- [ ] Parágrafo: "Conta o que você precisa. A Code House analisa, propõe e só avança quando você sentir que a solução faz sentido para o negócio."
- [ ] 3 bullets: "Diagnóstico sem compromisso" / "Orçamento transparente" / "Entrega acompanhada"
- [ ] Link WhatsApp: ícone SVG `#25D366` + "Prefere pelo WhatsApp?"

---

### H-62 — Footer com marquee, links e dados

**Critérios:**

*Layout 3 colunas:* Brand | Links | Contato
- [ ] `background: var(--surface)`, `border-top: 1px solid var(--border)`
- [ ] `padding: 4rem var(--pad-x)`
- [ ] Coluna Brand: logo + tagline + sub-tags de tecnologia
- [ ] Coluna Links: "Serviços / Processo / Exemplos / Contato" — hover `translateX(4px)` via transition
- [ ] Coluna Contato: email como `<a href="mailto:">` + WhatsApp como `<a href="https://wa.me/">`

*Marquee de rodapé:*
- [ ] Acima do footer-bottom: faixa com texto repetindo infinitamente (igual H-54 mas variante)
- [ ] Texto: "CODE HOUSE · SOLUÇÕES EM TI · PERSONALIZADO · " repetido 6×
- [ ] Animação contrária à seção de tecnologias (da direita para a esquerda, mesmo mecanismo)

*Footer bottom:*
- [ ] `border-top: 1px solid var(--border)`, `padding: 1.5rem var(--pad-x)`
- [ ] Grid `1fr auto`: copyright (esquerda) + links legais (direita)
- [ ] "© 2026 Code House" + CNPJ placeholder
- [ ] Links: "Política de Privacidade" + tema toggle secundário

---

### H-63 — WhatsApp floating button

**Critérios:**
- [ ] `position: fixed; bottom: 2rem; right: 2rem; z-index: 200`
- [ ] Círculo 56px, `background: var(--wpp)`, `border-radius: 50%`
- [ ] SVG WhatsApp branco 26px centralizado
- [ ] `box-shadow: 0 4px 20px rgba(37,211,102,.4)`
- [ ] Hover: `scale(1.08)`, sombra mais intensa, transition 200ms
- [ ] Pulse ring: `::after` com `border: 2px solid var(--wpp)`, border-radius 50%, `@keyframes wppPulse { 0%{transform:scale(1);opacity:.7} 100%{transform:scale(1.7);opacity:0} }`, 2.2s infinite
- [ ] Tooltip à esquerda: "Falar pelo WhatsApp" — fade-in 150ms ao hover
- [ ] Aparece apenas após scroll > 400px: `opacity 0→1` transition quando scroll ultrapassa threshold
- [ ] `aria-label="Abrir conversa no WhatsApp"`, `target="_blank" rel="noopener noreferrer"`
- [ ] Mobile: tamanho reduzido para 48px

---

### H-64 — GSAP ScrollTrigger: reveals globais de seção

**Critérios para cada seção (padrão universal):**
- [ ] Eyebrow: `translateX(-16px) opacity(0 → 1)`, 0.4s, `start: "top 85%"`
- [ ] H2: `translateY(16px) opacity(0 → 1)`, 0.5s, delay 80ms
- [ ] Parágrafo de seção: `translateY(12px) opacity(0 → 1)`, 0.5s, delay 150ms
- [ ] Cards em grid: stagger 0.1s, cada card `translateY(20px) opacity(0 → 1)`, 0.4s
- [ ] Linhas de tabela: stagger 0.06s, `translateX(-8px) opacity(0 → 1)`, 0.3s

**Configuração ScrollTrigger:**
- [ ] Usar `toggleClass: 'is-visible'` + CSS transitions (mais performático que `gsap.to` massivo)
- [ ] `once: true` em todos (não re-anima ao rolar de volta)
- [ ] `ScrollTrigger.refresh()` chamado após 200ms do load (aguardar font-swap)
- [ ] `will-change: transform, opacity` em elementos animados ANTES de entrar na viewport; removido APÓS (`onComplete`)
- [ ] `prefers-reduced-motion`: `ScrollTrigger.disable()` — sem scroll-based animations, tudo visível desde o início

---

### H-65 — Lenis smooth scroll

**Critérios:**
- [ ] `const lenis = new Lenis({ duration: 1.1, easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10*t)) })`
- [ ] Ticker: `lenis.on('scroll', ScrollTrigger.update)` + `gsap.ticker.add(time => lenis.raf(time * 1000))`
- [ ] `gsap.ticker.lagSmoothing(0)` — evita lag spikes
- [ ] Links âncora com `event.preventDefault()` + `lenis.scrollTo(target, { offset: -60 })` para compensar nav sticky
- [ ] Mobile (`pointer: coarse`): `Lenis({ smoothWheel: false })` — scroll nativo no mobile
- [ ] Deactivate em preloader ativo, ativar após reveal

---

### H-66 — Noise/grain texture overlay

**O que é:** Overlay sutil de grain/noise sobre a página inteira para dar textura premium e eliminar look de "flat design AI".

**Critérios:**
- [ ] `<canvas id="noise">` fixo, `pointer-events: none`, `z-index: 1`, `opacity: .035` (light) / `.05` (dark)
- [ ] Gerado via JS com `ImageData` — random pixels cinza-transparentes, `2×2px` por "grain cell"
- [ ] `800×800px` de canvas tileado com `background: url(canvasDataURL) repeat`
- [ ] Atualizado a `9fps` (não 60fps) para efeito de grain estático e performance
- [ ] Filtro CSS alternativo se canvas não suportado: `filter: url("data:image/svg+xml,<svg...><feTurbulence.../></svg>#noise")` no body
- [ ] `prefers-reduced-motion`: canvas não anima (grain estático, 1fps)

---

### H-67 — Dark mode: transição animada de tema

**Critérios:**
- [ ] Ao clicar no toggle: `document.documentElement.classList.add('theme-transitioning')`
- [ ] CSS: `.theme-transitioning *, .theme-transitioning *::before, .theme-transitioning *::after { transition: background-color 300ms ease, color 300ms ease, border-color 200ms ease, box-shadow 200ms ease !important }`
- [ ] Após 400ms: remover a classe (transitions temporárias)
- [ ] `localStorage` persistindo `'ch-theme'` → `'light'` ou `'dark'`
- [ ] Anti-flash inline no `<head>` (antes de qualquer `<link>`):
  ```js
  (function(){var t=localStorage.getItem('ch-theme');if(t)document.documentElement.setAttribute('data-theme',t)})()
  ```
- [ ] Ícone do toggle: SVG sol (light mode) / SVG lua (dark mode) — troca com `opacity 0→1` 200ms
- [ ] Three.js canvas: ao trocar tema, `scene.background` e `material.color` atualizam em 300ms (lerp de cor via Anime.js)

---

### H-68 — Magnetic effect nos botões CTA

**O que é:** Botões CTA "atraem" o cursor quando ele passa próximo, criando micro-interação magnética.

**Critérios:**
- [ ] Aplicado em: botão hero "Falar com a gente" e botão flutuante WhatsApp
- [ ] Detectar `mousemove` no documento
- [ ] Para cada botão magnético: calcular distância do cursor ao centro do botão
- [ ] Se distância < `threshold` (80px): `gsap.to(btn, { x: (cursorX - btnCenterX) * .35, y: (cursorY - btnCenterY) * .35, duration: .4, ease: 'power2.out' })`
- [ ] Se distância > threshold: `gsap.to(btn, { x: 0, y: 0, duration: .6, ease: 'elastic.out(1, .4)' })` (volta com spring)
- [ ] Mobile: não aplicado (pointer:coarse)
- [ ] `prefers-reduced-motion`: não aplicado

---

### H-69 — Página 404 personalizada

**Critérios:**
- [ ] Arquivo `404.html` na raiz
- [ ] Mesmo design system (tokens importados inline ou via `<link rel="stylesheet">` se extraído)
- [ ] Nav simplificada: logo + link "Voltar ao início"
- [ ] Centro da página: código "404" grande em Syne 800, `8rem`, `var(--cloud-f)` (levemente apagado)
- [ ] Sobre o 404: H2 "Essa página não existe." e parágrafo "Parece que o link está errado ou a página foi movida."
- [ ] Botão: "← Voltar para o início"
- [ ] Easter egg: texto pequeno abaixo "PS: enquanto você estava aqui, desenvolvemos mais um módulo." em Space Mono 0.55rem, `var(--ink-f)`
- [ ] `render.yaml` com `notFoundPage: 404.html`

---

### H-70 — SEO e metadados completos

**Critérios no `<head>` do `index.html`:**
- [ ] `<title>Code House — Soluções Personalizadas em TI para Pequenas Empresas</title>`
- [ ] `<meta name="description" content="CRM, ERP, e-shop, sites institucionais e sistemas sob medida. A Code House constrói a solução que encaixa no seu negócio — sem templates, sem engessamento.">`
- [ ] `<meta name="viewport" content="width=device-width, initial-scale=1">`
- [ ] `<meta name="theme-color" content="#2D74A0">`
- [ ] Open Graph: `og:title`, `og:description`, `og:url`, `og:type` (website), `og:image` (placeholder `/og-image.png`)
- [ ] Twitter Card: `twitter:card` (summary_large_image), `twitter:title`, `twitter:description`, `twitter:image`
- [ ] `<link rel="canonical" href="https://codehouse-PLACEHOLDER.onrender.com">` — substituir em H-20
- [ ] `<link rel="icon" href="/favicon.svg" type="image/svg+xml">` — favicon SVG com as iniciais "CH" em azul
- [ ] JSON-LD Schema:
  ```json
  { "@context": "https://schema.org", "@type": "Organization", "name": "Code House", "url": "https://PLACEHOLDER", "description": "...", "serviceType": ["CRM", "ERP", "E-commerce", "Site Institucional"] }
  ```
- [ ] `<meta name="robots" content="index, follow">`
- [ ] Charset: `<meta charset="UTF-8">`

---

### H-71 — Favicon SVG

**Critérios:**
- [ ] `favicon.svg` na raiz: 32×32px
- [ ] Conteúdo: `<svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><rect width="32" height="32" rx="4" fill="#2D74A0"/><text x="16" y="21" text-anchor="middle" font-family="Space Mono,monospace" font-size="13" font-weight="700" fill="white">CH</text></svg>`
- [ ] `<link rel="icon" href="/favicon.svg" type="image/svg+xml">` no `<head>`
- [ ] Apple Touch Icon: `favicon.svg` serve como fallback (suficiente para v1)

---

### H-72 — Responsividade completa (mobile-first)

**Breakpoints:**
- `--bp-lg: 1140px` — container max-width
- `--bp-md: 900px` — principal layout change
- `--bp-sm: 600px` — ajustes finos mobile

**Hero (< 900px):**
- [ ] Grid single column, canvas passa para `height: 220px` na parte superior
- [ ] H1 reduz para `clamp(2rem, 8vw, 3rem)`
- [ ] Botões em column, 100% width

**Serviços (< 900px):**
- [ ] Lista + painel vira accordion: click no item de serviço expande/colapsa detalhe abaixo (Anime.js slideDown/Up)
- [ ] Apenas 1 expandido por vez (fechar anterior ao abrir novo)

**Exemplos (< 900px):**
- [ ] Abas: overflow-x auto com `-webkit-overflow-scrolling: touch` + sombra fade nos lados
- [ ] Painéis internos: single column, sem divisor vertical

**Stats (< 900px):**
- [ ] Grid 2×2 (não 4 colunas)
- [ ] Border entre colunas mantida, border top adicionada na segunda linha

**Processo (< 900px):**
- [ ] Cards em coluna vertical
- [ ] Sem scrub horizontal — apenas fade-in normal via IntersectionObserver

**Contato (< 900px):**
- [ ] Single column, copy acima do formulário
- [ ] Formulário full-width

**Cursor customizado (< 900px / pointer: coarse):**
- [ ] Não inicializado — cursor padrão do sistema

**Hamburger mobile:**
- [ ] Breakpoint 900px: links sumem, hamburger aparece
- [ ] Ícone 3 barras → X via CSS transform (não troca SVG)
- [ ] Drawer: `position: fixed`, `top: 60px`, `left: 0`, `right: 0`, Anime.js slideDown 250ms
- [ ] `backdrop-filter: blur(12px)`, `background: rgba(--bg, .95)`
- [ ] Foco armadilhado: Tab vai ciclicamente entre links do drawer, Escape fecha
- [ ] `aria-expanded`, `aria-label` no botão

---

### H-73 — Performance e deploy (Render)

**Critérios:**

`render.yaml`:
```yaml
services:
  - type: web
    name: codehouse-landing
    env: static
    staticPublishPath: ./
    headers:
      - path: /*
        name: X-Frame-Options
        value: DENY
      - path: /*
        name: X-Content-Type-Options
        value: nosniff
      - path: /*
        name: Referrer-Policy
        value: strict-origin-when-cross-origin
      - path: /*
        name: Permissions-Policy
        value: camera=(), microphone=(), geolocation=()
    routes:
      - type: rewrite
        source: /404
        destination: /404.html
    notFoundPage: 404.html
```

`_headers`:
```
/*
  Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com https://fonts.googleapis.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdnjs.cloudflare.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data:; connect-src 'none'; frame-src 'none'; object-src 'none'
```

**Performance:**
- [ ] Todos os scripts CDN com `defer`
- [ ] Google Fonts com `<link rel="preconnect">` + `display=swap`
- [ ] `requestAnimationFrame` + throttle no scroll handler
- [ ] Three.js: `antialias: false` em mobile (`window.innerWidth < 900`)
- [ ] Lenis desabilitado em mobile para scroll nativo (melhor performance)
- [ ] Lighthouse: Perf ≥ 90, A11y ≥ 95, SEO ≥ 95, BP ≥ 90

---

### H-74 — Acessibilidade global

**Critérios:**
- [ ] `lang="pt-BR"` no `<html>`
- [ ] Todos os ícones SVG decorativos: `aria-hidden="true"`
- [ ] Ícones com significado: `aria-label` descritivo ou `<title>` dentro do SVG
- [ ] Links externos (WhatsApp, etc.): `target="_blank"` + `rel="noopener noreferrer"` + `aria-label` incluindo "(abre em nova aba)"
- [ ] Contraste mínimo WCAG AA: 4.5:1 para texto, 3:1 para UI
- [ ] Focus visible em TODOS elementos interativos: `outline: 2px solid var(--cloud); outline-offset: 3px`
- [ ] Skip link: `<a href="#main" class="skip-link">Ir para o conteúdo</a>` no início do body, visível apenas no foco
- [ ] `prefers-reduced-motion`: GSAP global `defaults({duration:0})`, Anime.js com `duration:0`, Lenis desabilitado, Three.js sem rotação
- [ ] Abas de exemplos: ARIA roles completos (tablist/tab/tabpanel), teclado (setas, Home, End, Enter)
- [ ] Serviços (tabs/accordion): mesmo padrão ARIA
- [ ] Formulário: `<label>` associado a cada `<input>`, mensagens de erro associadas via `aria-describedby`

---

---

### H-75 — IHC: Feedback imediato e estados de sistema visíveis

**Princípio:** Usuário deve saber o que está acontecendo a todo momento (Nielsen #1).

**Critérios:**

*Estados de loading:*
- [ ] Botão submit do formulário: spinner SVG + "Enviando..." enquanto processa — jamais ficar estático durante operação
- [ ] Qualquer ação do usuário (click em aba, click em adicionar produto) tem feedback visual em < 100ms — se a ação demora, mostrar estado intermediário
- [ ] Prefetch de fontes e scripts com `<link rel="preload">` para os críticos — o preloader H-50 cobre a espera inicial

*Estados vazios (Empty states):*
- [ ] Carrinho vazio: não deixar área em branco — ícone + mensagem orientadora "Adicione produtos ao catálogo ao lado"
- [ ] Busca sem resultado: "Nenhum produto encontrado para '{termo}'." + sugestão de "Limpar busca"
- [ ] Se JS desabilitado: `<noscript>` exibe mensagem "Este site usa JavaScript para a melhor experiência. Ative-o no navegador."

*Confirmação de ações:*
- [ ] Click em "+ Adicionar" → botão muda imediatamente para "✓ Adicionado!" (sem delay perceptível)
- [ ] Remover item do carrinho → item some com fade-out 150ms (não desaparece abruptamente)
- [ ] Submit do formulário → loading imediato ao click, sem delay de debounce no feedback visual

*Estados de erro (globais):*
- [ ] Se CDN do GSAP/Anime/Three falhar (script error): página continua funcionando sem animações — graceful degradation
- [ ] `window.onerror` captura erros não tratados e remove preloader para não bloquear a página

---

### H-76 — IHC: Affordance e visibilidade de ações

**Princípio:** Elementos interativos devem parecer interativos. (Nielsen #1, #4)

**Critérios:**

*Affordances visuais:*
- [ ] Todos os botões: `cursor: pointer`, hover com mudança de cor E mudança sutil de posição (`translateY(-1px)`) — não apenas cor
- [ ] Links de texto: `text-decoration: underline` em hover (não só cor) — especialmente no footer
- [ ] Items de lista interativa (serviços, abas): hover muda background E mostra indicador de "→" ou ícone
- [ ] Abas de exemplos: `cursor: pointer` + hover escurece fundo — óbvio que são clicáveis
- [ ] Cards de produto no e-shop: hover `box-shadow` aumenta + `translateY(-3px)` — comunicam interatividade

*Labels descritivos:*
- [ ] Botão submit: "Enviar mensagem" (não apenas "Enviar" ou "OK")
- [ ] CTA hero: "Falar com a gente" (não "Clique aqui" ou "Saiba mais")
- [ ] Link WhatsApp: "Prefere pelo WhatsApp? Resposta em até 30 min"
- [ ] Todas as ações destrutivas (remover item do carrinho): mostrar ×  vermelho com `aria-label="Remover [nome do produto]"`

*Hierarquia visual:*
- [ ] Uma única ação primária por seção (botão sólido) — nunca dois botões sólidos no mesmo bloco
- [ ] CTAs secundários: sempre outline ou texto, nunca sólido azul
- [ ] Formulário: botão submit é o elemento mais proeminente do bloco de formulário

---

### H-77 — IHC: Consistência e prevenção de erros

**Princípio:** Consistência entre elementos, e prevenir erros antes que aconteçam. (Nielsen #4, #5)

**Critérios:**

*Consistência:*
- [ ] Todas as animações de entrada usam as mesmas direções por tipo: seções entram de baixo, itens de lista entram da esquerda, modais/toasts entram de baixo
- [ ] Todos os chips/tags seguem o mesmo padrão: Space Mono, uppercase, `border-radius: var(--r)`, cores do token system
- [ ] Espaçamentos derivados de 4px base: `4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80px` — nunca valores arbitrários como 7px ou 13px
- [ ] Todos os hover states têm exatamente a mesma `transition: var(--trans)` — sem divergências

*Prevenção de erros no formulário:*
- [ ] Campo email: `type="email"` + validação regex explícita — não apenas validação do browser
- [ ] Campo nome: `minlength="2"` + trim em whitespace antes de validar
- [ ] Botão submit: `disabled` enquanto qualquer campo obrigatório estiver vazio ou com erro — impossível submeter estado inválido
- [ ] Ao digitar em campo com erro: erro some imediatamente (não espera blur) — feedback durante a correção
- [ ] Limite de caracteres na mensagem: `maxlength="2000"` com contador "X/2000" abaixo do textarea, Space Mono 0.5rem, `var(--ink-f)`
- [ ] Ao perder foco com campo válido: feedback positivo sutil (border `var(--cloud)`) — confirma que está correto

*Undo:*
- [ ] Remover item do carrinho: "Desfazer" aparece em toast por 4s (`translateX` do canto, Anime.js)
- [ ] Toast "Desfazer": click restaura o item com slide-in

---

### H-78 — IHC: Gestalt, hierarquia visual e espaço branco

**Princípio:** Layout deve guiar o olhar e agrupar informações relacionadas.

**Critérios:**

*Espaço branco intencional:*
- [ ] Seções com eyebrow + H2 + parágrafo: `margin-bottom` do eyebrow = `1.5rem` (separação do H2 = `0.5rem` — eles são um grupo)
- [ ] Entre grupos de conteúdo: `gap` maior que dentro dos grupos (ex: `gap: 2rem` entre cards, `gap: 0.75rem` dentro de card)
- [ ] Hero: nunca ultrapassar `max-width: 50ch` no subtítulo — espaço negativo à direita é parte do design

*Hierarquia tipográfica clara (3 níveis máximo por seção):*
- [ ] Nível 1: H2 da seção — Syne 700/800, grande
- [ ] Nível 2: H3 dos cards/painéis — Syne 700, menor
- [ ] Nível 3: texto de suporte — Inter 400, `var(--ink-m)`
- [ ] Labels/tags: Space Mono — nível meta, não de conteúdo principal
- [ ] Nunca misturar mais de 2 pesos de fonte em um mesmo bloco

*Gestalt — proximidade:*
- [ ] Ícone de serviço sempre `margin-bottom: 1.25rem` antes do nome (ícone pertence ao card, não à seção)
- [ ] Label da seção sempre `margin-bottom: 1.5rem` em relação ao H2 (são um grupo)
- [ ] No formulário: label + input sempre com `gap: 0.3rem` (inseparáveis visualmente)

*Cor como informação, não decoração:*
- [ ] `var(--ok)` somente para: sucesso, confirmações, "Ativo", "Entregue", "Fechado"
- [ ] `var(--warn)` somente para: alertas, "Em rota", "Ruptura iminente"
- [ ] `var(--red)` somente para: erros de validação, erros de sistema
- [ ] `var(--cloud)` para: ações, links, elementos interativos, identidade da marca
- [ ] NUNCA usar cor como único diferenciador — sempre acompanhar de ícone ou texto

---

### H-79 — LGPD: Compliance completo

**Base legal:** Lei 13.709/2018 — dados coletados pelo formulário de contato.

**Critérios:**

*Banner de aviso:*
- [ ] Banner discreto: `position: sticky; bottom: 0`, `background: var(--surface)`, `border-top: 1px solid var(--border)`, `z-index: 80`
- [ ] Texto: "Este site coleta apenas os dados informados no formulário de contato, usados exclusivamente para responder seu contato. [Política de Privacidade]"
- [ ] Link "Política de Privacidade" → `/politica-privacidade.html`
- [ ] Botão "Entendi": `background: var(--cloud)`, click fecha o banner com `translateY(100%)` em 250ms e salva `ch-consent: true` no `localStorage`
- [ ] Banner não aparece se `ch-consent === 'true'`
- [ ] Banner NÃO bloqueia conteúdo (nunca overlay opaco)

*Formulário:*
- [ ] Abaixo do botão submit: "Seus dados são usados apenas para responder seu contato. Nunca compartilhamos com terceiros."
- [ ] Texto em Inter 0.75rem, `var(--ink-f)`
- [ ] Nenhum campo opcional marcado como obrigatório
- [ ] Campo empresa: claramente opcional com "(opcional)" após o label

*Política de Privacidade (`politica-privacidade.html`):*
- [ ] Arquivo separado na raiz
- [ ] Mesmo design system
- [ ] Nav simplificada: logo + "← Voltar"
- [ ] Conteúdo obrigatório em linguagem clara (não juridiquês):
  - Quais dados são coletados: nome, email, empresa (opcional), mensagem
  - Para que são usados: exclusivamente para responder o contato
  - Por quanto tempo: enquanto necessário para atendimento (máx. 12 meses)
  - Com quem são compartilhados: nenhum terceiro (formulário v1 é simulado — quando Formspree integrado, nomear)
  - Como exercer direitos: email `privacidade@codehouse.dev` para solicitar exclusão, correção ou acesso
  - Data da última atualização: 2026-08-08
- [ ] `<title>Política de Privacidade — Code House</title>`
- [ ] `<link rel="canonical">` correto

*Cookies/analytics:*
- [ ] v3 não usa cookies de rastreamento — banner menciona isso explicitamente
- [ ] Nenhum script de terceiros que coleta dados PII (Google Fonts carrega apenas fontes)
- [ ] `Referrer-Policy: strict-origin-when-cross-origin` no `_headers` para limitar dados de referrer enviados a terceiros

---

### H-80 — UX: Microinterações e feedback de estado rico

**Critérios:**

*Hover states (além do básico):*
- [ ] Cards de serviço: ao hover, linha de `1px` na borda superior se transforma em `3px` com transition (detalhe brutalista ativado)
- [ ] Links do footer: texto desliza levemente para a direita (`translateX(0 → 4px)`) com `→` aparecendo — como se o link "chamasse"
- [ ] Eyebrow das seções: ao scroll-reveal entrar, o `::before` (linha decorativa) anima da esquerda (`width: 0 → 24px`)
- [ ] Números KPI nos mockups: ao aparecer na viewport, fazem micro-bounce (`scale 1→1.04→1`, 300ms)

*Scroll-jacking consciente (não agressivo):*
- [ ] Lenis `duration: 1.1` — smooth mas não excessivamente lento
- [ ] Nenhuma seção "prende" o scroll (scroll-jacking completo está proibido)
- [ ] ScrollTrigger `scrub: 0.8` (não `scrub: true`) — máximo 0.8 para não parecer travado

*Estados de seleção:*
- [ ] Aba ativa nos exemplos: fundo + borda inferior + cor — 3 indicadores simultâneos (não apenas cor)
- [ ] Serviço ativo: borda esquerda + fundo + cor do texto — 3 indicadores
- [ ] Pill de categoria ativa no e-shop: fundo sólido + cor de texto invertida — contraste máximo

*Mensagens contextuais:*
- [ ] No formulário, ao preencher todos os campos corretamente: botão submit muda de `var(--cloud)` para levemente mais vibrante com micro-pulse animation (sinaliza "pronto para enviar")
- [ ] Tooltip no botão WhatsApp float: "Resposta em até 30 min" — expectativa clara

---

### H-81 — UX: Motion design com propósito

**Princípio:** Cada animação tem função — não é decoração.

**Critérios por tipo de animação:**

*Animações de reveal (propósito: progressão):*
- [ ] Direção: de baixo para cima — simula "emergir" (peso natural, não arbitrário)
- [ ] `translateY: 20px → 0` + `opacity: 0 → 1` — sempre os dois juntos
- [ ] Duração: 400-500ms — legível mas não lenta
- [ ] Stagger em grupos: 80-120ms entre itens — suficiente para perceber sequência, não tão lento que parece bug

*Animações de transição (propósito: orientação espacial):*
- [ ] Troca de aba: slide horizontal — comunica que existe um eixo de navegação
- [ ] Troca de serviço: fade com leve slide — saída e entrada no mesmo eixo
- [ ] Accordion mobile: expand/collapse vertical — respeita o eixo real do layout

*Animações de feedback (propósito: confirmação):*
- [ ] Countup: `easeOutExpo` — rápido no início, desacelera no final (chega no valor certo)
- [ ] Chart line draw: `easeInOutSine` — entra e sai suave (como se fosse traçada à mão)
- [ ] Barras do pipeline: `easeOutCubic` com stagger — como se fossem "preenchidas" uma a uma
- [ ] Toast notifications: slide-up 250ms entrada, fade 150ms saída — não compete com conteúdo principal

*Animações ambientes (propósito: atmosfera):*
- [ ] Three.js: rotação `0.0008` por frame — quase imperceptível, não distrai
- [ ] Dot pulsando no feed live: 2s infinite — ritmo tranquilo, não alarmante
- [ ] Noise texture: 9fps — grain estático "vivo" mas não chamar atenção

*O que NÃO fazer (proibido):*
- [ ] Nenhuma animação de conteúdo acima do fold no carregamento (após preloader)
- [ ] Nenhum `animation-iteration-count: infinite` em elementos grandes — apenas em micro-detalhes
- [ ] Nenhum parallax agressivo que dessincrona texto de fundo
- [ ] Nenhum hover effect que move o elemento de lugar de forma que quebre layout (sem `position: relative` em elementos que empurram outros)

---

### H-82 — UX: Tipografia como diferencial de identidade

**Propósito:** A tipografia escolhida (Syne) deve ser explorada de forma que reforce a identidade, não apenas "aparecer".

**Critérios:**

*Uso estratégico do Syne:*
- [ ] H1 do hero em Syne 800, `letter-spacing: -0.03em` — tight tracking que define o caráter
- [ ] Números grandes (stats, KPIs): Syne 800 — consistência entre título e dados de impacto
- [ ] H2 das seções: Syne 700 (levemente mais leve que H1, hierarquia clara)
- [ ] H3 (cards, painéis): Syne 700, tamanho menor — mesmo peso, tamanho diferencia o nível

*Uso estratégico do Space Mono:*
- [ ] Labels de seção (`// serviços`, `// exemplos`): Space Mono com `//` como prefixo — marca visual recorrente
- [ ] Todos os badges, chips, tags: Space Mono — cria linguagem visual consistente para metainformação
- [ ] Navegação: Space Mono em caps — nav parece mais "de sistema", reforça identidade tech
- [ ] Números tabulares em tabelas: `font-variant-numeric: tabular-nums` SEMPRE — nunca números que desalinham

*Espaçamento tipográfico apurado:*
- [ ] Line-height: 1.06 para H1 (display), 1.2 para H2/H3, 1.6 para parágrafos, 1.4 para captions
- [ ] O parágrafo do hero (`max-width: 46ch`) — 46 chars é o máximo ideal para leitura confortável (estudos de IHC)
- [ ] Listas de features: `line-height: 1.5`, `gap: 0.6rem` entre itens — nem apertado nem espaçado demais
- [ ] `text-wrap: balance` em todos H1, H2, H3 — prevenção de linhas órfãs

*Contraste e legibilidade:*
- [ ] Body text (`var(--ink-m)`) sobre `var(--bg)`: verificar ratio ≥ 4.5:1 (obrigatório)
- [ ] Texto sobre `var(--cloud)` (botões): sempre `var(--bg)` (branco/cinza claro) — jamais escuro
- [ ] Tags sobre `var(--cloud-f)`: `var(--cloud)` — verificar ratio no modo escuro também

---

### H-83 — UX: Estados de erro e recuperação

**Critérios:**

*Formulário — todos os cenários de erro:*
- [ ] Nome vazio: `"Por favor, insira seu nome."`
- [ ] Nome < 2 chars: `"Nome muito curto — mínimo 2 caracteres."`
- [ ] Email vazio: `"Por favor, insira seu email."`
- [ ] Email formato inválido: `"Email inválido. Exemplo: nome@empresa.com.br"`
- [ ] Mensagem vazia: `"Descreva o que você precisa."`
- [ ] Mensagem < 20 chars: `"Mensagem muito curta. Conte um pouco mais sobre o que precisa."`

*Estilo das mensagens de erro:*
- [ ] Cor: `var(--red)`, tamanho: 0.78rem, Inter 400
- [ ] Ícone `!` pequeno (SVG, 12px) antes do texto
- [ ] Slide-down com Anime.js: `height: 0 → auto, opacity: 0 → 1`, 200ms
- [ ] Slide-up ao corrigir: `height → 0, opacity → 0`, 150ms

*Falha de CDN (graceful degradation):*
- [ ] GSAP falha: `typeof gsap === 'undefined'` → página carrega sem animações, elementos visíveis por padrão
- [ ] Anime.js falha: barras do pipeline, chart e tabs ainda funcionam sem transições
- [ ] Three.js falha: canvas fica com fundo gradiente CSS (fallback declarado no CSS do container)
- [ ] Lenis falha: scroll nativo do browser (fallback natural)
- [ ] Google Fonts falha: fallback `system-ui` — layout não quebra (tamanho das fontes é similar)

---

### H-84 — UX: Densidade de informação e escaneabilidade

**Princípio:** Visitantes scaneia antes de ler. Layout deve favorecer escaneação.

**Critérios:**

*Scanning path (F-pattern):*
- [ ] Primeira linha de cada seção: elemento mais importante (H2, não eyebrow)
- [ ] Eyebrow antes do H2: contexto em Space Mono, pequeno — para os que leem devagar
- [ ] H2 sem eyebrow: sem contexto suficiente — eyebrow sempre presente

*Chunks de informação:*
- [ ] Nenhum parágrafo de corpo com mais de 4 linhas visíveis sem break
- [ ] Listas de features: máx. 6 itens, depois quebrar em 2 colunas ou usar segunda lista
- [ ] Tabelas dos mockups: máx. 6 linhas — mais que isso cria cognitive overload

*Âncoras visuais:*
- [ ] Cada seção tem: eyebrow (onde estou) + H2 (o quê) + parágrafo de 1 frase (por quê)
- [ ] Ícones SVG nos serviços: reconhecíveis em 0.5s (não abstratos demais)
- [ ] Números grandes nos stats: visíveis a distância (Syne 800, `4rem`) — não precisam ser lidos, são percebidos

---

### H-85 — UX: Mobile-first e touch UX

**Critérios específicos para touch:**

*Tamanho de toque (touch targets):*
- [ ] Todos os elementos clicáveis em mobile: mínimo `44×44px` (recomendação Apple/Google/WCAG 2.5.5)
- [ ] Botões do formulário: `min-height: 48px`
- [ ] Abas dos exemplos: `min-height: 48px`, `padding: 0.75rem 1rem`
- [ ] Pills de categoria (e-shop): `min-height: 44px`, `padding: 0.5rem 1rem`
- [ ] Botões ±quantidade no carrinho: `44×44px`
- [ ] Links do footer: `padding: 0.4rem 0` para aumentar área de toque

*Prevenção de zoom involuntário:*
- [ ] Todos os `<input>`: `font-size: 16px` em mobile — abaixo de 16px o iOS faz zoom no foco (má UX)
- [ ] `touch-action: manipulation` nos botões interativos — elimina delay de 300ms em touch

*Feedback tátil (visual substitute):*
- [ ] Em touch, `active` state adiciona `background: var(--cloud-f)` imediatamente (< 100ms)
- [ ] Sem hover states em mobile — apenas `active` e `focus`

*Scroll nativo em mobile:*
- [ ] Lenis `smoothWheel: false` em `pointer: coarse`
- [ ] `overscroll-behavior: contain` em drawers e modais para não vazar scroll
- [ ] Abas com overflow horizontal: `-webkit-overflow-scrolling: touch` + scroll snap leve

*Legibilidade mobile:*
- [ ] Font size mínimo: 14px em qualquer elemento visível
- [ ] Line-height mínimo: 1.5 em textos de corpo
- [ ] `padding-bottom: env(safe-area-inset-bottom)` no footer e no WPP float — evitar sobreposição com home indicator do iPhone

---

## Checklist de Definição de Pronto

**Build completa quando:**

- [ ] H-50 a H-74: todos os critérios atendidos
- [ ] Arquivo `index.html` único, auto-suficiente (exceto CDNs e Google Fonts)
- [ ] Arquivo `404.html` presente
- [ ] Arquivo `render.yaml` presente
- [ ] Arquivo `_headers` presente
- [ ] Arquivo `favicon.svg` presente
- [ ] Zero console errors em Chrome DevTools
- [ ] Lighthouse: Perf ≥ 90, A11y ≥ 95, SEO ≥ 95, BP ≥ 90
- [ ] Testado em: Chrome, Firefox, Safari (desktop)
- [ ] Testado em: iPhone SE (375px) e iPad (768px) via DevTools
- [ ] `prefers-reduced-motion` testado: nenhuma animação GSAP/Anime rodando
- [ ] Dark mode testado: todos os elementos legíveis, contraste OK
- [ ] Cursor customizado testado: não aparece em mobile/touch
- [ ] Tabs (exemplos): teclado navegável completamente
- [ ] Accordion de serviços (mobile): funciona com touch e teclado
- [ ] Formulário: validação testada com todos os cenários de erro
- [ ] Three.js canvas: não quebra layout em nenhum tamanho de tela
- [ ] Preloader: aparece e desaparece corretamente em todos os browsers
- [ ] Smooth scroll: Lenis funcionando, sem conflito com ScrollTrigger
- [ ] Marquee: pausa corretamente ao hover
- [ ] WhatsApp float: aparece após 400px de scroll, não aparece antes

---

## Critérios de Rejeição

### P0 (bloqueia ship)
- Qualquer elemento com `opacity: 0` preso (animação que não completa)
- Three.js crash causando tela em branco em qualquer browser
- Formulário sem validação (aceita campos vazios)
- Cursor sumindo permanentemente em desktop
- Preloader não desaparecendo (página bloqueada)
- Lighthouse Performance < 80
- CLS > 0.1 (conteúdo pulando durante carregamento)
- Qualquer elemento inacessível por teclado

### P1 (corrigir antes de share)
- Countup animando mais de uma vez
- Magnetic buttons com jitter (oscilando sem parar)
- Chart tooltip fora do viewport
- Filtros E-shop deixando produto em categoria errada
- Hamburger sem foco armadilhado
- WhatsApp float sobrepondo botão submit do formulário em mobile

---

## Ordem de implementação

```
1. H-67  Dark mode toggle + anti-flash          (base de tokens primeiro)
2. H-70  SEO + metadados + <head> completo
3. H-71  Favicon SVG
4. H-52  Nav structure (sem animações ainda)
5. H-53  Hero: estrutura HTML/CSS
6. H-57  Mockup CRM (componente)
7. H-54  Marquee ticker
8. H-55  Stats section
9. H-56  Services section
10. H-58  Process section
11. H-59  Examples: container de abas
12. H-59a   └─ Aba CRM
13. H-59b   └─ Aba ERP
14. H-59c   └─ Aba E-shop
15. H-59d   └─ Aba Site
16. H-60  Why Code House section
17. H-61  Contact form
18. H-62  Footer
19. H-63  WhatsApp float
20. H-69  Página 404
21. H-73  render.yaml + _headers
22. H-72  Responsividade (media queries)
23. H-74  Acessibilidade (pass global)
--- Agora as animações e libs JS ---
24. H-50  Preloader
25. H-65  Lenis smooth scroll
26. H-64  GSAP ScrollTrigger reveals
27. H-53  Three.js canvas (hero)
28. H-53  GSAP headline timeline
29. H-55  Anime.js countup (stats)
30. H-59  Anime.js transições de abas
31. H-59a   └─ CRM: barras animadas
32. H-59b   └─ ERP: SVG line chart animado
33. H-59c   └─ E-shop: filtro com Anime.js
34. H-56  Serviços: Anime.js painel transition
35. H-58  GSAP scrub horizontal (processo)
36. H-51  Cursor customizado
37. H-68  Magnetic buttons
38. H-66  Noise/grain canvas
39. H-52  Nav: progress bar + indicador ativo
--- Final ---
40. Lighthouse audit + ajustes de performance
41. Cross-browser test
42. Accessibility pass
```
