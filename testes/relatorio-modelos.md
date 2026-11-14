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

<!-- tabela gerada por testes/modelos/relatorio.py: não editar à mão -->
| Habilidade | Agente | Modelo | Esforço | Prova | Aprovação | Tokens | Chamadas | Execução |
|---|---|---|---|---|---|---|---|---|
| extrair-evidencia | avaliador | claude-haiku-5-5 | high | ee-en1369-en1544 (rodada 1) | reprova (4 checagem(ns): TR-0032 (EN-1369) NÃO coberto por um Trecho da saída) | 96.849 | 22 | EX-0129 |
| extrair-evidencia | avaliador | claude-haiku-5-5 | high | ee-en1369-en1544 (rodada 2) | reprova (5 checagem(ns): TR-0032 (EN-1369) NÃO coberto por um Trecho da saída) | 108.689 | 22 | EX-0130 |
| extrair-evidencia | avaliador | claude-haiku-5-5 | high | ee-en1369-en1544 (rodada 3) | passa | 131.465 | 25 | EX-0131 |
| gerar-grafo | arquivista | claude-haiku-5-5 | high | gg-pr0042-cadeia (rodada 1) | reprova (4 checagem(ns): scripts/validar_acervo.py: código 1: ERRO acervo\faltas\F-0031.json: /onde_aparece/0 apont) | 155.681 | 20 | EX-0134 |
| gerar-grafo | arquivista | claude-haiku-5-5 | high | gg-pr0042-cadeia (rodada 2) | reprova (1 checagem(ns): X de cada Elemento = ['IN-0001']) | 158.529 | 19 | EX-0135 |
| gerar-grafo | arquivista | claude-sonnet-5-5 | high | gg-pr0042-cadeia (rodada 1) | passa | 81.323 | 12 | EX-0136 |
| montar-ficha | arquivista | claude-haiku-5-5 | high | mf-cl0001-temporalidade (rodada 1) | passa | 139.247 | 18 | EX-0133 |
| registrar-termo | arquivista | claude-haiku-5-5 | high | rt-te0002 (rodada 1) | passa | 115.825 | 15 | EX-0132 |
| triagem-juridica | juridico | claude-haiku-5-5 | high | tj-tr0018 (rodada 1) | reprova (2 checagem(ns): Falta conhecimento_tradicional / publicar no TR-0018: 0) | 108.338 | 14 | EX-0137 |
| triagem-juridica | juridico | claude-haiku-5-5 | high | tj-tr0018 (rodada 2) | reprova (1 checagem(ns): nenhuma Falta só sobre os itens sem Falta pela regra ['TR-0494', 'TR-0100', 'TR-0031']; ac) | 127.077 | 14 | EX-0138 |
| triagem-juridica | juridico | claude-sonnet-5-5 | high | tj-tr0018 (rodada 1) | passa | 65.298 | 9 | EX-0139 |

| Habilidade | Modelo mais barato que passa |
|---|---|
| extrair-evidencia | claude-haiku-5-5 |
| gerar-grafo | claude-sonnet-5-5 |
| montar-ficha | claude-haiku-5-5 |
| registrar-termo | claude-haiku-5-5 |
| triagem-juridica | claude-sonnet-5-5 |
<!-- fim da tabela gerada -->

## Resultado da parte 1 (K-115a, 12 e 13/11/2026)
| Habilidade | Agente | Modelo que fica | Como chega à rotina com IA (K-113) |
|---|---|---|---|
| extrair-evidencia | avaliador | **Haiku 5.5** | frontmatter do avaliador (trocado, com Histórico) |
| registrar-termo | arquivista | **Haiku 5.5** | `model: haiku` por chamada |
| montar-ficha | arquivista | **Haiku 5.5** | `model: haiku` por chamada |
| gerar-grafo | arquivista | **Sonnet 5.5** | frontmatter do arquivista (fica Sonnet, o modelo que passa nas três) |
| triagem-juridica | juridico | **Sonnet 5.5** | frontmatter do juridico até o K-115b (que testa as outras habilidades dele) |

- **Reforços do harness antes de subir (l. 698):** extrair-evidencia 0.2.1 (cobertura; voz do autor que cita outra obra) fez o Haiku passar na 3ª rodada. gerar-grafo 0.2.1 (Y pelos Processos registrados; X pelas Proposições do gesto) e triagem-juridica 0.2.1 (como ler o trecho na pergunta 2) não bastaram ao Haiku; o Sonnet passou na 1ª rodada com eles.
- **Correção do banco:** a prova `gg-pr0042-cadeia` foi corrigida na banco-0.2 (a F-0031 apontava para os Elementos retirados, e o pedido não dava as Proposições que dizem o insumo); a rodada 1 do Haiku correu na 0.1 e fica na tabela como estava.
- **Segunda leitura do auditor** (Sonnet 5.5 alto; `trilhas/2026-11-12_K-115a/auditor-leitura.json`): triagem-juridica (Sonnet) serve; as outras quatro servem com ressalvas, com erros de leitura fiel que nenhum validador pega: no Haiku, Evidência de fragmento sem sujeito nem verbo e Trecho emendado por cima de elisão (extrair-evidencia), divergência inventada (registrar-termo), frase sobre Faltas marcada com Proposições que não a dizem (montar-ficha); no Sonnet, uma Aresta com Proposição a mais e μ inflado (gerar-grafo). Erros do mesmo tipo apareceram com o Sonnet na produção do K-109 e do K-110. Pela regra, a escolha é a do validador; os erros vão ao insumo 122, para o reforço do harness e a segunda leitura da rotina com IA (D-038).
- **Custo:** em tokens, o Haiku gastou mais que o Sonnet nas provas em que os dois rodaram (gerar-grafo: 158.529 contra 81.323; triagem-juridica: 127.077 contra 65.298); por token, custa cerca de 1/20 (C115.4). O peso de cada modelo no limite da assinatura não foi conferido, e o teto de 20% da D-050 é medido nela: a rotina de teste do K-113 mede.
- **O que não foi feito:** as provas rodaram uma vez por modelo e rodada (sem repetição para medir variação); só os candidatos Haiku 5.5 e Sonnet 5.5; o esforço ficou o do frontmatter (alto) em todas.

## Gemini (K-125; D-054)
Pelo executor `scripts/gemini_agente.py` (gemini-agente-0.1), com o mesmo banco (base `288c4b0`) e os mesmos validadores; os tokens são os que a API informa (`usageMetadata`), somados por rodada em `trilhas/rotina-ia/consumo-gemini.jsonl`. Entrada = prompt + ferramentas; saída = resposta + pensamento. Chamadas = chamadas de ferramenta (pedidos à API à parte).

| Habilidade | Modelo | Prova | Aprovação | Entrada | Saída | Pedidos à API | Chamadas | Execução |
|---|---|---|---|---|---|---|---|---|
| extrair-evidencia | gemini-4-hydrogen | ee-en1369-en1544 (rodada 1, 13/11) | reprova (TR-0035, TR-0039, TR-0040, TR-0041 não cobertos; teto de 25 chamadas atingido) | 299.975 | 28.037 | 7 | 25 | log de 13/11 em `trilhas/logs/2026-11-13_avaliador.jsonl` |
| extrair-evidencia | gemini-4-hydrogen | ee-en1369-en1544 (rodada 2, 13/11; executor 0.2, histórico encurtado) | **interrompida** no 4º pedido pela cota diária (não conta como reprova do modelo) | 57.097 | 7.435 | 3 | 14 | EX-0145 |
| gerar-grafo | gemini-4-argon | gg-pr0042-cadeia (rodada 1, 13/11) | **não rodou**: o primeiro pedido recusado (nível gratuito sem cota para o argon: limite 0 de tokens de entrada) | 0 | 0 | 0 | 0 | EX-0146 |
| gerar-grafo | gemini-3.8-flash (candidato do nível gratuito à vaga do argon; não muda a D-054) | gg-pr0042-cadeia (rodada 1, 13/11; executor 0.4, com ritmo) | reprova (gastou as 25 chamadas a listar, ler e validar a raiz sem gravar; relatou a validação da raiz intocada como resultado) | 121.485 | 8.206 | 10 | 25 | EX-0147 |

**Limites da chave (tela do AI Studio lida por Vicente em 13/11; `ambientes/rotinas-ia/limites-gemini.json`):** no nível gratuito, o hydrogen e os Flash (3.8, 3.6, 3 e 2.5) têm 5 pedidos por minuto, 250 mil tokens por minuto e 20 pedidos por dia; os Flash Lite 3.5 e 3.1, 15 por minuto e 500 por dia; o argon, o carbon e os Pro, nenhuma cota; os Gemma 4, 16 mil tokens por minuto (menos que o pedido do sistema de uma habilidade). A tela marcava 31 pedidos do hydrogen no dia, contra 10 no registro do executor: os pedidos recusados e as tentativas antigas também contam; desde a 0.4 o executor conta cada tentativa HTTP.

**Cotas da chave (conferidas pela resposta da API em 13/11):** o projeto está no nível gratuito: o gemini-4-hydrogen tem 20 pedidos por dia por projeto (`GenerateRequestsPerDayPerProjectPerModel-FreeTier`; volta por volta das 05h de Brasília), e o gemini-4-argon não tem cota nenhuma (`generate_content_free_tier_input_token_count`, limite 0). As provas do argon e a segunda leitura da rotina só rodam com a cobrança ligada no projeto (passo de dono, K-125).

Faltam: a rodada 2 do hydrogen na extrair-evidencia (a l. 698 pede o reforço do harness antes de trocar de modelo; o Haiku passou na rodada 3) e as provas rt, mf (hydrogen), gg, tj e a segunda leitura (argon). Insumos 133 e 134.
