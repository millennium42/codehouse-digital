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
      desc: 'Pipeline visual completo para gerenciar leads desde o primeiro contato ate o fechamento. Cada etapa tem regras own automaticas e gatilhos de follow-up.',
      features: [
        'Drag-and-drop entre etapas sem perder historico',
        'Score automatico baseado em comportamento',
        'Alertas de follow-up que nao deixam lead esfriar',
        'Relatorios de conversao por etapa e vendedor',
        'Integracao nativa com WhatsApp Business API',
        'Timeline completa: email, ligacao, reuniao, proposta'
      ],
      stack: ['React', 'Node.js', 'PostgreSQL', 'Redis', 'WhatsApp API'],
      result: { num: '+180%', label: 'Aumento em vendas no primeiro trimestre' }
    },
    'crm-dash': {
      tag: 'CRM & Vendas',
      title: 'Dashboard Analytics 360',
      desc: 'Visao consolidada de todo o ciclo de vendas com forecast baseado em dados historicos, funil invertido e alertas de replesao automatica.',
      features: [
        'Forecast de receita baseado em pipeline atual',
        'Funil invertido mostrando gargalos reais',
        'Ranking de vendedores com metricas justas',
        'Alertas de replesao: substituir perdas automaticamente',
        'Exportacao de relatorios em PDF/Excel',
        'Dashboard personalizado por cargo (vendedor vs gerente)'
      ],
      stack: ['React', 'Chart.js', 'PostgreSQL', 'Python', 'Celery'],
      result: { num: '+31%', label: 'Aumento na taxa de conversao em 60 dias' }
    },
    'erp-financeiro': {
      tag: 'ERP & Gestao',
      title: 'Modulo Financeiro Inteligente',
      desc: 'Conciliacao bancaria automatica, DRE em tempo real, centro de custos e fluxo de caixa projetado comMachine Learning.',
      features: [
        'Conciliacao bancaria automatica via OFX/Febraban',
        'DRE em tempo real com drill-down por centro de custo',
        'Fluxo de caixa projetado com IA (ML)',
        'Contas a pagar e receber com alertas de vencimento',
        'Multiplas empresas em um unico painel',
        'API para integracao com contabilidade externa'
      ],
      stack: ['React', 'Python/Django', 'PostgreSQL', 'Celery', 'Redis'],
      result: { num: '-40%', label: 'Reducao de custo operacional no primeiro semestre' }
    },
    'erp-estoque': {
      tag: 'ERP & Gestao',
      title: 'Controle de Estoque Avancado',
      desc: 'Gestao de multiplos depositos, leitura de codigo de barras, curva ABC e alertas de ruptura com sugestao de compra automatica.',
      features: [
        'Multiplos depositos com transferencia entre eles',
        'Leitura de codigo de barras (camera ou scanner)',
        'Curva ABC com sugestao de ponto de pedido',
        'Alertas de ruptura: email, WhatsApp e push',
        'Ficha tecnica (receita de produtos) integrada',
        'Inventario ciclico e geral com mobile'
      ],
      stack: ['React', 'Python', 'PostgreSQL', 'PWA', 'Firebase'],
      result: { num: '-72%', label: 'Reducao de rupturas de estoque em 90 dias' }
    },
    'shop-catalogo': {
      tag: 'E-Commerce',
      title: 'Catalogo Inteligente',
      desc: 'Vitrine com filtros faceted, buscaElastic, variacoes ilimitadas e avaliacao social. Cada produto e uma pagina de conversao otimizada.',
      features: [
        'Filtros faceted (categoria, preco, atributos customizados)',
        'BuscaElastic com autocomplete e correcao ortografica',
        'Variacoes ilimitadas (cor, tamanho, material)',
        'Zoom e galeria de imagens com video',
        'Avaliacoes verificadas com foto do cliente',
        'SEO tecnico: schema.org, sitemap, meta tags dinamicas'
      ],
      stack: ['Next.js', 'Elasticsearch', 'PostgreSQL', 'Vercel', 'Stripe'],
      result: { num: '+240%', label: 'Aumento em paginas vistas por sessao' }
    },
    'shop-checkout': {
      tag: 'E-Commerce',
      title: 'Checkout Otimizado',
      desc: 'One-page checkout que converte. Multiplos gateways, calculo de frete em tempo real e recuperacao de carrinho automatica.',
      features: [
        'One-page checkout com progress indicator',
        'Multiplos gateways: PIX, boleto, cartao, PayPal',
        'Calculo de frete em tempo real (Correios, Jadlog, total)',
        'Cupons de desconto com regras avancadas',
        'Recuperacao de carrinho via email e WhatsApp (2h depois)',
        'One-click checkout para clientes recorrentes'
      ],
      stack: ['Next.js', 'Stripe', 'Correios API', 'Redis', 'Queue'],
      result: { num: '+67%', label: 'Aumento na taxa de conversao de checkout' }
    },
    'web-landing': {
      tag: 'Web & Landing',
      title: 'Landing Page Conversora',
      desc: 'Pagina de alta conversao com hero section impacto, forms otimizados, A/B testing nativo e tempo de carga inferior a 1.8s.',
      features: [
        'Hero section com copy testada e CTA unico',
        'Formularios otimizados (menos campos = mais leads)',
        'A/B testing nativo sem depender de terceiros',
        'Tempo de carga inferior a 1.8s (Core Web Vitals)',
        'Mobile-first: 70% do trafego sao celulares',
        'Integracao com CRM e notificacao em tempo real'
      ],
      stack: ['Next.js', 'TypeScript', 'Vercel Edge', 'Plausible', 'Formspree'],
      result: { num: '+210%', label: 'Aumento de leads qualificados em 60 dias' }
    },
    'web-institucional': {
      tag: 'Web & Institucional',
      title: 'Site Institucional Premium',
      desc: 'Site corporativo completo com blog integrado, SEO tecnico e multi-idioma. Painel CMS proprio sem dependencias de WordPress.',
      features: [
        'Paginas institucionais: sobre, servicos, equipe, contato',
        'Blog integrado com editor markdown e SEO avancado',
        'Multi-idioma (PT/EN/ES) com roteamento inteligente',
        'Formulario de contato com validacao e Captcha',
        'Integracao com redes sociais (og:image, Twitter cards)',
        'Painel CMS leve: editar textos, imagens e paginas'
      ],
      stack: ['Next.js', 'MDX', 'PostgreSQL', 'Vercel', 'i18n'],
      result: { num: '+85%', label: 'Aumento organico em 6 meses' }
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