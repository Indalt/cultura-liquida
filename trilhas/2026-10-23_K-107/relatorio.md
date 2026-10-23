# K-107 — Bloco 5: adaptadores, Recorte, deduplicação, modo assistido, entrada por link e Wayback

Conversa de 23/10/2026, desenvolvimento, Opus 5.5 médio. O relatório não pede aprovação (l. 512 relida pela D-037).

## O que se fez
- **Scripts** (`scripts/`): `_coleta.py` (robô identificado, robots.txt, 1 pedido por segundo, anti-robô sem contornar, Execução com alcance no log); `adaptador_vufind.py` e `adaptador_oai.py`; `ambientes/adaptadores.json` (uma linha por ambiente); `recorte.py`; `deduplicar.py`; `assistido.py`; `entrada_link.py`; `wayback.py`; `fila_curadoria.py`; `pegadas.py`; `relatorio_dia.py`. Entrada 0.2.0 (`identificador`, `localizador`); `vale_para` na Falta.
- **Testes:** 25 casos em `testes/coleta/` (respostas reais da BDTD e da Infoteca-e sem autoria; procedência em `LEIA-ME.md`). `rodar_testes.py`: OK 162 · FALHA 0 · PENDENTE 5.
- **Rodada real curta:** BDTD, CO-0005 e CO-0003 percorridos (10 de 10; 80 de 80); Infoteca-e, uma colheita de 300 dos 59.357 registros para as cinco Consultas, interrompida por teto com o cursor salvo. **83 Entradas**, sem duplicata, depois da chave do handle local (a primeira rodada, descartada antes do commit, deixara quatro itens da BDTD em dois registros).

## O que entrou, a quarentena e as Faltas novas
- **Entraram:** 83 Entradas brutas (77 da BDTD, 6 da Infoteca-e) e 7 Recortes (2 percorridos, 5 interrompidos por teto). Quarentena: nenhuma (a triagem é do bloco 7).
- **Faltas novas:** F-0004 (jurídica, Lei 9.610, art. 29: barra a captura no Wayback em si), F-0005 (os termos do Internet Archive não lidos), F-0006 a F-0010 (busca interrompida por teto na Infoteca-e).
- **Cartão na operação:** K-202, a F-0004 a liberar, que chama Vicente. Fila: 1 de 15.

## Agentes e consumo
- juridico, triagem-juridica: 46.107 tokens, 9 chamadas (EX-0021).
- auditor, segunda leitura do código: 194.329 tokens, 15 chamadas (EX-0024); 16 achados, 14 corrigidos e 2 em parte (`achados-auditor.json`).
- Total: 240.436 tokens em 24 chamadas. Estimativa da conta (não é medida): 5,8 pp; a medida vem da abertura seguinte.

## Não feito ou não conferido
- Nenhuma captura real no Wayback (F-0004). O modo assistido e a entrada por link não têm registro real: são de Vicente, no bloco 6.
- Não conferidos: os termos do Internet Archive e a documentação oficial do SPN2; o limite de resultados da BDTD e o filtro de período na fonte real; o host dos links permanentes da Hemeroteca.
- Insumos 44 a 49.

## Arquivos desta trilha
`triagem-wayback.json`, `achados-auditor.json`, `relatorio-lote-2.md`, `pegadas.md`, `relatorio-dia.md`.
