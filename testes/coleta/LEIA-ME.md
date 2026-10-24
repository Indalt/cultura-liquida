# Casos dos scripts da coleta (K-107, bloco 5)

Rodados por `scripts/rodar_testes.py` (`casos.json`). Todos os scripts rodam com `--simular` e `--raiz` numa pasta daqui: nada se grava no acervo real.

## De onde vem cada resposta gravada (fixture)

| Pasta | Origem | O que se tirou |
|---|---|---|
| `fixtures/bdtd/` | respostas reais da API v1 da BDTD em 23/10/2026 (CO-0005 e CO-0003, `limit=100`, e o robots.txt), gravadas por `recorte.py --gravar-fixtures` | nada: o pedido só traz os campos `id` e `urls`, sem autoria |
| `fixtures/oai/` | a primeira página real do ListRecords da Infoteca-e em 23/10/2026 e o robots.txt | recortada aos 4 registros que casam com caju ou cajuína e mais 15; no `oai_dc`, ficam só título, assunto, identificador, data e tipo (saem autoria, descrição e o resto); o resumptionToken vazio e o `completeListSize` trocado por 19, para a página ser a última |
| `fixtures/saturada/` | as de `bdtd/` e duas sintéticas: a resposta real de CO-0005 partida em 5 + 5 registros, uma por metade da janela | o `resultCount` de cada metade é o número de registros dela |
| `fixtures/robots/`, `fixtures/antirobo/`, `fixtures/wayback/` | sintéticas, em hosts `.example` ou com o texto "registro de teste (K-107), sintético"; as de `wayback/` (K-124) são respostas sintéticas da Availability API para handles de teste | não há dado real |

Os registros em `raiz-*` e os quadros `quadro-fila*.md` também são de teste: os IDs da faixa 900000 e os textos marcados como sintéticos. `triagem-teste.json` só existe para o `wayback.py` rodar no teste; a triagem real é a do juridico, na trilha do K-107.
