# Base A — campos e controle de qualidade
**Natureza:** lista preliminar de candidatas, não mailing para contato. Importar [CSV vazio](modelos/base-a.csv) como UTF-8 com separador ponto e vírgula.

| Campo | Regra |
|---|---|
| empresa, municipio, segmento | Identificação da unidade e recorte corretos |
| servico_itep_relacionado | Serviço efetivamente ofertado pela ITEP Jr. |
| site_institucional, cnpj, contato_institucional | Não preencher por suposição |
| fonte_identidade_url, fonte_cnpj_url, fonte_contato_url | URL específica que comprova o campo |
| data_consulta | Data da verificação, não prova de atualidade da página |
| status_identidade, status_cnpj, status_contato | Classificação **por campo** |
| hipotese_aderencia, prioridade, observacoes | Interpretação condicional e pendências |

## Estados permitidos
- **VERIFICADO:** fonte pertinente comprova aquele dado.
- **NAO_VERIFICADO:** o valor existe na pesquisa, mas falta prova suficiente.
- **CONFLITANTE:** fontes divergem; preservar ambas.
- **NAO_LOCALIZADO:** informação não encontrada; deixar campo vazio.

Uma empresa pode ter nome verificado, CNPJ não localizado e contato não verificado. Não colapsar tudo em uma única etiqueta.

## Priorização qualitativa
| Aderência ao serviço | Evidência | Tratamento |
|---|---|---|
| Alta | Alta | Priorizar revisão comercial humana |
| Alta | Baixa | Pesquisar mais antes de qualquer contato |
| Baixa | Alta | Não priorizar neste recorte |
| Baixa | Baixa | Deixar fora da prioridade |

A hipótese "vale investigar se..." é aceitável; "precisa comprar" sem informação independente, não. CNPJ válido e telefone institucional não provam orçamento, interesse ou consentimento.

## Auditoria ao vivo
Selecionar uma empresa; verificar nome/município/atividade em canal institucional; checar CNPJ via serviço oficial quando disponível; confirmar contato no canal correto; guardar URLs e data; aplicar status separados; descrever lacunas. **Não publicar registros reais nem listas com contatos** neste repositório público.
