# Lote C2 - conferencias (2026-10-16)

Modelo: sonnet-5.5, esforco alto. Chamadas de ferramenta usadas: 18 (teto 18).
Niveis: oficial = pagina oficial aberta e trecho lido; secundaria = fonte nao oficial que abriu; nao conferido.

## C2.1 TK Labels (Local Contexts)

**Resposta:** Labels sao etiquetas para comunidades indigenas e organizacoes locais indicarem condicoes de acesso e uso. So podem ser aplicados por conta de comunidade. Complementam as licencas CC, nao as substituem (sao extra-legais; nao exigem ser titular de direito autoral). Notices sao avisos de pesquisadores/instituicoes, nao personalizaveis.

- O que sao: "identify cultural material that has community-specific conditions regarding access and use" - https://localcontexts.org/labels/traditional-knowledge-labels/ - **oficial**
- Quem aplica: "Labels can only be applied by a community account." - https://localcontexts.org/support/frequently-asked-questions/ - **oficial**
- Convivencia com CC: "have been developed to complement Creative Commons licenses" - mesma FAQ - **oficial**
- Extra-legais: "extra-legal mechanisms, meaning that they work outside existing legislation"; "To use the Labels or Notices you do not need to be a copyright holder." - mesma FAQ - **oficial**
- Labels x Notices: "Labels are for use by Indigenous communities ... Notices are for use by researchers and institutions ... Notices are not customizable." - mesma FAQ - **oficial**

Obs.: a FAQ nao diz se Labels sao juridicamente vinculantes. Existem tambem "TK Licenses" (outra ferramenta), nao conferida.

## C2.2 Principios CARE (GIDA)

**Resposta:** pagina oficial: https://www.gida-global.org/careprinciples (/care deu 404). CARE complementa FAIR. Enunciado curto de cada principio: nao conferido.

- URL: link "The CARE Principles for Indigenous Data Governance" no site - https://www.gida-global.org/careprinciples - **oficial**
- Relacao com FAIR: "complement the existing FAIR principles"; FAIR ignora "power differentials and historical contexts" - mesma URL - **oficial**
- Enunciado de Collective Benefit, Authority to Control, Responsibility, Ethics: o texto recuperado nao os trazia (talvez no PDF de uma pagina linkado) - **nao conferido**

Obs.: os nomes dos quatro principios vieram do enunciado da tarefa e de resumos de busca nao abertos.

## C2.3 Flora e Funga do Brasil

**Resposta:** ha coluna "origin" na tabela do pacote R florabr, mas valores exatos nao conferidos. Dados em Darwin Core Archive, atualizados semanalmente. API: nao conferido.

- DwC-A semanal: "stored in Darwin Core Archive data sets, which is updated weekly" - https://cran.csiro.au/web/packages/florabr/vignettes/getting_started.html - **secundaria**
- Coluna `"origin"` (23 e 39 colunas), sem valores listados - mesma URL - **secundaria**
- IPT do JBRJ (https://ipt.jbrj.gov.br/jbrj/resource?r=lista_especies_flora_brasil): HTTP 403 - **nao conferido**
- Valores (nativa/naturalizada/cultivada), termo DwC e API: **nao conferido**

## C2.4 Rotinas do Claude Code

**Resposta:** rede padrao "Trusted" (lista de dominios permitidos), configuravel para "Custom" ou "Full" por ambiente; ha seletor de modelo por rotina; consumo da assinatura mais limites por hora. Fonte: https://code.claude.com/docs/en/routines - **oficial** para tudo abaixo.

- Rede padrao: "A Default environment is provided with Trusted network access, which allows only the default allowlist ..."
- Configuravel: "change Network access to Custom ... Select Full instead for unrestricted access."
- Conectores: "MCP connector traffic is routed through Anthropic's servers rather than that path"
- Modelo: "The prompt input includes a model selector. Claude uses the selected model on every run."
- Custo: "Routines draw down subscription usage the same way interactive sessions do."
- Limites: 100 execucoes agendadas/h por conta; 30/h por rotina (Run now e API); "None of these hourly limits has overage."; sem creditos de uso, execucoes alem do limite sao rejeitadas.
- Estado: "Routines are in research preview" (limites podem mudar). Planos Pro, Max, Team, Enterprise; intervalo minimo de 1 hora.

Nao aberta: pagina cloud-environments (lista exata de dominios padrao).

## C2.5 Save Page Now 2 (Internet Archive)

**Resposta:** a doc da SPN2 diz que exige autenticacao (chaves S3 preferidas; cookies como alternativa), mas tambem que anonimos podem usar com limites menores. Fonte: https://docs.google.com/document/d/1Nsv52MvSjbLb2PCpHlat0gkzw0EvtSgpKHu4mk0MnrA/mobilebasic - **secundaria** (documento de comunidade, fora de archive.org).

- Autenticacao: "requires authentication using two alternative methods: S3 API keys ... Cookies"
- Anonimo: "Anonymous users can use SPN2 but their total captures per day cannot be more than this limit."
- Por minuto: "authenticated users = 7 and for anonymous users = 3"
- Por dia: anonimo 200; autenticado 30k; "Max captures per day for a URL = 5"
- Concorrencia: "When more than 20 concurrent captures target the same host, additional requests are delayed"
- Pagina oficial web.archive.org/save: dominio bloqueado na ferramenta - **nao conferido**

Obs.: a doc se contradiz sobre o teto de dados anonimo (500MB vs 2GB/dia); um resultado de busca nao aberto cita 6 URLs/min (2023). Numeros podem estar desatualizados.

## Nao conferido

- C2.2: enunciado curto de cada principio CARE.
- C2.3: valores do campo de origem, termo Darwin Core e existencia de API (IPT deu 403; site da Flora nao aberto).
- C2.5: documentacao oficial em archive.org (inacessivel pela ferramenta).
- C2.4: lista exata de dominios do acesso Trusted.
