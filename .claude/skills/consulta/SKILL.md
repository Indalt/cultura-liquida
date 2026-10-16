---
name: consulta
description: Roda uma consulta num ambiente de busca do projeto Cultura Líquida (termo + variantes + descritores processuais, na sintaxe do ambiente) e grava o estado — total informado, total visto, cursor, saturação, erros e próxima ação — mais a bola de neve pelas citações. Use para monitoramento e escavação, sem teto de coleta.
---

# consulta

**Versão do harness:** 0.1.0 · **Quem usa:** rastreador · **Rodada:** B

## Objetivo
Saber, para cada consulta, quanto o ambiente diz ter, quanto já vimos e o que falta, para que nenhuma fonte seja dada como esgotada cedo demais (D-016: os "15" são lote de tratamento, nunca teto).

## Quando usar / quando não usar
- **Usar:** a partir do caso-piloto (Passo 1) e no Passo 4; para monitoramento (novidades por data) e escavação (paginação completa).
- **Não usar:** em ambiente sem ficha de acesso (`ficha-de-acesso` primeiro); em ambiente que bloqueia robôs.

## Entradas e saídas
- **Entrada:** termo e variantes (da terminologia), ambiente (ficha de acesso), modo (monitoramento ou escavação), cursor anterior.
- **Saída:** estado da consulta: `ambiente`, `consulta` (texto exato enviado), `data`, `total_informado`, `total_visto`, `cursor`, `saturacao`, `erros`, `proxima_acao`, `resultados_novos` (IDs e links, nunca texto integral), `bola_de_neve` (citadas e citantes). **Esquema:** pendente; o contrato de Consulta (§6) é entrega do Passo 1.

## Passos
1. Monte a consulta na sintaxe do ambiente (ficha de acesso). País e idioma **nunca** recortam: só anotam (PA-4).
2. Peça o total antes de paginar (ex.: `limit=0` ou `per_page=1`).
3. Pagine com o cursor do ambiente, em ritmo baixo, gravando o cursor a cada página.
4. Compare os IDs com as pegadas; anote só os novos.
5. Bola de neve (PA-3): para cada fonte admitida com trecho localizado, peça ao OpenAlex o que ela cita e quem a cita.
6. Grave o estado e a próxima ação. Termine com o bloco LOG.

## Critérios de aceitação
- O total informado e a data aparecem; o total visto nunca passa do informado sem explicação.
- O ambiente só fica "exaurido" quando tudo o que cada consulta informa foi visto e a bola de neve não traz nada novo; variante nova reabre o ambiente.
- Ruído (itens sem relação) é anotado, não apagado.

## Regras herdadas
- **Nível:** totais com URL da consulta e data.
- **Essência:** D-016 e D-017.
- **Dado pessoal:** não registrar autor de post ou perfil; em redes sociais, só link enviado por pessoa.
- **Anti-robô:** bloqueio interrompe a consulta e vira registro.
- **Falta dita:** o que não se conseguiu ver é vácuo registrado.

## Teto e custo
Teto de chamadas informado pelo curador por lote; ao chegar nele, grava o cursor e para. Estimativa a medir no caso-piloto (Sonnet 5.5 alto, a testar contra o Haiku 5.5).

## Critério de parada
Total informado visto; ou teto de chamadas (cursor gravado); ou bloqueio.

## O que não faz
Não avalia relevância (isso é do avaliador), não guarda texto integral de terceiros, não recorta por país ou idioma, não contorna bloqueio.

## Campos do log
`agente: "rastreador"`, `habilidade: "consulta"`, `entrada_ref` (ambiente + consulta), `acoes` (pedidos), `resultados` (totais), `decisoes` (resultados novos aceitos para triagem; ruído `descartado` com motivo), `erros`.

## Exemplos (reais, da pesquisa de 15/10)
- [exemplos/cauim-totais.json](exemplos/cauim-totais.json): "cauim" → 54 no OpenAlex, 10 na BDTD, 30 no Oasisbr, 12 na Crossref; e a bola de neve do artigo do Boletim Goeldi (8 trabalhos que o citam; 22 referências).
- Casos (validador pendente): [exemplos/casos.json](exemplos/casos.json).

## Histórico
- 0.1.0 (16/10/2026): papel, formato, passos e exemplo real; esquema pendente do Passo 1.
