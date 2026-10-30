# Exemplos de montar-ficha (rodada B, K-111)

Pares reais do caso-piloto (K-110), em `casos-rodada-b.json`, rodados pelo `testes/rodada-b/caso_real.py` sobre uma cópia do acervo do momento (fora do Git).

| Caso | Espera | De onde vem |
|---|---|---|
| `real-cl0001` | passa | a ficha `acervo/fichas/CL-0001.md`, com as Proposições que ela marca |
| `erro-cl0001-frase-sem-proposicao` | reprova | erro do brief: a frase da PR-0402 sem a marca |
| `real-educacao-cl0001` | passa | a camada Educação (`acervo/fichas/educacao/CL-0001.md`), pela regra educacao-0.1 (insumo 80; `validar_acervo.py` acervo-0.4, item 14) |
| `erro-educacao-bncc-sem-pagina` | reprova | insumo 80: habilidade da BNCC sem a página do PDF oficial |

Não dado pelo piloto: a Falta preenchida numa ficha (nenhuma foi); o caso segue como exemplo de esquema (`esquemas/exemplos/`, Falta completada por inferência) e na `triagem-juridica`.
