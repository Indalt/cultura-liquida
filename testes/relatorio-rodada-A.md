# Relatório de testes da rodada A

Gerado por `scripts/rodar_testes.py` em 2026-10-22T13:49:17-03:00.
Validador: `jsonschema` se instalado (.venv), senão o validador mínimo de `scripts/_comum.py`. Python: 3.12.10.

**Totais:** OK: 40 · FALHA: 0 · PENDENTE: 0.

"OK (reprovou como esperado)" = o caso com erro foi recusado pelo validador, como deve ser.

### conferir-fato (rodada A)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| C1 real (jurídico essencial, nível no item) | passa | passa | OK |  |
| C2 real (padrões e serviços, nível por parte) | passa | passa | OK |  |
| oficial sem URL | reprova | reprova | OK (reprovou como esperado) | itens/0: {'id': 'C1.1', 'pergunta': 'Lei 9.610/1998: em qual inciso do art. 7º estão as obras orais (conferências, alocuções, sermões)? Texto literal do art. 46, II.', 'resposta': 'Art. 7º, inciso II.', 'citacao': 'II - as conferências, alocuções, sermões e outras obras da mesma natureza;', 'nivel': 'oficial', 'observacao': 'CASO DE TESTE: cópia do C1.1 real sem o campo url. Deve reprovar.'} is not valid under any of the given schemas |
| oficial sem citação, em parte | reprova | reprova | OK (reprovou como esperado) | itens/0/partes/0: 'citacao' is a required property |

### escrever-secao-fundacao (rodada A)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| §9 pelas essências da seção 2 | passa | passa | OK | } |
| D-018 como transcrição literal da fala | reprova | reprova | OK (reprovou como esperado) | } |
| AGENTS.md segue as essências | passa | passa | OK | } |

### executar-brief (rodada A)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| conta real da janela 1 antes do C2 (teto de 600 mil da v0.2): pode | passa | passa | OK | PODE abrir o agente |
| folga menor que 2x o maior lote: parar | reprova | reprova | OK (reprovou como esperado) | PARAR: salvar o estado e encerrar a janela |
| log real do teste do auditor (Bloco 2.5) | passa | passa | OK |  |
| log com e-mail de terceiro é recusado | reprova | reprova | OK (reprovou como esperado) |     - dado pessoal de terceiros: e-mail: [dado pessoal omitido] |
| conta da semana com o teto de 300 mil (seção 0 do brief): pode | passa | passa | OK | PODE abrir o agente |
| log de agente sem alcance é recusado (D-030) | reprova | reprova | OK (reprovou como esperado) |     - esquema: (raiz): 'alcance' is a required property |
| log de agente de workflow com tokens nulos e sem o motivo | reprova | reprova | OK (reprovou como esperado) | (raiz): {'agente': 'workflow-subagent', 'habilidade': 'verificar-fundacao', 'versao_harness': '0.1.1', 'modelo': 'claude-sonnet-5-5', 'esforco': 'high', 'entrada_ref': 'caso de teste do K-101', 'acoes': ['caso fictício para o validador'], 'resultados': ['nenhum'], 'decisoes': [], 'tokens': None, 'chamadas': None, 'duracao_s': 10, 'erros': [], 'workflow': 'wf_b6288315-eba', 'data_hora': '2026-10-17T22:00:00-03:00', 'fonte_do_registro': 'curador', 'id': 'EX-9001', 'alcance': {'olhado': ['caso fictício']}} is not valid under any of the given schemas |
| log de agente de workflow com tokens nulos e o motivo | passa | passa | OK |  |
| log de script sem alcance | reprova | reprova | OK (reprovou como esperado) | (raiz): 'alcance' is a required property; (raiz): 'alcance' is a required property |
| log de script com alcance, sem campos de agente | passa | passa | OK |  |
| decisão automática sem a versão da regra | reprova | reprova | OK (reprovou como esperado) | decisoes/0: 'versao_regra' is a required property |
| os logs gravados até hoje continuam válidos | passa | passa | OK | PASSA  trilhas/logs/2026-10-22_curador.jsonl |

### guia-de-liberacao (rodada A)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| guia SisGen (C1, oficial; telas não conferidas) | passa | passa | OK |  |
| passo de tela 'oficial' sem URL | reprova | reprova | OK (reprovou como esperado) | passos/0: 'url' is a required property |
| guia sem limites | reprova | reprova | OK (reprovou como esperado) | (raiz): 'limites' is a required property |

### registrar-decisao (rodada A)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| D-025: 'por princípio' era 'de início' | passa | passa | OK |  |
| D-021: repositório passou a público | passa | passa | OK |  |
| diretriz sem confirmação de Vicente | reprova | reprova | OK (reprovou como esperado) | confirmada_por_vicente: True was expected |

### registrar-melhoria (rodada A)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| insumo 22 no formato fixo | passa | passa | OK |  |
| insumo explorado na sessão e com campo inventado | reprova | reprova | OK (reprovou como esperado) | (raiz): Additional properties are not allowed ('solucao_aplicada' was unexpected); sem_explorar: True was expected |
| o script daria o número seguinte e as duas linhas | passa | passa | OK |     mapa-tres-frentes.md, seção 6: / 28, o script do mapa lê a 6A do brief por linhas fixas (exemplo da registrar-melhoria) / P; D / K-006 / |
| texto de insumo já anotado é recusado | reprova | reprova | OK (reprovou como esperado) |     - insumo: o mesmo texto já está anotado em trilhas/insumos-planejamento.md |
| insumo com e-mail de terceiro é recusado | reprova | reprova | OK (reprovou como esperado) |     - dado pessoal de terceiros: e-mail: [dado pessoal omitido] |

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
| v0.1: as 38 ausências conhecidas (37 até a D-029 + D-030) | reprova | reprova | OK (reprovou como esperado) | } |
| divergência real de 16/10: D-018 sem 'traduzível' | reprova | reprova | OK (reprovou como esperado) | } |
| D-018 correta | passa | passa | OK | } |
| Anexos A e B intactos (commit e868a98) | passa | passa | OK | IDÊNTICO: Anexos A e B (694 linhas) iguais ao commit e868a98 (fins de linha normalizados) |
| relatório de exemplo com achado confirmado | passa | passa | OK |  |
| achado de contradição sem linha nem trecho | reprova | reprova | OK (reprovou como esperado) | achados/0: 'linha' is a required property; achados/0: 'trecho' is a required property |
