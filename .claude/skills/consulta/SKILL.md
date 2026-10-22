---
name: consulta
description: Roda uma consulta num ambiente de busca do projeto Cultura Líquida (termo + variantes + descritores processuais, na sintaxe do ambiente) e grava o estado — total informado, total visto, cursor, saturação, erros e próxima ação — e as pegadas (IDs já vistos). Bola de neve pelas citações só na fase 2. Use para monitoramento e escavação, sem teto de coleta.
---

# consulta

**Versão do harness:** 0.1.1 · **Quem usa:** rastreador · **Rodada:** B

## Objetivo
Saber, para cada consulta, quanto o ambiente diz ter, quanto já vimos e o que falta, para que nenhuma fonte seja dada como esgotada cedo demais (D-016: os "15" são lote de tratamento, nunca teto).

## Quando usar / quando não usar
- **Usar:** a partir do caso-piloto (Passo 1) e no Passo 4; para monitoramento (novidade = ID ainda não visto nas pegadas, nunca por data; l. 428) e escavação (paginação completa).
- **Não usar:** em ambiente sem ficha de acesso (`ficha-de-acesso` primeiro); em ambiente que bloqueia robôs.

## Entradas e saídas
- **Entrada:** termo e variantes (da terminologia), ambiente (do Anexo E da Fundação e da ficha em `ambientes/`, que é a fonte de trabalho a partir do bloco 2 do brief), modo (monitoramento ou escavação), cursor anterior e pegadas.
- **Saída:** estado da consulta: `ambiente`, `consulta` (texto exato enviado), `data`, `total_informado`, `total_visto`, `cursor`, `saturacao`, `erros`, `proxima_acao`, `resultados_novos` (IDs e links, nunca texto integral). `bola_de_neve` (citadas e citantes) só na fase 2 (l. 438; §6, Recorte, l. 592). **Esquema:** pendente; o contrato de Consulta (§6) é entrega do Passo 1.

## Passos
1. Monte a consulta na sintaxe do ambiente (ficha de acesso). País e idioma **nunca** recortam: só anotam (PA-4).
2. Peça o total antes de paginar (ex.: `limit=0` ou `per_page=1`).
3. Pagine com o cursor do ambiente, em ritmo baixo, gravando o cursor a cada página.
4. Compare os IDs com as pegadas; anote só os novos. A novidade é sempre pelo ID não visto, nunca pela data (l. 428): fonte que reindexa ou corrige datas não esconde item.
5. Bola de neve (PA-3): **só na fase 2** (l. 438; §6, Recorte, l. 592). Na fase 1, o Recorte fica "percorrido pela busca" sem ela.
6. Grave o estado e a próxima ação. Termine com o bloco LOG.

## Critérios de aceitação
- O total informado e a data aparecem; o total visto nunca passa do informado sem explicação.
- O ambiente só fica "exaurido" quando tudo o que cada consulta informa foi visto (e, na fase 2, a bola de neve não traz nada novo); variante nova reabre o ambiente.
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
`agente: "rastreador"`, `habilidade: "consulta"`, `entrada_ref` (ambiente + consulta), `acoes` (pedidos), `resultados` (totais), `decisoes` (resultados novos aceitos para triagem; ruído `descartado` com motivo), `ambientes`, `consultas` e `recortes` usados (l. 593), `erros`, `alcance` (total informado × visto, páginas abertas, o que ficou fora; D-030).

## Exemplos (reais, da pesquisa de 15/10)
- [exemplos/cauim-totais.json](exemplos/cauim-totais.json): "cauim" → 54 no OpenAlex, 10 na BDTD, 30 no Oasisbr, 12 na Crossref; e a bola de neve do artigo do Boletim Goeldi (8 trabalhos que o citam; 22 referências).
- Casos (validador pendente): [exemplos/casos.json](exemplos/casos.json).

## Histórico
- 0.1.1 (22/10/2026, K-101): bola de neve só na fase 2 (l. 438, 592); novidade por ID não visto, nunca por data (l. 428); entrada pelo Anexo E e por `ambientes/`; Ambientes, Consultas, Recortes e alcance no log.
- 0.1.0 (16/10/2026): papel, formato, passos e exemplo real; esquema pendente do Passo 1.
