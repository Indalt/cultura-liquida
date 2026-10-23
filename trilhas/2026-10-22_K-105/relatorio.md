# K-105 (bloco 3): relatório

**Data:** 22/10/2026. **Quem fez:** o curador (Opus 5.5, esforço médio). **Quem conferiu:** o auditor (Sonnet 5.5, esforço alto). O juridico deu as normas (Sonnet 5.5, esforço alto). Este relatório não pede aprovação (D-037).

## O que entrou
Sete scripts em `scripts/`. Cada um lê do registro de valores provisórios a regra e a versão que usa:
- **`localizar_trecho.py`** (normalizacao-0.1): acha o trecho na fonte ou na captura do Wayback, com hash, antes e depois, localizador e grau. Abaixo do limiar, ou num PDF sem texto, emite a Falta "trecho não verificável por máquina". O texto da fonte só fica numa pasta temporária fora do repositório. O modo `conferir` relê a mesma captura e diz se o Trecho se sustenta.
- **`validar_acervo.py`** (acervo-0.2): confere os esquemas e as ligações do acervo. Roda como gancho de pre-commit em `.githooks/pre-commit`. Num clone novo, o gancho pede `git config core.hooksPath .githooks`.
- **`triagem_fixa.py`** (triagem-fixa-0.2): seis casos óbvios viram Faltas jurídicas, cada uma com a norma e o caminho de liberação. Os seis casos: licença, dado pessoal, dado sensível, conhecimento tradicional, substância controlada, criança ou adolescente. As normas vêm do lote C5 e ficam em `esquemas/triagem-fixa.json`. Se uma norma estiver incompleta, a Falta não sai.
- **`calcular_mu_lambda.py`** (mu-lambda-0.1): calcula μ, λ, Dc, Dct e o estado por linhagem independente e gera `grafo/` com as tabelas X×Y e Z. O estado inconsistente marca a tensão.
- **`gerar_termo.py`** (termo-0.1): gera os booleanos, o glossário e a Consulta nova proposta.
- **`sortear_amostra.py`** (amostra-0.2): sorteia 15 itens com semente registrada, entre o que nenhuma amostra anterior viu.
- **`semear_ambientes.py`:** os 69 ambientes do Anexo E entraram em `ambientes/` como "proposto". A contagem bate com a da Fundação.

Testes: `testes/nucleo/casos.json` tem 32 casos, com acervos sintéticos na faixa de exemplos. `rodar_testes.py` dá OK 120 · FALHA 0 · PENDENTE 5. Os 5 pendentes são das habilidades dos blocos 7 e 8.

## O que o auditor achou
Foram 18 achados (`achados-auditor.json`).
- **13 corrigidos neste cartão, com casos novos:** trecho vazio, licença null, marca no meio da frase, seção isenta por prefixo, fato depois de comentário, aspas no booleano, glossário parcial, "cocada" lida como coca, OCR rotulado como "erro de transcrição", amostra cortada por data, ciclo em deriva_de, Falta com ID F-0000, hífen entre números.
- **4 são regra, não código, e foram para o planejamento:**
  - A-009 e A-010, que tratam de quais Evidências contam em μ e λ e da mesma linhagem nos dois lados (insumos 34 e 36);
  - A-015, o limiar de 0,9 que deixa passar um "nunca" inserido (insumo 36);
  - A-008, a Falta escrita à mão com norma "não conferido": segue válida, porque fato não conferido não para.
- **A-018:** o próprio curador gravou os insumos durante a passada do auditor.

A conferência das correções do K-104:
- A-002, A-003 e A-005 estavam certas.
- A-001 faltava na Pessoa e foi corrigida agora, com exemplos que passam e que reprovam.
- A-004 está certa: o "não calculado" que restou fica só na descrição.

## Quarentena e Faltas
Nenhuma Entrada nem Falta real entrou: o bloco 3 só construiu a ferramenta. A Portaria SVS/MS 344/1998 não foi conferida (503 e 404). Ela aparece no `triagem-fixa.json` só pela citação do art. 66 da Lei 11.343.

## Não conferido
- A Portaria 344/1998.
- Imagem e voz de adulto (CF art. 5º, X; Código Civil art. 20) e o ECA art. 2º.
- A leitura por rede (URL e Wayback), que não rodou contra fonte real.
- Uma nova leitura independente das correções deste cartão.
