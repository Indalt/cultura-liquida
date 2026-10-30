# Exemplos de registrar-termo (rodada B, K-111)

Pares reais do caso-piloto (K-106, K-110 e K-102), em `casos-rodada-b.json`, rodados pelo `testes/rodada-b/caso_real.py` sobre uma cópia do acervo do momento (fora do Git).

| Caso | Espera | De onde vem |
|---|---|---|
| `real-te0002` | passa | TE-0002 (cajuína), atestado no K-110; com o TE-0004, que divide a forma "mocororó" (termo ambíguo, D-039); valida e gera os booleanos |
| `erro-te0002-ocr-variante` | reprova | erro do brief: forma de OCR ("cajuina", forma de busca) registrada como variante |
| `erro-te0002-ambiguo-sem-marca` | reprova | insumos 26 e 88: "mocororó" como designação local, sem a marca de termo ambíguo (o erro do K-110, que tratou a forma como nome de uma CLB só); regra do `validar_acervo.py` acervo-0.4, item 12 |

Não dado pelo piloto: a língua da designação (nenhuma fonte a deu; insumo 30): os casos de língua ficam como exemplo de esquema em `esquemas/exemplos/`.
