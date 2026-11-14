# RETOMAR — K-114 (kit de fonte primária; bloco 11; D-056)

**14/11/2026:** a D-056 está registrada. O piloto se entrega com o K-114 e depois o K-116. O K-125, o
K-115b e o K-115c estão estacionados (o estado do K-125 em `trilhas/2026-11-14_manutencao/retomar-K-125.md`).
Leitura de uso informada por Vicente em 14/11: semana em 66%, janela de 5 h em 80% (vira por volta das 10h).

## Feito
- D-056 em `trilhas/decisoes/D-056.json`, com a linha no AGENTS.md, o quadro acertado (K-114 em Fazendo) e
  a linha no checklist do piloto.
- A vistoria da casa (`scripts/manutencao.py`) e a limpeza de 14/11.

## Falta
1. **K-114:** o pedido ao campo-de-acao com a habilidade kit-fonte-primaria (Sonnet 5.5 alto, teto de 15
   chamadas, 1 a 2 chamadas previstas), pelos critérios do bloco 11 do brief (l. 381-387): toda afirmação
   sobre a cajuína aponta para uma Proposição da ficha; só fontes do acervo do piloto, com link e nível;
   nenhum dado pessoal de terceiros; o alcance dito; as Faltas à vista; rascunho em `campo_de_acao/`, sem
   publicar. O kit usa só conteúdo sem Falta jurídica aberta (a regra do campo-de-acao vale como está). O
   curador grava o log (`registrar_log.py`) e o par real da habilidade; Vicente revisa o rascunho. Sem
   teste de modelo (D-056).
2. **K-116:** o relatório do piloto, calculado dos logs, escrito pelo redator e conferido pelo auditor
   (bloco 14, "Antes da v0.3"), com o que foi estacionado dito às claras. Fecha a entrega.
3. Depois da entrega: reconfigurar a rotina do Claude do K-113 para propor e reler (D-056, item 4), como
   primeiro ato da operação; a reunião do K-004.

## Próximo comando
Conversa nova em Opus 5.5 médio, depois das 10h: `python scripts/relatorio_dia.py`; a conta com
`python scripts/orcamento.py --a0 66 --janela <leitura> --agente campo-de-acao --habilidade kit-fonte-primaria`;
depois, o pedido do K-114.
