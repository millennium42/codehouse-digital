# Skills e repositórios de referência
**Prompt** é uma solicitação ao modelo. **Skill** é um procedimento reutilizável que orienta o agente. **Plugin/app** dá acesso a funções ou sistemas, conforme permissão. Não são sinônimos.

## Skill local do curso
[skills/instrutor-itep/SKILL.md](skills/instrutor-itep/SKILL.md) instrui um agente a apoiar a preparação e a explicação da demonstração. O arquivo no GitHub **não instala** a skill automaticamente em nenhuma plataforma.

## Repositórios consultados
| Referência | Uso concreto | Limite |
|---|---|---|
| [Anthropic Skills / PPTX](https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md) | Estruturar apresentações, notas e validação visual | Não confirma empresas |
| [wshobson/agents / pptx-deck-creation](https://github.com/wshobson/agents/tree/main/plugins/pptx-deck-creation) | Organização de deck, especificações e quality gates | Uso na produção de material |
| [obra/superpowers](https://github.com/obra/superpowers) | Planejamento, revisão e processo disciplinado | Não é base de contatos |
| [Anthropic Skills](https://github.com/anthropics/skills) | Convenções de definição de skills | Verificar instalação/compatibilidade |
| [CodeHouse Digital](https://github.com/millennium42/codehouse-digital) | Ilustração conceitual de descoberta/enriquecimento/qualificação | Dados e operações reais fora da aula |

**Não confirmado:** o repositório `millennium42/about-my-toolbox` não estava acessível na consulta em 17/11/2026; por isso não atribuí a ele nenhuma funcionalidade específica.

## Como usá-los
**Antes da aula:** aplicar skills para revisar estrutura, gramática, notes e consistência do material. **Durante:** abrir somente chatbot, fontes e planilha; não instalar ou demonstrar frameworks complexos. **Depois:** guardar os prompts e a metodologia, não dados de leads.

## Critérios para recomendar plugin/skill
Verificar o que lê e escreve; se precisa de credenciais; se tem envio/efeitos externos; limites, políticas e quota; fonte e grau de comprovação do resultado; modo seguro sem envio; e como interromper. **Quanto mais automático, maior a necessidade de controle e auditoria.**
