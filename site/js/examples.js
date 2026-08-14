/* examples.js */

// Tab functionality
document.addEventListener('DOMContentLoaded', function() {
  var tabs = document.querySelectorAll('.tab-btn');
  var panels = document.querySelectorAll('.tab-panel');
  
  tabs.forEach(function(tab) {
    tab.addEventListener('click', function() {
      var target = tab.getAttribute('data-tab');
      
      tabs.forEach(function(t) { t.classList.remove('active'); });
      tab.classList.add('active');
      
      panels.forEach(function(p) {
        p.classList.toggle('active', p.getAttribute('id') === 'panel-' + target);
      });
    });
  });
});

// Modal content
var modalData = {
  'crm-funil': {
    title: 'Funil de Vendas',
    body: '<p>Pipeline visual completo para gerenciar leads desde o primeiro contato até o fechamento da venda.</p>' +
          '<ul><li>Drag-and-drop entre etapas</li><li>Histórico completo de interações</li><li>Alertas automáticos de follow-up</li><li>Relatórios de conversão por etapa</li><li>Integração com email e WhatsApp</li></ul>'
  },
  'crm-pipeline': {
    title: 'Pipeline de Clientes',
    body: '<p>Visão geral do relacionamento com clientes e oportunidades em andamento.</p>' +
          '<ul><li>Score automático de leads</li><li>Integração nativa com email</li><li>Agenda de tarefas integrada</li><li>Dashboard personalizado por cargo</li><li>Metas e acompanhamento</li></ul>'
  },
  'erp-dash': {
    title: 'Dashboard Financeiro',
    body: '<p>Painel com indicadores financeiros em tempo real para tomada de decisão.</p>' +
          '<ul><li>Receita x Despesas em tempo real</li><li>Fluxo de caixa projetado</li><li>Conciliação bancária automática</li><li>Relatórios DRE e Balanço</li><li>Centro de custos</li></ul>'
  },
  'erp-estoque': {
    title: 'Controle de Estoque',
    body: '<p>Gestão completa de produtos com alertas inteligentes e controle de movimentação.</p>' +
          '<ul><li>Alertas de estoque mínimo</li><li>Leitura de código de barras</li><li>Múltiplos depósitos</li><li>Histórico completo de movimentação</li><li>Curva ABC de produtos</li></ul>'
  },
  'shop-catalogo': {
    title: 'Catálogo de Produtos',
    body: '<p>Vitrine virtual organizada com filtros avançados e busca inteligente.</p>' +
          '<ul><li>Filtros por categoria, preço e atributos</li><li>Zoom e múltiplas imagens por produto</li><li>Variações (cor, tamanho, etc)</li><li>SEO otimizado para Google</li><li>Avaliações de clientes</li></ul>'
  },
  'shop-cart': {
    title: 'Carrinho de Compras',
    body: '<p>Experiência de checkout otimizada para maximizar conversões.</p>' +
          '<ul><li>Cálculo de frete automático (Correios e outros)</li><li>Boleto, PIX, cartão de crédito</li><li>Cupons de desconto</li><li>Carrinho salvo entre sessões</li><li>Recuperação de carrinho abandonado</li></ul>'
  },
  'site-landing': {
    title: 'Landing Page Premium',
    body: '<p>Página de alta conversão com design profissional e performance otimizada.</p>' +
          '<ul><li>Hero section impactante</li><li>Animações suaves de scroll</li><li>Formulários otimizados</li><li>Tempo de carregamento inferior a 2s</li><li>Mobile-first responsivo</li></ul>'
  },
  'site-institucional': {
    title: 'Página Institucional',
    body: '<p>Site corporativo completo com design moderno e profissional.</p>' +
          '<ul><li>Página institucional e sobre</li><li>Catálogo de serviços/produtos</li><li>Blog integrado para conteúdo</li><li>Formulário de contato inteligente</li><li>Integração com redes sociais</li></ul>'
  }
};

function openModal(id) {
  var data = modalData[id];
  if (!data) return;
  
  var overlay = document.getElementById('modal-overlay');
  var content = document.getElementById('modal-content');
  
  content.innerHTML = '<h3>' + data.title + '</h3>' + data.body;
  overlay.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  var overlay = document.getElementById('modal-overlay');
  overlay.classList.remove('open');
  document.body.style.overflow = '';
}

// Close on overlay click
document.getElementById('modal-overlay').addEventListener('click', function(e) {
  if (e.target === this) closeModal();
});

// Close on Escape
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') closeModal();
});
