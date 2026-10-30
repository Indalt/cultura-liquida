# Exemplos de gerar-grafo (rodada B, K-111)

Pares reais do caso-piloto (K-110), em `casos-rodada-b.json`, rodados pelo `testes/rodada-b/caso_real.py` sobre uma cópia do acervo do momento (fora do Git), com o `calcular_mu_lambda.py --conferir`.

| Caso | Espera | De onde vem |
|---|---|---|
| `real-pr0016` | passa | PR-0016: duas linhagens a favor (FO-0008 e FO-0009), μ 1,0 |
| `erro-pr0016-mesma-linhagem` | reprova | erro do brief: a FO-0009 derivada da FO-0008 e o μ gravado contando as duas |
| `real-pr0065` | passa | PR-0065: tensão interna de linhagem (FO-0032 e FO-0034), fora de μ e λ (D-041) |
| `erro-pr0065-tensao-apagada` | reprova | a tensão interna escondida |

Não dado pelo piloto: nenhuma Proposição ficou "inconsistente" nem "falsa" (371 intermediárias, 52 verdadeiras, 4 paracompletas em 30/10/2026); o cartão de conflito segue testado só com exemplo de esquema (`testes/coleta/`, fila), sem par real (brief, seção 6C, item 7).
