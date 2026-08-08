# Code House Landing Page — Regras e Aprendizados (Ralph Loop)

## Decisões Arquiteturais
- **Sem Frameworks CSS:** O projeto foi construído usando CSS Vanilla com uma estrutura de pastas modular (`css/layout`, `css/components`, `css/tokens.css`). Nunca introduza Tailwind ou Bootstrap neste repositório.
- **Sistema de Tokens:** Toda a gestão de temas (Dark/Light) opera em cima das Custom Properties definidas em `tokens.css`. Se precisar de uma nova cor, registre-a lá primeiro com o fallback de contraste para o dark mode.
- **Performance de Mockups:** Optamos por recriar UI elements (gráficos, tabelas, dashboards) puramente em HTML/CSS para os showcases. Isso manteve o DOM leve e evitou dependência de assets grandes, garantindo nota máxima em métricas de performance. Não substitua esses mockups por imagens estáticas no futuro.

## Padrões Adotados
- **Ponytail Strict:** Nenhuma funcionalidade extra foi construída se não constava nas histórias (H-01 a H-13). O formulário de contato só faz a simulação e previne default, conforme estipulado.
- **Mobile First / Breakpoints:** Os limites sagrados de quebra do projeto são `900px` (Tablets/Colapsos pesados) e `600px` (Mobiles pequenos).
- **Sem Fontes Externas:** Utilizamos a stack do sistema operativo para manter a promessa de performance.
- **Área de Toque:** Interativos respeitam estritamente um `min-height: 44px` ou `padding` que atinja essa volumetria.

*(Documento gerado automaticamente pela Fase 4 do Ralph Loop. Guia o comportamento futuro de IA na edição deste código).*
