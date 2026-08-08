# Code House — Ralph Loop Learnings
**Data:** 2026-08-07
**Projeto:** Landing Page (v1.0.0)

Este documento registra os aprendizados práticos capturados durante o ciclo de build da landing page. Estes insights devem guiar futuros projetos da Code House.

## 1. Mockups Zero-Asset (CSS Puro)
Descobrimos que é extremamente viável criar representações visuais ricas (Kanban boards, gráficos de barras de ERP, grids de e-commerce) consumindo **zero requisições de rede**. Usar `flexbox` com barras baseadas em % para gráficos e `border-radius` controlados simula interfaces nativas com muita perfeição.
- **Diretriz:** Padronizar a classe base `.mockup-window` para todos os projetos da Code House como assinatura visual ("janelas de OS").

## 2. Dark Mode Defensivo (Sem "Flash")
Implementamos uma técnica resiliente usando um inline `<script>` colocado no final da tag `<head>`.
- **Diretriz:** Sempre injetar `document.documentElement.setAttribute('data-theme', ...)` sincronamente antes da árvore do DOM terminar de ser montada no `<body>`. Isso impede que layouts carreguem na cor do tema incorreto (gerando um flash visual) antes do JS engatilhar.

## 3. O Poder do Token Brutalista Restrito
A restrição estrita de usar apenas "system fonts" (sem chamadas a Google Fonts) combinada com um `border-radius` brutalista leve de 2px e uma paleta de duas cores (azul-nuvem e grafite) construiu um visual extremamente maduro.
- **Diretriz:** Manter bloqueios a frameworks pesados e fontes externas como restrição padrão para clientes PME. Isso força a interface a ser criativa no contraste e espaçamento, atingindo o cliente que valoriza velocidade e performance (Core Web Vitals sempre no verde).

## 4. Deploy Infrastructure as Code
A adição do `render.yaml` desde o dia 1 simplificou o CI/CD para site estático e unificou documentação técnica com topologia de deploy. O fallback dinâmico para `404.html` via redirect rule previne problemas em SPAs e assets quebrados.
