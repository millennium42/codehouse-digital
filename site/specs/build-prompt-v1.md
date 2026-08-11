# Prompt de Execução — Code House Landing Page v1
## Cole este prompt inteiro no início de uma nova sessão para executar o build

---

Você é um engenheiro executando o **build da landing page da Code House** seguindo o Ralph Loop. Leia tudo antes de escrever qualquer código.

---

## Contexto do projeto

**Empresa:** Code House — soluções de TI personalizadas para pequenas empresas.
**Produto a construir:** Landing page estática em HTML/CSS/JS puro.
**Deploy:** Render (static site).
**Repositório:** criar em GitHub como `codehouse-landing` com branch `main`.

**O que a Code House faz:**
Desenvolve CRM, ERP, sites institucionais, e-shops e soluções sob medida, adaptados ao fluxo real de cada cliente — não impõe templates. A marca fala por si: sem foto de fundador. O que convence é a identidade visual e exemplos de sistemas que a empresa pode construir.

**Design system:**
- Estilo: minimalista brutalista leve — bordas retas (border-radius 2px), sem shadows excessivas, sem cards flutuantes, sem border-radius grande.
- Paleta azul nuvem — tranquilidade, humanidade, técnico sem frieza.
- Tipografia: `Courier New` para labels/eyebrows/monospace; `system-ui` para corpo.
- Sensação: "faz o que você precisa, sem enrolação."

**Personas:**
- **Pedro** — dono de loja física, nunca contratou sistema.
- **Marina** — gerente de PME, já usou ERP engessado.
- **Thiago** — gestor de e-commerce pequeno.

---

## Regras que governam este build (não negociáveis)

### Escopo
- Implemente **exatamente** o que está descrito em cada história. Nem mais, nem menos.
- **Proibido:** adicionar feature não especificada, refatorar código não relacionado, inventar requisito.
- Se identificar algo importante fora do escopo: registre como comentário `// TODO: [descrição]` e continue.

### Qualidade
- Nomes descritivos — sem comentário para O QUÊ, só para o PORQUÊ não-óbvio.
- Sem `console.log`, `debugger` ou código de teste nos commits.
- Outputs de dados do usuário via `textContent` — nunca `innerHTML` (XSS).
- Sem cor hardcoded fora das variáveis CSS de token.

### Progresso
- Ao iniciar cada história: "**▶ Iniciando H-XX — [título]**"
- Ao concluir: "**✓ H-XX concluída.** Implementado: [lista]. Desvios: [nenhum ou lista]."
- Marque critérios atendidos com `[x]` no arquivo de spec se tiver acesso.

### Commits
- Um commit por história. Mensagem: `feat(H-XX): [por quê a mudança]`
- Todo commit deixa o projeto em estado que roda.
- Nunca commite `.env`, credenciais, ou número real de WhatsApp no histórico.

### Perguntas
- Ambiguidade = pergunta antes de assumir.
- Se uma dependência técnica falhar, diga imediatamente em vez de construir um substituto silencioso.

---

## Tokens CSS — paleta obrigatória

```css
:root {
  --bg:             #F0F4F8;
  --surface:        #E2EBF4;
  --surface-raised: #FAFCFE;
  --cloud:          #3E82AB;
  --cloud-hover:    #2E6E95;
  --cloud-light:    #6AAFD6;
  --cloud-faint:    #C0D8EC;
  --ink:            #17232E;
  --ink-muted:      #4A6275;
  --ink-faint:      #7A9AAF;
  --border:         #B4CCE0;
  --border-strong:  #7AADC8;
  --font-sans: system-ui, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif;
  --font-mono: 'Courier New', 'Courier', monospace;
}

/* Dark mode — redefinir apenas os tokens */
@media (prefers-color-scheme: dark) { :root {
  --bg:             #0C141D;
  --surface:        #13202E;
  --surface-raised: #192B3C;
  --cloud:          #5898C0;
  --cloud-hover:    #6AAFD6;
  --cloud-faint:    #1C3A52;
  --ink:            #D8E8F4;
  --ink-muted:      #7A9AB4;
  --ink-faint:      #4A6880;
  --border:         #1E3A52;
  --border-strong:  #2E567A;
}}

:root[data-theme="dark"]  { /* mesmos valores do dark acima */ }
:root[data-theme="light"] { /* mesmos valores do light acima */ }
```

---

## Histórias — execute nesta ordem exata

---

### H-00 — Design system e tokens CSS
**Antes de qualquer HTML:** crie `index.html` com apenas `<head>` e `<style>` definindo os tokens, reset e base.

- [ ] Todas as variáveis CSS conforme paleta acima
- [ ] Reset: `*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }`
- [ ] Base: `html { scroll-behavior: smooth; font-size: 16px; }` + `body { background: var(--bg); color: var(--ink); font-family: var(--font-sans); }`
- [ ] Arquivo CSS organizado: tokens → reset → base → componentes reutilizáveis → layout → responsividade
- [ ] Border-radius: 2px (brutalista)
- [ ] Nenhuma cor hardcoded fora dos tokens

**Commit:** `feat(H-00): design system e tokens CSS`

---

### H-15 — Favicon e `<head>` de assets
Ainda no `<head>`, antes de qualquer conteúdo:

- [ ] Favicon SVG inline como `data:` URI — fundo `#3E82AB` + "C" branco em monospace
- [ ] `<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,...">`
- [ ] `<meta name="theme-color" content="#3E82AB">`
- [ ] `og-image.png` criado: 1200×630, fundo azul nuvem, "CODE.HOUSE" em branco — commitado na raiz
- [ ] `<link rel="apple-touch-icon" href="/og-image.png">` (placeholder aceitável)

**Commit:** `feat(H-15): favicon e assets base`

---

### H-12 — SEO e metadados
Completar o `<head>`:

- [ ] `<meta charset="utf-8">`
- [ ] `<meta name="viewport" content="width=device-width, initial-scale=1">`
- [ ] `<html lang="pt-BR">`
- [ ] `<title>Code House — Soluções Personalizadas em TI para Pequenas Empresas</title>`
- [ ] `<meta name="description">` — até 160 chars, menciona CRM, ERP, e-shop, personalizado
- [ ] `<link rel="canonical" href="PLACEHOLDER_URL">` — substituir em H-20
- [ ] Open Graph: `og:type`, `og:title`, `og:description`, `og:url`, `og:image` (caminho `/og-image.png`), `og:locale` (`pt_BR`), `og:site_name`
- [ ] Twitter Card: `twitter:card` (`summary_large_image`), `twitter:title`, `twitter:description`, `twitter:image`
- [ ] JSON-LD `LocalBusiness` no `<head>`:
  ```html
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"LocalBusiness","name":"Code House",
  "description":"Soluções de TI personalizadas para pequenas empresas","url":"PLACEHOLDER_URL",
  "serviceType":["CRM","ERP","E-commerce","Site Institucional"]}
  </script>
  ```
- [ ] `robots.txt` na raiz: `User-agent: *\nAllow: /`
- [ ] `sitemap.xml` na raiz com a URL canônica
- [ ] Script anti-flash do tema (inline no `<head>`, antes do CSS):
  ```html
  <script>
    (function(){var t=localStorage.getItem('ch-theme');
    if(t)document.documentElement.setAttribute('data-theme',t);})();
  </script>
  ```

**Commit:** `feat(H-12): SEO, metadados e anti-flash de tema`

---

### H-01 — Navegação global + H-09 Dark/Light toggle
Nav e tema juntos (o toggle é parte da nav):

- [ ] `<nav>` sticky (`position: sticky; top: 0; z-index: 100`) com `border-bottom: 1px solid var(--border)`
- [ ] Logo `CODE<span style="color:var(--cloud)">.</span>HOUSE` em monospace — ancora ao topo
- [ ] Links: Serviços (`#servicos`) / Processo (`#processo`) / Exemplos (`#exemplos`) / "Falar com a gente" (`#contato`)
- [ ] "Falar com a gente": `border: 1px solid var(--cloud); border-radius: 2px` — hover: background azul, texto fundo
- [ ] Toggle de tema: botão com ícone SVG sol (light) / lua (dark); `aria-label="Alternar tema"`
- [ ] Toggle JS: `document.documentElement.setAttribute('data-theme', novoTema); localStorage.setItem('ch-theme', novoTema);`
- [ ] Mobile (< 900px): links ocultos, somente logo + "Falar com a gente" + toggle
- [ ] Focus visível em todos os itens
- [ ] Dark mode tokens já funcionando por H-00

**Commit:** `feat(H-01 H-09): nav sticky com toggle de dark/light mode`

---

### H-02 — Hero — mensagem principal

- [ ] `<section class="hero">` — grid 2 colunas (texto 1.1fr / mockup 0.9fr)
- [ ] Eyebrow: `<p class="eyebrow">` — monospace uppercase, cor `--cloud`, com traço horizontal antes
- [ ] `<h1>` — "Sistemas feitos para o <span>seu</span> jeito de trabalhar." — "seu" em `--cloud`
- [ ] H1 único em toda a página
- [ ] Subtítulo: menciona CRM, ERP, lojas virtuais, sites; reforça personalização
- [ ] Dois botões: "Falar com a gente" (`#contato`, sólido) + "Ver exemplos" (`#exemplos`, outline)
- [ ] Mobile: coluna única, mockup acima do texto
- [ ] `padding-top` calculado para não sobrepor a nav sticky

**Commit:** `feat(H-02): hero com headline e CTAs`

---

### H-03 — Hero mockup CRM
Mockup CSS dentro da coluna direita do hero — `aria-hidden="true"`:

- [ ] `.app-window` com `border: 1px solid var(--border); border-radius: 4px; overflow: hidden`
- [ ] Barra de título: dots (vermelho/amarelo/verde) + label "CRM — Clientes"
- [ ] Sidebar: 5 itens, item "Clientes" ativo (`background: var(--cloud-faint); border-left: 2px solid var(--cloud)`)
- [ ] Área de conteúdo: header + 3 stat cards (Total 42/Novos 7/Taxa 94%) + tabela 4 linhas
- [ ] Tags de status: "Ativo" verde-água / "Proposta" azul — `background` semitransparente
- [ ] Tudo em variáveis de token — funciona em dark e light
- [ ] Mobile: mockup se ajusta à largura sem overflow horizontal
- [ ] Fade-in ao carregar: `@media (prefers-reduced-motion: no-preference) { .fade { opacity: 0; transition: opacity 0.5s; } .fade.in { opacity: 1; } }` + IntersectionObserver

**Commit:** `feat(H-03): mockup CRM no hero`

---

### H-04 — Seção de serviços
`id="servicos"`:

- [ ] Eyebrow `// serviços` + H2 "O que a Code House entrega"
- [ ] Grid 5 colunas com `border: 1px solid var(--border)` separando cada card (sem shadow)
- [ ] 5 cards com ícone SVG inline (stroke `currentColor`, 16×16) + nome monospace uppercase + descrição
- [ ] Hover: `background: var(--surface)`
- [ ] Mobile < 900px: 2 colunas. Mobile < 600px: 1 coluna

**Commit:** `feat(H-04): seção de serviços`

---

### H-05 — Seção de processo
`id="processo"`:

- [ ] Eyebrow `// como funciona` + H2 "Do problema à solução em três etapas"
- [ ] Grid 3 colunas com border — mesmo padrão dos serviços
- [ ] Cada etapa: `<p class="step-num">Etapa 01</p>` + H3 + parágrafo
- [ ] Mobile: 1 coluna com `border-bottom` entre etapas

**Commit:** `feat(H-05): seção de processo`

---

### H-16 — Seção de credibilidade
Entre processo e exemplos:

- [ ] Grid 3–4 itens horizontais: diferencial + texto curto
- [ ] Conteúdo: apenas fatos verdadeiros. Sugestões se não houver dados reais:
  - "Cada sistema é único. Sem templates."
  - "Adaptamos ao seu fluxo, não o contrário."
  - "Acompanhamos após o lançamento."
- [ ] **Regra absoluta:** nada inverídico. Em dúvida, omitir.

**Commit:** `feat(H-16): seção de credibilidade`

---

### H-06 — Seção de exemplos
`id="exemplos"`:

- [ ] Eyebrow + H2 + grid 2×2 de cards
- [ ] Card 1 (CRM funil): tabela com 5 linhas de dados fictícios brasileiros, tags de status
- [ ] Card 2 (ERP painel): gráfico de barras CSS 6 meses + 3 stat cards
- [ ] Card 3 (E-shop): grid 3×2 de mini produtos com gradiente + preço monospace
- [ ] Card 4 (Site): mini navbar escura + hero block + linhas de conteúdo + botões
- [ ] Tudo `aria-hidden="true"`, tudo em tokens CSS
- [ ] Mobile: 1 coluna

**Commit:** `feat(H-06): exemplos de sistemas com mockups CSS`

---

### H-07 — Seção de contato
`id="contato"`:

- [ ] Fundo `var(--surface)` — diferenciação visual
- [ ] 2 colunas (desktop): copy + formulário
- [ ] Copy: eyebrow "Vamos conversar" + H2 "Seu sistema ainda não existe. A gente constrói." + subtítulo + link WhatsApp
- [ ] Link WhatsApp: `href="https://wa.me/5500000000000"` (PLACEHOLDER) + `target="_blank" rel="noopener noreferrer"`
- [ ] Formulário: Nome (obrigatório) / Empresa (opcional) / "O que você precisa?" textarea (obrigatório)
- [ ] Labels monospace uppercase com `<label for="...">` explícito
- [ ] Focus: `border-color: var(--cloud)`
- [ ] Validação: erro inline abaixo do campo, mensagem humana
- [ ] Submit: simula 800ms de loading → exibe mensagem de sucesso (formulário some)
- [ ] NUNCA usar `innerHTML` com dados do usuário — usar `textContent`
- [ ] Mobile: coluna única

**Commit:** `feat(H-07): seção de contato com formulário`

---

### H-14 — CTA flutuante WhatsApp

- [ ] `position: fixed; bottom: 1.5rem; right: 1.5rem; z-index: 90`
- [ ] `width: 52px; height: 52px; border-radius: 50%; background: #25D366`
- [ ] Ícone SVG WhatsApp branco inline
- [ ] `href="https://wa.me/5500000000000"` (PLACEHOLDER) + `target="_blank" rel="noopener noreferrer"`
- [ ] `aria-label="Conversar pelo WhatsApp"`
- [ ] Tooltip CSS ao hover: "Falar pelo WhatsApp"
- [ ] Não cobre conteúdo crítico em mobile — verificar em 375px

**Commit:** `feat(H-14): botão flutuante WhatsApp`

---

### H-08 — Footer

- [ ] `border-top: 1px solid var(--border)`
- [ ] Esquerda: logo + tagline + link WhatsApp + email (placeholder)
- [ ] Direita: links Serviços / Processo / Exemplos / Contato (monospace uppercase faint)
- [ ] Linha final: "© 2026 Code House — Soluções em TI"
- [ ] Mobile: coluna única

**Commit:** `feat(H-08): footer`

---

### H-17 — Página 404

- [ ] `404.html` na raiz — mesmo design system (CSS inline)
- [ ] Logo + mensagem + botão "Voltar para o início"
- [ ] Mensagem: "Esta página não existe. Mas a solução que você precisa, a gente constrói."
- [ ] `<title>`: "Página não encontrada — Code House"

**Commit:** `feat(H-17): página 404`

---

### H-10 — Revisão de responsividade end-to-end
Não é nova feature — é verificação manual de tudo junto:

- [ ] Testar em 375px portrait: sem overflow horizontal
- [ ] Testar em 375px landscape: sem overflow horizontal
- [ ] Testar em 768px: grids colapsam corretamente
- [ ] Testar em 1280px: layout desktop completo
- [ ] Todos os botões/inputs: min-height 44px
- [ ] Texto: nunca menor que 14px em mobile
- [ ] Corrigir qualquer overflow ou layout quebrado encontrado

**Commit:** `fix(H-10): ajustes de responsividade end-to-end`

---

### H-11 — Revisão de acessibilidade end-to-end

- [ ] Focus visível em todo elemento interativo (rodar Tab pela página)
- [ ] `prefers-reduced-motion`: desativar no SO, confirmar que animações param
- [ ] Contraste: verificar texto/fundo em light e dark com ferramenta (Chrome DevTools Accessibility)
- [ ] SVGs decorativos: confirmar `aria-hidden="true"` em todos
- [ ] Toggle de tema: confirmar `aria-label`
- [ ] Formulário: confirmar `<label for>` em cada input
- [ ] Headings: H1 único, H2 por seção, H3 dentro de seção — sem saltos
- [ ] Corrigir qualquer violação encontrada

**Commit:** `fix(H-11): ajustes de acessibilidade end-to-end`

---

### H-18 — Auditoria Lighthouse

- [ ] Abrir Chrome DevTools → Lighthouse → Mobile
- [ ] Gerar relatório: Performance, Accessibility, Best Practices, SEO
- [ ] Targets: todos ≥ 90
- [ ] Corrigir tudo que estiver abaixo do target antes de continuar
- [ ] Registrar scores finais em comentário no commit

**Commit:** `fix(H-18): correções pós-auditoria Lighthouse — scores: P[X] A[X] BP[X] SEO[X]`

---

### H-19 — Setup do repositório Git

- [ ] `.gitignore`: `.DS_Store`, `node_modules/`, `*.log`, `.env`
- [ ] `README.md`: descrição, stack, como rodar, como fazer deploy no Render
- [ ] `render.yaml`:
  ```yaml
  services:
    - type: web
      name: codehouse-landing
      env: static
      staticPublishPath: .
      buildCommand: ""
      routes:
        - type: rewrite
          source: /404
          destination: /404.html
  ```
- [ ] `_headers`:
  ```
  /*
    X-Frame-Options: DENY
    X-Content-Type-Options: nosniff
    Referrer-Policy: strict-origin-when-cross-origin
    Cache-Control: public, max-age=3600
  /index.html
    Cache-Control: no-cache
  ```
- [ ] Push para GitHub no repositório `codehouse-landing`, branch `main`

**Commit:** `chore(H-19): setup repositório, render.yaml e headers`

---

### H-13 — Deploy no Render

- [ ] Criar Static Site no Render apontando para o repositório GitHub
- [ ] Branch: `main`
- [ ] Build command: vazio
- [ ] Publish directory: `.`
- [ ] Auto-deploy: ativo
- [ ] Após o deploy: verificar HTTPS, verificar `/404` redireciona para `404.html`
- [ ] Health check: URL raiz retorna 200

**Este passo é manual — executado pelo dono da conta Render.**

---

### H-20 — Substituição de placeholders antes do deploy público

- [ ] Buscar por `5500000000000` — substituir pelo número real em todos os arquivos
- [ ] Buscar por `PLACEHOLDER_URL` — substituir pela URL real do Render
- [ ] Atualizar `<link rel="canonical">`, OG `og:url`, JSON-LD `url`, `sitemap.xml`
- [ ] Email placeholder no footer → email real
- [ ] Rodar Lighthouse uma última vez após substituições
- [ ] Confirmar que nenhum dado sensível foi commitado no histórico Git

**Commit:** `chore(H-20): substituir placeholders pré-deploy`

---

## Definition of Done — checklist universal

Toda história só está concluída quando:

- [ ] Todos os critérios de aceitação da história estão implementados
- [ ] Nenhum critério de rejeição P0 ou P1 foi ativado
- [ ] O projeto ainda roda após o commit desta história
- [ ] Nenhuma feature fora do spec foi adicionada
- [ ] Sem `console.log`, `debugger` ou código de teste no commit
- [ ] Sem cor hardcoded fora dos tokens
- [ ] Nenhum `innerHTML` com dados do usuário
- [ ] Commit feito com mensagem descrevendo o PORQUÊ

---

## Critérios de rejeição — o que bloqueia o ship

### P0 (nunca fazer ship com estes)
- Página não carrega
- Scroll horizontal no body em qualquer breakpoint
- H1 ausente ou duplicado
- Âncora da nav aponta para `id` que não existe
- `innerHTML` com dados do usuário (XSS)
- Cor hardcoded em elemento visível (quebra dark mode)
- `render.yaml` ausente

### P1 (nunca fazer ship com estes)
- Dark mode com contraste < 4.5:1 em texto normal
- Flash de tema no reload
- Formulário submete campos obrigatórios vazios sem feedback
- Mockup causa overflow em mobile
- `prefers-reduced-motion` ignorado
- Lighthouse Performance < 90 em mobile
- Focus ausente em elemento interativo
- SVG decorativo sem `aria-hidden`
- OG image ausente

---

## Ao concluir o build completo

Declare: **"Build v1 concluído. Histórias implementadas: [lista]. Desvios: [lista ou 'nenhum']. Pronto para /review."**

O /review deve ser feito por uma perspectiva independente (novo agente ou peer) comparando cada critério de aceitação com o que foi construído. Não faça ship sem o /review aprovado.
