# Demonstração operacional — o que fazer, dizer e justificar
Deixar este guia na janela secundária junto às notas do apresentador. Executar um **único fluxo**.

## 1. Preparação
- Confirmar um serviço atual da ITEP Jr. e selecionar [SEGMENTO] e [CIDADE/REGIÃO]. Não assumir serviços que não foram validados.
- Abrir apresentação, chatbot, planilha vazia, navegador e fonte de [consulta de CNPJ](https://www.gov.br/pt-br/servicos/consultar-cadastro-nacional-de-pessoas-juridicas).
- Testar acesso real a pesquisa web. Uma IA sem navegação pode estruturar pesquisa, mas não atestar informações atuais.
- Ocultar notificações, dados de contas e abas pessoais. Não abrir leads reais da CodeHouse.

## 2. Mostrar o recorte
**Fazer:** registrar os três critérios: segmento, geografia e serviço.
**Dizer:** "Não estou procurando qualquer empresa, mas organizações com uma hipótese justificável de aderência."
**Por quê:** reduz resultados fora do perfil e evita confundir mapeamento com prospecção.

## 3. Pesquisar uma única vez
**Fazer:** executar o [prompt principal](05-prompts.md#1-pesquisa-principal) já completo com as variáveis reais.
**Dizer:** "Peço fontes, restrições e tratamento de lacunas antes da pesquisa, porque depois vou conferir os registros."
**Por quê:** estabelecer a auditabilidade desde a primeira saída.
**Atenção:** se o chatbot não navegar de fato, não atribuir atualidade a uma lista gerada apenas pelo modelo.

## 4. Construir a Base A
**Fazer:** importar [modelo de cabeçalho](modelos/base-a.csv) na planilha e preencher campos somente quando houver registro/URL pertinente. Ver [regras](08-base-a.md).
**Dizer:** "Uma célula preenchida não é um dado confirmado. Preciso saber de onde veio e o que ainda falta."
**Por quê:** outro analista deve conseguir retomar a pesquisa.
**Checar:** duplicatas, homônimos, matriz x filial, município e contato institucional.

## 5. Auditar UMA empresa
**Fazer:** selecionar uma linha; abrir site institucional para nome/atividade/localidade; consultar CNPJ em fonte oficial quando disponível; confirmar canal institucional na unidade correta; registrar URLs, data e status separados.
**Dizer:** "Não uso o próprio chatbot para provar o que ele disse. A página externa deve demonstrar exatamente a informação."
**Por quê:** reduzir erro de identidade, contato incorreto e evidência genérica.
**Regra:** se a fonte não sustentar o campo, marcar NAO_VERIFICADO, CONFLITANTE ou NAO_LOCALIZADO, conforme o caso.

## 6. Qualificar sem exagerar
**Fazer:** descrever aderência à oferta e força da evidência; marcar prioridade revisável.
**Dizer:** "Vale investigar se existe uma necessidade; ainda não sei se há demanda, verba ou interesse."
**Por quê:** a prospecção produz hipóteses, não diagnósticos nem autorização para contato.

## 7. Encerrar
**Fazer:** voltar ao fluxograma e percorrer: definir alvo → buscar → registrar → verificar → qualificar → decidir. Mostrar quais lacunas permaneceram abertas.
**Critério de sucesso:** audiência entende o motivo de cada decisão, mesmo sem operar ferramenta durante o encontro.
