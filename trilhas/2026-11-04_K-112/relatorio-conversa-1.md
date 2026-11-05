# K-112, conversa 1 (04 e 05/11/2026): relatório de uma tela

**O cartão segue em Fazendo.** Nada está ligado ainda: a rotina diária está pronta e testada aqui, mas os
workflows não puderam ser enviados ao GitHub (falta um escopo do token, que só Vicente renova).

## O que entrou
- **Camada 1 sem IA** (scripts e casos): agenda pela cadência medida (agenda-0.1), rotina diária que só
  grava com novidade, feed de novidades, checagem de links, portão da camada 1, relatório do dia 0.4,
  faixa própria da rotina nos IDs (50000-89999), teste das fichas no runner, hook SubagentStop sem o
  Python do Windows, `ler_fonte.py` com a cópia arquivada só na falha.
- **Workflows** `validar`, `rotinas` e `testar-fichas`, guardados em `workflows/` desta pasta até o envio.
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

## Próximo (conversa seguinte)
Mover os workflows para `.github/` e enviar; o rastreador (que volta a carregar: a descrição dele estava
quebrada desde o K-111, insumo 105) testa as fichas do BCR, do Oasisbr e da OpenAlex e a tradução da
CO-0008 na BDTD; a resposta real dos adaptadores; o teste no runner; uma rodada pedida à mão; a falha
provocada; ligar o agendamento; depois, os ambientes do Anexo E, em lotes de 4.
