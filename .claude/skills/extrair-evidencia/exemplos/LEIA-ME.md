# Exemplos de extrair-evidencia (rodada B, K-111)

Pares reais do caso-piloto da cajuína (K-109 e K-110), em `casos-rodada-b.json`. Cada `real-*.json` e `erro-*.json` é um caso que o `testes/rodada-b/caso_real.py` roda sobre uma cópia do acervo do momento (fora do Git, apagada no fim); o erro é injetado na cópia do real (padrão da rodada A).

| Caso | Espera | De onde vem |
|---|---|---|
| `real-tr0001` | passa | TR-0001 (EV-0001, conferida pelo auditor no K-109), relocalizado pelo script |
| `erro-tr0034-palavra-de-outro-trecho` | reprova | erro do brief (trecho não localizado marcado como localizado), com o erro real do achado A5 do K-109 (insumo 72): "fresco" veio de outro trecho |
| `real-tr0101-ligadura` | passa | achado A6 do K-110 (insumo 83): ligadura no texto exato, grau da leitura com "fi" |
| `real-pr0001` / `erro-pr0001-divergente-contada` | passa / reprova | achado A1 do K-109 (insumo 72): a EV-0004 diz menos que a PR-0001; fica fora de μ e λ |
| `real-pr0002` / `erro-pr0002-marca-perdida` | passa / reprova | achado A3 do K-109 (insumo 72): a marca de saúde da Evidência vai à Proposição |
| `erro-tr0505-rotulo-sem-palavra` (comando sobre `erro-tr0505-separadas.json`) | reprova | insumo 88: "mocororó" declarado num trecho da p. 100 que não traz a palavra (o erro real do K-110) |

**Fonte reduzida à janela.** Nos casos de Trecho, a fonte é a janela de citação que já está no Git (antes + texto exato + depois); o texto integral nunca entra no repositório (l. 100). O caso confere o script de localização, não a captura: a captura se confere com o `localizar_trecho.py conferir` sobre a fonte, na pasta temporária.

**O que o piloto deu e nenhum script pega** (não contam como par de script; ficam com a leitura do auditor, eixo 3): A2 (voz atribuída a autor citado na frase vizinha, EV-0005) e A4 (qualificativo perdido no valor, PR-0003, "bom teor de"). A regra está na habilidade (passos 5 e 6).
