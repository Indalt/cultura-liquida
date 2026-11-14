# RETOMAR — K-114 (kit de fonte primária; bloco 11; D-056)

**14/11/2026:** a D-056 está registrada. O piloto se entrega com o K-114 e depois o K-116. O K-125, o
K-115b e o K-115c estão estacionados (o estado do K-125 em `trilhas/2026-11-14_manutencao/retomar-K-125.md`).
Leitura de uso informada por Vicente em 14/11: semana em 66%, janela de 5 h em 80% (vira por volta das 10h).

## Feito
- D-056 em `trilhas/decisoes/D-056.json`, com a linha no AGENTS.md, o quadro acertado (K-114 em Fazendo) e
  a linha no checklist do piloto.
- A vistoria da casa (`scripts/manutencao.py`) e a limpeza de 14/11.

## Feito em 14/11 (conversa 1 do K-114, janela de 5 h em 83%: um lote só)
- O rascunho do kit em `campo_de_acao/kit-fonte-primaria-cajuina.md` (campo-de-acao, EX-0151, 103.960 tokens,
  14 chamadas); o caso real e dois casos que reprovam em `.claude/skills/kit-fonte-primaria/exemplos/casos.json`;
  a linha da conversa na tabela "Semana da conta" e a linha do K-114 no checklist.

## Falta
1. **K-114 (fecho):** Vicente revisa o rascunho (pronto-quando do bloco 11). Antes, o curador confere, sem
   agente, os quatro pontos do agente: (a) a Falta da escuta de comunidades, do K-110, que o agente não achou
   (`grep -rn "escuta" acervo/faltas trilhas/logs`); (b) as 8 perguntas do formulário (P53), se o kit deve
   trazê-las; (c) se a F-0032 alcança EV-0128 e EV-0403 (PR-0100, seção 6.4 do kit), para o juridico se a
   leitura não bastar; (d) a licença das fontes, "não conferido" (fica dito). As correções vão ao rascunho, e o
   K-114 fecha no quadro.
2. **K-116:** o relatório do piloto, calculado dos logs, escrito pelo redator e conferido pelo auditor
   (bloco 14, "Antes da v0.3"), com o que foi estacionado dito às claras. Fecha a entrega.
3. Depois da entrega: reconfigurar a rotina do Claude do K-113 para propor e reler (D-056, item 4), como
   primeiro ato da operação; a reunião do K-004.

## Próximo comando
Conversa nova em Opus 5.5 médio, com a janela de 5 h renovada: `python scripts/relatorio_dia.py`; conferir os
pontos (a) a (d) do item 1; levar o rascunho a Vicente. O `orcamento.py` ainda soma os tetos de 50 e 60 pp, que
Vicente suspendeu em 14/11: vale só a linha de 90%.
