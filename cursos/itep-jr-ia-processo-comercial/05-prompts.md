# Prompts prontos — pesquisa única e rastreável
Substituir [SEGMENTO], [CIDADE/REGIÃO] e [SERVIÇO ITEP JR. VALIDADO] por valores verdadeiros. **Não elaborar uma versão deliberadamente ruim para comparar.** Prompt bem redigido melhora a tarefa, mas não substitui evidência externa.

## 1. Pesquisa principal
```text
Atue como apoio à pesquisa comercial da ITEP Jr. (empresa júnior).
Objetivo: identificar até 15 empresas candidatas do segmento [SEGMENTO]
em [CIDADE/REGIÃO], potencialmente aderentes a [SERVIÇO ITEP JR. VALIDADO].

Primeiro, confirme se a pesquisa na web está disponível nesta conversa.
Se não estiver, declare a limitação e NÃO apresente dados como atuais
ou confirmados: proponha o procedimento de busca manual.

Se houver busca real, retorne uma tabela com uma empresa por linha:
nome; município/unidade; segmento; site institucional; CNPJ (quando
comprovável); canal de contato empresarial (quando comprovável);
URLs específicas que sustentam os campos; data da consulta;
status por campo (VERIFICADO/NAO_VERIFICADO/CONFLITANTE/NAO_LOCALIZADO);
observações e hipótese de aderência em linguagem condicional.

Regras:
- Nunca invente ou complete CNPJ, telefone, e-mail ou endereço.
- Não misture homônimos, matriz e filial; sinalize duplicatas.
- Uma URL só sustenta o dado que efetivamente consta nela.
- Não conclua que a empresa tem orçamento, problema ou intenção de compra.
- Se houver menos de 15 candidatas sustentáveis, entregue menos.
- Deixe pendências explícitas e liste limitações ao final.
```

**O que explicar ao digitar:** cada campo auxilia uma etapa operacional; o recorte evita dispersão; as fontes permitem auditoria; lacunas explícitas são mais úteis do que dados inventados.

## 2. Estruturar Base A
```text
Converta os dados abaixo ao cabeçalho do modelo Base A deste curso,
em CSV separado por ponto e vírgula. Preserve a origem de cada valor,
os status e as lacunas. Não invente campos, não troque unidades
e não faça correções silenciosas. Sinalize possíveis duplicatas.
[DADOS EMPRESARIAIS NÃO SENSÍVEIS OBTIDOS DA PESQUISA]
```

## 3. Preparar a auditoria de uma linha
```text
Com base neste registro preliminar [REGISTRO SEM DADOS PESSOAIS],
liste o que deve ser confirmado por fonte independente para:
identidade, município, CNPJ, site e canal institucional.
Quando houver pesquisa web ativa, indique URL e o trecho que comprova
cada dado; caso contrário, explique os passos de conferência manual.
Classifique cada campo com um dos quatro status.
Não trate a própria resposta de IA como evidência independente.
```

## 4. Qualificar sem inventar demanda
```text
Use somente campos verificados para avaliar a possível aderência
da empresa a [SERVIÇO ITEP JR. VALIDADO]. Separe:
(1) fatos e fontes; (2) hipótese condicional; (3) lacunas;
(4) prioridade qualitativa e motivo; (5) razões para não priorizar.
Não infira orçamento, dor, consentimento ou intenção de compra.
Não redija nem envie mensagens comerciais.
```

## 5. Explicar uma decisão para o público
```text
Explique em três frases simples por que [FONTE/REGRA/STATUS]
foi usado na pesquisa comercial e qual erro evita.
Diferencie fato, hipótese e informação não verificada.
```

## 6. Contingência sem internet
```text
Não há pesquisa web disponível. Em vez de inventar empresas,
forneça um plano de busca manual para [SEGMENTO] em [CIDADE],
com termos, fontes adequadas, campos da Base A e passos
de verificação independente.
```

**Não commitar:** respostas com listas reais de contato ou dados pessoais; este GitHub é público.
