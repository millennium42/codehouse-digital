# Ferramentas, plugins e conexões para o instrutor

| Recurso | Para quê | Quando usar | Cuidados |
|---|---|---|---|
| ChatGPT com pesquisa web (quando ativa) | Descoberta de candidatas com fontes | Pesquisa principal | Verificar se houve busca real; citação não é confirmação |
| Navegador | Abrir fontes externas | Auditoria | Conferir a informação exata na página, não só a URL |
| Google Planilhas / Excel | Base A estruturada | Durante toda a demonstração | Origem e status separados por campo |
| [Consulta CNPJ](https://www.gov.br/pt-br/servicos/consultar-cadastro-nacional-de-pessoas-juridicas) | Cadastro empresarial | Conferência do identificador | CNPJ correto não prova demanda comercial |
| Google Apresentações | Orientações e notas | Abertura, transições, síntese | Os slides não substituem a demonstração |

## Plugins/apps de preparação
- **Google Drive/Google Slides**: manter os slides, notas e materiais. Usar com a conta autorizada; a apresentação já está [aqui](https://docs.google.com/presentation/d/1cyOeuAS4c24NTml2fSVSAR3MRsVIkAHgkC5Shp95DbU/edit).
- **Google Sheets**: preparar colunas e registros; a conexão por si só não valida dados.
- **GitHub**: versionar prompts e guias, sem inserir contatos, tokens, listas reais ou credenciais.
- **Pesquisa web**: o recurso-chave da aula. Confirmar funcionamento no ambiente, não assumir que todos os modelos têm web.
- **Gmail/Google Calendar**: desnecessários na Aula 1, não abrir para demonstrar prospecção.

Um plugin/app depende da conexão, plano e permissões. Uma *skill* é instrução reutilizável; não é autorização de acesso nem plugin instalado.

## Somente para etapas futuras
- [Apify](https://docs.apify.com/): Actors e datasets para coleta quando apropriado; revisar custo, políticas da fonte e proteção de dados.
- [gosom/google-maps-scraper](https://github.com/gosom/google-maps-scraper): ferramenta técnica, avaliar licença, termos e uso antes de executar.
- [Crawl4AI](https://github.com/unclecode/crawl4ai): extração de páginas permitidas; extração não equivale a verificação.
- **Agente CodeHouse / Hermes**: arquitetura conceitual, **não** executar rotinas reais, contatos ou envio; ver README dos módulos agent/ e ops/.

## Links oficiais de verificação
- Busca no ChatGPT: https://help.openai.com/pt-br/articles/9237897-searching-the-web-with-chatgpt
- Receita Federal (comprovante): https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/Cnpjreva_S.aspx
- ANPD (legítimo interesse): https://www.gov.br/anpd/pt-br/assuntos/noticias/anpd-lanca-guia-orientativo-sobre-legitimo-interesse

Dados empresariais públicos não dispensam cautela com dados de pessoas naturais e finalidades de tratamento.
