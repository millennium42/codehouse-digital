# PROMPT DE EXECUÇÃO — Code House Landing Page
## Cole este texto numa nova sessão para iniciar o Ralph Loop /build completo

---

Você é um engenheiro frontend experiente executando o Ralph Loop `/build`.

**Objetivo:** Produzir a landing page completa da Code House — empresa de soluções personalizadas em TI para pequenas empresas. O entregável é um conjunto de arquivos prontos para deploy no Render como site estático.

**Spec de referência obrigatória:** Leia integralmente o arquivo `C:\Users\Admin\Documents\Projetos\code-house\specs\build-prompt-master.md` antes de qualquer linha de código.

---

## Contexto do projeto

**Empresa:** Code House — soluções personalizadas em TI para pequenas empresas (CRM, ERP, e-shop, site institucional, sistemas sob medida).

**Público:** Donos de pequenas empresas (dono de metalúrgica, gerente de padaria, proprietário de loja de roupas) — não técnicos, mas que reconhecem qualidade quando veem.

**Tom de voz:** Técnico mas acessível. Direto, sem firulas. "Entendemos o seu negócio e construímos o que ele precisa."

**Estética obrigatória:** Minimalista brutalista leve. Azul-nuvem. Tipografia com personalidade. SEM cara de template lovable, SEM cara de AI genérico.

---

## Arquivos a criar

```
code-house/
├── index.html                  ← landing page principal (auto-suficiente)
├── politica-privacidade.html   ← LGPD
├── 404.html                    ← página de erro
├── favicon.svg                 ← ícone CH azul
├── render.yaml                 ← configuração Render
└── _headers                    ← CSP e security headers
```

Não criar nenhum arquivo JS ou CSS externo — tudo inline em `index.html`.

---

## Stack obrigatória (CDN, todos com `defer`)

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/lenis/1.1.14/lenis.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r165/three.min.js" defer></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/splitting/1.0.6/splitting.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/splitting/1.0.6/splitting.min.js" defer></script>
```

Fontes Google:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Inter:wght@400;500&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
```

Todo JS de animação dentro de `window.addEventListener('load', () => { ... })`.

---

## Design Tokens (implementar exatamente como especificado)

```css
:root {
  --bg:#F1F4F8; --surface:#E6ECF3; --surface-up:#FAFCFF;
  --cloud:#2D74A0; --cloud-h:#1F5F88; --cloud-l:#5A9EC4; --cloud-f:#C5DEF0;
  --ink:#101820; --ink-m:#3D566E; --ink-f:#6A8CA4;
  --border:#C2D2E2; --border-s:#7AADC8;
  --ok:#2B8A5F; --ok-bg:rgba(43,138,95,.12);
  --warn:#B37C0A; --warn-bg:rgba(179,124,10,.12);
  --red:#B84040; --red-bg:rgba(184,64,64,.1);
  --wpp:#25D366;
  --f-display:'Syne',sans-serif;
  --f-body:'Inter',system-ui,sans-serif;
  --f-mono:'Space Mono','Courier New',monospace;
  --t-hero:clamp(3rem,6.5vw,5.2rem);
  --t-h2:clamp(1.8rem,3vw,2.6rem);
  --t-h3:1.1rem; --t-body:1rem; --t-sm:0.875rem; --t-label:0.62rem; --t-mono:0.68rem;
  --max-w:1140px; --pad-x:clamp(1.5rem,5vw,6rem); --pad-sec:clamp(4rem,8vw,8rem);
  --r:3px;
  --sh-sm:0 1px 3px rgba(14,30,55,.07),0 1px 2px rgba(14,30,55,.05);
  --sh-md:0 4px 14px rgba(14,30,55,.09),0 2px 4px rgba(14,30,55,.05);
  --sh-lg:0 12px 40px rgba(14,30,55,.12),0 4px 8px rgba(14,30,55,.06);
  --trans:160ms cubic-bezier(.4,0,.2,1);
  --trans-md:300ms cubic-bezier(.4,0,.2,1);
}
/* Dark mode completo — redefinir todos os tokens acima para variantes dark */
@media(prefers-color-scheme:dark){:root{
  --bg:#0C131C; --surface:#121E2A; --surface-up:#18293A;
  --cloud:#5898C0; --cloud-h:#6AAFD6; --cloud-f:#1A3550;
  --ink:#D6E6F4; --ink-m:#7A9AB4; --ink-f:#486880;
  --border:#1C3652; --border-s:#2C5070;
}}
:root[data-theme="dark"]{/* mesmos tokens dark */}
:root[data-theme="light"]{/* mesmos tokens light (:root original) */}
```

---

## Seções e componentes a implementar

Implementar nesta ordem exata:

### 1. `<head>` completo
- Charset, viewport, theme-color
- Anti-flash de tema: script inline antes de qualquer coisa
- Google Fonts com preconnect
- Título e metadados SEO completos
- Open Graph e Twitter Card
- Canonical placeholder
- JSON-LD Organization schema
- Favicon SVG inline ou referência a `favicon.svg`
- CDN scripts com defer (lista acima)

### 2. Preloader
- `<div id="preloader">` fullscreen, `z-index:9999`
- Logo "CODE.HOUSE" com Splitting.js animando char por char
- Barra de progresso 120px animando width
- Desaparece em `window.load` com fade+scale
- Graceful: `window.onerror` garante que nunca fica travado

### 3. Cursor customizado
- Círculo 16px com borda `var(--cloud)` + dot 4px
- Smooth follow via lerp (0.12)
- Estados: hover links (escala 2.2×), hover canvas (opacity 0)
- Não inicializar em `pointer: coarse` (mobile/touch)

### 4. Nav sticky
- Logo + links + CTA + toggle tema
- Progress bar 2px no topo (% scroll)
- IntersectionObserver para link ativo com underline animada
- Minifica ao scroll para baixo (60px→48px)
- Hamburger mobile (< 900px): 3 barras → X via CSS transform
- Drawer mobile: Anime.js slideDown, foco armadilhado, Escape fecha
- ARIA: `aria-expanded`, `aria-label` dinâmicos

### 5. Hero (min-height: 100svh)
- Grid 2 colunas desktop: `1.1fr 0.9fr`
- Headline com Splitting.js por char + GSAP timeline
- Eyebrow `// soluções personalizadas em TI` — Space Mono
- H1: "Sistemas feitos para o seu modo de operar." — Syne 800, `--t-hero`, `letter-spacing:-.03em`
- "seu" em `<span style="color:var(--cloud)">`
- Sub: Inter 400, `max-width:46ch`, 1.75 line-height
- 2 botões: sólido ("Falar com a gente") + outline ("Ver exemplos")
- Magnetic effect no botão primário (GSAP quickTo)
- Stat strip: "38+ projetos · 22 clientes · 5 anos"
- Canvas Three.js na coluna direita (ver spec Three.js abaixo)
- Mockup CRM flutuando sobre canvas (ver spec mockup abaixo)
- Toast notifications no mockup (1.5s e 5s após load)

**Three.js canvas:**
- ~500 partículas em campo 3D (`THREE.Points`)
- Cor lida de CSS var `--cloud` via `getComputedStyle`
- Rotação auto Y: `0.0008` por frame
- Mouse parallax: fator 0.04, com lerp
- Resize handler e cancelamento em unload
- Mobile (<900px): height 220px, sem mouse parallax
- `prefers-reduced-motion`: sem rotação, sem mouse response
- Dark mode: atualiza cores via Anime.js lerp em 300ms

**Mockup CRM no hero:**
- Window chrome: dots, label "CRM — Clientes"
- Sidebar: 6 itens, item "Clientes" ativo com borda esquerda 2px
- 3 KPI cards: Total (42), Novos (7), Retenção (94%)
- Tabela 5 clientes com chips de status
- Feed de atividade com dot pulsando
- Toasts com slide-up Anime.js

### 6. Marquee/ticker de tecnologias
- CSS `@keyframes marquee` puro (sem JS)
- Pausa ao hover
- Itens: Node.js · PostgreSQL · React · TypeScript · Docker · Python · Next.js · Supabase · AWS · Linux
- `prefers-reduced-motion`: parado

### 7. Stats section
- 4 colunas com borda vertical, ícones SVG, números grandes Syne 800
- Countup Anime.js `easeOutExpo` 1800ms, IntersectionObserver, uma vez só
- Valores: 38+ / 22+ / 5+ / 100%
- `prefers-reduced-motion`: valor final direto

### 8. Serviços — lista + painel de detalhe
- Grid `300px 1fr` desktop, accordion mobile
- 5 serviços: CRM / ERP / E-shop / Site Institucional / Sob Medida
- Lista: hover + ativo com borda esquerda 3px + fundo
- Painel: Anime.js fade+slide 120ms saída, 200ms entrada
- Conteúdo completo (H3, parágrafo, 5 features com checkmark SVG) para cada serviço
- ARIA tablist/tab/tabpanel completo
- CTA inline "→ Ver exemplo deste sistema" linka para aba de exemplos correspondente

### 9. Processo — GSAP ScrollTrigger scrub
- 3 etapas em row, números de fundo 01/02/03 em Syne 800 `6rem` `var(--border)` `opacity:.35`
- GSAP ScrollTrigger: cards 2 e 3 com scrub `0.8`, entram com `translateX(60px) opacity(0→1)`
- Connector SVG line entre cards com `stroke-dashoffset` animado pelo scrub
- Borda `3px solid var(--cloud)` no canto superior esquerdo de cada card (brutalismo)
- Mobile: coluna, fade-in simples

### 10. Exemplos — 4 abas
**Sistema de abas:**
- ARIA completo (tablist/tab/tabpanel, aria-selected, hidden nos painéis inativos)
- Teclado: setas ←→, Home/End, Enter/Space
- Transição: Anime.js slide horizontal (direção relativa à posição da aba)
- `min-height: 540px`

**Aba CRM** (H-59a):
- Grid `340px | 1fr`
- 4 KPIs 2×2, funil 4 estágios com barras animadas (width 0→final ao ativar, Anime.js stagger)
- Tabela 6 negócios com chips coloridos, linha 1 pulsando (live)
- Feed de atividade 3 itens, footer com total

**Aba ERP** (H-59b):
- 4 KPIs com trend arrows ▲▼
- SVG line chart 12 meses: `<polyline>` + área fill + grid tracejado + tooltip hover
- Animação ao ativar aba: stroke-dashoffset Anime.js 1.6s `easeInOutSine`
- Ponto final pulsando
- Tabela 5 pedidos recentes + mini-painel de ruptura de estoque

**Aba E-shop** (H-59c):
- Campo busca debounce 200ms
- Pills de categoria com filtro Anime.js (scale+opacity)
- Grid 3×2 de produtos: SVG silhuetas reconhecíveis, ratings SVG, badges Oferta/Novo
- Botão Adicionar com feedback "✓ Adicionado!" 1.5s
- Carrinho lateral: lista, ±quantidade, remover, total countup Anime.js
- Carrinho pré-carregado com 2 itens
- Desfazer ao remover (toast 4s)

**Aba Site** (H-59d):
- Prévia interativa simulada: nav, hero, 3 feature cards com hover `translateY(-4px)`, testimonial
- Painel lateral: 8 features incluídas + CTA

### 11. Seção "Por que a Code House?"
- Grid `1fr 1fr`
- Tabela de comparação: "Template genérico" (tachado) vs "Code House" (checkmarks `var(--ok)`)
- Reveal por linha com stagger via ScrollTrigger

### 12. Formulário de contato
- Grid `1fr 1fr`: copy + formulário
- Labels flutuantes (position absolute, animate no foco)
- Campos: Nome* / Email* / Empresa / Mensagem* com contador 0/2000
- Validação `onblur` com mensagens específicas por erro
- Estado de erro: `var(--red)` border + mensagem slide-down Anime.js
- Estado válido: border `var(--cloud)` (feedback positivo)
- Botão submit: `disabled` se inválido; loading com spinner SVG; sucesso com checkmark SVG animado
- Copy: eyebrow + H2 + parágrafo + 3 bullets + link WhatsApp
- LGPD: aviso discreto abaixo do botão

### 13. Footer
- 3 colunas: Brand / Links / Contato
- Links com hover `translateX(4px)`
- Marquee de rodapé (direção invertida ao de cima)
- Footer bottom: copyright + "Política de Privacidade" link
- `padding-bottom: env(safe-area-inset-bottom)`

### 14. WhatsApp floating button
- `position:fixed`, 56px, `background:var(--wpp)`
- Pulse ring via `::after`, `@keyframes wppPulse`
- Tooltip à esquerda no hover
- Aparece apenas após scroll > 400px
- 48px em mobile
- `aria-label` completo

### 15. LGPD banner
- Sticky bottom, não bloqueia conteúdo
- Fecha ao "Entendi" + `localStorage` ch-consent
- Link para `politica-privacidade.html`

### 16. Animações globais
**Reveals via ScrollTrigger:**
- Padrão: eyebrow `translateX(-16px)`, H2 `translateY(16px)`, cards `translateY(20px)` com stagger
- `once: true`, `start: "top 85%"`
- `ScrollTrigger.refresh()` após 200ms do load

**Lenis:**
- `duration: 1.1`, easing exponencial
- `lenis.on('scroll', ScrollTrigger.update)` + `gsap.ticker.add`
- `smoothWheel: false` em `pointer:coarse`
- Âncoras: `preventDefault` + `lenis.scrollTo(target, { offset: -60 })`

**Graceful degradation:**
- Verificar `typeof gsap === 'undefined'` etc antes de usar
- Elementos com `opacity:0` nos estados iniciais das animações: sempre ter CSS fallback `@media(prefers-reduced-motion:reduce) { * { opacity:1!important; transform:none!important } }`

### 17. Noise/grain overlay
- Canvas 800×800 com ImageData random, tileado via `background-image: url(dataURL)`
- `opacity:.035` (light) / `.05` (dark)
- 9fps update

### 18. Dark mode transition
- Ao clicar toggle: `classList.add('theme-transitioning')` por 400ms
- CSS transitions temporárias em background, color, border, box-shadow
- Icone sol/lua com fade-in 200ms

### 19. Cursor customizado
- (ver spec acima)
- Inicializar após `load`, verificar `pointer:coarse` antes

### 20. Magnetic buttons
- GSAP `quickTo` nos 2 elementos (botão hero, nenhum outros)
- Threshold 80px, fator 0.35
- Spring de volta `elastic.out(1, .4)`

---

## Regras invioláveis de IHC e acessibilidade

- **Touch targets ≥ 44px** em todos os elementos clicáveis em mobile
- **`font-size: 16px` em inputs mobile** (previne zoom do iOS)
- **Contraste WCAG AA**: 4.5:1 texto, 3:1 UI — verificar TODOS os pares em light E dark
- **Focus visible** em todos os elementos interativos: `outline: 2px solid var(--cloud); outline-offset: 3px`
- **Skip link** no início do body: `<a href="#main" class="skip-link">Ir para o conteúdo</a>`
- **`prefers-reduced-motion`**: GSAP `defaults({duration:0})`, Anime.js `duration:0`, Three.js sem rotação, Lenis desabilitado, marquee parado
- **Ícones decorativos**: `aria-hidden="true"` em todos
- **Links externos**: `target="_blank" rel="noopener noreferrer"` + aviso no aria-label
- **Formulário**: `<label>` para cada `<input>`, erros via `aria-describedby`
- **Abas**: ARIA tablist/tab/tabpanel completo, teclado setas+Home+End+Enter
- **Jamais**: elemento com `opacity:0` permanente, scroll-jacking agressivo, animação infinite em elementos grandes

## Regras de LGPD

- Banner sticky bottom com aceite persistido em localStorage
- Texto abaixo do submit: dados usados apenas para responder o contato
- Arquivo `politica-privacidade.html` com todos os campos obrigatórios
- Nenhum cookie de rastreamento na v3 (sem Google Analytics, sem Pixel)
- `Referrer-Policy: strict-origin-when-cross-origin` nos headers

## Regras de Performance

- Todos CDNs com `defer` — nenhum bloqueia render
- `requestAnimationFrame` em scroll handlers (nunca `scroll` direto)
- `will-change: transform, opacity` adicionado antes da animação, REMOVIDO após completar
- Three.js `antialias: false` em mobile
- `font-display: swap` nas Google Fonts
- Lighthouse meta: Perf ≥ 90, A11y ≥ 95, SEO ≥ 95, BP ≥ 90

---

## Dados e copy definitivos

**Headline hero:** "Sistemas feitos para o seu modo de operar."
**Subtítulo:** "A Code House entende como sua empresa funciona de verdade — e constrói o sistema que acompanha esse ritmo, sem templates e sem engessamento."
**Stats:** 38+ projetos / 22+ clientes / 5+ anos / 100% suporte
**WhatsApp:** `https://wa.me/5500000000000` (placeholder — H-20 substituirá)
**Email:** `contato@codehouse.dev` (placeholder)

---

## Verificação final antes de entregar

Após toda implementação:

1. Checar: nenhum `console.error` no browser
2. Checar: preloader desaparece corretamente
3. Checar: todos os 4 painéis de exemplos abrem e fecham com teclado
4. Checar: formulário rejeita envio com campos vazios
5. Checar: dark mode funciona (toggle e media query)
6. Checar: `prefers-reduced-motion` remove todas as animações
7. Checar: página legível com JS desabilitado (conteúdo visível, sem animações travadas)
8. Checar: mobile 375px — nenhum overflow horizontal
9. Checar: hamburger abre e fecha com Escape e foco armadilhado
10. Checar: Three.js não quebra layout em nenhum tamanho

Se qualquer item falhar: corrigir antes de declarar conclusão.

---

**Agora execute o `/build` lendo o spec completo em `build-prompt-master.md` e produza os 6 arquivos.**
