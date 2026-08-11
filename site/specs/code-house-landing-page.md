# Code House — Landing Page
## Spec completo para o Ralph Loop

**Objetivo:** Landing page de apresentação da Code House para pequenas empresas.  
**Deploy:** Render (static site)  
**Data:** 2026-08-07  
**Definição de "concluído":** Página publicada no Render, responsiva, dark/light mode, formulário funcional, sem bug P0/P1.

---

## Contexto do produto

A Code House entrega soluções de TI personalizadas para pequenas empresas (CRM, ERP, site institucional, e-shop e sob medida). O diferencial é adaptar o sistema ao fluxo e linguagem do cliente, não impor um template genérico. A marca fala por si — sem rosto de fundador, sem foto pessoal. O que convence é a identidade visual e os exemplos de sistemas que a empresa pode construir.

---

## Personas

- **Pedro** — dono de loja física, nunca contratou sistema, quer saber "o que vocês fazem e quanto custa começar"
- **Marina** — gerente de PME, já usou ERP engessado, busca flexibilidade
- **Thiago** — gestor de e-commerce pequeno, quer loja virtual com identidade própria

---

## Histórias de usuário

---

### H-01 — Navegação global
**Como** visitante, **quero** uma barra de navegação fixa com links para as seções, **para** acessar qualquer parte da página sem perder contexto.

**Critérios de aceitação:**
- [ ] Logo `CODE.HOUSE` em monospace à esquerda, link ancora ao topo
- [ ] Links: Serviços / Processo / Exemplos / "Falar com a gente" (CTA estilizado)
- [ ] Barra sticky (fixa no scroll), fundo da paleta com `border-bottom` sutil
- [ ] CTA da nav com borda azul nuvem; ao hover: preenchimento sólido
- [ ] Em mobile (< 900px): links ocultos, somente logo + CTA
- [ ] Focus visível em todos os itens (acessibilidade teclado)
- [ ] Não sobrepõe conteúdo (z-index correto)

---

### H-02 — Hero — mensagem principal
**Como** visitante que chegou pela primeira vez, **quero** entender em 5 segundos o que a Code House faz e para quem, **para** decidir se vale continuar lendo.

**Critérios de aceitação:**
- [ ] Layout em duas colunas: texto à esquerda, mockup de app à direita
- [ ] Eyebrow em monospace uppercase: "Soluções Personalizadas em TI"
- [ ] Headline principal: "Sistemas feitos para o *seu* jeito de trabalhar." (palavra "seu" em azul nuvem)
- [ ] Subtítulo (1 parágrafo): menciona CRM, ERP, lojas virtuais e sites; reforça personalização vs template genérico
- [ ] Dois botões: "Falar com a gente" (sólido) + "Ver exemplos" (outline)
- [ ] Fade-in suave no mockup ao carregar (respeitar `prefers-reduced-motion`)
- [ ] Em mobile: mockup aparece acima do texto ou abaixo (definir na implementação), layout em coluna única

---

### H-03 — Hero mockup — CRM interativo
**Como** visitante, **quero** ver um preview visual de como um sistema CRM parece, **para** ter concretamente a sensação de qualidade antes de ler mais.

**Critérios de aceitação:**
- [ ] "Janela de app" com barra de título (dots coloridos + label "CRM — Clientes")
- [ ] Sidebar com itens: Clientes (ativo), Negócios, Tarefas, Relatórios, Config
- [ ] Item ativo com destaque em azul nuvem + borda lateral
- [ ] Área de conteúdo com:
  - [ ] Header "Clientes ativos" + badge "42 registros"
  - [ ] Grid de 3 stat cards: Total 42 / Novos 7 / Taxa 94%
  - [ ] Tabela com 4 linhas: Nome / Empresa / Status (tags "Ativo" verde-água / "Proposta" azul)
- [ ] Mockup responde ao dark/light mode com as variáveis de token
- [ ] Não é clicável — é decorativo/demonstrativo

---

### H-04 — Seção de serviços
**Como** visitante, **quero** ver a lista de soluções que a Code House oferece com uma descrição curta de cada uma, **para** identificar se têm o que eu preciso.

**Critérios de aceitação:**
- [ ] Eyebrow monospace: "// serviços"
- [ ] Título H2: "O que a Code House entrega"
- [ ] Grid horizontal com 5 colunas separadas por `border` (sem shadow, sem border-radius além de 2px)
- [ ] Cada card: ícone SVG próprio + nome em monospace uppercase + descrição curta
- [ ] Serviços:
  1. **CRM** — "Gestão de clientes, funil de vendas e histórico de relacionamento."
  2. **ERP** — "Controle integrado de estoque, financeiro, compras e operações."
  3. **Site Institucional** — "Presença digital com identidade visual e conteúdo da sua empresa."
  4. **E-shop** — "Loja virtual com catálogo, pagamentos e gestão de pedidos."
  5. **Sob Medida** — "Qualquer solução de TI adaptada ao seu processo, do zero."
- [ ] Hover sutil: fundo do card muda para `--surface`
- [ ] Em mobile < 900px: grid 2 colunas. Em < 600px: 1 coluna

---

### H-05 — Seção de processo
**Como** visitante, **quero** entender como funciona o processo de trabalho da Code House, **para** saber o que esperar ao contratar.

**Critérios de aceitação:**
- [ ] Eyebrow monospace: "// como funciona"
- [ ] Título H2: "Do problema à solução em três etapas"
- [ ] Grid de 3 colunas separadas por `border` (mesmo padrão dos serviços)
- [ ] Cada etapa: número em monospace faint ("Etapa 01", "Etapa 02", "Etapa 03") + título + parágrafo
- [ ] Etapas:
  1. **Entendemos seu negócio** — conversamos sobre fluxo, gargalos e o que automatizar
  2. **Construímos a solução** — sistema personalizado com a linguagem e regras do cliente
  3. **Acompanhamos o crescimento** — suporte contínuo e melhorias conforme o negócio evolui
- [ ] Sem numeração visual ornamental (só o texto "Etapa 0X" — a ordem é informação, não decoração)
- [ ] Em mobile: colunas em linha vertical, separadas por `border-bottom`

---

### H-06 — Seção de exemplos de sistemas
**Como** visitante, **quero** ver exemplos visuais dos sistemas que a Code House constrói, **para** ter confiança na qualidade antes de entrar em contato.

**Critérios de aceitação:**
- [ ] Eyebrow monospace: "// exemplos de sistemas"
- [ ] Título H2: "O que sistemas feitos assim parecem"
- [ ] Grid 2×2 com 4 cards de exemplo
- [ ] Cada card: header (nome do sistema + badge "Personalizado" ou "Sob medida") + área de preview com mockup CSS
- [ ] **Card 1 — CRM Funil de vendas:** tabela com colunas Cliente / Etapa / Valor / Status
- [ ] **Card 2 — ERP Painel operacional:** gráfico de barras CSS (6 meses) + row de 3 stat cards (Estoque / Pedidos / Saldo)
- [ ] **Card 3 — E-shop Catálogo:** grid 3×2 de mini cards de produto (imagem placeholder em gradiente + nome + preço)
- [ ] **Card 4 — Site institucional:** mini mockup com navbar escura + bloco hero + linhas de conteúdo + botões CTA
- [ ] Todos os mockups usam variáveis CSS de token (funcionam em dark/light mode)
- [ ] Nenhum mockup é clicável
- [ ] Em mobile: grid 1 coluna

---

### H-07 — Formulário de contato
**Como** visitante interessado, **quero** enviar uma mensagem diretamente pela landing page, **para** iniciar o contato sem sair do site.

**Critérios de aceitação:**
- [ ] Seção com fundo `--surface` (diferencia do restante da página)
- [ ] Layout 2 colunas: copy à esquerda + formulário à direita
- [ ] Copy à esquerda:
  - [ ] Eyebrow: "Vamos conversar"
  - [ ] Headline: "Seu sistema ainda não existe. A gente constrói."
  - [ ] Subtítulo: reforça personalização, convida a descrever o negócio
- [ ] Campos do formulário: Nome / Empresa / "O que você precisa?" (textarea)
- [ ] Labels em monospace uppercase acima dos campos
- [ ] Inputs com `border` sutil; `border-color: --cloud` ao focus
- [ ] Botão "Enviar mensagem" (sólido, azul nuvem)
- [ ] Formulário **não tem backend ainda** — submit exibe mensagem inline "Mensagem recebida! Em breve entraremos em contato." sem recarregar a página
- [ ] Validação mínima: campos Nome e Mensagem não podem estar vazios
- [ ] Em mobile: layout em coluna única

---

### H-08 — Footer
**Como** visitante, **quero** um rodapé com links de navegação e identificação da marca, **para** ter referência ao final da página.

**Critérios de aceitação:**
- [ ] `border-top` sutil separando do conteúdo
- [ ] Esquerda: "© 2026 Code House — Soluções em TI" em monospace faint uppercase
- [ ] Direita: links Serviços / Processo / Contato
- [ ] Em mobile: coluna única centralizada

---

### H-09 — Dark mode e Light mode
**Como** visitante, **quero** que a página respeite minha preferência de tema do sistema operacional e do toggle da aplicação, **para** ter conforto visual independente do ambiente.

**Critérios de aceitação:**
- [ ] Sistema de tokens CSS com variáveis em `:root` para light mode
- [ ] Override via `@media (prefers-color-scheme: dark)` para dark mode
- [ ] Override via `:root[data-theme="dark"]` e `:root[data-theme="light"]` para toggle manual
- [ ] Dark mode não é inversão ingênua — cores revisadas para contraste legível e accent funcionando
- [ ] Mockups CSS usam variáveis e funcionam em ambos os temas
- [ ] Nenhum elemento usa cor hardcoded fora dos tokens (exceto tags de status)

---

### H-10 — Responsividade
**Como** visitante mobile, **quero** que a página seja utilizável em qualquer tamanho de tela, **para** não precisar dar zoom ou scrollar horizontalmente.

**Critérios de aceitação:**
- [ ] Breakpoint principal: 900px (colapsa grids de 2+ colunas)
- [ ] Breakpoint secundário: 600px (colapsa grid de serviços para 1 coluna)
- [ ] Hero: coluna única em mobile, mockup aparece acima ou abaixo do texto
- [ ] Nav: links ocultos em mobile
- [ ] Nenhum elemento causa scroll horizontal no body
- [ ] Wide content (tabelas, mockups) com `overflow-x: auto` no container
- [ ] Botões e inputs têm tamanho de toque adequado (min 44px de altura)
- [ ] Testado em: 375px (iPhone SE), 768px (tablet), 1280px (desktop)

---

### H-11 — Acessibilidade e performance
**Como** visitante com necessidades específicas, **quero** que a página seja acessível e rápida, **para** ter boa experiência independente do dispositivo ou condição.

**Critérios de aceitação:**
- [ ] Focus visível em todos os elementos interativos (nav, botões, inputs, links)
- [ ] `prefers-reduced-motion`: animações de fade-in desabilitadas quando ativo
- [ ] Contraste de texto: mínimo 4.5:1 para texto normal, 3:1 para texto grande (WCAG AA)
- [ ] Imagens e SVGs com atributos `aria` quando necessário
- [ ] Scroll suave (`scroll-behavior: smooth`) apenas quando motion não reduzido
- [ ] Página carrega sem JS funcional (formulário pode degradar para mailto link)
- [ ] Sem fontes externas (CDN bloqueado no Artifact CSP) — usar system fonts

---

### H-12 — SEO e meta
**Como** dono da Code House, **quero** que a página tenha meta tags básicas, **para** que o Google indexe corretamente.

**Critérios de aceitação:**
- [ ] `<title>`: "Code House — Soluções Personalizadas em TI"
- [ ] `<meta name="description">`: até 160 caracteres descrevendo CRM, ERP, e-shop, site institucional para pequenas empresas
- [ ] `<meta name="viewport" content="width=device-width, initial-scale=1">`
- [ ] `<meta charset="utf-8">`
- [ ] `<meta property="og:title">` e `<meta property="og:description">` para compartilhamento
- [ ] `<html lang="pt-BR">`
- [ ] H1 único, hierarquia de headings correta (H1 → H2 → H3)

---

### H-13 — Deploy no Render
**Como** dono da Code House, **quero** a landing page publicada no Render, **para** ter URL pública e estável.

**Critérios de aceitação:**
- [ ] Projeto configurado como **Static Site** no Render
- [ ] `index.html` na raiz do repositório
- [ ] Build command: vazio (sem build step — HTML puro)
- [ ] Publish directory: `.` (raiz)
- [ ] Auto-deploy ativo na branch `main`
- [ ] URL customizada configurada (se domínio disponível)
- [ ] HTTPS ativo (padrão Render)
- [ ] `_redirects` ou `render.yaml` opcional para SPA (não necessário aqui)

---

## Critérios de rejeição (bloqueia ship)

- P0: página quebra ou não carrega
- P0: scroll horizontal no body em qualquer breakpoint
- P0: formulário envia dados para lugar errado
- P1: dark mode com contraste ilegível
- P1: nav links não funcionam (âncoras quebradas)
- P1: mockups quebram visualmente em mobile

---

## Fora de escopo (v1)

- Backend real para o formulário (email/webhook)
- Blog ou área de cases
- Multi-idioma
- Animações pesadas (Three.js, GSAP)
- Sistema de CMS
- Analytics (pode ser adicionado na v2 com Plausible ou similar)

---

## Ordem de implementação sugerida

1. Estrutura HTML + sistema de tokens CSS
2. Nav + Hero (texto)
3. Hero mockup CRM
4. Seção de serviços
5. Seção de processo
6. Seção de exemplos (4 mockups)
7. Formulário de contato
8. Footer
9. Dark mode completo
10. Responsividade
11. Meta tags + SEO
12. Deploy Render
