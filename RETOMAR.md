# RETOMAR — K-125 (rotina com IA na API do Gemini; D-054)

> **14/11, conversa de limpeza (sem agentes):** antes de retomar o K-125, ler
> `trilhas/planejamento/caminho-entrega-piloto.md`. É uma [PROPOSTA] à espera de Vicente: entregar o piloto
> com o K-114 e o K-116 e estacionar o K-125, o K-115b e o K-115c. Se ele confirmar a essência (seção 6 do
> arquivo), o primeiro passo é registrar a D-056 (habilidade registrar-decisao), acertar o quadro e abrir o
> K-114. Se não, vale o que está abaixo. Feito nesta conversa: `scripts/manutencao.py` (vistoria da casa,
> sem IA, com casos em `testes/manutencao/`), o Passo corrente do AGENTS.md enxugado (o texto antigo em
> `trilhas/2026-11-14_manutencao/`), a tabela de modelos acertada, o arquivo solto `-` fora do Git e o
> insumo 135.

Conversa 2, continuação (13/11/2026, noite): **D-055** registrada. A segunda leitura fica com o Claude Opus 5.5
médio, numa rotina do Claude Code que roda depois da rotina do Gemini. Essa rotina está ligada: sextas às 03h UTC,
`trig_01VTM4aiUKUFmwewkJTtuem1`, roteiro `ambientes/rotinas-ia/segunda-leitura.md`. O workflow do Gemini fica
desligado no GitHub até o teste à mão e o segredo.

**14/11:** Vicente mandou ignorar as medições e retomar (tetos de 50 e 60 pp suspensos; fica a linha de 90%). Provas do hydrogen: ee r3 e rt r1 reprovam pelo teto de chamadas gasto em leituras uma a uma; mf sem cota do dia. Executor 0.6 com `ler_varios` e `rodar_varios`. Semana do Gemini em 76% da entrada: as próximas provas depois de 18/11, 23h (cota do hydrogen: 20 pedidos por dia, desde 05h de Brasília).

## Feito
- `scripts/gemini_agente.py` 0.4: ferramentas restritas, teto de chamadas, histórico encurtado, contador semanal
  (`trilhas/rotina-ia/consumo-gemini.jsonl`; `--semana`), cota diária (código 4), `--ler-tambem`, `--log` e o
  **ritmo** pelos limites da tela do dono (`ambientes/rotinas-ia/limites-gemini.json`).
- `.github/workflows/rotina-ia-gemini.yml` (escrito, não testado), `rotina_ia.py` 0.2, vigia com o autor novo,
  `ambientes/rotinas-ia/rotinas.json` 0.2 (rotina "gemini", lote 5).
- Provas: ee/hydrogen rodada 1 reprova; rodada 2 interrompida pela cota; gg/argon recusada (sem cota);
  gg/gemini-3.8-flash reprova (gastou o teto sem gravar; EX-0147).
- D-055, a rotina da segunda leitura (Claude) ligada, o workflow do Gemini só com o avaliador e a marca, `rotina_ia.py` 0.3, `rotinas.json` 0.3.
- Semana do Gemini (desde 11/11, 23h): 478.557 de entrada (48% do teto), 43.678 de saída.

## Falta
1. As provas do hydrogen (ee, rt e mf), com o reforço do harness pela l. 698 se reprovar, espalhadas por dias
   (20 pedidos por dia). As provas gg e tj ficam com o Claude (D-055), sem prova no Gemini.
2. O teste à mão do workflow numa ramificação local, sem enviar: preparar, avaliador no hydrogen, filtrar e
   gravar, a marca; depois, `reler`, `amostra` e o auditor como a rotina do Claude faria.
3. O passo de dono: o segredo `GEMINI_API_KEY` no repositório (guiado); depois, `gh workflow enable rotina-ia-gemini.yml`.
4. A rodada no Actions (`gh workflow run rotina-ia-gemini.yml`), depois a rotina do Claude (`RemoteTrigger run`),
   o portão e a junção; o consumo medido dos dois lados.

## Próximo comando
`python scripts/relatorio_dia.py`; `python scripts/gemini_agente.py --semana`.
