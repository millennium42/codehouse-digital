/* examples.js */

// Tabs
document.querySelectorAll('.tbtn').forEach(function(btn){
  btn.addEventListener('click', function(){
    var target = btn.getAttribute('data-t');
    
    // Update buttons
    document.querySelectorAll('.tbtn').forEach(function(b){ b.classList.remove('active'); });
    btn.classList.add('active');
    
    // Update panels
    document.querySelectorAll('.tpanel').forEach(function(p){ p.classList.remove('active'); });
    var panel = document.getElementById('tp-' + target);
    if(panel) panel.classList.add('active');
  });
});

// Modal
var modalData = {
  'crm-funil': {
    title: 'Funil de Vendas',
    body: '<p>Pipeline visual completo para gerenciar leads desde o primeiro contato até o fechamento.</p><ul><li>Drag-and-drop entre etapas</li><li>Histórico de interações</li><li>Alertas de follow-up</li><li>Relatórios de conversão</li></ul>'
  },
  'crm-pipeline': {
    title: 'Pipeline de Clientes',
    body: '<p>Visão geral do relacionamento com clientes e oportunidades em andamento.</p><ul><li>Score automático de leads</li><li>Integração com email</li><li>Agenda de tarefas</li><li>Dashboard personalizado</li></ul>'
  },
  'erp-dash': {
    title: 'Dashboard Financeiro',
    body: '<p>Painel com indicadores financeiros em tempo real para tomada de decisão.</p><ul><li>Receita x Despesas</li><li>Fluxo de caixa projetado</li><li>Conciliação bancária</li><li>Relatórios DRE</li></ul>'
  },
  'erp-estoque': {
    title: 'Controle de Estoque',
    body: '<p>Gestão completa de produtos com alertas e controle de movimentação.</p><ul><li>Alertas de estoque mínimo</li><li>Código de barras</li><li>Múltiplos depósitos</li><li>Histórico de movimentação</li></ul>'
  },
  'shop-catalogo': {
    title: 'Catálogo de Produtos',
    body: '<p>Vitrine virtual organizada com filtros e busca inteligente.</p><ul><li>Filtros por categoria/preço</li><li>Zoom nas imagens</li><li>Variações de produto</li><li>SEO otimizado</li></ul>'
  },
  'shop-cart': {
    title: 'Carrinho de Compras',
    body: '<p>Experiência de checkout otimizada para conversão.</p><ul><li>Cálculo de frete automático</li><li>Múltiplas formas de pagamento</li><li>Cupons de desconto</li><li>Recuperação de carrinho</li></ul>'
  },
  'site-landing': {
    title: 'Landing Page Premium',
    body: '<p>Página de alta conversão com design profissional e performance.</p><ul><li>Hero section impactante</li><li>Animações suaves</li><li>Formulários otimizados</li><li>A/B testing integrado</li></ul>'
  },
  'site-institucional': {
    title: 'Página Institucional',
    body: '<p>Site corporativo completo com design moderno e responsivo.</p><ul><li>Institucional e sobre</li><li>Catálogo de serviços</li><li>Blog integrado</li><li>Formulário de contato</li></ul>'
  }
};

function openModal(id){
  var data = modalData[id];
  if(!data) return;
  
  var overlay = document.getElementById('modal-overlay');
  var content = document.getElementById('modal-content');
  
  content.innerHTML = '<h3>' + data.title + '</h3>' + data.body;
  overlay.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeModal(){
  var overlay = document.getElementById('modal-overlay');
  overlay.classList.remove('open');
  document.body.style.overflow = '';
}

// Close on overlay click
document.getElementById('modal-overlay').addEventListener('click', function(e){
  if(e.target === this) closeModal();
});

// Close on Escape
document.addEventListener('keydown', function(e){
  if(e.key === 'Escape') closeModal();
});
