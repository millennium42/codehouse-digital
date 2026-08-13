# Correções Técnicas v6 — Site Code House

> Ralph Loop: correção dos problemas técnicos encontrados na revisão.
> Data: 2026-08-13
> Spec base: `specs/landing-honesta-v6.md` (histórias H-V6-01 a H-V6-10)

---

## C01 — Extrair CSS inline para `css/styles.css`

**Tipo:** Refatoração
**Prioridade:** P1 (manutenibilidade, cache)

**Como** desenvolvedor que precisa manter o site, **quero** que o CSS viva em arquivo separado carregado via `<link>`, **para** que o navegador faça cache e a revisão seja simples.

#### Critérios
- [ ] Todo CSS inline de `<style>` em `index.html` é movido para `css/styles.css`
- [ ] `index.html` carrega `css/styles.css` via `<link rel="stylesheet" href="css/styles.css">`
- [ ] Nenhuma regra visual muda (screenshot comparison ou inspeção manual)
- [ ] O `<style>` block no `<head>` fica vazio ou é removido

#### Teste/Verificação
- Abrir `index.html` no navegador → visual idêntico ao antes
- DevTools Network → `css/styles.css` carregado com status 200

---

## C02 — Deduplicar tokens CSS

**Tipo:** Refatoração
**Prioridade:** P1 (consistência visual)

**Como** desenvolvedor, **quero** que exista uma única fonte de verdade para as variáveis de tema, **para** que dark/light mode funcione sem surpresas.

#### Critérios
- [ ] `:root` define tokens base (fontes, espaçamentos, raios)
- [ ] `[data-theme="dark"]` define apenas cores do dark mode
- [ ] `[data-theme="light"]` define apenas cores do light mode
- [ ] Não há mais de 3 definições de `--bg`, `--ink`, `--cloud`, etc.
- [ ] Toggle de tema funciona corretamente em ambos os modos

#### Teste/Verificação
- `grep -c "\-\-bg:" css/styles.css` → retorna 1
- Toggle dark/light no navegador → transição suave, sem flash

---

## C03 — Implementar accordion FAQ

**Tipo:** Feature
**Prioridade:** P2 (UX, conteúdo oculto)

**Como** visitante no FAQ, **quero** clicar numa pergunta para expandir/colapsar a resposta, **para** ler apenas o que me interessa sem scroll excessivo.

#### Critérios
- [ ] Cada pergunta é clicável (cursor: pointer, hover state)
- [ ] Clique toggle: `.faq-a` ganha classe `hidden` ou a pera
- [ ] Ícone do botão muda (rotação ou +/-) indicando estado
- [ ] Animação suave de expandir/colapsar (transition ou JS)
- [ ] Acessível: `aria-expanded` reflete estado, `aria-controls` aponta para o alvo

#### Teste/Verificação
- Abrir FAQ → todas respostas escondidas
- Clicar pergunta 1 → abre, clicar novamente → fecha
- Clicar pergunta 2 → pergunta 1 fecha (acordeão)

---

## C04 — Conectar formulário de contato

**Tipo:** Feature
**Prioridade:** P0 (conversão, lead)

**Como** visitante interessado, **quero** enviar minha mensagem pelo formulário, **para** que o Pablo receba e eu tenha confirmação de envio.

#### Critérios
- [ ] Formulário envia dados para endpoint (Formspree, Netlify Forms, ou webhook custom)
- [ ] Validação client-side permanece (nome e necessidade obrigatórios)
- [ ] Feedback visual de envio (loading → sucesso/erro)
- [ ] Mensagem de sucesso exibe nome do usuário (sem XSS)
- [ ] Sem alteração visual significativa no formulário

#### Teste/Verificação
- Preencher nome + necessidade → submit → mensagem de sucesso aparece
- Submeter vazio → erros de validação aparecem
- DevTools Network → request POST com payload correto

---

## C05 — Limpar arquivos de build e seções fantasma

**Tipo:** Housekeeping
**Prioridade:** P2 (organização do repo)

**Como** desenvolvedor, **quero** que o repositório contenha apenas arquivos de produção e spec, **para** não confundir quem clona ou revisa.

#### Critérios
- [ ] Scripts Python de build/patch movidos para `.build/` ou deletados
- [ ] Backups HTML (`index-redesign.html`, `index-v4-backup.html`, `_servido.html`) movidos para `.build/` ou deletados
- [ ] Screenshots movidas para `.build/screenshots/`
- [ ] Comentários órfãos `<!-- ========== STACK ========== -->` removidos de `index.html`
- [ ] `css/` morto deletado se C01 extrair tudo para `styles.css` (ou reestruturado)

#### Teste/Verificação
- `ls site/` → apenas: `index.html`, `css/`, `specs/`, `robots.txt`, `sitemap.xml`, `render.yaml`, `favicon.svg`, `og-image.png`, `politica-privacidade.html`
- `git status` → limpo após mover/deletar

---

## C06 — Remover número WhatsApp hardcoded (feature flag simples)

**Tipo:** Config
**Prioridade:** P3 (manutenibilidade)

**Como** administrador do site, **quero** que o número do WhatsApp esteja em um único lugar (constante JS ou data-attribute), **para** atualizar sem buscar em múltiplas linhas.

#### Critérios
- [ ] Número do WhatsApp (`55559991441700`) aparece em exatamente 1 lugar (constante JS no `<script>` ou `data-whatsapp` no HTML)
- [ ] Todos os links `wa.me/...` leem da constante
- [ ] Botão de contato e flutuante usam a mesma fonte

#### Teste/Verificação
- `grep -rn "55559991441700" index.html` → retorna 1 (a constante)
- Ambos os botões abrem o mesmo número no WhatsApp

---

## Ordem de execução

1. **C05** (limpar) — reduz ruído antes de codar
2. **C01** (extrair CSS) — base para C02
3. **C02** (deduplicar tokens) — depende de C01
4. **C03** (accordion FAQ) — independente
5. **C04** (formulário) — independente
6. **C06** (whatsapp hardcoded) — independente, pode ser último

## Definição de concluído

Todas as histórias com checkboxes marcadas + commit por história + smoke test no navegador.
