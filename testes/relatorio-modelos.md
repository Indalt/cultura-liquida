# Relatório de modelos (bloco 12 do brief de execuções)

**Cartões:** K-115a (esta parte), K-115b e K-115c (D-053). **Regra (Fundação, l. 698; D-027):** cada habilidade roda nos modelos candidatos sobre pares reais; fica o mais barato que passa nos validadores; se falha, reforça-se o harness antes de subir de modelo.

## Como o teste é feito
- **Modelo por chamada:** a ferramenta Agent recebe `model` (alias `haiku` ou `sonnet`) por chamada, com precedência sobre o frontmatter (C115.1, oficial: `trilhas/2026-11-12_K-115a/conferencia-c115.json`). O frontmatter só muda no fecho de cada parte, para os agentes testados por inteiro. O esforço segue o do frontmatter (`high`), que vale também no modelo trocado (C115.3).
- **Banco de provas:** `testes/modelos/banco.py` (banco-0.1). Cada prova toma a entrada real de um par num commit fixo (`288c4b0`, por `git archive`), não do acervo do momento, porque a rotina diária muda registros (insumo 119). O agente trabalha numa pasta fora do repositório; a saída passa pelos mesmos validadores da habilidade e pelo confronto com a saída real do par (o gabarito, lido da base, fora da pasta do agente). O pedido é o mesmo para cada modelo (`testes/modelos/provas/<prova>.md`, com `_comum.md`), com o mesmo teto de chamadas (insumo 15). O banco confere a si mesmo: a saída real de cada par passa e a saída com o erro da prova reprova (`banco.py casos`, OK 10 · FALHA 0).
- **Registros de teste:** a `entrada_ref` do log começa por `[teste de modelo]`; o `orcamento.py` não os usa como estimativa de lote, e o relatório do piloto (K-116) e a calibração do K-005 também não os contam como produção (D-051, D-053).
- **Custo:** os tokens e as chamadas são os do retorno do Agent. Por token, o Haiku 5.5 custa cerca de 1/20 do Sonnet 5.5 na API (C115.4, oficial); o peso de cada modelo no limite da assinatura não foi conferido.

## As provas da parte 1 (K-115a)
| Prova | Habilidade | Par real | O que se confere |
|---|---|---|---|
| `ee-en1369-en1544` | extrair-evidencia | K-109, lote 1: EN-1369 e EN-1544 (TR-0031 a TR-0035, TR-0038 a TR-0042) | cada Trecho relocalizado pelo script; o lote passa no `gravar_extracao.py --simular` (esquemas de Fonte, Trecho, Evidência, Proposição e Entrada); os 10 Trechos reais cobertos |
| `rt-te0002` | registrar-termo | K-110: TE-0002 (cajuína) | `validar_acervo.py` (termo ambíguo marcado, forma de OCR fora das variantes) e `gerar_termo.py`; estado, designação, a variante "mocororó" e as abonações só das Evidências dadas |
| `mf-cl0001-temporalidade` | montar-ficha | K-110: a seção Temporalidade da ficha CL-0001 (17 Proposições) | `validar_acervo.py` (toda frase com a marca da Proposição); as 17 marcadas, nenhuma fora; o μ citado bate com a Proposição |
| `gg-pr0042-cadeia` | gerar-grafo | K-110: a cadeia de etapas da PR-0042 e PR-0059 (6 Elementos, 5 Arestas) | `validar_acervo.py` e `calcular_mu_lambda.py --conferir`; a cadeia com os processos na ordem real, X e W reais, 5 Arestas |
| `tj-tr0018` | triagem-juridica | K-109 e D-047: a F-0024 (TR-0018), e TR-0494, TR-0100 e TR-0031 sem Falta pela regra | cada Falta pelo esquema; Falta de conhecimento tradicional só para publicar no TR-0018; nenhuma que barre agora; nenhuma só sobre os três de controle |

## Tabela (calculada dos logs por `testes/modelos/relatorio.py`)
