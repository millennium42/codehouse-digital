/* examples.js — Tabs, modals, counters, spotlight */

document.addEventListener('DOMContentLoaded', function() {

  /* --- 1. SPOTLIGHT --- */
  const spotlight = document.getElementById('spotlight');
  if (spotlight) {
    let ticking = false;
    document.addEventListener('mousemove', function(e) {
      if (!ticking) {
        window.requestAnimationFrame(function() {
          spotlight.style.setProperty('--mx', e.clientX + 'px');
          spotlight.style.setProperty('--my', e.clientY + 'px');
          ticking = false;
        });
        ticking = true;
      }
    });
  }

  /* --- 2. TABS FILTER --- */
  const tabs = document.querySelectorAll('.ex-tab');
  const cards = document.querySelectorAll('.ex-card');
  const emptyState = document.getElementById('exEmpty');

  function filterCards(cat) {
    let visible = 0;
    cards.forEach(function(card) {
      const cardCat = card.getAttribute('data-cat');
      if (cardCat === cat) {
        card.classList.remove('hidden');
        visible++;
      } else {
        card.classList.add('hidden');
      }
    });
    if (emptyState) {
      emptyState.style.display = visible === 0 ? 'block' : 'none';
    }
  }

  tabs.forEach(function(tab) {
    tab.addEventListener('click', function() {
      const cat = tab.getAttribute('data-tab');
      tabs.forEach(function(t) { t.classList.remove('active'); });
      tab.classList.add('active');
      filterCards(cat);
    });
  });

  // Initial filter: show only CRM on load
  filterCards('crm');



  /* --- 4. MODAL DATA --- */
  const modalData = {
    'crm-funil': {
      tag: 'CRM & Vendas',
      title: 'Funil de Vendas Premium',
      desc: 'Pipeline visual completo para gerenciar leads desde o primeiro contato até o fechamento. Cada etapa tem regras automáticas e gatilhos de follow-up.',
      features: [
        'Drag-and-drop entre etapas sem perder histórico',
        'Score automático baseado em comportamento',
        'Alertas de follow-up que não deixam lead esfriar',
        'Relatórios de conversão por etapa e vendedor',
        'Integração nativa com WhatsApp Business API',
        'Timeline completa: email, ligação, reunião, proposta'
      ],
      stack: ['React', 'Node.js', 'PostgreSQL', 'Redis', 'WhatsApp API'],
      result: { num: '+29%', label: 'Aumento médio em vendas com CRM estruturado', source: 'Fonte: Salesforce, "State of Sales", 2024 — salesforce.com/resources' }
    },
    'crm-dash': {
      tag: 'CRM & Vendas',
      title: 'Dashboard Analytics 360',
      desc: 'Visão consolidada de todo o ciclo de vendas com forecast baseado em dados históricos, funil invertido e alertas de reposição automática.',
      features: [
        'Forecast de receita baseado em pipeline atual',
        'Funil invertido mostrando gargalos reais',
        'Ranking de vendedores com métricas justas',
        'Alertas de reposição: substituir perdas automaticamente',
        'Exportação de relatórios em PDF/Excel',
        'Dashboard personalizado por cargo (vendedor vs gerente)'
      ],
      stack: ['React', 'Chart.js', 'PostgreSQL', 'Python', 'Celery'],
      result: { num: '+42%', label: 'Melhoria na precisão de forecast de vendas', source: 'Fonte: Nucleus Research, "CRM Pays Back", 2024 — nucleusresearch.com' }
    },
    'erp-financeiro': {
      tag: 'ERP & Gestão',
      title: 'Módulo Financeiro Inteligente',
      desc: 'Conciliação bancária automática, DRE em tempo real, centro de custos e fluxo de caixa projetado com Machine Learning.',
      features: [
        'Conciliação bancária automática via OFX/Febraban',
        'DRE em tempo real com drill-down por centro de custo',
        'Fluxo de caixa projetado com IA (ML)',
        'Contas a pagar e receber com alertas de vencimento',
        'Múltiplas empresas em um único painel',
        'API para integração com contabilidade externa'
      ],
      stack: ['React', 'Python/Django', 'PostgreSQL', 'Celery', 'Redis'],
      result: { num: '50%', label: 'Redução no tempo de fechamento mensal com ERP', source: 'Fonte: Panorama Consulting Group, "ERP Report", 2024 — panorama-consulting.com' }
    },
    'erp-estoque': {
      tag: 'ERP & Gestão',
      title: 'Controle de Estoque Avançado',
      desc: 'Gestão de múltiplos depósitos, leitura de código de barras, curva ABC e alertas de ruptura com sugestão de compra automática.',
      features: [
        'Múltiplos depósitos com transferência entre eles',
        'Leitura de código de barras (câmera ou scanner)',
        'Curva ABC com sugestão de ponto de pedido',
        'Alertas de ruptura: email, WhatsApp e push',
        'Ficha técnica (receita de produtos) integrada',
        'Inventário cíclico e geral com mobile'
      ],
      stack: ['React', 'Python', 'PostgreSQL', 'PWA', 'Firebase'],
      result: { num: '-30%', label: 'Redução média de rupturas de estoque com automação', source: 'Fonte: IHL Group / Firework Research, 2024 — ihlservices.com' }
    },
    'shop-catalogo': {
      tag: 'E-Commerce',
      title: 'Catálogo Inteligente',
      desc: 'Vitrine com filtros faceted, busca Elastic, variações ilimitadas e avaliação social. Cada produto é uma página de conversão otimizada.',
      features: [
        'Filtros faceted (categoria, preço, atributos customizados)',
        'Busca Elastic com autocomplete e correção ortográfica',
        'Variações ilimitadas (cor, tamanho, material)',
        'Zoom e galeria de imagens com vídeo',
        'Avaliações verificadas com foto do cliente',
        'SEO técnico: schema.org, sitemap, meta tags dinâmicas'
      ],
      stack: ['Next.js', 'Elasticsearch', 'PostgreSQL', 'Vercel', 'Stripe'],
      result: { num: '-67%', label: 'Redução de abandono com UX otimizada no catálogo', source: 'Fonte: Baymard Institute, "Product Page UX", 2024 — baymard.com/research' }
    },
    'shop-checkout': {
      tag: 'E-Commerce',
      title: 'Checkout Otimizado',
      desc: 'One-page checkout que converte. Múltiplos gateways, cálculo de frete em tempo real e recuperação de carrinho automática.',
      features: [
        'One-page checkout com progress indicator',
        'Múltiplos gateways: PIX, boleto, cartão, PayPal',
        'Cálculo de frete em tempo real (Correios, Jadlog, total)',
        'Cupons de desconto com regras avançadas',
        'Recuperação de carrinho via email e WhatsApp (2h depois)',
        'One-click checkout para clientes recorrentes'
      ],
      stack: ['Next.js', 'Stripe', 'Correios API', 'Redis', 'Queue'],
      result: { num: '+35%', label: 'Potencial de aumento na conversão do checkout', source: 'Fonte: Baymard Institute, "Cart Abandonment Stats", 2024 — baymard.com/lists/cart-abandonment-rate' }
    },
    'web-landing': {
      tag: 'Web & Landing',
      title: 'Landing Page Conversora',
      desc: 'Página de alta conversão com hero section impactante, forms otimizados, A/B testing nativo e tempo de carga inferior a 1.8s.',
      features: [
        'Hero section com copy testada e CTA único',
        'Formulários otimizados (menos campos = mais leads)',
        'A/B testing nativo sem depender de terceiros',
        'Tempo de carga inferior a 1.8s (Core Web Vitals)',
        'Mobile-first: 70% do tráfego são celulares',
        'Integração com CRM e notificação em tempo real'
      ],
      stack: ['Next.js', 'TypeScript', 'Vercel Edge', 'Plausible', 'Formspree'],
      result: { num: '+202%', label: 'Aumento com CTAs personalizados vs. genéricos', source: 'Fonte: HubSpot, "Marketing Statistics", 2024 — hubspot.com/marketing-statistics' }
    },
    'web-institucional': {
      tag: 'Web & Institucional',
      title: 'Site Institucional Premium',
      desc: 'Site corporativo completo com blog integrado, SEO técnico e multi-idioma. Painel CMS próprio sem dependências de WordPress.',
      features: [
        'Páginas institucionais: sobre, serviços, equipe, contato',
        'Blog integrado com editor markdown e SEO avançado',
        'Multi-idioma (PT/EN/ES) com roteamento inteligente',
        'Formulário de contato com validação e Captcha',
        'Integração com redes sociais (og:image, Twitter cards)',
        'Painel CMS leve: editar textos, imagens e páginas'
      ],
      stack: ['Next.js', 'MDX', 'PostgreSQL', 'Vercel', 'i18n'],
      result: { num: '+85%', label: 'Aumento orgânico típico com redesign e SEO técnico', source: 'Fonte: Backlinko / Ahrefs, Case Studies SEO, 2024 — backlinko.com' }
    }
  };

  /* --- 5. MODAL OPEN/CLOSE --- */
  const overlay = document.getElementById('modal-overlay');
  const content = document.getElementById('modal-content');
  const closeBtn = document.getElementById('modalClose');
  const modalBox = document.querySelector('.modal-box');
  let firstFocusableElement;
  let lastFocusableElement;
  let previousActiveElement;

  function updateModalFocusables() {
    if (!modalBox) return;
    const focusableElementsString = 'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])';
    const focusableContent = modalBox.querySelectorAll(focusableElementsString);
    if(focusableContent.length === 0) return;
    firstFocusableElement = focusableContent[0];
    lastFocusableElement = focusableContent[focusableContent.length - 1];
  }

  function openModal(id) {
    const data = modalData[id];
    if (!data || !overlay || !content) return;
    
    previousActiveElement = document.activeElement;

    let html = '<span class="modal-tag">' + data.tag + '</span>' +
               '<h2>' + data.title + '</h2>' +
               '<p class="modal-desc">' + data.desc + '</p>' +
               '<h4>Funcionalidades</h4>' +
               '<ul>';
    
    data.features.forEach(function(f) {
      html += '<li>' + f + '</li>';
    });
    
    html += '</ul>' +
            '<h4>Stack Técnica</h4>' +
            '<div class="stack-list">';
    
    data.stack.forEach(function(s) {
      html += '<span class="stack-badge">' + s + '</span>';
    });
    
    html += '</div>' +
            '<div class="result-box">' +
            '<span class="result-num">' + data.result.num + '</span>' +
            '<p>' + data.result.label + '</p>' +
            (data.result.source ? '<span class="result-source">' + data.result.source + '</span>' : '') +
            '</div>';

    content.innerHTML = html;
    overlay.classList.add('open');
    overlay.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    
    updateModalFocusables();
    if(firstFocusableElement) firstFocusableElement.focus();
  }

  function closeModal() {
    if (!overlay) return;
    overlay.classList.remove('open');
    overlay.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    if(previousActiveElement) previousActiveElement.focus();
  }

  // Bind card clicks
  cards.forEach(function(card) {
    card.addEventListener('click', function() {
      const id = card.getAttribute('data-id');
      openModal(id);
    });

    // Keyboard accessible
    card.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        const id = card.getAttribute('data-id');
        openModal(id);
      }
    });
  });

  // Make cards focusable
  cards.forEach(function(card) {
    card.setAttribute('tabindex', '0');
    card.setAttribute('role', 'button');
  });

  // Close button
  if (closeBtn) {
    closeBtn.addEventListener('click', closeModal);
  }

  // Click outside
  if (overlay) {
    overlay.addEventListener('click', function(e) {
      if (e.target === overlay) closeModal();
    });
  }

  // Escape key & Tab
  document.addEventListener('keydown', function(e) {
    if (!overlay || !overlay.classList.contains('open')) return;
    
    if (e.key === 'Escape') {
      closeModal();
      return;
    }

    if (e.key === 'Tab') {
      updateModalFocusables();
      if (!firstFocusableElement) return;

      if (e.shiftKey) { // Shift + Tab
        if (document.activeElement === firstFocusableElement) {
          lastFocusableElement.focus();
          e.preventDefault();
        }
      } else { // Tab
        if (document.activeElement === lastFocusableElement) {
          firstFocusableElement.focus();
          e.preventDefault();
        }
      }
    }
  });

});