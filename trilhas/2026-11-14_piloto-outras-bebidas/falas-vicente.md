# Piloto com outras bebidas: falas de Vicente e essência à espera de confirmação (14/11/2026)

Conversa de planejamento depois da entrega do piloto (D-056), Opus 5.5, esforço máximo. As falas ficam aqui só por rastreabilidade: o texto de trabalho usa a essência confirmada (habilidade `registrar-decisao`), nunca a transcrição.

## Falas
1. "antes preciso ver o piloto funcionando para as clbs que se pode ter com o que foi construido como teste piloto. o que conseguimos encontrar?"
2. Depois do levantamento (o que a ferramenta achou; insumo 140): "adicione estas entradas liberando o filtro e sinalizando que elas fazem parte do piloto. nao precisa coletar dados sobre elas ou fazer verificacao juridica. precisamos olhar o que conseguimos fazer com com o cultura liquida"

## Essência devolvida (pendente; vira a D-057 só depois da confirmação)
Para ver o que a ferramenta consegue fazer além da cajuína, as Entradas de outras bebidas que as rotinas já coletaram entram no piloto, cada uma com a marca de que entrou por esta decisão. Elas passam à frente na fila da rotina com IA e seguem a ferramenta como a cajuína seguiu (Evidências e Proposições; depois Termo, CLB, ficha e grafo de cada bebida), em vez de parar em candidata (D-039). Nada novo se coleta sobre elas, e o juridico não faz a triagem delas. Segue o resto da ferramenta: trecho localizado, validador, portão, segunda leitura do auditor, o filtro de pessoa citada e a busca de dado pessoal antes do commit; e a Falta F-0024, já aberta para as outras bebidas de caju. Para elas serem lidas, a rotina do Claude volta a propor e reler (o primeiro ato da D-056).

Muda, só para estas Entradas: a D-039 (no piloto, só a cajuína ia até a ficha), a ordem da fila (`fila-ia-0.1`) e a triagem jurídica da lista de rigor da D-056.

## Palavras a conferir
- **"estas entradas":** as 199 da Consulta geral (CO-0008) com um dos 10 nomes listados na conversa (cerveja, suco, refrigerante, bebida láctea, cachaça, vinho, água de coco, caldo de cana, néctar, hidromel) e as 7 das CLB candidatas (vinho de caju, mocororó); não as 567 da Consulta geral inteiras, nem bebidas que as rotinas não trouxeram. Lista em `escopo-proposto.json`.
- **"o filtro":** a ordem da fila (que lê primeiro a cajuína) e o limite da D-039; não o filtro de pessoa citada nem o portão.
- **"fazem parte do piloto":** uma marca em cada Entrada (a decisão e a data), para os relatórios separarem o que veio daqui.
- **"verificação jurídica":** a triagem do juridico (triagem-juridica, Faltas novas, guias); não os scripts da ferramenta.
- **"coletar dados":** nenhuma Consulta ou Recorte novo para essas bebidas; a rotina diária segue como está.

## Estado
Nada mudou na ferramenta. Custo previsto: 14 lotes de 15 Entradas; um lote da rotina com IA custou de 270 a 350 mil tokens em 13/11 (insumo 132). Nada roda antes de 18/11, 23h: a semana da conta está em 88% (estimada), e o limite é 90%.
