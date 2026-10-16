# Relatório de testes

Gerado por `scripts/rodar_testes.py` em 2026-10-16T11:33:35-03:00.
Validador: `jsonschema` se instalado (.venv), senão o validador mínimo de `scripts/_comum.py`. Python: 3.12.10.

**Totais:** OK: 27 · FALHA: 0 · PENDENTE: 9.

"OK (reprovou como esperado)" = o caso com erro foi recusado pelo validador, como deve ser.

### conferir-fato (rodada A)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| C1 real (jurídico essencial, nível no item) | passa | passa | OK |  |
| C2 real (padrões e serviços, nível por parte) | passa | passa | OK |  |
| oficial sem URL | reprova | reprova | OK (reprovou como esperado) | itens/0: {'id': 'C1.1', 'pergunta': 'Lei 9.610/1998: em qual inciso do art. 7º estão as obras orais (conferências, alocuções, sermões)? Texto literal do art. 46, II.', 'resposta': 'Art. 7º, inciso II.', 'citacao': 'II - as conferências, alocuções, sermões e outras obras da mesma natureza;', 'nivel': 'oficial', 'observacao': 'CASO DE TESTE: cópia do C1.1 real sem o campo url. Deve reprovar.'} is not valid under any of the given schemas |
| oficial sem citação, em parte | reprova | reprova | OK (reprovou como esperado) | itens/0/partes/0: 'citacao' is a required property |

### consulta (rodada B)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| 'cauim' em quatro bases + bola de neve do Boletim Goeldi | pendente | pendente | PENDENTE | exemplo real pronto; validador pendente do contrato de Consulta (Passo 1). Aceitação: total informado e data por base; total visto nunca maior que o informado; 'não exaurido' até tudo ser visto e a bola de neve não trazer nada novo; país e idioma só anotam |

### escrever-secao-fundacao (rodada A)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| §9 pelas essências da seção 2 | passa | passa | OK | } |
| D-018 como transcrição literal da fala | reprova | reprova | OK (reprovou como esperado) | } |
| AGENTS.md segue as essências | passa | passa | OK | } |

### executar-brief (rodada A)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| conta real da janela 1 antes do C2: pode | passa | passa | OK | PODE abrir o agente |
| folga menor que 2x o maior lote: parar | reprova | reprova | OK (reprovou como esperado) | PARAR: salvar o estado e encerrar a janela |
| log real do teste do auditor (Bloco 2.5) | passa | passa | OK |  |
| log com e-mail de terceiro é recusado | reprova | reprova | OK (reprovou como esperado) |     - dado pessoal de terceiros: e-mail: [dado pessoal omitido] |

### extrair-evidencia (rodada B)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| exemplos do caso-piloto | pendente | pendente | PENDENTE | pendente: caso-piloto (Passo 1). Entradas reais do caso-piloto com as Evidências esperadas (trecho, localizador, voz) e um caso que deve reprovar (trecho não localizado marcado como localizado). |

### ficha-de-acesso (rodada B)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| Hemeroteca respondendo 403 | pendente | pendente | PENDENTE | exemplo real pronto; validador pendente do contrato de Ambiente (Passo 1). Aceitação: teste com data e resposta literal; bloqueio registrado e não contornado; decisão = falta com via humana |
| API da BDTD funcionando | pendente | pendente | PENDENTE | exemplo real pronto; validador pendente (Passo 1). Aceitação: endpoint, link permanente, termos e cobertura com data; decisão = aceito |
| Querido Diário instável | pendente | pendente | PENDENTE | exemplo real pronto; validador pendente (Passo 1). Aceitação: falhas registradas tal como vieram; 'não conferido' onde cabe |

### gerar-grafo (rodada B)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| exemplos do caso-piloto | pendente | pendente | PENDENTE | pendente: caso-piloto (Passo 1). As arestas do caso-piloto com μ e λ calculados e um caso que deve reprovar (duas fontes da mesma linhagem contadas como duas). |

### guia-de-liberacao (rodada A)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| guia SisGen (C1, oficial; telas não conferidas) | passa | passa | OK |  |
| passo de tela 'oficial' sem URL | reprova | reprova | OK (reprovou como esperado) | passos/0: 'url' is a required property |
| guia sem limites | reprova | reprova | OK (reprovou como esperado) | (raiz): 'limites' is a required property |

### kit-fonte-primaria (rodada B)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| exemplos do caso-piloto | pendente | pendente | PENDENTE | pendente: caso-piloto (Passo 1). O primeiro pedido real de Vicente e os critérios de aceitação dele. |

### montar-ficha (rodada B)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| exemplos do caso-piloto | pendente | pendente | PENDENTE | pendente: caso-piloto (Passo 1). A ficha da CLB do caso-piloto e um caso que deve reprovar (frase sem afirmação que a sustente, ou Falta preenchida). |

### registrar-decisao (rodada A)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| D-025: 'por princípio' era 'de início' | passa | passa | OK |  |
| D-021: repositório passou a público | passa | passa | OK |  |
| diretriz sem confirmação de Vicente | reprova | reprova | OK (reprovou como esperado) | confirmada_por_vicente: True was expected |

### registrar-termo (rodada B)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| exemplos do caso-piloto | pendente | pendente | PENDENTE | pendente: caso-piloto (Passo 1). Termos reais do caso-piloto (candidato e atestado) e um caso que deve reprovar (variante de busca de OCR registrada como variante linguística). |

### triagem-juridica (rodada A)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| caso A: dado sensível → Falta (norma não conferida, dita como tal) | passa | passa | OK |  |
| caso B: conhecimento tradicional de origem identificável → Falta | passa | passa | OK |  |
| Falta jurídica sem caminho de liberação | reprova | reprova | OK (reprovou como esperado) | (raiz): 'caminho_de_liberacao' is a required property |
| Falta completada por inferência | reprova | reprova | OK (reprovou como esperado) | (raiz): {'id': 'F-9002', 'tipo': 'compreensao_local_nao_captada', 'o_que_falta': 'como a comunidade entende a bebida (W)', 'por_que': 'a fonte só traz a leitura do pesquisador, sem a fala de quem pratica', 'onde_aparece': ['ficha da CLB, coordenada W'], 'valor_inferido': 'provavelmente entendida como bebida ritual', 'criada_por': 'CASO DE TESTE', 'data': '2026-10-16', 'nota': "A Falta foi completada por inferência (campo valor_inferido): fere a regra 'a Falta é dita, nunca completada' (D-018). Deve reprovar."} should not be valid under {'anyOf': [{'required': ['valor']}, {'required': ['valor_inferido']}]} |

### verificar-fundacao (rodada A)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| v0.1: as 37 ausências conhecidas | reprova | reprova | OK (reprovou como esperado) | } |
| divergência real de 16/10: D-018 sem 'traduzível' | reprova | reprova | OK (reprovou como esperado) | } |
| D-018 correta | passa | passa | OK | } |
| Anexos A e B intactos (commit e868a98) | passa | passa | OK | IDÊNTICO: Anexos A e B (694 linhas) iguais ao commit e868a98 (fins de linha normalizados) |
| relatório de exemplo com achado confirmado | passa | passa | OK |  |
| achado de contradição sem linha nem trecho | reprova | reprova | OK (reprovou como esperado) | achados/0: 'linha' is a required property; achados/0: 'trecho' is a required property |

## Leitura do resultado (16/10/2026)

- **Rodada A — passou nos exemplos reais e reprovou os exemplos com erro:** `conferir-fato` (C1 e C2 reais; "oficial" sem URL e sem citação recusados), `guia-de-liberacao` (SisGen; tela "oficial" sem URL e guia sem limites recusados), `triagem-juridica` (casos do 16-J; Falta sem caminho e Falta completada recusadas), `verificar-fundacao` (37 ausências da v0.1; D-018 sem "traduzível" acusada; Anexos intactos), `escrever-secao-fundacao` (§9 pelas essências passa; transcrição recusada; `AGENTS.md` passa), `registrar-decisao` ("de início" e D-021 pública passam; diretriz sem confirmação recusada), `executar-brief` (conta real da janela 1; regra da folga; log real do teste; log com e-mail de terceiro recusado).
- **Rodada B — pendente:** `ficha-de-acesso` e `consulta` têm exemplos reais (Hemeroteca 403, BDTD, Querido Diário; "cauim" em quatro bases e bola de neve), mas o validador depende dos contratos de Ambiente e Consulta (§6), que são entrega do Passo 1. `extrair-evidencia`, `registrar-termo`, `montar-ficha`, `gerar-grafo` e `kit-fonte-primaria`: "pendente: caso-piloto (Passo 1)".
- **Teste de log (passo 2.5.5):** o hook `SubagentStop` gravou a linha mínima (`trilhas/logs/2026-10-16_general-purpose.jsonl`) e o curador gravou a completa (`trilhas/logs/2026-10-16_auditor.jsonl`). As duas passam no esquema de log.
- **Comparação entre modelos (Haiku × Sonnet × Opus):** não é agora; vem no Passo 1, com o caso-piloto e os logs reais.
