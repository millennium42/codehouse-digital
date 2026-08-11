# Code House — Fix Stories v3
## Diagnóstico do HTML atual + Histórias de correção

**Data:** 2026-08-08  
**Arquivo auditado:** `codehouse.html` (857 linhas)  
**Status:** REPROVADO — não atende critério de site profissional

---

## Auditoria — Tabela de problemas encontrados

| ID | Severidade | Categoria | Problema | Linha(s) |
|---|---|---|---|---|
| BUG-01 | **P0** | Funcional | Exemplos são 4 cards estáticos em grid 2×2 — não há tabs | 502–717 |
| BUG-02 | **P0** | Funcional | E-shop category tabs: `cursor:default`, não clicáveis | 207 |
| BUG-03 | **P0** | Funcional | Formulário sem campo email — impossível responder o visitante | 732–750 |
| BUG-04 | **P0** | Funcional | Formulário sem validação inline — aceita submit com campos inválidos sem feedback no campo | 834–855 |
| BUG-05 | **P0** | Visual | Tipografia genérica: usa `system-ui` e `Courier New` — zero identidade | 12–13 |
| BUG-06 | **P0** | Funcional | Zero bibliotecas JS — sem GSAP, Anime.js, Three.js, Lenis, Splitting.js | inteiro |
| BUG-07 | **P0** | Visual | Hero sem impacto — grid simples, sem canvas 3D, headline estática | 347–401 |
| BUG-08 | **P1** | Visual | Stats: apenas números, sem ícones, countup manual sem easing profissional | 403–423 |
| BUG-09 | **P1** | Visual | Serviços: 5 cards estáticos sem painel de detalhe interativo | 428–460 |
| BUG-10 | **P1** | Visual | Processo: 3 cards simples, sem ScrollTrigger, sem connector animado | 464–492 |
| BUG-11 | **P1** | Visual | ERP chart: `stroke-dasharray:600` hardcoded, anima ao carregar (não ao entrar na viewport) | 582 |
| BUG-12 | **P1** | Visual | Barras do pipeline CRM: largura fixa no CSS, nunca animam (sem trigger) | 157–160 |
| BUG-13 | **P1** | Visual | Seção "Por que Code House" ausente — sem diferenciação competitiva | — |
| BUG-14 | **P1** | Visual | Marquee/ticker de tecnologias ausente | — |
| BUG-15 | **P1** | Visual | Sem preloader — página aparece sem entrada | — |
| BUG-16 | **P1** | Visual | Sem LGPD banner | — |
| BUG-17 | **P2** | Visual | Sem cursor customizado | — |
| BUG-18 | **P2** | Visual | Sem noise/grain texture | — |
| BUG-19 | **P2** | Visual | Sem progress bar na nav | — |
| BUG-20 | **P2** | Visual | Sem indicador de seção ativa na nav | — |
| BUG-21 | **P2** | Visual | Sem smooth scroll (Lenis) | — |
| BUG-22 | **P2** | SEO | Sem meta description, OG tags, favicon, canonical | — |
| BUG-23 | **P2** | Segurança | Sem `_headers` CSP para Render | — |
| BUG-24 | **P2** | Segurança | WPP float aparece imediatamente (sem verificar scroll > 400px) | 273–277 |
| BUG-25 | **P2** | Visual | Nav sem hamburger mobile funcional (links apenas `display:none`, nada substitui) | 294–295 |
| BUG-26 | **P2** | Visual | Sem seção de processo com animação horizontal | — |
| BUG-27 | **P2** | Visual | Hero mockup CRM sem toast notifications | — |
| BUG-28 | **P2** | Acessibilidade | Formulário sem `type="email"`, sem `aria-describedby` em erros | 735 |
| BUG-29 | **P2** | Acessibilidade | `.wf-quote` CSS tem `"` extra causando syntax error no CSS (linha 240) | 240 |
| BUG-30 | **P2** | Visual | Linha `display:none` no `proc-line` — conector do processo está oculto intencionalmente | 125 |

---

## Decisão arquitetural: reescrever do zero

O HTML atual tem 857 linhas de código que estabelecem estrutura correta para nav, hero mockup, stats, serviços, processo e formulário. O problema é que **falta o JavaScript inteiro e a estrutura dos exemplos precisa ser demolida e refeita como tabs**.

**Decisão:** Reescrever `index.html` do zero seguindo este spec, reutilizando os componentes CSS/HTML que funcionam (tokens de cor, nav, footer, mockup CRM).

---

## Histórias de Fix — Execução obrigatória

---

### FX-01 — Fontes: Syne + Inter + Space Mono

**Diagnóstico:** `--sans: system-ui` e `--mono: 'Courier New'`. O visual parece um browser default.

**Fix:**
- [ ] Adicionar ao `<head>` (antes de qualquer CSS):
  ```html
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Inter:wght@400;500&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
  ```
- [ ] Substituir `--sans` e `--mono` por:
  ```css
  --f-display: 'Syne', sans-serif;
  --f-body: 'Inter', system-ui, sans-serif;
  --f-mono: 'Space Mono', 'Courier New', monospace;
  ```
- [ ] Aplicar `font-family: var(--f-display)` em todos os `h1, h2, h3`
- [ ] Aplicar `font-family: var(--f-body)` em `body, p, input, textarea`
- [ ] Aplicar `font-family: var(--f-mono)` em `.eyebrow, .sec-tag, nav a, .btn, .tg, .pill, .sk-l, .fl`
- [ ] H1: `letter-spacing: -.03em` (Syne é tight por padrão mas precisa de ajuste)
- [ ] Nav links: `letter-spacing: .12em` (Space Mono precisa de espaçamento)
- [ ] Ajustar `font-size` do `h1` para `clamp(3rem, 6.5vw, 5.2rem)` — Syne é mais larga que system-ui
- [ ] Verificar contraste: Syne 700 em `var(--ink)` sobre `var(--bg)` — ratio ≥ 4.5:1

---

### FX-02 — Libraries JS: carregar GSAP, Anime.js, Three.js, Lenis

**Diagnóstico:** Nenhuma biblioteca JS carregada. Todas as animações dependem de IntersectionObserver + CSS transitions simples.

**Fix:**
- [ ] Adicionar antes do `</body>` (todos com `defer`):
  ```html
  <script src="https://cdnjs.cloudflare.com/ajax/libs/lenis/1.1.14/lenis.min.js" defer></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js" defer></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r165/three.min.js" defer></script>
  ```
- [ ] No `<head>`:
  ```html
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/splitting/1.0.6/splitting.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/splitting/1.0.6/splitting.min.js" defer></script>
  ```
- [ ] Todo JS de animação dentro de `window.addEventListener('load', () => { ... })`
- [ ] Graceful degradation: envolver cada bloco de animação em `if (typeof gsap !== 'undefined') { ... }` etc.
- [ ] `prefers-reduced-motion`: verificar e desativar animações:
  ```js
  const noMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!noMotion) { /* iniciar animações */ }
  ```

---

### FX-03 — Hero: Three.js canvas + GSAP headline + impacto visual

**Diagnóstico (linha 347–401):** Hero é grid simples com dot-grid CSS. Headline aparece sem animação. Lado direito tem o mockup mas sem visual de fundo impactante.

**Fix:**

*Estrutura HTML:*
- [ ] Hero: `min-height: 100svh` (não `padding:7rem`)
- [ ] Coluna direita: adicionar `<canvas id="heroCanvas"></canvas>` que ocupa 100% do espaço
- [ ] Mockup CRM flutua sobre o canvas: `position: absolute; bottom: 2rem; right: 2rem`
- [ ] Wrapper do canvas: `position: relative; overflow: hidden`

*Three.js canvas:*
```js
window.addEventListener('load', () => {
  if (typeof THREE === 'undefined') return;
  const canvas = document.getElementById('heroCanvas');
  if (!canvas) return;
  const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: window.innerWidth > 900 });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.setSize(canvas.parentElement.offsetWidth, canvas.parentElement.offsetHeight);
  
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(60, canvas.parentElement.offsetWidth / canvas.parentElement.offsetHeight, 0.1, 100);
  camera.position.z = 5;
  
  const geo = new THREE.BufferGeometry();
  const count = 500;
  const positions = new Float32Array(count * 3);
  for (let i = 0; i < count * 3; i++) positions[i] = (Math.random() - 0.5) * 8;
  geo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
  
  const cloudColor = getComputedStyle(document.documentElement).getPropertyValue('--cloud').trim() || '#3E82AB';
  const mat = new THREE.PointsMaterial({ color: cloudColor, size: 0.04, sizeAttenuation: true });
  const points = new THREE.Points(geo, mat);
  scene.add(points);
  
  let mouseX = 0, mouseY = 0, targetX = 0, targetY = 0;
  if (window.innerWidth > 900) {
    document.addEventListener('mousemove', e => {
      mouseX = (e.clientX / window.innerWidth - 0.5) * 2;
      mouseY = (e.clientY / window.innerHeight - 0.5) * 2;
    });
  }
  
  let rafId;
  const animate = () => {
    rafId = requestAnimationFrame(animate);
    if (!noMotion) {
      points.rotation.y += 0.0008;
      targetX += (mouseX * 0.04 - targetX) * 0.05;
      targetY += (-mouseY * 0.04 - targetY) * 0.05;
      points.rotation.x = targetY;
      points.rotation.z = targetX;
    }
    renderer.render(scene, camera);
  };
  animate();
  
  window.addEventListener('resize', () => {
    const w = canvas.parentElement.offsetWidth;
    const h = canvas.parentElement.offsetHeight;
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
    renderer.setSize(w, h);
  });
  
  window.addEventListener('beforeunload', () => cancelAnimationFrame(rafId));
  
  // Atualizar cor ao trocar tema
  document.addEventListener('themeChanged', () => {
    const newColor = getComputedStyle(document.documentElement).getPropertyValue('--cloud').trim();
    mat.color.set(newColor);
  });
});
```

*GSAP headline com Splitting.js:*
```js
window.addEventListener('load', () => {
  if (typeof Splitting !== 'undefined' && typeof gsap !== 'undefined') {
    Splitting(); // aplica data-splitting em elements com [data-splitting]
    const tl = gsap.timeline({ delay: 0.3 });
    tl.from('.eyebrow', { opacity: 0, y: 12, duration: 0.45, ease: 'power2.out' })
      .from('.hero h1 .char', { opacity: 0, y: 24, rotateX: 45, stagger: 0.025, duration: 0.5, ease: 'power3.out', transformOrigin: 'bottom center' }, '-=0.2')
      .from('.hero-sub', { opacity: 0, y: 10, duration: 0.45, ease: 'power2.out' }, '-=0.2')
      .from('.btn-row .btn', { opacity: 0, y: 8, stagger: 0.1, duration: 0.35, ease: 'power2.out' }, '-=0.2')
      .from('.hero-stats', { opacity: 0, duration: 0.3, ease: 'power1.out' }, '-=0.1');
  }
});
```
- [ ] Adicionar `data-splitting` ao `<h1>` no HTML
- [ ] Adicionar `<p class="hero-stats">38+ projetos · 22 clientes · 5 anos</p>` abaixo dos botões

*Toast notifications no mockup:*
```js
function showToast(container, text, delay) {
  setTimeout(() => {
    if (!document.contains(container)) return;
    const toast = document.createElement('div');
    toast.className = 'app-toast';
    toast.textContent = text; // textContent, não innerHTML
    container.appendChild(toast);
    requestAnimationFrame(() => { toast.classList.add('visible'); });
    setTimeout(() => {
      toast.classList.remove('visible');
      setTimeout(() => toast.remove(), 300);
    }, 3500);
  }, delay);
}
```
- [ ] CSS para `.app-toast`: `position:absolute; bottom:4px; left:4px; right:4px; background:var(--ok-bg); border:1px solid var(--ok); border-radius:2px; padding:.4rem .6rem; font-family:var(--f-mono); font-size:.5rem; color:var(--ok); transform:translateY(8px); opacity:0; transition:transform .25s ease, opacity .25s ease`
- [ ] CSS `.app-toast.visible`: `transform:translateY(0); opacity:1`
- [ ] Chamar após load: toast 1 (1500ms) + toast 2 (5000ms)

---

### FX-04 — Stats: ícones SVG + Anime.js countup + easing profissional

**Diagnóstico (linhas 403–423):** Countup usa `requestAnimationFrame` manual sem easing. Sem ícones. Visual fraco.

**Fix HTML — cada `.stat-item` recebe ícone SVG antes do número:**
```html
<div class="stat-item">
  <div class="stat-icon" aria-hidden="true"><!-- SVG inline --></div>
  <span class="stat-num" data-target="38">0</span>
  <span class="stat-label">Projetos entregues</span>
</div>
```

Ícones SVG (stroke, 24px, stroke-width 1.4, stroke: var(--cloud)):
- Projetos: `<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>` (code icon)
- Clientes: `<circle cx="9" cy="7" r="4"/><path d="M3 21v-2a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v2"/><path d="M19 11c1.657 0 3 1.343 3 3v3"/>` (people icon)
- Anos: `<rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>` (calendar)
- Suporte: `<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/>` (shield check)

**Fix JS — substituir countup manual por Anime.js:**
- [ ] Remover contadores manuais (linhas 811–831)
- [ ] Substituir por:
  ```js
  if (typeof anime !== 'undefined') {
    const statObs = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (!e.isIntersecting) return;
        statObs.unobserve(e.target);
        const el = e.target;
        const target = parseInt(el.dataset.target);
        if (!target || noMotion) { el.textContent = el.dataset.suffix || target + '+'; return; }
        anime({ targets: el, innerHTML: [0, target], round: 1, duration: 1800, easing: 'easeOutExpo',
          update: () => { if (el.dataset.suffix) el.textContent = el.textContent + el.dataset.suffix; }
        });
      });
    }, { threshold: 0.6 });
    document.querySelectorAll('.stat-num[data-target]').forEach(el => statObs.observe(el));
  }
  ```
- [ ] Adicionar `data-suffix="+"` nos 3 primeiros stat-num; `data-suffix="%"` no suporte

**Fix CSS `.stat-icon`:**
```css
.stat-icon { color: var(--cloud); margin-bottom: 0.75rem; display: flex; justify-content: center; }
.stat-item { display: flex; flex-direction: column; align-items: center; }
```

---

### FX-05 — Exemplos: demolir grid 2×2 e construir sistema de 4 abas

**Diagnóstico (linhas 497–717):** 4 cards comprimidos em grid 2×2. Não há tabs, não há interatividade, mockups estão espremidos e os textos ficam ilegíveis.

**Fix — estrutura HTML completa da seção exemplos:**

```html
<section class="sec" id="exemplos">
  <div class="sec-hdr fade">
    <span class="sec-tag">// exemplos de sistemas</span>
    <h2>O que sistemas feitos assim parecem</h2>
  </div>

  <!-- Tab bar -->
  <div class="tabs-bar" role="tablist" aria-label="Exemplos de sistemas">
    <button class="tab-btn active" role="tab" id="tab-crm" aria-controls="panel-crm" aria-selected="true" tabindex="0">
      <svg width="14" height="14"><!-- ícone CRM --></svg> CRM
    </button>
    <button class="tab-btn" role="tab" id="tab-erp" aria-controls="panel-erp" aria-selected="false" tabindex="-1">
      <svg width="14" height="14"><!-- ícone ERP --></svg> ERP
    </button>
    <button class="tab-btn" role="tab" id="tab-eshop" aria-controls="panel-eshop" aria-selected="false" tabindex="-1">
      <svg width="14" height="14"><!-- ícone E-shop --></svg> E-shop
    </button>
    <button class="tab-btn" role="tab" id="tab-site" aria-controls="panel-site" aria-selected="false" tabindex="-1">
      <svg width="14" height="14"><!-- ícone Site --></svg> Site Institucional
    </button>
  </div>

  <!-- Painéis -->
  <div class="tab-panels">
    <div class="tab-panel" id="panel-crm" role="tabpanel" aria-labelledby="tab-crm">
      <!-- conteúdo CRM full-size (ver FX-06a) -->
    </div>
    <div class="tab-panel" id="panel-erp" role="tabpanel" aria-labelledby="tab-erp" hidden>
      <!-- conteúdo ERP full-size (ver FX-06b) -->
    </div>
    <div class="tab-panel" id="panel-eshop" role="tabpanel" aria-labelledby="tab-eshop" hidden>
      <!-- conteúdo E-shop full-size (ver FX-06c) -->
    </div>
    <div class="tab-panel" id="panel-site" role="tabpanel" aria-labelledby="tab-site" hidden>
      <!-- conteúdo Site full-size (ver FX-06d) -->
    </div>
  </div>
</section>
```

**Fix CSS:**
```css
.tabs-bar {
  display: flex;
  gap: 0;
  border-bottom: 2px solid var(--border);
  margin-bottom: 0;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}
.tab-btn {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  padding: .9rem 1.5rem;
  font-family: var(--f-mono);
  font-size: .62rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--ink-m);
  background: transparent;
  border: none;
  border-bottom: 2px solid transparent;
  margin-bottom: -2px;
  cursor: pointer;
  transition: color var(--trans), background var(--trans);
  white-space: nowrap;
}
.tab-btn:hover { color: var(--ink); background: var(--surface); }
.tab-btn.active { color: var(--cloud); border-bottom-color: var(--cloud); background: var(--cloud-f); }
.tab-btn:focus-visible { outline: 2px solid var(--cloud); outline-offset: -2px; }

.tab-panels { border: 1px solid var(--border); border-top: none; border-radius: 0 0 var(--r) var(--r); min-height: 520px; overflow: hidden; }
.tab-panel { padding: 1.5rem; display: none; }
.tab-panel:not([hidden]) { display: block; }
```

**Fix JS — lógica de tabs:**
```js
function initTabs() {
  const tabs = document.querySelectorAll('[role="tab"]');
  const panels = document.querySelectorAll('[role="tabpanel"]');
  
  tabs.forEach((tab, i) => {
    tab.addEventListener('click', () => activateTab(i));
    tab.addEventListener('keydown', e => {
      let newIndex = i;
      if (e.key === 'ArrowRight') newIndex = (i + 1) % tabs.length;
      else if (e.key === 'ArrowLeft') newIndex = (i - 1 + tabs.length) % tabs.length;
      else if (e.key === 'Home') newIndex = 0;
      else if (e.key === 'End') newIndex = tabs.length - 1;
      else return;
      e.preventDefault();
      activateTab(newIndex);
      tabs[newIndex].focus();
    });
  });

  function activateTab(index) {
    const currentIndex = [...tabs].findIndex(t => t.classList.contains('active'));
    const direction = index > currentIndex ? 1 : -1;

    tabs.forEach((t, i) => {
      t.classList.toggle('active', i === index);
      t.setAttribute('aria-selected', i === index);
      t.tabIndex = i === index ? 0 : -1;
    });

    panels.forEach((p, i) => {
      if (i === index) {
        p.removeAttribute('hidden');
        if (typeof anime !== 'undefined') {
          anime.remove(p);
          anime({ targets: p, translateX: [direction * 24, 0], opacity: [0, 1], duration: 220, easing: 'easeOutCubic' });
        }
        // Disparar animações do painel ativado
        onTabActivated(p.id);
      } else {
        p.setAttribute('hidden', '');
      }
    });
  }
}
document.addEventListener('DOMContentLoaded', initTabs);
```

---

### FX-06a — Aba CRM: pipeline full-size com barras animadas

**O que construir no `#panel-crm`:**
- [ ] Layout interno: `display: grid; grid-template-columns: 340px 1fr; gap: 1.5rem`
- [ ] Coluna esquerda: 4 KPIs grid 2×2 + funil com 4 barras
- [ ] Coluna direita: tabela 6 clientes + footer com total

**KPIs (`.crm-kpis` existente — manter e adaptar):**
- Total negócios: 19 · Pipeline: R$68k · Fechados: R$28k · Conversão: 41%

**Funil de barras (animação ao ativar aba):**
- [ ] Barras com `width: 0` no CSS inicial
- [ ] `data-fill="100"` / `"66"` / `"48"` / `"26"` em cada `.pipe-fill`
- [ ] Na função `onTabActivated('panel-crm')`:
  ```js
  document.querySelectorAll('#panel-crm .pipe-fill').forEach((bar, i) => {
    anime({ targets: bar, width: bar.dataset.fill + '%', duration: 900, delay: i * 150, easing: 'easeOutCubic' });
  });
  ```

**Tabela de negócios (6 linhas, coluna direita):**
```html
<table class="mt">
  <thead><tr><th>Cliente</th><th>Empresa</th><th>Valor</th><th>Etapa</th><th>Últ. contato</th></tr></thead>
  <tbody>
    <tr class="live-row"><td>Ana Lima</td><td>MerceTex Ind.</td><td>R$ 4.200</td><td><span class="tg tg-ok">Ativo</span></td><td>Hoje 09:14</td></tr>
    <tr><td>Bruno Dias</td><td>LojaTech Sul</td><td>R$ 8.700</td><td><span class="tg tg-pnd">Proposta</span></td><td>Ontem</td></tr>
    <tr><td>Carla Mota</td><td>Studio CM</td><td>R$ 2.800</td><td><span class="tg tg-w">Negociação</span></td><td>3 dias</td></tr>
    <tr><td>Diego Ramos</td><td>FerroMax Ltda</td><td>R$ 12.500</td><td><span class="tg tg-ok">Ativo</span></td><td>Hoje 11:40</td></tr>
    <tr><td>Elisa Cunha</td><td>Padaria Doce</td><td>R$ 1.900</td><td><span class="tg" style="background:var(--surface);color:var(--ink-m)">Prospecção</span></td><td>5 dias</td></tr>
    <tr><td>Felipe Silva</td><td>TecnoFretes</td><td>R$ 6.300</td><td><span class="tg tg-pnd">Proposta</span></td><td>2 dias</td></tr>
  </tbody>
</table>
```
- [ ] `.live-row td` tem `animation: liveRow 3s ease infinite`
- [ ] `@keyframes liveRow { 0%,100%{background:transparent} 50%{background:var(--ok-bg)} }`

---

### FX-06b — Aba ERP: SVG chart animado ao ativar aba

**Diagnóstico:** O `stroke-dashoffset` anima no carregamento da página (linha 286–289 CSS), não quando o painel ERP é ativado.

**Fix:**
- [ ] Remover `animation: drawLine` e `animation: fadeArea` do CSS (linhas 286–289)
- [ ] Adicionar `data-dash="600"` na polyline e `style="stroke-dasharray:600; stroke-dashoffset:600"` inline
- [ ] Adicionar `class="chart-area-svg"` na área e `style="opacity:0"` inline
- [ ] Na função `onTabActivated('panel-erp')`:
  ```js
  const line = document.querySelector('#panel-erp .chart-line');
  const area = document.querySelector('#panel-erp .chart-area');
  if (line && typeof anime !== 'undefined') {
    anime({ targets: line, strokeDashoffset: [600, 0], duration: 1600, easing: 'easeInOutSine' });
    anime({ targets: area, opacity: [0, 1], duration: 600, delay: 1200, easing: 'linear' });
  }
  ```
- [ ] Adicionar tabela de 5 pedidos (ver BUG-11 dados)
- [ ] Mini-painel de ruptura de estoque (3 itens críticos)

---

### FX-06c — Aba E-shop: filtros funcionais + carrinho interativo

**Diagnóstico (linha 207):** `cursor:default` nos botões de categoria, `cursor:default` no botão "+ Add" — nada funciona.

**Fix HTML:**
- [ ] Trocar `.sh-tab` de `<div>` para `<button>` com `cursor:pointer`
- [ ] Cada produto: `data-category="roupas"` etc.
- [ ] Botão add: `<button class="prod-add-btn" data-name="Camiseta Premium" data-price="89.90">+ Adicionar</button>`
- [ ] Adicionar painel de carrinho lateral (coluna direita):
  ```html
  <div class="shop-layout">
    <div class="shop-catalog"><!-- filtros + grid --></div>
    <div class="shop-cart-panel">
      <div class="cart-header"><span>Carrinho</span><span class="cart-badge" id="cartBadge">2</span></div>
      <div class="cart-items" id="cartItems"><!-- items --></div>
      <div class="cart-footer">
        <div class="cart-total-row">
          <span>Total</span>
          <span class="cart-total" id="cartTotal">R$ 219,80</span>
        </div>
        <button class="btn btn-solid" style="width:100%">Finalizar compra</button>
      </div>
    </div>
  </div>
  ```

**Fix JS — filtros:**
```js
document.querySelectorAll('#panel-eshop .sh-tab').forEach(tab => {
  tab.addEventListener('click', () => {
    document.querySelectorAll('#panel-eshop .sh-tab').forEach(t => t.classList.remove('on'));
    tab.classList.add('on');
    const cat = tab.dataset.category;
    document.querySelectorAll('#panel-eshop .prod-card').forEach(card => {
      const match = cat === 'todos' || card.dataset.category === cat;
      card.style.display = match ? '' : 'none';
    });
  });
});
```

**Fix JS — adicionar ao carrinho:**
```js
let cartItems = [
  { name: 'Camiseta Premium', price: 89.90 },
  { name: 'Tênis Esporte', price: 129.90 }
];

document.querySelectorAll('#panel-eshop .prod-add-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const name = btn.dataset.name;
    const price = parseFloat(btn.dataset.price);
    cartItems.push({ name, price });
    renderCart();
    // Feedback
    const original = btn.textContent;
    btn.textContent = '✓ Adicionado!';
    btn.disabled = true;
    setTimeout(() => { btn.textContent = original; btn.disabled = false; }, 1500);
  });
});

function renderCart() {
  const list = document.getElementById('cartItems');
  const badge = document.getElementById('cartBadge');
  const total = document.getElementById('cartTotal');
  if (!list) return;
  
  list.textContent = ''; // limpar com textContent
  cartItems.forEach((item, i) => {
    const row = document.createElement('div');
    row.className = 'cart-item-row';
    
    const name = document.createElement('span');
    name.className = 'cart-item-name';
    name.textContent = item.name;
    
    const price = document.createElement('span');
    price.className = 'cart-item-price';
    price.textContent = 'R$ ' + item.price.toFixed(2).replace('.', ',');
    
    const remove = document.createElement('button');
    remove.className = 'cart-remove';
    remove.textContent = '×';
    remove.setAttribute('aria-label', 'Remover ' + item.name);
    remove.addEventListener('click', () => {
      cartItems.splice(i, 1);
      renderCart();
    });
    
    row.appendChild(name);
    row.appendChild(price);
    row.appendChild(remove);
    list.appendChild(row);
  });
  
  badge.textContent = cartItems.length;
  const sum = cartItems.reduce((a, c) => a + c.price, 0);
  total.textContent = 'R$ ' + sum.toFixed(2).replace('.', ',');
}
renderCart(); // inicializar com 2 itens pré-carregados
```

---

### FX-06d — Aba Site: wireframe com hover effects reais

**Diagnóstico:** Wireframe tem `cursor:default` em todo elemento visual. Não demonstra interatividade.

**Fix:**
- [ ] Links do nav simulado: `cursor:pointer`, `:hover { text-decoration: underline }`
- [ ] Botões simulados: `cursor:pointer`, `:hover { opacity: .85 }`
- [ ] Feature cards: `cursor:pointer`, `:hover { transform:translateY(-3px); box-shadow:var(--sh-sm) }`
- [ ] Todos os `.wf-*` interativos: `transition: var(--trans)`
- [ ] Adicionar painel lateral de "funcionalidades incluídas" com 8 checkmarks
- [ ] CTA no painel lateral: `href="#contato"`, `onclick="lenis?.scrollTo('#contato')"` ou `href="#contato"` nativo

---

### FX-07 — Formulário: campo email + validação inline completa

**Diagnóstico (linhas 732–750):** Sem campo email. Sem validação onblur. Sem mensagens específicas. Sem contador de caracteres.

**Fix HTML — adicionar campo email após nome:**
```html
<div class="field">
  <label class="fl" for="email">Email *</label>
  <input class="fi" id="email" type="email" placeholder="nome@empresa.com.br" autocomplete="email">
  <span class="field-error" id="email-error" role="alert" aria-live="polite"></span>
</div>
```

**Fix — validação por campo:**
```js
const validators = {
  nome: v => v.trim().length < 2 ? 'Nome muito curto — mínimo 2 caracteres.' : null,
  email: v => {
    if (!v.trim()) return 'Por favor, insira seu email.';
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim()) ? null : 'Email inválido. Ex: nome@empresa.com';
  },
  msg: v => v.trim().length < 20 ? 'Mensagem muito curta. Conte mais sobre o que precisa.' : null
};

['nome', 'email', 'msg'].forEach(id => {
  const el = document.getElementById(id);
  const errEl = document.getElementById(id + '-error');
  if (!el || !errEl) return;
  
  el.addEventListener('blur', () => {
    const err = validators[id](el.value);
    showFieldError(el, errEl, err);
  });
  el.addEventListener('input', () => {
    if (el.classList.contains('has-error')) {
      const err = validators[id](el.value);
      showFieldError(el, errEl, err);
    }
  });
});

function showFieldError(input, errEl, message) {
  if (message) {
    input.classList.add('has-error');
    input.style.borderColor = 'var(--red)';
    errEl.textContent = message;
    errEl.style.display = 'block';
  } else {
    input.classList.remove('has-error');
    input.style.borderColor = 'var(--cloud)';
    errEl.textContent = '';
    errEl.style.display = 'none';
  }
}
```

**Fix — submit com validação completa:**
```js
document.getElementById('contactForm').addEventListener('submit', function(e) {
  e.preventDefault();
  
  let hasError = false;
  ['nome', 'email', 'msg'].forEach(id => {
    const el = document.getElementById(id);
    const errEl = document.getElementById(id + '-error');
    if (!el || !errEl) return;
    const err = validators[id](el.value);
    showFieldError(el, errEl, err);
    if (err) hasError = true;
  });
  
  if (hasError) {
    const firstError = this.querySelector('.has-error');
    if (firstError) firstError.focus();
    return;
  }
  
  const btn = this.querySelector('button[type="submit"]');
  btn.innerHTML = `<svg class="spinner" width="14" height="14" viewBox="0 0 14 14"><circle cx="7" cy="7" r="5" fill="none" stroke="currentColor" stroke-width="2" stroke-dasharray="16 16"/></svg> Enviando...`;
  btn.disabled = true;
  
  setTimeout(() => {
    this.style.display = 'none';
    const success = document.getElementById('formSuccess');
    success.classList.add('visible');
    success.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }, 900);
});
```

**Fix CSS:**
```css
.field-error { display:none; color:var(--red); font-size:.72rem; font-family:var(--f-body); margin-top:.25rem; }
.fi.has-error { border-color:var(--red); }
@keyframes spin { to { transform: rotate(360deg); } }
.spinner { animation: spin .8s linear infinite; display:inline-block; vertical-align:middle; }
```

---

### FX-08 — Serviços: painel de detalhe interativo

**Diagnóstico (linhas 428–460):** 5 cards simples em grid. Click não faz nada. Sem painel de detalhes.

**Fix — layout e HTML:**
```html
<section class="sec" id="servicos">
  <div class="sec-hdr fade">
    <span class="sec-tag">// serviços</span>
    <h2>O que a Code House entrega</h2>
  </div>
  <div class="svc-layout">
    <ul class="svc-list" role="tablist" aria-label="Serviços">
      <li role="tab" class="svc-item active" aria-selected="true" aria-controls="svc-detail" id="svc-crm" tabindex="0" data-svc="crm">
        <div class="svc-icon" aria-hidden="true"><!-- SVG --></div>
        <div><p class="svc-name">CRM</p><p class="svc-sub">funil · histórico · automação</p></div>
      </li>
      <!-- repetir para ERP, Site, E-shop, Sob Medida -->
    </ul>
    <div class="svc-detail" id="svc-detail" role="tabpanel" aria-labelledby="svc-crm">
      <p class="svc-detail-eye">// CRM</p>
      <h3>Gestão de clientes que acompanha seu funil de vendas</h3>
      <p>Não é um CRM genérico de prateleira — é construído em cima de como você já trabalha. Funil de vendas configurado do seu jeito, campos que fazem sentido para o negócio, histórico de cada cliente ao alcance.</p>
      <ul class="svc-features">
        <li><svg><!-- check --></svg> Pipeline personalizado</li>
        <li><svg><!-- check --></svg> Histórico de interações</li>
        <li><svg><!-- check --></svg> Alertas e lembretes</li>
        <li><svg><!-- check --></svg> Relatórios do que importa</li>
        <li><svg><!-- check --></svg> Integração com WhatsApp (opcional)</li>
      </ul>
      <a class="svc-cta" href="#exemplos" data-tab="tab-crm">→ Ver exemplo deste sistema</a>
    </div>
  </div>
</section>
```

**Fix CSS:**
```css
.svc-layout { display: grid; grid-template-columns: 280px 1fr; border: 1px solid var(--border); border-radius: var(--r); overflow: hidden; }
.svc-list { list-style: none; border-right: 1px solid var(--border); }
.svc-item { padding: 1.1rem 1.25rem; display: flex; align-items: center; gap: .75rem; cursor: pointer; transition: background var(--trans); border-left: 3px solid transparent; }
.svc-item:hover { background: var(--cloud-f); }
.svc-item.active { border-left-color: var(--cloud); background: var(--cloud-f); }
.svc-item.active .svc-name { color: var(--cloud); }
.svc-item:focus-visible { outline: 2px solid var(--cloud); outline-offset: -2px; }
.svc-sub { font-family: var(--f-mono); font-size: .5rem; color: var(--ink-f); letter-spacing: .06em; margin-top: .15rem; }
.svc-detail { padding: 2.5rem; }
.svc-detail-eye { font-family: var(--f-mono); font-size: var(--t-label); letter-spacing: .16em; text-transform: uppercase; color: var(--cloud); margin-bottom: .75rem; }
.svc-features { list-style: none; margin-top: 1rem; display: flex; flex-direction: column; gap: .55rem; }
.svc-features li { display: flex; align-items: center; gap: .5rem; font-size: .9rem; color: var(--ink-m); }
.svc-features li svg { color: var(--ok); flex-shrink: 0; }
.svc-cta { display: inline-flex; align-items: center; gap: .3rem; margin-top: 1.5rem; font-family: var(--f-mono); font-size: .62rem; letter-spacing: .1em; text-transform: uppercase; color: var(--cloud); text-decoration: none; }
.svc-cta:hover { gap: .6rem; }
```

**Fix JS:**
```js
const svcData = {
  crm: { eye:'// CRM', title:'Gestão de clientes que acompanha seu funil', desc:'...', features:['Pipeline personalizado','Histórico de interações','Alertas e lembretes','Relatórios do que importa','WhatsApp opcional'] },
  erp: { eye:'// ERP', title:'Operação integrada sem planilhas paralelas', desc:'...', features:['Estoque em tempo real','Fluxo de caixa','Pedidos de compra','Dashboard operacional','Alertas de ruptura'] },
  site: { eye:'// Site', title:'Presença digital que representa quem você é', desc:'...', features:['Design único','Mobile-first','SEO técnico incluso','Core Web Vitals','CMS para atualizar'] },
  eshop: { eye:'// E-shop', title:'Loja virtual que vende, não que parece', desc:'...', features:['Catálogo com filtros','Checkout Pix e cartão','Gestão de pedidos','Cálculo de frete','Dashboard de vendas'] },
  sobmedida: { eye:'// Sob Medida', title:'Qualquer sistema que o negócio precise', desc:'...', features:['Levantamento incluso','Prototipagem','Tecnologia certa','Documentação entregue','Suporte pós-lançamento'] }
};

document.querySelectorAll('.svc-item').forEach(item => {
  item.addEventListener('click', () => activateSvc(item));
  item.addEventListener('keydown', e => {
    if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); activateSvc(item); }
  });
});

function activateSvc(item) {
  document.querySelectorAll('.svc-item').forEach(i => { i.classList.remove('active'); i.setAttribute('aria-selected','false'); });
  item.classList.add('active');
  item.setAttribute('aria-selected','true');
  
  const data = svcData[item.dataset.svc];
  const detail = document.getElementById('svc-detail');
  detail.setAttribute('aria-labelledby', item.id);
  
  if (typeof anime !== 'undefined') {
    anime({ targets: detail, opacity: [0,1], translateX: [-12,0], duration: 200, easing: 'easeOutCubic' });
  }
  
  // Atualizar conteúdo com textContent (XSS safe)
  detail.querySelector('.svc-detail-eye').textContent = data.eye;
  detail.querySelector('h3').textContent = data.title;
  detail.querySelector('p:not(.svc-detail-eye)').textContent = data.desc;
  const ul = detail.querySelector('.svc-features');
  ul.textContent = '';
  data.features.forEach(f => {
    const li = document.createElement('li');
    const svg = createCheckSVG();
    li.appendChild(svg);
    const span = document.createElement('span');
    span.textContent = f;
    li.appendChild(span);
    ul.appendChild(li);
  });
}
```

---

### FX-09 — Processo: ScrollTrigger scrub + connector animado

**Diagnóstico (linhas 464–492):** 3 cards estáticos. Sem animação de scroll. Connector line com `display:none`.

**Fix:**
- [ ] Remover `.proc-line` CSS e HTML (será substituído por SVG)
- [ ] Adicionar connector SVG entre os cards:
  ```html
  <div class="process-wrap">
    <svg class="proc-connector" aria-hidden="true" viewBox="0 0 840 4" preserveAspectRatio="none">
      <line x1="140" y1="2" x2="700" y2="2" stroke="var(--cloud)" stroke-width="2" stroke-dasharray="8 4"
            style="stroke-dashoffset:560; transition:stroke-dashoffset 1s ease"/>
    </svg>
    <div class="p-grid"><!-- cards existentes --></div>
  </div>
  ```
- [ ] GSAP ScrollTrigger para entrada dos cards 2 e 3:
  ```js
  if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
    gsap.registerPlugin(ScrollTrigger);
    
    gsap.fromTo('#processo .p-step:nth-child(2)', 
      { opacity: 0, x: 40 },
      { opacity: 1, x: 0, duration: 0.6, ease: 'power2.out',
        scrollTrigger: { trigger: '#processo .p-grid', start: 'top 75%', once: true } }
    );
    gsap.fromTo('#processo .p-step:nth-child(3)',
      { opacity: 0, x: 60 },
      { opacity: 1, x: 0, duration: 0.6, delay: 0.15, ease: 'power2.out',
        scrollTrigger: { trigger: '#processo .p-grid', start: 'top 75%', once: true } }
    );
    
    // Connector line
    ScrollTrigger.create({
      trigger: '#processo .p-grid',
      start: 'top 75%',
      once: true,
      onEnter: () => {
        const line = document.querySelector('.proc-connector line');
        if (line) line.style.strokeDashoffset = '0';
      }
    });
  }
  ```

---

### FX-10 — Preloader

**Diagnóstico:** Ausente. Página aparece instantaneamente sem entrada, especialmente feio quando as fontes CDN demoram.

**Fix HTML — logo antes do `<nav>`:**
```html
<div id="preloader" aria-hidden="true">
  <span class="pre-logo" data-splitting>CODE.HOUSE</span>
  <div class="pre-bar"><div class="pre-fill"></div></div>
</div>
```

**Fix CSS:**
```css
#preloader {
  position: fixed; inset: 0; z-index: 9999;
  background: var(--bg);
  display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 1.5rem;
  transition: opacity .4s ease, transform .4s ease;
}
#preloader.hidden { opacity: 0; transform: scale(1.04); pointer-events: none; }
.pre-logo { font-family: var(--f-mono); font-size: 1.1rem; font-weight: 700; letter-spacing: .08em; color: var(--ink); }
.pre-logo .char { display: inline-block; opacity: 0; transform: translateY(6px); }
.pre-bar { width: 120px; height: 2px; background: var(--border); border-radius: 1px; overflow: hidden; }
.pre-fill { height: 100%; width: 0; background: var(--cloud); border-radius: 1px; transition: width .8s ease; }
```

**Fix JS:**
```js
document.addEventListener('DOMContentLoaded', () => {
  const preloader = document.getElementById('preloader');
  const fill = preloader?.querySelector('.pre-fill');
  
  if (Splitting && preloader) Splitting({ target: '.pre-logo', by: 'chars' });
  
  // Animar chars com delay manual (sem Anime.js pois pode não estar carregado ainda)
  document.querySelectorAll('.pre-logo .char').forEach((c, i) => {
    c.style.transition = `opacity .3s ${i * 60}ms ease, transform .3s ${i * 60}ms ease`;
    requestAnimationFrame(() => { c.style.opacity = '1'; c.style.transform = 'none'; });
  });
  
  if (fill) requestAnimationFrame(() => { fill.style.width = '100%'; });
});

window.addEventListener('load', () => {
  const preloader = document.getElementById('preloader');
  setTimeout(() => {
    preloader?.classList.add('hidden');
    setTimeout(() => { preloader?.remove(); }, 450);
  }, 400);
});
```

---

### FX-11 — LGPD banner

**Fix HTML — logo antes de `</body>`:**
```html
<div id="lgpdBanner" class="lgpd-banner" role="dialog" aria-label="Aviso de privacidade" aria-live="polite" hidden>
  <p class="lgpd-text">
    Este site coleta apenas os dados informados no formulário, usados exclusivamente para responder seu contato.
    <a href="/politica-privacidade.html" class="lgpd-link">Política de Privacidade</a>
  </p>
  <button class="lgpd-btn" id="lgpdAccept">Entendi</button>
</div>
```

**Fix CSS:**
```css
.lgpd-banner {
  position: fixed; bottom: 0; left: 0; right: 0; z-index: 150;
  background: var(--surface); border-top: 1px solid var(--border);
  padding: .85rem var(--pad-x, 3rem);
  display: flex; align-items: center; justify-content: space-between; gap: 1rem;
  flex-wrap: wrap;
}
.lgpd-banner[hidden] { display: none; }
.lgpd-text { font-size: .82rem; color: var(--ink-m); flex: 1; }
.lgpd-link { color: var(--cloud); }
.lgpd-btn { font-family: var(--f-mono); font-size: .6rem; letter-spacing: .1em; text-transform: uppercase; background: var(--cloud); color: var(--bg); border: none; padding: .5rem 1rem; border-radius: var(--r); cursor: pointer; flex-shrink: 0; }
.lgpd-btn:hover { background: var(--cloud-h); }
```

**Fix JS:**
```js
const banner = document.getElementById('lgpdBanner');
if (banner && !localStorage.getItem('ch-consent')) {
  banner.removeAttribute('hidden');
}
document.getElementById('lgpdAccept')?.addEventListener('click', () => {
  localStorage.setItem('ch-consent', 'true');
  if (typeof anime !== 'undefined') {
    anime({ targets: '#lgpdBanner', translateY: ['0', '100%'], opacity: [1, 0], duration: 250, easing: 'easeInCubic',
      complete: () => document.getElementById('lgpdBanner')?.remove() });
  } else {
    document.getElementById('lgpdBanner')?.remove();
  }
});
```

---

### FX-12 — Marquee de tecnologias

**Fix HTML — entre `stats-strip` e `<hr>`:**
```html
<div class="marquee-strip" aria-hidden="true">
  <div class="marquee-track">
    <span class="mq-item">Node.js</span><span class="mq-sep">·</span>
    <span class="mq-item">PostgreSQL</span><span class="mq-sep">·</span>
    <span class="mq-item">React</span><span class="mq-sep">·</span>
    <span class="mq-item">TypeScript</span><span class="mq-sep">·</span>
    <span class="mq-item">Docker</span><span class="mq-sep">·</span>
    <span class="mq-item">Python</span><span class="mq-sep">·</span>
    <span class="mq-item">Next.js</span><span class="mq-sep">·</span>
    <span class="mq-item">Supabase</span><span class="mq-sep">·</span>
    <span class="mq-item">AWS</span><span class="mq-sep">·</span>
    <span class="mq-item">REST API</span><span class="mq-sep">·</span>
    <!-- repetir 2× -->
  </div>
</div>
```

**Fix CSS:**
```css
.marquee-strip { background: var(--surface); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); padding: .9rem 0; overflow: hidden; }
.marquee-track { display: flex; gap: 0; width: max-content; animation: marquee 28s linear infinite; }
.marquee-track:hover { animation-play-state: paused; }
.mq-item { font-family: var(--f-mono); font-size: .58rem; letter-spacing: .12em; text-transform: uppercase; color: var(--ink-f); padding: 0 .6rem; white-space: nowrap; }
.mq-sep { color: var(--border-s); font-size: .7rem; }
@keyframes marquee { 0% { transform: translateX(0) } 100% { transform: translateX(-50%) } }
@media (prefers-reduced-motion: reduce) { .marquee-track { animation-play-state: paused; } }
```

---

### FX-13 — Nav: progress bar + active indicator + hamburger mobile

**Fix CSS:**
```css
.nav-progress { position: absolute; bottom: -1px; left: 0; height: 2px; background: linear-gradient(90deg, var(--cloud-f), var(--cloud)); width: 0; transition: none; pointer-events: none; }
nav { position: relative; } /* já é sticky */

/* Hamburger */
.hamburger { display: none; background: none; border: 1px solid var(--border); border-radius: var(--r); width: 36px; height: 36px; cursor: pointer; flex-direction: column; align-items: center; justify-content: center; gap: 4px; transition: border-color var(--trans); }
.hamburger span { display: block; width: 16px; height: 1.5px; background: var(--ink); transition: transform .2s ease, opacity .2s ease; }
.hamburger.open span:first-child { transform: translateY(5.5px) rotate(45deg); }
.hamburger.open span:nth-child(2) { opacity: 0; }
.hamburger.open span:last-child { transform: translateY(-5.5px) rotate(-45deg); }
@media (max-width: 900px) { .nav-links { display: none; } .hamburger { display: flex; } }

/* Mobile drawer */
.nav-drawer { position: fixed; top: 60px; left: 0; right: 0; background: rgba(var(--bg-rgb, 241,244,248),.97); backdrop-filter: blur(12px); border-bottom: 1px solid var(--border); z-index: 99; padding: 1rem var(--pad-x, 1.5rem); display: none; flex-direction: column; gap: 0; }
.nav-drawer.open { display: flex; }
.nav-drawer a { padding: .85rem 0; font-family: var(--f-mono); font-size: .68rem; letter-spacing: .1em; text-transform: uppercase; color: var(--ink-m); text-decoration: none; border-bottom: 1px solid var(--border); }
.nav-drawer a:last-child { border-bottom: none; }
```

**Fix HTML — adicionar ao `<nav>`:**
```html
<div class="nav-progress" id="navProgress"></div>
<!-- Hamburger -->
<button class="hamburger" id="hamburger" aria-label="Abrir menu" aria-expanded="false" aria-controls="navDrawer">
  <span></span><span></span><span></span>
</button>
```

**Fix HTML — drawer após `</nav>`:**
```html
<div id="navDrawer" class="nav-drawer" role="navigation" aria-label="Menu mobile">
  <a href="#servicos" class="drawer-link">Serviços</a>
  <a href="#processo" class="drawer-link">Processo</a>
  <a href="#exemplos" class="drawer-link">Exemplos</a>
  <a href="#contato" class="drawer-link">Falar com a gente</a>
</div>
```

**Fix JS:**
```js
// Progress bar
const navProgress = document.getElementById('navProgress');
window.addEventListener('scroll', () => {
  if (!navProgress) return;
  const scrolled = window.scrollY / (document.body.scrollHeight - window.innerHeight);
  navProgress.style.width = (scrolled * 100) + '%';
}, { passive: true });

// Hamburger
const hamburger = document.getElementById('hamburger');
const drawer = document.getElementById('navDrawer');
hamburger?.addEventListener('click', () => {
  const isOpen = drawer?.classList.toggle('open');
  hamburger.classList.toggle('open', isOpen);
  hamburger.setAttribute('aria-expanded', isOpen);
  hamburger.setAttribute('aria-label', isOpen ? 'Fechar menu' : 'Abrir menu');
});

// Fechar drawer ao clicar em link
drawer?.querySelectorAll('a').forEach(a => {
  a.addEventListener('click', () => {
    drawer.classList.remove('open');
    hamburger?.classList.remove('open');
    hamburger?.setAttribute('aria-expanded', 'false');
  });
});

// Fechar com Escape + foco armadilhado
document.addEventListener('keydown', e => {
  if (e.key === 'Escape' && drawer?.classList.contains('open')) {
    drawer.classList.remove('open');
    hamburger?.classList.remove('open');
    hamburger?.setAttribute('aria-expanded','false');
    hamburger?.focus();
  }
});
```

---

### FX-14 — SEO, metadados e favicon

**Fix HTML — no `<head>`:**
```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="CRM, ERP, e-shop e sites institucionais feitos para o seu jeito de trabalhar. A Code House constrói sistemas personalizados para pequenas empresas — sem templates, sem engessamento.">
<meta name="theme-color" content="#2D74A0">
<meta property="og:title" content="Code House — Soluções Personalizadas em TI">
<meta property="og:description" content="Sistemas feitos para o seu modo de operar.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://codehouse-PLACEHOLDER.onrender.com">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://codehouse-PLACEHOLDER.onrender.com">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='4' fill='%232D74A0'/><text x='16' y='21' text-anchor='middle' font-family='monospace' font-size='13' font-weight='700' fill='white'>CH</text></svg>" type="image/svg+xml">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization","name":"Code House","url":"https://codehouse-PLACEHOLDER.onrender.com","description":"Soluções personalizadas em TI para pequenas empresas"}</script>
```

---

### FX-15 — Skip link e acessibilidade global

**Fix HTML — primeira linha do body:**
```html
<a href="#main-content" class="skip-link">Ir para o conteúdo principal</a>
```

**Fix — adicionar `id="main-content"` na seção hero:**
```html
<section class="hero" id="main-content">
```

**Fix CSS:**
```css
.skip-link {
  position: absolute; top: -100px; left: 0; z-index: 10000;
  background: var(--cloud); color: var(--bg); padding: .5rem 1rem;
  font-family: var(--f-mono); font-size: .7rem; text-decoration: none;
  transition: top .15s;
}
.skip-link:focus { top: 0; }
```

**Fix global — todos os elementos interativos:**
```css
:focus-visible { outline: 2px solid var(--cloud); outline-offset: 3px; }
```

**Fix CSS BUG-29 — linha 240 tem `"` espúrio no CSS:**
```css
/* ANTES (bug): */
.wf-quote{...;line-height:1}"   /* <-- " extra quebra o CSS */
/* DEPOIS: */
.wf-quote{...;line-height:1}
```

---

### FX-16 — Lenis smooth scroll

**Fix JS:**
```js
window.addEventListener('load', () => {
  if (typeof Lenis === 'undefined') return;
  const lenis = new Lenis({
    duration: 1.1,
    easing: t => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
    smoothWheel: !matchMedia('(pointer:coarse)').matches
  });
  
  if (typeof ScrollTrigger !== 'undefined') {
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add(time => lenis.raf(time * 1000));
    gsap.ticker.lagSmoothing(0);
  } else {
    function raf(time) { lenis.raf(time); requestAnimationFrame(raf); }
    requestAnimationFrame(raf);
  }
  
  // Âncoras com offset nav
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const id = a.getAttribute('href');
      const target = document.querySelector(id);
      if (!target) return;
      e.preventDefault();
      lenis.scrollTo(target, { offset: -60 });
    });
  });
  
  window.lenis = lenis; // expor globalmente
});
```

---

### FX-17 — WPP float: pulse ring + aparece após scroll

**Diagnóstico (linha 273):** Float aparece imediatamente na página, sem pulse ring.

**Fix CSS:**
```css
.wpp-float {
  /* manter propriedades existentes */
  opacity: 0;
  pointer-events: none;
  transition: opacity .3s ease, transform .2s ease, box-shadow .2s ease;
}
.wpp-float.visible { opacity: 1; pointer-events: auto; }
.wpp-float::after {
  content: '';
  position: absolute; inset: 0;
  border: 2px solid var(--wpp);
  border-radius: 50%;
  animation: wppPulse 2.2s ease-out infinite;
}
@keyframes wppPulse {
  0% { transform: scale(1); opacity: .7; }
  100% { transform: scale(1.8); opacity: 0; }
}
```

**Fix JS:**
```js
const wppBtn = document.querySelector('.wpp-float');
let wppShown = false;
window.addEventListener('scroll', () => {
  if (!wppBtn || wppShown) return;
  if (window.scrollY > 400) { wppBtn.classList.add('visible'); wppShown = true; }
}, { passive: true });
```

---

### FX-18 — GSAP ScrollTrigger: reveals globais substituindo IntersectionObserver básico

**Fix — substituir o observer manual (linhas 804–808):**
```js
if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
  gsap.registerPlugin(ScrollTrigger);
  
  // Eyebrows
  document.querySelectorAll('.sec-tag, .eyebrow').forEach(el => {
    gsap.fromTo(el, { opacity:0, x:-16 }, { opacity:1, x:0, duration:.45, ease:'power2.out',
      scrollTrigger: { trigger: el, start: 'top 88%', once: true } });
  });
  
  // Headings
  document.querySelectorAll('h2').forEach(el => {
    gsap.fromTo(el, { opacity:0, y:16 }, { opacity:1, y:0, duration:.5, delay:.08, ease:'power2.out',
      scrollTrigger: { trigger: el, start: 'top 85%', once: true } });
  });
  
  // Cards em grid com stagger
  document.querySelectorAll('.p-step, .stat-item').forEach((el, i) => {
    gsap.fromTo(el, { opacity:0, y:20 }, { opacity:1, y:0, duration:.45, delay: i * 0.1, ease:'power2.out',
      scrollTrigger: { trigger: el.parentElement, start: 'top 80%', once: true } });
  });
  
  // Remover classes .fade .fade2 .fade3 do HTML (substituídas pelo GSAP)
  // Manter as classes no CSS mas sem o opacity:0 inicial (GSAP controla agora)
}
```

---

### FX-19 — CSS syntax error: linha 240

**Diagnóstico:** Linha 240 tem `}` seguido de `"` que é um syntax error silencioso no CSS.

**Fix (linha 240):**
```css
/* REMOVER o " no final desta linha: */
.wf-quote{font-size:.5rem;color:var(--cloud);font-weight:700;flex-shrink:0;line-height:1}
/* sem " extra */
```

---

### FX-20 — `render.yaml`, `_headers` e política de privacidade

**Criar `render.yaml`:**
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
    routes:
      - type: rewrite
        source: /404
        destination: /404.html
    notFoundPage: 404.html
```

**Criar `_headers`:**
```
/*
  Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com https://fonts.googleapis.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdnjs.cloudflare.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data:; connect-src 'none'; frame-src 'none'; object-src 'none'
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
```

**Criar `politica-privacidade.html`:** ver spec H-79 no build-prompt-master.md.

---

## Ordem de execução dos fixes

```
FX-19  Bug CSS crítico (syntax error linha 240)
FX-01  Fontes (Syne, Inter, Space Mono)
FX-02  Libraries JS (GSAP, Anime.js, Three.js, Lenis)
FX-14  SEO + favicon + metadados
FX-15  Skip link + :focus-visible
FX-10  Preloader
FX-03  Hero: Three.js + GSAP headline + toasts
FX-04  Stats: ícones + Anime.js countup
FX-12  Marquee ticker
FX-08  Serviços: lista interativa + painel de detalhe
FX-09  Processo: ScrollTrigger scrub + connector
FX-05  Exemplos: demolir grid, construir tab system
FX-06a   └─ Aba CRM
FX-06b   └─ Aba ERP  
FX-06c   └─ Aba E-shop
FX-06d   └─ Aba Site
FX-07  Formulário: campo email + validação inline
FX-11  LGPD banner
FX-13  Nav: progress bar + active + hamburger
FX-16  Lenis smooth scroll
FX-17  WPP float: pulse + aparece após scroll
FX-18  GSAP ScrollTrigger reveals globais
FX-20  render.yaml + _headers + politica-privacidade.html
```

---

## Critérios de aprovação após todos os fixes

- [ ] Exemplos: 4 abas funcionam com teclado (setas, Enter, Escape)
- [ ] E-shop: filtros por categoria funcionam, botão adicionar ao carrinho funciona
- [ ] CRM: barras do pipeline animam ao ativar a aba
- [ ] ERP: chart SVG anima ao ativar a aba
- [ ] Formulário: submit com campos vazios é bloqueado com mensagem por campo
- [ ] Formulário: campo email valida formato
- [ ] Preloader: aparece e desaparece — página nunca fica bloqueada
- [ ] Three.js: canvas renderiza no hero desktop
- [ ] Tipografia: Syne visível nos títulos (font diferente de system-ui)
- [ ] LGPD banner: aparece e fecha, localStorage persiste decisão
- [ ] Hamburger: abre e fecha em mobile, Escape funciona
- [ ] WPP float: aparece após scroll > 400px, tem pulse ring
- [ ] Nav progress bar: mostra % de scroll
- [ ] CSS: nenhum syntax error no DevTools
- [ ] Console: zero erros (warnings de CORS aceitáveis apenas se CDN bloqueado)
- [ ] Dark mode: todos os elementos legíveis
- [ ] `prefers-reduced-motion`: animações paradas
- [ ] Mobile 375px: sem overflow horizontal
