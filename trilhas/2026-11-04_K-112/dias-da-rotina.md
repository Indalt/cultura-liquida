# K-112: os dias da rotina diária sem IA (05 a 12/11/2026)

Fonte: `gh run list --workflow rotinas.yml` (lido em 12/11) e os relatórios do dia em `trilhas/relatorios/`.
Os dias de erro ficam aqui como informação: mostram o que pode falhar na rotina e como se consertou.

| Dia | Execução (Actions) | Como | Resultado | Causa e conserto |
|---|---|---|---|---|
| 05/11 | 42019165807 | à mão | passou, mas o portão tinha reprovado | `tee` sem pipefail escondeu a reprovação; commits 87ae840 e 62e0df8 de `rotinas` dizem "passa" sem ter passado; corrigido no bffd3b4 |
| 05/11 | 42068431829 | à mão | falha | caso da suíte com a faixa de IDs da rotina (`CL_GRAVADOR`); corrigido no 467d9b5 |
| 05/11 | 42070639701 | à mão | portão passa; junção recusada | proteção do `main` exigia pull request; Vicente mudou a proteção |
| 05/11 | 42072270905 | à mão | falha provocada | aviso por e-mail chegou a Vicente (pronto-quando) |
| 05/11 | 42116185819 | à mão | passou e juntou ao `main` | primeira junção (1c9df40) |
| 06/11 | 42255111696 | agendada | passou | relatório no Issue #1 |
| 07/11 | 42387359215 | agendada | passou | relatório no Issue #1 |
| 08/11 | 42490655777 | à mão | passou | e-mail do relatório confirmado por Vicente (Issue atribuído a ele) |
| 08/11 | 42493664560 | à mão | falha | conferência das pegadas não aceitava o item do agregador (Oasisbr) ligado pelo link; corrigido no 93540aa |
| 08/11 | 42494850740 | à mão | portão passa, juntou 1.028 Entradas; rotina com erro | ID do Oasisbr com espaço; corrigido no 1fcb938 |
| 08/11 | 42497353480 | agendada | passou | |
| 09/11 | 42686550279 | agendada | falha | (1) a coleta quebrou com "EN-0212 já é de outro item" (a pegada da chave do agregador apontava a Entrada achada pelo link noutro dia); (2) com a rodada interrompida, o caso do RC-0010 passou e o portão reprovou; nada gravado |
| 10/11 | 42860363809 | agendada | falha | as mesmas duas causas; nada gravado |
| 11/11 | 43064621599 | agendada | falha | as mesmas duas causas; nada gravado |
| 12/11 | 43195921492 | à mão | falha | causa (1) consertada no 6dd5d99 (349 Entradas novas na rodada); o caso do RC-0010 seguiu passando: a rotina grava `explicacao_total_visto` no RC-0010 real; nada gravado |
| 12/11 | 43203545917 | à mão | **passou e juntou ao `main`** (350 Entradas novas; portão OK 257 · FALHA 0) | o caso tira a explicação (ff8fd66) |

O que se aprende: os casos da suíte que leem registros reais do acervo quebram quando a rotina muda esses
registros; um agregador (Oasisbr) traz o mesmo item por chaves e links diferentes, e a deduplicação tem de
ligar os dois em dias diferentes; a falha de uma rodada não grava nada e avisa por e-mail, como planejado.
