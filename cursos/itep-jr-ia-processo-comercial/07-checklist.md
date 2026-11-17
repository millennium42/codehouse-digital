# Checklist pré-aula, ao vivo e contingência

## Antes
- [ ] Apresentação com notas aberta: https://docs.google.com/presentation/d/1cyOeuAS4c24NTml2fSVSAR3MRsVIkAHgkC5Shp95DbU/edit
- [ ] Serviço real da ITEP Jr., segmento e município/região confirmados.
- [ ] Chatbot autenticado, busca web testada e [prompt principal](05-prompts.md#1-pesquisa-principal) copiado.
- [ ] Planilha vazia criada com [base-a.csv](modelos/base-a.csv).
- [ ] [Consulta oficial de CNPJ](https://www.gov.br/pt-br/servicos/consultar-cadastro-nacional-de-pessoas-juridicas) e navegador funcionando.
- [ ] Compartilhamento de janela, microfone e fonte testados.
- [ ] Notificações desativadas; abas privadas, tokens e dados reais fechados.
- [ ] Não executar agentes de prospecção ou envio do monorepo.

## Durante
- [ ] Falar o objetivo antes do prompt.
- [ ] Mostrar uma pesquisa direta já com regras de qualidade.
- [ ] Verificar se houve busca web real.
- [ ] Explicar o motivo de cada campo da Base A.
- [ ] Auditar uma empresa em fonte independente.
- [ ] Identificar status por campo e hipóteses comerciais separadamente.
- [ ] Não disparar mensagens, enriquecer dados pessoais sem necessidade ou publicar leads.

## Plano B
| Falha | Alternativa | Frase |
|---|---|---|
| IA sem busca web | Consulta manual; IA só estrutura | "Sem consulta real, não afirmo atualidade." |
| Poucas empresas | Menos registros; manter qualidade | "Meta de linhas não é licença para inventar." |
| Site indisponível | Outra fonte pertinente ou NAO_VERIFICADO | "Indisponível não é confirmado." |
| CNPJ ausente | NAO_LOCALIZADO | "Sem número não concluo inexistência." |
| Fontes divergentes | CONFLITANTE com URLs | "Conflito fica visível para investigação." |
| Planilha travada | CSV local | "A ferramenta muda; o método permanece." |
| Pouco tempo | Três linhas, uma auditoria completa | "A evidência tem prioridade." |

## Depois
- [ ] Guardar somente roteiro e prompts públicos no Git.
- [ ] Salvar Base A real em local com acesso autorizado, conforme política da instituição.
- [ ] Rever se gravação ou prints expõem dados.
- [ ] Preparar Aula 2 sem mudar retrospectivamente os critérios de auditoria.
