# Code House — Landing Page Honesta v6
## Spec para Ralph Loop — empresa nova, 1 pessoa, 1 cliente

**Objetivo:** Landing page premium que venda desenvolvimento de sistemas sob medida para pequenas empresas, sem inventar números, depoimentos ou dados. Demonstra capacidade pela qualidade do site, clareza do processo e stack real.

**Dados reais (confirmados):**
- Email: codehouse42@gmail.com
- CNPJ: 68.489.569/0001-04
- WhatsApp: (número real do dono — manter que já está no index-redesign se for o mesmo, senão perguntar)

**Empresa:** 1 pessoa (o dono), 1 cliente atual. Sem funcionários. Sem inventar equipe, sem inventar números.

**Persona:** Pequena empresa (restaurante, clínica, varejo, serviço) que tem um processo manual que dá trabalho, Considerando contratar alguém para resolver. Ofegante: desenvolvedor sozinho, honesto, capaz.

**Definição de concluído:** Página que: (1) não contém números/depoimentos inventados; (2) usa somente dados reais; (3) é bonita e funciona; (4) deixa claro o que a empresa entrega e como; (5) convida ao contato pelo WhatsApp real.

---

## Histórias

### H-V6-01 — Copy honesta: headline + proposta de valor
**Como** visitante que pode ser seu próximo cliente, **quero** entender em 5 segundos o que a Code House faz e para quem, **para** decidir se continua lendo ou vai embora.

#### Critérios
- [ ] Headline: "Sistemas feitos sob medida para o seu negócio." ou variante que capture a essência (não promete resultados, não usa "pagamento" como bait)
- [ ] Subheadline: explica o que entrega (CRM, ERP, e-shop, site) e para quem (pequenas empresas com processo específico)
- [ ] Nenhuma promessa de resultado ("aumente suas vendas em X%") — a Code House entrega sistema, não resultado de negócio
- [ ] CTA claro: "Falar no WhatsApp" (direct, honesto) — não "Agendar consultoria gratuita de 1h" se não é consultoria

### H-V6-02 — Stack real: tecnologias que a empresa realmente usa
**Como** visitante técnico (ou dono de empresa que se importa com tecnologia), **quero** ver as tecnologias reais que a Code House usa, **para** saber se é um time com o qual eu me contagionário.

#### Critérios
- [ ] Grid de tecnologias com ícones (FA 6.5.1 via CDN, ou SVG inline)
- [ ] Só tecnologias que a empresa really usa — se usa Node.js, PostgreSQL, React, etc., aparece. Se não usa WordPress, não aparece.
- [ ] Nenhuma tecnologia inventada só para encher o grid

### H-V6-03 — Processo: como a empresa trabalha (honesto)
**Como** potencial cliente que não conhece desenvolvimento, **quero** entender como funciona o processo de contratação e entrega, **para** saber o que esperar e quando pagar.

#### Critérios
- [ ] 3-4 etapas claras: diagnóstico → construção → entrega → suporte
- [ ] Linguagem acessível, sem jargão de engenharia
- [ ] Se houver "sprint" ou "entrega semanaal", ser verdade — não inventar metodologia ágil sofisticada se a empresa trabalha de outro jeito
- [ ] Se houver depósito/intervalo de pagamento, mencionar com honestidade (não preciso detalhar valores, mas não esconder que há pagamento)

### H-V6-04 — Tipos de sistema: o que a empresa entrega
**Como** visitante que não sabe se precisa de CRM, ERP ou e-shop, **quero** ver os tipos de sistema que a Code House entrega, **para** saber se eu encaixo no que ela faz.

#### Critérios
- [ ] CRM, ERP, E-shop, Site institucional, e talvez "Sob medida" (qualquer sistema que o negócio precise)
- [ ] Cada tipo com: nome, 1-2 linhas do que é, para quem faz sentido
- [ ] Hero com cards mockados (CRM, ERP, E-shop) — mostra a qualidade visual do trabalho, não dados de clientes reais (usar dados demo, não "Ana Lima pagou R$ 3.200")
- [ ] Se usar mockups, os dados dentro são demo ("R$ XX.XXX", "Cliente A") — não fingir que são dados reais de clientes

### H-V6-05 — FAQ: tirar dúvidas comuns de forma honesta
**Como** visitante com dúvidas típicas sobre desenvolvimento sob medida, **quero** ver perguntas e respostas reais, **para** não ter que esperar resposta para decidir se meço um orçamento.

#### Critérios
- [ ] 5-7 perguntas: prazo, custo, código-fonte, mudança de ideia, empresa pequena faz sentido, tecnologias, como começa
- [ ] Respostas honestas: se o prazo varia, dizer que varia. Se o custo é por projeto com estimativa, dizer. Não prometer prazos fixos se não são fixos.
- [ ] Copy humanizada (humanizer principles: direto, útil, sem robótico): sem "como uma IA", sem encher de adjetivos, sem bullet points genéricos

### H-V6-06 — Contato: WhatsApp real + formulário opcional
**Como** visitante pronto para contato, **quero** entrar em contato de forma fácil e segura, **para** dar o primeiro passo sem burocracia.

#### Critérios
- [ ] Botão/flutuante WhatsApp com número real (não placeholder)
- [ ] Se houver formulário, ele é opcional — o WhatsApp é o principal
- [ ] Nenhum dado falso no formulário (sem "empresa X already usou")
- [ ] Se usar email codehouse42@gmail.com, aparece onde faz sentido (footer, contato)

### H-V6-07 — Footer honesto
**Como** visitante que chega no final da página, **quero** ver informações reais de contato e dados da empresa, **para** ter confiança de que é uma empresa real, não um template.

#### Critérios
- [ ] CNPJ real: 68.489.569/0001-04
- [ ] Email real: codehouse42@gmail.com
- [ ] WhatsApp real: número do dono
- [ ] Sem inventar endereço, sem inventar cidade se não é real. Se a empresa é de Santa Maria/RS (como está no index atual), manter se verdade. Se não, remover.
- [ ] Social: se tiver Instagram/LinkedIn real, incluir. Se não, remover.

### H-V6-08 — Qualidade técnica: o site em si demonstra capacidade
**Como** visitante que avalia a qualidade da empresa pelos seus resultados visíveis, **quero** que a landing page seja tecnicamente impecável, **para** ter confiança de que se contratar, o sistema também será bem feito.

#### Critérios
- [ ] Rápido (Lighthouse performance bom)
- [ ] Acessível (WCAG AA básico, contraste, navegação por teclado)
- [ ] Responsivo (funciona bem em mobile, tablet, desktop)
- [ ] Sem erros de console
- [ ] Dark mode funcional (se implementado)
- [ ] Animações sutis e que melhoram a experiência, não distraem

### H-V6-09 — Design premium: tirar o melhor do redesign
**Como** visitante, **quero** que a página seja visualmente impressionante, **para** perceber que a Code House se preocupa com qualidade também na apresentação.

#### Critérios
- [ ] Tirar do redesign: paleta dark-first com tokens (--void: #050505, --surface: #0C0C0C, --surface-raised, --accent-1: #FF6B35, --accent-2: #FF2E63, --accent-3: #9D4EDD), tipografia Syne/Inter/JetBrains Mono, favicon SVG inline, theme-color #050505
- [ ] Fa-6.5.1 CDN para ícones
- [ ] FAQ com design do redesign (cards com accordion)
- [ ] Stack grid com ícones FA coloridos
- [ ] Hero com cards mockados flutuantes (CRM, ERP, E-shop) — dados demo, não reais
- [ ] Copy "seu modo de operar" no hero (se soa natural em pt-BR)
- [ ] LGPD banner se estiver no redesign (animado com anime.js)
- [ ] Floating WhatsApp scroll-driven

### H-V6-10 — Revisão B2B: validar se a página vende para pequenas empresas
**Como** dono de empresa nova que precisa de clientes, **quero** que alguém analise a página do ponto de vista de um potencial cliente de pequena empresa, **para** ajustar copy, clareza e posição antes de divulgar.

#### Critérios
- [ ] Análise: a página comunica claramente o que entrega e para quem?
- [ ] A proposta de valor é honesta e não promete resultados impossíveis?
- [ ] O CTA é claro e fácil?
- [ ] A página passa credibilidade sem inventar números?
- [ ] Sugestões de ajuste documentadas

---

## Out of scope
- E-shop funcional (catálogo, carrinho) — é exemplo de sistema, não produto da página
- Tabs de exemplos com painéis interativos (CRM/ERP/E-shop mockups) — usar cards mockados estáticos simples, não painéis completos
- Integração com APIs externas
- Blog, newsletter (a menos que a empresa realmente queira)
- Múltiplos idiomas

## Rejeição
- P0: qualquer dado inventado (número, depoimento, empresa, endereço, nota)
- P1: página lenta, acessível, ou que não converte para contato

## Ordem de implementação
1. H-V6-01 (copy)
2. H-V6-02 (stack)
3. H-V6-04 (tipos de sistema + hero cards)
4. H-V6-05 (FAQ)
5. H-V6-03 (processo)
6. H-V6-06 (contato)
7. H-V6-07 (footer)
8. H-V6-08 (qualidade técnica)
9. H-V6-09 (design premium)
10. H-V6-10 (revisão B2B)
