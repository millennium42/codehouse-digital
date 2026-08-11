import os

HTML_CONTENT = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
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
  
  <title>Code House — Soluções Personalizadas em TI</title>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Inter:wght@400;500&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
  
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/splitting/1.0.6/splitting.min.css">
  
  <style>
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

      /* Tipografia FX-01 */
      --f-display: 'Syne', sans-serif;
      --f-body: 'Inter', system-ui, sans-serif;
      --f-mono: 'Space Mono', 'Courier New', monospace;

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

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body, p, input, textarea {
      font-family: var(--f-body);
      background-color: var(--bg);
      color: var(--ink-m);
      line-height: 1.6;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
    }
    h1, h2, h3, h4, h5, h6 {
      font-family: var(--f-display);
      color: var(--ink);
      text-wrap: balance;
    }
    .eyebrow, .sec-tag, nav a, .btn, .tg, .pill, .sk-l, .fl { font-family: var(--f-mono); }
    h1 { letter-spacing: -.03em; }
    nav a { letter-spacing: .12em; }
    
    a { text-decoration: none; color: inherit; }
    ul { list-style: none; }
    button { font-family: inherit; cursor: pointer; border: none; background: none; }
    
    :focus-visible { outline: 2px solid var(--cloud); outline-offset: 3px; }
    .skip-link {
      position: absolute; top: -100px; left: 0; z-index: 10000;
      background: var(--cloud); color: var(--bg); padding: .5rem 1rem;
      font-family: var(--f-mono); font-size: .7rem; text-decoration: none;
      transition: top .15s;
    }
    .skip-link:focus { top: 0; }

    .container { max-width: var(--max-w); margin: 0 auto; padding: 0 var(--pad-x); }
    .btn-solid, .btn {
      display: inline-flex; align-items: center; justify-content: center;
      background: var(--cloud); color: var(--bg);
      font-family: var(--f-mono); font-size: var(--t-label);
      text-transform: uppercase; letter-spacing: .12em;
      padding: 0.8rem 1.6rem; border-radius: var(--r);
      transition: var(--trans); font-weight: 700;
    }
    .btn-solid:hover, .btn:hover { background: var(--cloud-h); transform: translateY(-2px); box-shadow: var(--sh-md); }
    .btn-outline {
      display: inline-flex; align-items: center; justify-content: center;
      background: transparent; color: var(--ink);
      border: 1px solid var(--border-s);
      font-family: var(--f-mono); font-size: var(--t-label);
      text-transform: uppercase; letter-spacing: .12em;
      padding: 0.8rem 1.6rem; border-radius: var(--r);
      transition: var(--trans); font-weight: 700;
    }
    .btn-outline:hover { background: var(--cloud-f); transform: translateY(-2px); }

    /* Nav */
    nav { position: sticky; top: 0; z-index: 100; background-color: rgba(241,244,248,0.95); backdrop-filter: blur(12px); border-bottom: 1px solid var(--border); }
    .nav-progress { position: absolute; bottom: -1px; left: 0; height: 2px; background: linear-gradient(90deg, var(--cloud-f), var(--cloud)); width: 0; transition: none; pointer-events: none; }
    .navbar-container { display: flex; align-items: center; justify-content: space-between; height: 72px; }
    .logo { font-family: var(--f-mono); font-size: 1.1rem; font-weight: 700; color: var(--ink); }
    .nav-links { display: flex; align-items: center; gap: 2rem; }
    .nav-link { font-family: var(--f-mono); font-size: var(--t-label); text-transform: uppercase; letter-spacing: .12em; color: var(--ink-m); position: relative; padding: 0.5rem 0; }
    .nav-link::after { content: ''; position: absolute; bottom: 0; left: 0; width: 0; height: 2px; background-color: var(--cloud); transition: width 200ms ease; }
    .nav-link.active::after, .nav-link:hover::after { width: 100%; }
    .nav-link:hover { color: var(--ink); }
    .hamburger { display: none; background: none; border: 1px solid var(--border); border-radius: var(--r); width: 36px; height: 36px; cursor: pointer; flex-direction: column; align-items: center; justify-content: center; gap: 4px; transition: border-color var(--trans); }
    .hamburger span { display: block; width: 16px; height: 1.5px; background: var(--ink); transition: transform .2s ease, opacity .2s ease; }
    .hamburger.open span:first-child { transform: translateY(5.5px) rotate(45deg); }
    .hamburger.open span:nth-child(2) { opacity: 0; }
    .hamburger.open span:last-child { transform: translateY(-5.5px) rotate(-45deg); }
    @media (max-width: 900px) { .nav-links { display: none; } .hamburger { display: flex; } }
    .nav-drawer { position: fixed; top: 72px; left: 0; right: 0; background: rgba(241,244,248,.97); backdrop-filter: blur(12px); border-bottom: 1px solid var(--border); z-index: 99; padding: 1rem var(--pad-x); display: none; flex-direction: column; gap: 0; }
    .nav-drawer.open { display: flex; }
    .nav-drawer a { padding: .85rem 0; font-family: var(--f-mono); font-size: .68rem; letter-spacing: .1em; text-transform: uppercase; color: var(--ink-m); text-decoration: none; border-bottom: 1px solid var(--border); }
    .nav-drawer a:last-child { border-bottom: none; }

    /* Preloader */
    #preloader { position: fixed; inset: 0; z-index: 9999; background: var(--bg); display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 1.5rem; transition: opacity .4s ease, transform .4s ease; }
    #preloader.hidden { opacity: 0; transform: scale(1.04); pointer-events: none; }
    .pre-logo { font-family: var(--f-mono); font-size: 1.1rem; font-weight: 700; letter-spacing: .08em; color: var(--ink); }
    .pre-logo .char { display: inline-block; opacity: 0; transform: translateY(6px); }
    .pre-bar { width: 120px; height: 2px; background: var(--border); border-radius: 1px; overflow: hidden; }
    .pre-fill { height: 100%; width: 0; background: var(--cloud); border-radius: 1px; transition: width .8s ease; }

    /* Hero FX-03 */
    .hero { min-height: 100svh; overflow: hidden; display: grid; grid-template-columns: 1.1fr 0.9fr; align-items: center; position: relative; }
    .hero-content { padding: 0 var(--pad-x); position: relative; z-index: 10; }
    .hero-canvas-col { position: relative; width: 100%; height: 100%; overflow: hidden; }
    #heroCanvas { width: 100%; height: 100%; }
    .hero-stats { margin-top: 1rem; font-family: var(--f-mono); font-size: 0.6rem; color: var(--ink-f); }
    
    .mockup-crm { position: absolute; right: 2rem; bottom: 2rem; width: 340px; background: var(--surface-up); box-shadow: var(--sh-lg); border: 1px solid var(--border); border-radius: var(--r); overflow: hidden; z-index: 20; }
    .mockup-header { background: var(--surface); border-bottom: 1px solid var(--border); padding: 0.5rem 0.75rem; display: flex; align-items: center; gap: 0.5rem; }
    .mockup-dots { display: flex; gap: 4px; }
    .mockup-dot { width: 8px; height: 8px; border-radius: 50%; }
    .mockup-dot.r { background: #FF5F56; } .mockup-dot.y { background: #FFBD2E; } .mockup-dot.g { background: #27C93F; }
    .mockup-body { display: grid; grid-template-columns: 80px 1fr; height: 280px; }
    .mockup-sidebar { border-right: 1px solid var(--border); padding: 0.5rem 0; background: var(--surface); font-size: 0.5rem; }
    .mockup-content { padding: 0.75rem; background: var(--bg); position: relative; }
    
    .app-toast { position:absolute; bottom:4px; left:4px; right:4px; background:var(--ok-bg); border:1px solid var(--ok); border-radius:2px; padding:.4rem .6rem; font-family:var(--f-mono); font-size:.5rem; color:var(--ok); transform:translateY(8px); opacity:0; transition:transform .25s ease, opacity .25s ease; }
    .app-toast.visible { transform:translateY(0); opacity:1; }

    /* Stats FX-04 */
    .stats-strip { display: grid; grid-template-columns: repeat(4, 1fr); padding: 3rem var(--pad-x); background: var(--surface); }
    .stat-item { display: flex; flex-direction: column; align-items: center; }
    .stat-icon { color: var(--cloud); margin-bottom: 0.75rem; display: flex; justify-content: center; }
    .stat-num { font-family: var(--f-display); font-size: 3rem; font-weight: 800; color: var(--cloud); }
    .stat-label { font-family: var(--f-mono); font-size: 0.6rem; text-transform: uppercase; color: var(--ink-f); }

    /* Marquee FX-12 */
    .marquee-strip { background: var(--surface); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); padding: .9rem 0; overflow: hidden; }
    .marquee-track { display: flex; gap: 0; width: max-content; animation: marquee 28s linear infinite; }
    .marquee-track:hover { animation-play-state: paused; }
    .mq-item { font-family: var(--f-mono); font-size: .58rem; letter-spacing: .12em; text-transform: uppercase; color: var(--ink-f); padding: 0 .6rem; white-space: nowrap; }
    .mq-sep { color: var(--border-s); font-size: .7rem; }
    @keyframes marquee { 0% { transform: translateX(0) } 100% { transform: translateX(-50%) } }
    @media (prefers-reduced-motion: reduce) { .marquee-track { animation-play-state: paused; } }

    /* Services FX-08 */
    .sec { padding: var(--pad-sec) var(--pad-x); max-width: var(--max-w); margin: 0 auto; }
    .sec-tag { font-family: var(--f-mono); color: var(--cloud); font-size: var(--t-label); text-transform: uppercase; margin-bottom: 1rem; display: block; }
    .sec-hdr h2 { font-size: var(--t-h2); margin-bottom: 3rem; }
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

    /* Process FX-09 */
    .process-wrap { position: relative; margin-top: 3rem; }
    .proc-connector { position: absolute; top: 18px; left: 0; width: 100%; height: 4px; z-index: 0; }
    .p-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; position: relative; z-index: 1; }
    .p-step { background: var(--bg); padding-top: 1rem; }
    .p-step h3 { font-size: 1.2rem; margin-bottom: .5rem; }
    .p-step p { font-size: .9rem; }

    /* Examples FX-05 */
    .tabs-bar { display: flex; gap: 0; border-bottom: 2px solid var(--border); margin-bottom: 0; overflow-x: auto; -webkit-overflow-scrolling: touch; }
    .tab-btn { display: inline-flex; align-items: center; gap: .4rem; padding: .9rem 1.5rem; font-family: var(--f-mono); font-size: .62rem; letter-spacing: .1em; text-transform: uppercase; color: var(--ink-m); background: transparent; border: none; border-bottom: 2px solid transparent; margin-bottom: -2px; cursor: pointer; transition: color var(--trans), background var(--trans); white-space: nowrap; }
    .tab-btn:hover { color: var(--ink); background: var(--surface); }
    .tab-btn.active { color: var(--cloud); border-bottom-color: var(--cloud); background: var(--cloud-f); }
    .tab-btn:focus-visible { outline: 2px solid var(--cloud); outline-offset: -2px; }
    .tab-panels { border: 1px solid var(--border); border-top: none; border-radius: 0 0 var(--r) var(--r); min-height: 520px; overflow: hidden; background: var(--bg); }
    .tab-panel { padding: 1.5rem; display: none; height: 100%; }
    .tab-panel:not([hidden]) { display: block; }
    
    /* FX-06a CRM */
    .crm-layout { display: grid; grid-template-columns: 340px 1fr; gap: 1.5rem; height: 100%; }
    .crm-kpis { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1.5rem; }
    .pipe-fill { height: 100%; background: var(--cloud); width: 0; border-radius: 4px; }
    .mt { width: 100%; border-collapse: collapse; font-size: .8rem; }
    .mt th, .mt td { padding: .8rem; text-align: left; border-bottom: 1px solid var(--border); }
    .mt th { font-family: var(--f-mono); font-size: .6rem; text-transform: uppercase; color: var(--ink-f); }
    .tg { padding: .2rem .4rem; border-radius: var(--r); font-size: .6rem; }
    .tg-ok { background: var(--ok-bg); color: var(--ok); }
    .tg-pnd { background: var(--warn-bg); color: var(--warn); }
    .tg-w { background: var(--cloud-f); color: var(--cloud); }
    .live-row td { animation: liveRow 3s ease infinite; }
    @keyframes liveRow { 0%,100%{background:transparent} 50%{background:var(--ok-bg)} }
    
    /* FX-06b ERP */
    .erp-layout { display: flex; flex-direction: column; gap: 1rem; height: 100%; }
    
    /* FX-06c Eshop */
    .shop-layout { display: grid; grid-template-columns: 1fr 280px; gap: 1.5rem; height: 100%; }
    .sh-tab { font-family: var(--f-mono); font-size: .6rem; padding: .3rem .8rem; cursor: pointer; border: 1px solid var(--border); border-radius: 20px; background: transparent; }
    .sh-tab.on { background: var(--cloud); color: var(--bg); }
    .prod-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 1rem; }
    .prod-card { border: 1px solid var(--border); padding: 1rem; border-radius: var(--r); text-align: center; }
    .prod-add-btn { margin-top: 1rem; width: 100%; background: var(--cloud); color: var(--bg); border: none; padding: .4rem; cursor: pointer; font-size: .7rem; border-radius: var(--r); }
    .shop-cart-panel { border: 1px solid var(--border); border-radius: var(--r); display: flex; flex-direction: column; }
    .cart-header { padding: 1rem; border-bottom: 1px solid var(--border); display: flex; justify-content: space-between; font-weight: bold; }
    .cart-badge { background: var(--cloud); color: white; padding: .1rem .4rem; border-radius: 10px; font-size: .6rem; }
    .cart-items { flex: 1; padding: 1rem; overflow-y: auto; }
    .cart-item-row { display: flex; justify-content: space-between; margin-bottom: .5rem; font-size: .8rem; }
    .cart-footer { padding: 1rem; border-top: 1px solid var(--border); }
    
    /* FX-06d Site */
    .site-wireframe { display: grid; grid-template-columns: 1fr 250px; gap: 1.5rem; height: 100%; }
    .wf-nav { display: flex; gap: 1rem; }
    .wf-link { cursor: pointer; color: var(--ink-m); }
    .wf-link:hover { text-decoration: underline; color: var(--ink); }
    .wf-btn { cursor: pointer; transition: var(--trans); }
    .wf-btn:hover { opacity: .85; }
    .wf-card { cursor: pointer; transition: var(--trans); padding: 1rem; border: 1px solid var(--border); border-radius: var(--r); }
    .wf-card:hover { transform: translateY(-3px); box-shadow: var(--sh-sm); }
    .wf-quote { font-size: .5rem; color: var(--cloud); font-weight: 700; flex-shrink: 0; line-height: 1; }

    /* FX-07 Form */
    .contact-wrap { display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; }
    .field { margin-bottom: 1.5rem; }
    .fl { display: block; font-size: .7rem; margin-bottom: .4rem; }
    .fi { width: 100%; padding: .8rem; border: 1px solid var(--border); border-radius: var(--r); background: var(--surface); color: var(--ink); }
    .field-error { display: none; color: var(--red); font-size: .72rem; margin-top: .25rem; }
    .fi.has-error { border-color: var(--red); }
    @keyframes spin { to { transform: rotate(360deg); } }
    .spinner { animation: spin .8s linear infinite; display: inline-block; vertical-align: middle; }
    #formSuccess { display: none; background: var(--ok-bg); border: 1px solid var(--ok); padding: 2rem; border-radius: var(--r); text-align: center; color: var(--ok); }
    #formSuccess.visible { display: block; }

    /* FX-11 LGPD */
    .lgpd-banner { position: fixed; bottom: 0; left: 0; right: 0; z-index: 150; background: var(--surface); border-top: 1px solid var(--border); padding: .85rem var(--pad-x); display: flex; align-items: center; justify-content: space-between; gap: 1rem; flex-wrap: wrap; }
    .lgpd-banner[hidden] { display: none; }
    .lgpd-text { font-size: .82rem; color: var(--ink-m); flex: 1; }
    .lgpd-link { color: var(--cloud); }
    .lgpd-btn { font-family: var(--f-mono); font-size: .6rem; letter-spacing: .1em; text-transform: uppercase; background: var(--cloud); color: var(--bg); border: none; padding: .5rem 1rem; border-radius: var(--r); cursor: pointer; flex-shrink: 0; }
    .lgpd-btn:hover { background: var(--cloud-h); }

    /* FX-17 Wpp Float */
    .wpp-float { position: fixed; bottom: 2rem; right: 2rem; z-index: 200; width: 56px; height: 56px; background: var(--wpp); border-radius: 50%; display: flex; align-items: center; justify-content: center; opacity: 0; pointer-events: none; transition: opacity .3s ease, transform .2s ease, box-shadow .2s ease; }
    .wpp-float.visible { opacity: 1; pointer-events: auto; }
    .wpp-float:hover { transform: scale(1.08); box-shadow: 0 6px 24px rgba(37,211,102,.5); }
    .wpp-float::after { content: ''; position: absolute; inset: 0; border: 2px solid var(--wpp); border-radius: 50%; animation: wppPulse 2.2s ease-out infinite; }
    @keyframes wppPulse { 0% { transform: scale(1); opacity: .7; } 100% { transform: scale(1.8); opacity: 0; } }

    footer { padding: 4rem var(--pad-x); background: var(--surface); border-top: 1px solid var(--border); font-size: .8rem; }
    
    @media (max-width: 900px) {
      .hero { grid-template-columns: 1fr; }
      .mockup-crm { display: none; }
      .svc-layout { grid-template-columns: 1fr; }
      .svc-list { border-right: none; border-bottom: 1px solid var(--border); }
      .p-grid { grid-template-columns: 1fr; }
      .crm-layout, .shop-layout, .site-wireframe { grid-template-columns: 1fr; }
      .contact-wrap { grid-template-columns: 1fr; }
      .stats-strip { grid-template-columns: 1fr 1fr; gap: 1rem; }
    }
  </style>
</head>
<body>
  <a href="#main-content" class="skip-link">Ir para o conteúdo principal</a>

  <div id="preloader" aria-hidden="true">
    <span class="pre-logo" data-splitting>CODE.HOUSE</span>
    <div class="pre-bar"><div class="pre-fill"></div></div>
  </div>

  <nav aria-label="Menu principal">
    <div class="nav-progress" id="navProgress"></div>
    <div class="container navbar-container">
      <a href="#" class="logo">CODE.HOUSE</a>
      <div class="nav-links">
        <a href="#servicos" class="nav-link">Serviços</a>
        <a href="#processo" class="nav-link">Processo</a>
        <a href="#exemplos" class="nav-link">Exemplos</a>
        <a href="#contato" class="btn">Falar com a gente</a>
      </div>
      <button class="hamburger" id="hamburger" aria-label="Abrir menu" aria-expanded="false" aria-controls="navDrawer">
        <span></span><span></span><span></span>
      </button>
    </div>
  </nav>

  <div id="navDrawer" class="nav-drawer" role="navigation" aria-label="Menu mobile">
    <a href="#servicos" class="drawer-link">Serviços</a>
    <a href="#processo" class="drawer-link">Processo</a>
    <a href="#exemplos" class="drawer-link">Exemplos</a>
    <a href="#contato" class="drawer-link">Falar com a gente</a>
  </div>

  <section class="hero" id="main-content">
    <div class="hero-content">
      <span class="eyebrow">// soluções personalizadas em TI</span>
      <h1 data-splitting>Sistemas feitos para o seu modo de operar.</h1>
      <p style="margin-bottom: 2rem;">A Code House entende como sua empresa funciona de verdade — e constrói o sistema que acompanha esse ritmo, sem templates e sem engessamento.</p>
      <div style="display: flex; gap: 1rem;">
        <a href="#contato" class="btn-solid">Falar com a gente</a>
        <a href="#exemplos" class="btn-outline">Ver exemplos</a>
      </div>
      <p class="hero-stats">38+ projetos · 22 clientes · 5 anos</p>
    </div>
    <div class="hero-canvas-col">
      <canvas id="heroCanvas"></canvas>
      <div class="mockup-crm">
        <div class="mockup-header">
          <div class="mockup-dots"><div class="mockup-dot r"></div><div class="mockup-dot y"></div><div class="mockup-dot g"></div></div>
          <span style="font-family: var(--f-mono); font-size: .5rem; margin-left: 10px;">CRM</span>
        </div>
        <div class="mockup-body">
          <div class="mockup-sidebar" style="padding: 10px;">
            <div style="color: var(--cloud)">Dashboard</div>
            <div style="margin-top:5px">Clientes</div>
          </div>
          <div class="mockup-content">
            <div style="width: 100%; height: 20px; background: var(--surface); border-radius: 4px;"></div>
            <div style="width: 80%; height: 20px; background: var(--surface); border-radius: 4px;"></div>
            <div id="toastContainer"></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="stats-strip">
    <div class="stat-item">
      <div class="stat-icon" aria-hidden="true">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
      </div>
      <span class="stat-num" data-target="38" data-suffix="+">0</span>
      <span class="stat-label">Projetos entregues</span>
    </div>
    <div class="stat-item">
      <div class="stat-icon" aria-hidden="true">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="9" cy="7" r="4"/><path d="M3 21v-2a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v2"/><path d="M19 11c1.657 0 3 1.343 3 3v3"/></svg>
      </div>
      <span class="stat-num" data-target="22" data-suffix="+">0</span>
      <span class="stat-label">Clientes</span>
    </div>
    <div class="stat-item">
      <div class="stat-icon" aria-hidden="true">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
      </div>
      <span class="stat-num" data-target="5" data-suffix="+">0</span>
      <span class="stat-label">Anos</span>
    </div>
    <div class="stat-item">
      <div class="stat-icon" aria-hidden="true">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/></svg>
      </div>
      <span class="stat-num" data-target="100" data-suffix="%">0</span>
      <span class="stat-label">Suporte</span>
    </div>
  </section>

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
    </div>
  </div>

  <section class="sec" id="servicos">
    <div class="sec-hdr">
      <span class="sec-tag">// serviços</span>
      <h2>O que a Code House entrega</h2>
    </div>
    <div class="svc-layout">
      <ul class="svc-list" role="tablist" aria-label="Serviços">
        <li role="tab" class="svc-item active" aria-selected="true" aria-controls="svc-detail" id="svc-crm" tabindex="0" data-svc="crm">
          <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" class="svc-icon"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg>
          <div><p class="svc-name">CRM</p><p class="svc-sub">funil · histórico · automação</p></div>
        </li>
        <li role="tab" class="svc-item" aria-selected="false" aria-controls="svc-detail" id="svc-erp" tabindex="-1" data-svc="erp">
          <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" class="svc-icon"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
          <div><p class="svc-name">ERP</p><p class="svc-sub">operações · estoque · finanças</p></div>
        </li>
        <li role="tab" class="svc-item" aria-selected="false" aria-controls="svc-detail" id="svc-eshop" tabindex="-1" data-svc="eshop">
          <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" class="svc-icon"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
          <div><p class="svc-name">E-shop</p><p class="svc-sub">loja virtual · pagamentos</p></div>
        </li>
        <li role="tab" class="svc-item" aria-selected="false" aria-controls="svc-detail" id="svc-site" tabindex="-1" data-svc="site">
          <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" class="svc-icon"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/></svg>
          <div><p class="svc-name">Site Institucional</p><p class="svc-sub">presença digital · SEO</p></div>
        </li>
        <li role="tab" class="svc-item" aria-selected="false" aria-controls="svc-detail" id="svc-sobmedida" tabindex="-1" data-svc="sobmedida">
          <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" class="svc-icon"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
          <div><p class="svc-name">Sob Medida</p><p class="svc-sub">qualquer sistema específico</p></div>
        </li>
      </ul>
      <div class="svc-detail" id="svc-detail" role="tabpanel" aria-labelledby="svc-crm">
        <p class="svc-detail-eye">// CRM</p>
        <h3>Gestão de clientes que acompanha seu funil de vendas</h3>
        <p>Não é um CRM genérico de prateleira — é construído em cima de como você já trabalha. Funil de vendas configurado do seu jeito, campos que fazem sentido para o negócio, histórico de cada cliente ao alcance.</p>
        <ul class="svc-features">
          <li><svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> <span>Pipeline personalizado</span></li>
          <li><svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> <span>Histórico de interações</span></li>
          <li><svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> <span>Alertas e lembretes</span></li>
          <li><svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> <span>Relatórios do que importa</span></li>
          <li><svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> <span>Integração com WhatsApp (opcional)</span></li>
        </ul>
        <a class="svc-cta" href="#exemplos" data-tab="tab-crm">→ Ver exemplo deste sistema</a>
      </div>
    </div>
  </section>

  <section class="sec" id="processo">
    <div class="sec-hdr">
      <span class="sec-tag">// como trabalhamos</span>
      <h2>Desenvolvimento sem burocracia.</h2>
    </div>
    <div class="process-wrap">
      <svg class="proc-connector" aria-hidden="true" viewBox="0 0 840 4" preserveAspectRatio="none">
        <line x1="140" y1="2" x2="700" y2="2" stroke="var(--cloud)" stroke-width="2" stroke-dasharray="8 4" style="stroke-dashoffset:560; transition:stroke-dashoffset 1s ease"/>
      </svg>
      <div class="p-grid">
        <div class="p-step">
          <div style="font-family: var(--f-mono); color: var(--cloud); font-size: 2rem; font-weight: 800; margin-bottom: 1rem;">01</div>
          <h3>Diagnóstico</h3>
          <p>Reunião para mapear como o negócio funciona. Saímos com um documento de requisitos validado pelo cliente.</p>
        </div>
        <div class="p-step">
          <div style="font-family: var(--f-mono); color: var(--cloud); font-size: 2rem; font-weight: 800; margin-bottom: 1rem;">02</div>
          <h3>Construção</h3>
          <p>Desenvolvimento em sprints com entregas visíveis. O cliente valida cada etapa antes de avançar.</p>
        </div>
        <div class="p-step">
          <div style="font-family: var(--f-mono); color: var(--cloud); font-size: 2rem; font-weight: 800; margin-bottom: 1rem;">03</div>
          <h3>Entrega e Suporte</h3>
          <p>Deploy em produção, treinamento da equipe e suporte contínuo. O sistema cresce junto com o negócio.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="sec" id="exemplos">
    <div class="sec-hdr">
      <span class="sec-tag">// exemplos de sistemas</span>
      <h2>O que sistemas feitos assim parecem</h2>
    </div>
    
    <div class="tabs-bar" role="tablist" aria-label="Exemplos de sistemas">
      <button class="tab-btn active" role="tab" id="tab-crm" aria-controls="panel-crm" aria-selected="true" tabindex="0">CRM</button>
      <button class="tab-btn" role="tab" id="tab-erp" aria-controls="panel-erp" aria-selected="false" tabindex="-1">ERP</button>
      <button class="tab-btn" role="tab" id="tab-eshop" aria-controls="panel-eshop" aria-selected="false" tabindex="-1">E-shop</button>
      <button class="tab-btn" role="tab" id="tab-site" aria-controls="panel-site" aria-selected="false" tabindex="-1">Site Institucional</button>
    </div>

    <div class="tab-panels">
      <div class="tab-panel" id="panel-crm" role="tabpanel" aria-labelledby="tab-crm">
        <div class="crm-layout">
          <div>
            <div class="crm-kpis">
              <div style="background:var(--surface); padding: 1rem; border-radius: var(--r);">
                <div style="font-size: .6rem; text-transform: uppercase;">Negócios</div>
                <div style="font-size: 1.5rem; font-weight: bold; color: var(--cloud);">19</div>
              </div>
              <div style="background:var(--surface); padding: 1rem; border-radius: var(--r);">
                <div style="font-size: .6rem; text-transform: uppercase;">Fechados</div>
                <div style="font-size: 1.5rem; font-weight: bold; color: var(--ok);">R$28k</div>
              </div>
            </div>
            <div style="display:flex; flex-direction: column; gap: 1rem;">
              <div>
                <div style="display:flex; justify-content:space-between; font-size:.7rem; margin-bottom:.3rem"><span>Prospecção</span> <span>100%</span></div>
                <div style="height: 12px; background: var(--surface); border-radius: 4px;"><div class="pipe-fill" data-fill="100"></div></div>
              </div>
              <div>
                <div style="display:flex; justify-content:space-between; font-size:.7rem; margin-bottom:.3rem"><span>Contato Feito</span> <span>66%</span></div>
                <div style="height: 12px; background: var(--surface); border-radius: 4px;"><div class="pipe-fill" data-fill="66"></div></div>
              </div>
              <div>
                <div style="display:flex; justify-content:space-between; font-size:.7rem; margin-bottom:.3rem"><span>Proposta</span> <span>48%</span></div>
                <div style="height: 12px; background: var(--surface); border-radius: 4px;"><div class="pipe-fill" data-fill="48"></div></div>
              </div>
              <div>
                <div style="display:flex; justify-content:space-between; font-size:.7rem; margin-bottom:.3rem"><span>Fechado</span> <span>26%</span></div>
                <div style="height: 12px; background: var(--surface); border-radius: 4px;"><div class="pipe-fill" data-fill="26"></div></div>
              </div>
            </div>
          </div>
          <div>
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
          </div>
        </div>
      </div>
      
      <div class="tab-panel" id="panel-erp" role="tabpanel" aria-labelledby="tab-erp" hidden>
        <div class="erp-layout">
          <div style="height: 200px; position: relative;">
            <svg width="100%" height="100%" viewBox="0 0 600 200" preserveAspectRatio="none">
              <path class="chart-area chart-area-svg" d="M0,200 L0,150 L100,100 L200,120 L300,50 L400,80 L500,20 L600,60 L600,200 Z" fill="var(--cloud-f)" style="opacity:0"/>
              <polyline class="chart-line" points="0,150 100,100 200,120 300,50 400,80 500,20 600,60" fill="none" stroke="var(--cloud)" stroke-width="3" data-dash="1000" style="stroke-dasharray:1000; stroke-dashoffset:1000" />
            </svg>
          </div>
          <table class="mt">
            <thead><tr><th>Pedido</th><th>Data</th><th>Valor</th><th>Status</th></tr></thead>
            <tbody>
              <tr><td>#1001</td><td>01/08/2026</td><td>R$ 1.200</td><td><span class="tg tg-ok">Enviado</span></td></tr>
              <tr><td>#1002</td><td>02/08/2026</td><td>R$ 4.500</td><td><span class="tg tg-pnd">Processando</span></td></tr>
              <tr><td>#1003</td><td>03/08/2026</td><td>R$ 300</td><td><span class="tg tg-ok">Enviado</span></td></tr>
              <tr><td>#1004</td><td>04/08/2026</td><td>R$ 8.900</td><td><span class="tg tg-w">Pendente</span></td></tr>
              <tr><td>#1005</td><td>05/08/2026</td><td>R$ 2.100</td><td><span class="tg tg-ok">Enviado</span></td></tr>
            </tbody>
          </table>
        </div>
      </div>
      
      <div class="tab-panel" id="panel-eshop" role="tabpanel" aria-labelledby="tab-eshop" hidden>
        <div class="shop-layout">
          <div class="shop-catalog">
            <div style="display:flex; gap: 1rem;">
              <button class="sh-tab on" data-category="todos">Todos</button>
              <button class="sh-tab" data-category="roupas">Roupas</button>
              <button class="sh-tab" data-category="calcados">Calçados</button>
            </div>
            <div class="prod-grid">
              <div class="prod-card" data-category="roupas">
                <div style="font-size:3rem; margin-bottom:1rem;">👕</div>
                <div style="font-size:.7rem;">Camiseta Premium</div>
                <div style="font-weight:bold; color:var(--cloud); margin-top:.5rem">R$ 89,90</div>
                <button class="prod-add-btn" data-name="Camiseta Premium" data-price="89.90">+ Adicionar</button>
              </div>
              <div class="prod-card" data-category="calcados">
                <div style="font-size:3rem; margin-bottom:1rem;">👟</div>
                <div style="font-size:.7rem;">Tênis Esporte</div>
                <div style="font-weight:bold; color:var(--cloud); margin-top:.5rem">R$ 129,90</div>
                <button class="prod-add-btn" data-name="Tênis Esporte" data-price="129.90">+ Adicionar</button>
              </div>
              <div class="prod-card" data-category="roupas">
                <div style="font-size:3rem; margin-bottom:1rem;">👖</div>
                <div style="font-size:.7rem;">Calça Jeans</div>
                <div style="font-weight:bold; color:var(--cloud); margin-top:.5rem">R$ 149,90</div>
                <button class="prod-add-btn" data-name="Calça Jeans" data-price="149.90">+ Adicionar</button>
              </div>
            </div>
          </div>
          <div class="shop-cart-panel">
            <div class="cart-header"><span>Carrinho</span><span class="cart-badge" id="cartBadge">2</span></div>
            <div class="cart-items" id="cartItems"></div>
            <div class="cart-footer">
              <div class="cart-total-row"><span>Total</span><span class="cart-total-val" id="cartTotal">R$ 219,80</span></div>
              <button class="btn btn-solid" style="width:100%">Finalizar compra</button>
            </div>
          </div>
        </div>
      </div>
      
      <div class="tab-panel" id="panel-site" role="tabpanel" aria-labelledby="tab-site" hidden>
        <div class="site-wireframe">
          <div style="border: 1px solid var(--border); border-radius: var(--r); padding: 1.5rem;">
            <div class="wf-nav">
              <div class="wf-link">Home</div><div class="wf-link">Sobre</div><div class="wf-link">Contato</div>
            </div>
            <div style="margin-top: 3rem; text-align: center;">
              <h2 style="font-size: 2rem; margin-bottom: 1rem;">Seu Negócio Online</h2>
              <p style="margin-bottom: 2rem; font-size: .8rem;">Design moderno e responsivo.</p>
              <button class="wf-btn" style="background:var(--cloud); color:white; border:none; padding:.5rem 1rem; border-radius:var(--r);">Saiba Mais</button>
            </div>
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 3rem;">
              <div class="wf-card">Funcionalidade 1</div>
              <div class="wf-card">Funcionalidade 2</div>
            </div>
          </div>
          <div style="background: var(--surface); padding: 1.5rem; border-radius: var(--r);">
            <div class="wf-quote">// O que está incluído</div>
            <ul style="margin-top: 1rem; font-size: .8rem; display:flex; flex-direction:column; gap:.8rem;">
              <li>✓ Domínio grátis 1º ano</li>
              <li>✓ Hospedagem otimizada</li>
              <li>✓ Design Exclusivo</li>
              <li>✓ Formulário de Contato</li>
              <li>✓ Botão WhatsApp</li>
              <li>✓ Painel Administrador</li>
              <li>✓ SEO Técnico</li>
              <li>✓ Otimização Mobile</li>
            </ul>
            <a href="#contato" class="btn" style="width:100%; margin-top: 2rem; font-size:.6rem" onclick="window.lenis && window.lenis.scrollTo('#contato')">Começar Agora</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="sec" id="contato">
    <div class="contact-wrap">
      <div>
        <span class="sec-tag">// vamos construir</span>
        <h2>Fale com a gente.</h2>
        <p>Conte um pouco sobre o que sua empresa faz e onde estão os gargalos hoje. Responderemos em até 1 dia útil.</p>
        <a href="https://wa.me/" class="wpp-link" target="_blank" rel="noopener noreferrer" style="display:inline-flex; align-items:center; gap:.5rem; margin-top:2rem; font-weight:bold; color:var(--wpp)">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.274.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.099.824zm-3.423-14.416c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm.029 18.88c-1.161 0-2.305-.292-3.318-.844l-3.677.964.984-3.595c-.607-1.052-.927-2.246-.926-3.468.001-3.825 3.113-6.937 6.937-6.937 1.856.001 3.598.723 4.907 2.034 1.31 1.311 2.031 3.054 2.03 4.908-.001 3.825-3.113 6.938-6.937 6.938z"/></svg>
          Chamar no WhatsApp
        </a>
      </div>
      <div>
        <form id="contactForm">
          <div class="field">
            <label class="fl" for="nome">Nome *</label>
            <input class="fi" id="nome" type="text" placeholder="Seu nome" autocomplete="name">
            <span class="field-error" id="nome-error" role="alert" aria-live="polite"></span>
          </div>
          <div class="field">
            <label class="fl" for="email">Email *</label>
            <input class="fi" id="email" type="email" placeholder="nome@empresa.com.br" autocomplete="email">
            <span class="field-error" id="email-error" role="alert" aria-live="polite"></span>
          </div>
          <div class="field">
            <label class="fl" for="msg">Mensagem *</label>
            <textarea class="fi" id="msg" rows="4" placeholder="Como podemos ajudar?"></textarea>
            <span class="field-error" id="msg-error" role="alert" aria-live="polite"></span>
          </div>
          <button type="submit" class="btn-solid" style="width:100%">Enviar mensagem</button>
        </form>
        <div id="formSuccess">
          <svg width="48" height="48" fill="none" stroke="currentColor" stroke-width="2" style="margin-bottom:1rem"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
          <h3>Mensagem enviada!</h3>
          <p>Entraremos em contato em breve.</p>
        </div>
      </div>
    </div>
  </section>

  <footer>
    <div class="container" style="display:flex; justify-content:space-between; align-items:center;">
      <div>© 2026 Code House. Todos os direitos reservados.</div>
      <a href="/politica-privacidade.html" style="color:var(--cloud)">Política de Privacidade</a>
    </div>
  </footer>

  <div id="lgpdBanner" class="lgpd-banner" role="dialog" aria-label="Aviso de privacidade" aria-live="polite" hidden>
    <p class="lgpd-text">Este site coleta apenas os dados informados no formulário, usados exclusivamente para responder seu contato. <a href="/politica-privacidade.html" class="lgpd-link">Política de Privacidade</a></p>
    <button class="lgpd-btn" id="lgpdAccept">Entendi</button>
  </div>

  <a href="https://wa.me/" class="wpp-float" aria-label="Abrir conversa no WhatsApp" target="_blank" rel="noopener noreferrer">
    <svg width="32" height="32" viewBox="0 0 24 24" fill="white"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.274.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.099.824zm-3.423-14.416c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm.029 18.88c-1.161 0-2.305-.292-3.318-.844l-3.677.964.984-3.595c-.607-1.052-.927-2.246-.926-3.468.001-3.825 3.113-6.937 6.937-6.937 1.856.001 3.598.723 4.907 2.034 1.31 1.311 2.031 3.054 2.03 4.908-.001 3.825-3.113 6.938-6.937 6.938z"/></svg>
  </a>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/lenis/1.1.14/lenis.min.js" defer></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js" defer></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r165/three.min.js" defer></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/splitting/1.0.6/splitting.min.js" defer></script>

  <script>
    const noMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;

    // H-50 Preloader
    document.addEventListener('DOMContentLoaded', () => {
      const preloader = document.getElementById('preloader');
      const fill = preloader?.querySelector('.pre-fill');
      if (typeof Splitting !== 'undefined' && preloader) Splitting({ target: '.pre-logo', by: 'chars' });
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

      // Lenis Smooth Scroll
      if (typeof Lenis !== 'undefined') {
        const lenis = new Lenis({ duration: 1.1, easing: t => Math.min(1, 1.001 - Math.pow(2, -10 * t)), smoothWheel: !matchMedia('(pointer:coarse)').matches });
        if (typeof ScrollTrigger !== 'undefined') {
          lenis.on('scroll', ScrollTrigger.update);
          gsap.ticker.add(time => lenis.raf(time * 1000));
          gsap.ticker.lagSmoothing(0);
        } else {
          function raf(time) { lenis.raf(time); requestAnimationFrame(raf); }
          requestAnimationFrame(raf);
        }
        document.querySelectorAll('a[href^="#"]').forEach(a => {
          a.addEventListener('click', e => {
            const id = a.getAttribute('href');
            const target = document.querySelector(id);
            if (!target) return;
            e.preventDefault();
            lenis.scrollTo(target, { offset: -60 });
          });
        });
        window.lenis = lenis;
      }

      // Progress bar & Hamburger
      const navProgress = document.getElementById('navProgress');
      window.addEventListener('scroll', () => {
        if (!navProgress) return;
        const scrolled = window.scrollY / (document.body.scrollHeight - window.innerHeight);
        navProgress.style.width = (scrolled * 100) + '%';
      }, { passive: true });

      const hamburger = document.getElementById('hamburger');
      const drawer = document.getElementById('navDrawer');
      hamburger?.addEventListener('click', () => {
        const isOpen = drawer?.classList.toggle('open');
        hamburger.classList.toggle('open', isOpen);
        hamburger.setAttribute('aria-expanded', isOpen);
        hamburger.setAttribute('aria-label', isOpen ? 'Fechar menu' : 'Abrir menu');
      });
      drawer?.querySelectorAll('a').forEach(a => {
        a.addEventListener('click', () => {
          drawer.classList.remove('open');
          hamburger?.classList.remove('open');
          hamburger?.setAttribute('aria-expanded', 'false');
        });
      });
      document.addEventListener('keydown', e => {
        if (e.key === 'Escape' && drawer?.classList.contains('open')) {
          drawer.classList.remove('open');
          hamburger?.classList.remove('open');
          hamburger?.setAttribute('aria-expanded','false');
          hamburger?.focus();
        }
      });

      // Hero Canvas
      if (typeof THREE !== 'undefined') {
        const canvas = document.getElementById('heroCanvas');
        if (canvas) {
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
        }
      }

      // Headline
      if (typeof Splitting !== 'undefined' && typeof gsap !== 'undefined') {
        Splitting();
        if(!noMotion) {
          const tl = gsap.timeline({ delay: 0.3 });
          tl.from('.hero .eyebrow', { opacity: 0, y: 12, duration: 0.45, ease: 'power2.out' })
            .from('.hero h1 .char', { opacity: 0, y: 24, rotateX: 45, stagger: 0.025, duration: 0.5, ease: 'power3.out', transformOrigin: 'bottom center' }, '-=0.2')
            .from('.hero p:not(.hero-stats)', { opacity: 0, y: 10, duration: 0.45, ease: 'power2.out' }, '-=0.2')
            .from('.hero .btn-solid, .hero .btn-outline', { opacity: 0, y: 8, stagger: 0.1, duration: 0.35, ease: 'power2.out' }, '-=0.2')
            .from('.hero-stats', { opacity: 0, duration: 0.3, ease: 'power1.out' }, '-=0.1');
        }
      }

      // Toasts
      function showToast(container, text, delay) {
        setTimeout(() => {
          if (!document.contains(container)) return;
          const toast = document.createElement('div');
          toast.className = 'app-toast';
          toast.textContent = text;
          container.appendChild(toast);
          requestAnimationFrame(() => { toast.classList.add('visible'); });
          setTimeout(() => {
            toast.classList.remove('visible');
            setTimeout(() => toast.remove(), 300);
          }, 3500);
        }, delay);
      }
      const tc = document.getElementById('toastContainer');
      if(tc) {
        showToast(tc, '✓ Negócio fechado: Ana Lima', 1500);
        showToast(tc, '📅 Reunião às 14h: FerroMax', 5000);
      }

      // Stats Countup
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

      // Tabs
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
            onTabActivated(p.id);
          } else {
            p.setAttribute('hidden', '');
          }
        });
      }

      function onTabActivated(id) {
        if(id === 'panel-crm') {
          document.querySelectorAll('#panel-crm .pipe-fill').forEach((bar, i) => {
            anime({ targets: bar, width: bar.dataset.fill + '%', duration: 900, delay: i * 150, easing: 'easeOutCubic' });
          });
        }
        if(id === 'panel-erp') {
          const line = document.querySelector('#panel-erp .chart-line');
          const area = document.querySelector('#panel-erp .chart-area');
          if (line && typeof anime !== 'undefined') {
            anime({ targets: line, strokeDashoffset: [1000, 0], duration: 1600, easing: 'easeInOutSine' });
            anime({ targets: area, opacity: [0, 1], duration: 600, delay: 1200, easing: 'linear' });
          }
        }
      }

      // Eshop
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
        
        list.textContent = '';
        cartItems.forEach((item, i) => {
          const row = document.createElement('div');
          row.className = 'cart-item-row';
          const name = document.createElement('span');
          name.textContent = item.name;
          const price = document.createElement('span');
          price.textContent = 'R$ ' + item.price.toFixed(2).replace('.', ',');
          const remove = document.createElement('button');
          remove.className = 'cart-remove';
          remove.textContent = '×';
          remove.setAttribute('aria-label', 'Remover ' + item.name);
          remove.addEventListener('click', () => { cartItems.splice(i, 1); renderCart(); });
          row.appendChild(name); row.appendChild(price); row.appendChild(remove);
          list.appendChild(row);
        });
        badge.textContent = cartItems.length;
        const sum = cartItems.reduce((a, c) => a + c.price, 0);
        total.textContent = 'R$ ' + sum.toFixed(2).replace('.', ',');
      }
      renderCart();

      // Form
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

      document.getElementById('contactForm')?.addEventListener('submit', function(e) {
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

      // Services
      const svcData = {
        crm: { eye:'// CRM', title:'Gestão de clientes que acompanha seu funil', desc:'Não é um CRM genérico de prateleira — é construído em cima de como você já trabalha. Funil de vendas configurado do seu jeito, campos que fazem sentido para o negócio, histórico de cada cliente ao alcance.', features:['Pipeline personalizado','Histórico de interações','Alertas e lembretes','Relatórios do que importa','WhatsApp (opcional)'] },
        erp: { eye:'// ERP', title:'Operação integrada sem planilhas paralelas', desc:'Estoque, compras, faturamento e financeiro em um só lugar. Conecta os setores que já existem na sua empresa — não força mudança de processo, apenas organiza o que já acontece.', features:['Estoque em tempo real','Fluxo de caixa','Pedidos de compra','Dashboard operacional','Alertas de ruptura'] },
        site: { eye:'// Site', title:'Presença digital que representa quem você é', desc:'Não é template com as cores da empresa — é um site construído a partir da identidade visual, da linguagem e do que os clientes precisam encontrar.', features:['Design único','Mobile-first','SEO técnico incluso','Core Web Vitals','CMS para atualizar'] },
        eshop: { eye:'// E-shop', title:'Loja virtual que vende, não que parece', desc:'Catálogo, carrinho, pagamentos e gestão de pedidos integrados. Feito para funcionar no mobile, carregar rápido e converter.', features:['Catálogo com filtros','Checkout Pix e cartão','Gestão de pedidos','Cálculo de frete','Dashboard de vendas'] },
        sobmedida: { eye:'// Sob Medida', title:'Qualquer sistema que o negócio precise', desc:'Automação de processo, sistema de agendamento, painel de gestão interno — se existe um processo manual recorrente que trava a equipe, a Code House constrói a solução.', features:['Levantamento incluso','Prototipagem','Tecnologia certa','Documentação entregue','Suporte pós-lançamento'] }
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
        
        detail.querySelector('.svc-detail-eye').textContent = data.eye;
        detail.querySelector('h3').textContent = data.title;
        detail.querySelector('p:not(.svc-detail-eye)').textContent = data.desc;
        const ul = detail.querySelector('.svc-features');
        ul.textContent = '';
        data.features.forEach(f => {
          const li = document.createElement('li');
          const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
          svg.setAttribute('width', '16'); svg.setAttribute('height', '16'); svg.setAttribute('fill', 'none'); svg.setAttribute('stroke', 'currentColor'); svg.setAttribute('stroke-width', '2');
          const polyline = document.createElementNS('http://www.w3.org/2000/svg', 'polyline');
          polyline.setAttribute('points', '20 6 9 17 4 12');
          svg.appendChild(polyline);
          li.appendChild(svg);
          const span = document.createElement('span');
          span.textContent = f;
          li.appendChild(span);
          ul.appendChild(li);
        });
      }

      // Process GSAP
      if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);
        gsap.fromTo('#processo .p-step:nth-child(2)', 
          { opacity: 0, x: 40 },
          { opacity: 1, x: 0, duration: 0.6, ease: 'power2.out', scrollTrigger: { trigger: '#processo .p-grid', start: 'top 75%', once: true } }
        );
        gsap.fromTo('#processo .p-step:nth-child(3)',
          { opacity: 0, x: 60 },
          { opacity: 1, x: 0, duration: 0.6, delay: 0.15, ease: 'power2.out', scrollTrigger: { trigger: '#processo .p-grid', start: 'top 75%', once: true } }
        );
        ScrollTrigger.create({
          trigger: '#processo .p-grid', start: 'top 75%', once: true,
          onEnter: () => {
            const line = document.querySelector('.proc-connector line');
            if (line) line.style.strokeDashoffset = '0';
          }
        });

        // Global Reveals
        document.querySelectorAll('.sec-tag, .eyebrow').forEach(el => {
          gsap.fromTo(el, { opacity:0, x:-16 }, { opacity:1, x:0, duration:.45, ease:'power2.out', scrollTrigger: { trigger: el, start: 'top 88%', once: true } });
        });
        document.querySelectorAll('h2').forEach(el => {
          gsap.fromTo(el, { opacity:0, y:16 }, { opacity:1, y:0, duration:.5, delay:.08, ease:'power2.out', scrollTrigger: { trigger: el, start: 'top 85%', once: true } });
        });
        document.querySelectorAll('.stat-item').forEach((el, i) => {
          gsap.fromTo(el, { opacity:0, y:20 }, { opacity:1, y:0, duration:.45, delay: i * 0.1, ease:'power2.out', scrollTrigger: { trigger: el.parentElement, start: 'top 80%', once: true } });
        });
      }

      // LGPD Banner
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

      // Wpp Float
      const wppBtn = document.querySelector('.wpp-float');
      let wppShown = false;
      window.addEventListener('scroll', () => {
        if (!wppBtn || wppShown) return;
        if (window.scrollY > 400) { wppBtn.classList.add('visible'); wppShown = true; }
      }, { passive: true });

    });
  </script>
</body>
</html>"""

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(HTML_CONTENT)

if __name__ == '__main__':
    main()
