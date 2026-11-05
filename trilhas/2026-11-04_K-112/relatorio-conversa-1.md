# K-112, conversa 1 (04 e 05/11/2026): relatório de uma tela

**O cartão segue em Fazendo.** Nada está ligado ainda: a rotina diária está pronta e testada aqui, mas os
workflows não puderam ser enviados ao GitHub (falta um escopo do token, que só Vicente renova).

## O que entrou
- **Camada 1 sem IA** (scripts e casos): agenda pela cadência medida (agenda-0.1), rotina diária que só
  grava com novidade, feed de novidades, checagem de links, portão da camada 1, relatório do dia 0.4,
  faixa própria da rotina nos IDs (50000-89999), teste das fichas no runner, hook SubagentStop sem o
  Python do Windows, `ler_fonte.py` com a cópia arquivada só na falha.
- **Workflows** `validar`, `rotinas` e `testar-fichas`, guardados em `workflows/` desta pasta até o envio
  (05/11, com o escopo renovado: estão em `.github/workflows/`, e a cópia da trilha saiu).
- **Adaptadores novos** Tainacan (BCR) e "API com cursor" (OpenAlex; Scrape API do Internet Archive), com
  casos sintéticos; falta a resposta real gravada e a rodada curta.
- **Consulta geral CO-0008** ("bebida" E um processo do piloto), já na colheita da Infoteca-e.
- **Rodada simulada real** da rotina na BDTD: 39 pedidos, 1 Entrada nova e 27 itens só como pegada
  (nada gravado: simulação).

## Paradas e conferências
- **Termos do Actions (parada a):** nenhum gatilho da D-033 (C112); vale a leitura do Flat Data.
- **Mapa de hospedagem (insumo 7):** 9 fatos confirmados, 1 corrigido, 1 não conferido (C112h).
- **Fontes:** BCR, Oasisbr e OpenAlex sem Falta pela regra; **Internet Archive fechado pela F-0034**
  (termos não lidos, vale agora; cartão K-208, que chama Vicente). A F-0034 barra também a cópia
  arquivada do `ler_fonte.py`, pela regra do `wayback.py`.

## Faltas novas
- F-0034 (termos do Internet Archive).

## Para Vicente (ajustes de dono, não decisões novas)
1. **Escopo `workflow` do gh** (sem ele, o GitHub recusa os workflows): no terminal desta máquina,
   `gh auth refresh -h github.com -s workflow` e confirmar no navegador.
2. **Junção sem esperar você:** o segredo `ROTINAS_TOKEN`, pelo `passo-a-passo-juncao.md`. Sem ele, a
   rotina grava todo dia em `rotinas`, e os 7 dias contam.

## Não conferido
- O que conta como atividade contra a desativação de 60 dias (insumo 104).
- Se o commit da rotina passa pela proteção do `main` com o seu token (confere-se na primeira junção).
- Os termos de uso do BCR, do Oasisbr e da OpenAlex (não achados ou só a casca da página).

## Continuação de 05/11 (pedido de Vicente: rodar os workflows; o segredo; contas e chaves)
- O token do gh seguia sem o escopo `workflow`; o pedido de autorização por código foi aberto pelo curador
  e Vicente o confirma no navegador. Depois disso, os workflows vão a `.github/workflows/` e rodam.
- **O segredo `ROTINAS_TOKEN`** não se escreve no arquivo: a linha `TOKEN: ${{ secrets.ROTINAS_TOKEN }}`
  do `rotinas.yml` só o lê pelo nome. O valor (um token fino de Vicente) fica na página de segredos do
  repositório, pelo `passo-a-passo-juncao.md`. Serve só à junção automática ao `main` (D-048).
- **Contas e chaves (insumo 108):** a exigência é da fonte e vale igual para a rotina; login pessoal
  (gov.br, CAFe) não cabe num robô; nenhuma conta se abre por agente ou rotina (parada c do brief, l. 49);
  a chave fica fora do Git (l. 69), como segredo do repositório. O "sem cadastro" da D-048 vale só para o
  Internet Archive; a regra de quando abrir conta vai ao planejamento.

## Primeira rodada no runner (05/11, execução 42019165807) e a D-049
- Workflows no repositório (2b241f3); `validar` e `testar-fichas` passaram; a BDTD e a Infoteca-e abrem no
  runner (gravado nas fichas, 2e22d98). A rodada: 1 Entrada nova da BDTD e 4 da Infoteca-e, estas pela
  CO-0008 (só descritores, sem caju nem cajuína).
- **Os commits 87ae840 e 62e0df8 da ramificação `rotinas` dizem "portão: passa" sem ter passado:** o
  portão reprovou nas duas tentativas (1 caso da suíte) e o `tee` sem pipefail escondeu a reprovação.
  Corrigido no bffd3b4 (bash -eo pipefail; portão reprovado não grava nem tenta junção).
- A junção da tentativa 2 ("Re-run") foi recusada por non-fast-forward: o checkout repetiu o main antigo.
  Endurecido: o workflow busca o main na hora antes do merge e antes da junção, e o main que andou cai em
  "fica para a rodada seguinte".
- O `validar` do bffd3b4 e do 5e8b678 falhou só nos dois casos do verificar-fundacao que pedem o commit
  e868a98 (checkout raso); o `validar.yml` passa a buscar a história inteira. Nenhum outro caso falhou no Linux.
- **D-049 no bloco 10a:** fonte que pede cadastro (conta, chave grátis, login) ou pagamento não entra nas
  rotinas; nenhum segredo de fonte; os adaptadores não leem chave; a OpenAlex sem chave (cursor só dá a
  primeira página; a paginação por página, o rastreador testa). A ordem segue: Oasisbr, OpenAlex, Anexo E.
- **O caso que reprovava o portão** (rodada 42068431829): "Recorte: o teto de chamadas vale para a rodada
  inteira" esperava RC-0003 e recebeu RC-50000, porque a suíte herdava do workflow a faixa de IDs da rotina
  (`CL_GRAVADOR`). Falha do teste no servidor, não do conteúdo de 87ae840 e 62e0df8, que não se revertem:
  `rodar_testes.py` roda os casos sem a variável (o caso da rotina a liga no próprio comando).
- Insumo 111: a contagem de commits à frente do main no relatório do dia sai antes do commit da rodada.

## Próximo (conversa seguinte)
Mover os workflows para `.github/` e enviar; o rastreador (que volta a carregar: a descrição dele estava
quebrada desde o K-111, insumo 105) testa as fichas do BCR, do Oasisbr e da OpenAlex e a tradução da
CO-0008 na BDTD; a resposta real dos adaptadores; o teste no runner; uma rodada pedida à mão; a falha
provocada; ligar o agendamento; depois, os ambientes do Anexo E, em lotes de 4.
