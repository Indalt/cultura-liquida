---
name: registrar-melhoria
description: Anota um insumo para o planejamento de melhorias do projeto Cultura Líquida — o que surgiu numa sessão ou numa rotina e não se explora ali — num formato fixo (data, origem por apontamento, insumo, aonde se quer chegar, frente e cartão proposto), validado em esquemas/insumo.schema.json e gravado por scripts/registrar_melhoria.py em trilhas/insumos-planejamento.md e na seção 6 do mapa das três frentes. Use no fechamento de cada lote e sempre que algo fora do cartão aparecer.
---

# registrar-melhoria

**Versão do harness:** 0.1.0 · **Quem usa:** curador e toda sessão das três frentes; a rotina, pelo script, sem IA · **Rodada:** A

## Objetivo
Que o que surge no meio do trabalho chegue ao planejamento sem ser explorado ali (D-035) e sempre no mesmo formato (D-036; insumo 10; P36, a consolidação ao fim de cada etapa). É a primeira habilidade do agente de melhorias e contribuições (K-006).

## Quando usar / quando não usar
- **Usar:** no fechamento de cada lote e de cada cartão (brief, seção 3a, item 7); quando aparece algo fora do cartão em curso: um achado sobre a ferramenta, uma medida que contraria a estimativa, uma regra com duas leituras, uma ideia de Vicente que ainda não é decisão; quando a amostra que audita a ferramenta acha algo que vai além do lote de correção (D-037, diretriz 2).
- **Não usar:** para decisão (é a `registrar-decisao`, com a essência confirmada por Vicente); para o que o conteúdo da base pede a Vicente (é cartão de conflito ou de Falta jurídica a liberar, na frente de operação; D-037, diretriz 1); para o que o cartão em curso já resolve; para explorar o insumo ou propor a solução como decidida.

## Entradas e saídas
- **Entrada:** o que se viu e onde (arquivo e linha, achado, log ou commit).
- **Saída:** um objeto válido em `esquemas/insumo.schema.json`: `data`, `origem`, `insumo`, `aonde`, `rotulo`, `frente` (P, D, O), `vira` (K-nnn, V-nn ou "a definir pelo planejamento") e `sem_explorar: true`. Só esses campos. O script dá o número e grava uma linha em `trilhas/insumos-planejamento.md` e outra na seção 6 de `trilhas/planejamento/mapa-tres-frentes.md`.

## Passos
1. **Confira se já está anotado.** Leia as entradas abertas de `trilhas/insumos-planejamento.md` (`grep -n` por palavras-chave). Se o assunto já tem insumo, não abra outro: aponte o número no log. O script só recusa o texto idêntico; a repetição pelo sentido é com quem anota.
2. **Escreva o insumo sem explorar:** o que se viu, em uma ou duas frases, com o número que houver; nada de solução tratada como decidida.
3. **Origem por apontamento:** cartão ou rotina, e arquivo com linha ou seção, achado ou commit. Fala de Vicente só por referência, nunca transcrita.
4. **Aonde se quer chegar:** o resultado esperado, não o caminho.
5. **Frente e cartão:** as frentes que o insumo toca (D-036) e o cartão do quadro ou o item de `proxima-versao.md` que o levaria. Quem anota propõe; o planejamento confirma. Sem cartão claro, "a definir pelo planejamento".
6. **Grave o objeto** num arquivo JSON (Write, sem heredoc) e confira: `python scripts/registrar_melhoria.py <arquivo> --simular`.
7. **Grave de verdade:** `python scripts/registrar_melhoria.py <arquivo>`. Anote o número no log da sessão e no checklist do bloco. O arquivo JSON é de trabalho: fica no scratchpad, fora do Git.
8. **Na rotina:** o mesmo script, sem IA, com o objeto montado pela rotina; a gravação segue o caminho da rotina (bloco 10 do brief; junção pelo portão, D-038).

## Regras herdadas
- **Nível:** fato novo no insumo traz URL e nível, ou "não conferido".
- **Essência:** insumo não é decisão; o que for regra nova vai a Vicente pela `registrar-decisao`.
- **Dado pessoal:** nada de terceiros; o script recusa.
- **Anti-robô:** não se aplica.
- **Falta dita:** o que não se olhou para anotar o insumo fica dito no alcance do log (D-030).

## Teto e custo
Sem web e sem subagente. Custo só de quem anota; o script não usa IA.

## Critério de parada
Insumo gravado com número; ou recusado pelo script, com o motivo no log. Se a tabela de insumos e a seção 6 do mapa estiverem fora de sincronia, o script recusa: acertar as duas antes de anotar, ou anotar o motivo no log e deixar para o planejamento.

## O que não faz
Não explora o insumo, não decide o cartão por conta própria (só propõe), não fecha insumo (ele fica aberto até o cartão que o leva ser concluído), não edita insumo já gravado.

## Campos do log
`agente` (quem anotou), `habilidade: "registrar-melhoria"`, `entrada_ref` (origem do insumo), `acoes` (conferência de repetição, simulação, gravação), `resultados` (número do insumo), `decisoes` (`aceito` ou `descartado`, com motivo: repetido, recusado pelo script), `erros`, `alcance` (o que se leu para anotar e o que ficou fora).

## Exemplos e validador
- [exemplos/insumo-22-no-formato.json](exemplos/insumo-22-no-formato.json): o insumo 22 (K-003) reescrito no formato fixo. **Passa** no esquema e na simulação do script.
- [exemplos/erro-explorado-e-campo-inventado.json](exemplos/erro-explorado-e-campo-inventado.json): insumo explorado na sessão, com um campo fora da lista. **Reprova.**
- [exemplos/erro-repetido.json](exemplos/erro-repetido.json): o texto do insumo 26 de novo. **Reprova** no script.
- [exemplos/erro-dado-pessoal.json](exemplos/erro-dado-pessoal.json): e-mail fictício de terceiro. **Reprova** no script.
- Validadores: `scripts/validar.py insumo` e `scripts/registrar_melhoria.py --simular`. Casos: [exemplos/casos.json](exemplos/casos.json).

## Histórico
- 0.1.0 (22/10/2026): primeira versão (K-103).
