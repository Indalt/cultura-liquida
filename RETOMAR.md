# RETOMAR — K-112 (bloco 10a), 12/11/2026

Uso ao parar: semana em cerca de 98% (estimativa da linha de uso), janela de 5 h baixa. Parado antes de agentes.

## Feito nesta retomada
- As rodadas agendadas de 09, 10 e 11/11 **falharam** (execuções 42686550279, 42860363809, 43064621599); nada
  delas foi gravado (portão reprovou). Duas causas:
  1. A rotina quebrou no Oasisbr: `EN-0212 já é de outro item` (a pegada de uma chave aponta a Entrada achada
     antes pelo link; o apelido de 08/11 valia só na memória da rodada). **Consertado** neste commit: na coleta,
     `deduplicar.registrar(..., mesmo_item_pela_pegada=True)` acrescenta o Recorte à Entrada que a pegada aponta;
     o `reavaliar_pegadas.py` segue recusando (caso A-001). Suíte local OK 257 · FALHA 0 · PENDENTE 1.
  2. No runner, o caso "consulta: Recorte RC-0010 com o total visto acima do informado, sem explicação" falha
     (o `validar.py` aceita o RC-0010 mudado). Passa na máquina. **Não consertado**: suspeita no
     `testes/rodada-b/caso_real.py`, `indice()` (o primeiro arquivo com o id RC-0010 vence, e a ordem dos
     arquivos no Linux é outra; ver `id_do_registro` e `arquivos_acervo`).

## Falta (D-052; o sétimo dia era 12/11)
1. Consertar a causa 2 e conferir no Linux pelo `validar` (roda a suíte a cada envio), **antes** de pedir rodada
   à mão: cada rodada que falha manda e-mail a Vicente.
2. Uma rodada à mão (`gh workflow run rotinas.yml`) que passe sem falha.
3. Fechamento: boletim do redator (teto de 10), `procurar_dado_pessoal.py --git`, amostra do auditor, insumo das
   fontes que ficaram fora (OpenAlex sem chave; Internet Archive pela F-0034; Anexo E não testado; o que pede
   cadastro ou barra o robô), quadro com o K-112 em Concluído e a rotina na operação.
4. Insumo 115 (data da Entrada pelo relógio) segue aberto.

## Próximo comando
`git pull` e `.venv/Scripts/python.exe testes/rodada-b/caso_real.py` no caso do RC-0010 numa cópia da ramificação `rotinas`.
