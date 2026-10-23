# Relatório de testes

Gerado por `scripts/rodar_testes.py` em 2026-10-22T23:31:38-03:00.
Validador: `jsonschema` se instalado (.venv), senão o validador mínimo de `scripts/_comum.py`. Python: 3.12.10.

**Totais:** OK: 112 · FALHA: 0 · PENDENTE: 5.

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
| 'cauim' em quatro bases + bola de neve do Boletim Goeldi | passa | passa | OK |  |
| total_visto maior que total_informado sem explicação | reprova | reprova | OK (reprovou como esperado) | consultas/1: total_visto 14 maior que total_informado 10 sem explicacao_total_visto |

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

### extrair-evidencia (rodada B)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| exemplos do caso-piloto | pendente | pendente | PENDENTE | pendente: caso-piloto (Passo 1). Entradas reais do caso-piloto com as Evidências esperadas (trecho, localizador, voz) e um caso que deve reprovar (trecho não localizado marcado como localizado). |

### ficha-de-acesso (rodada B)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| Hemeroteca respondendo 403 | passa | passa | OK |  |
| API da BDTD funcionando | passa | passa | OK |  |
| Querido Diário instável | passa | passa | OK |  |
| ficha com 403 e decisão 'aceito' | reprova | reprova | OK (reprovou como esperado) | decisao: 'aceito como via automática' does not match '^falta' |

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

### registrar-melhoria (rodada A)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| insumo 22 no formato fixo | passa | passa | OK |  |
| insumo explorado na sessão e com campo inventado | reprova | reprova | OK (reprovou como esperado) | (raiz): Additional properties are not allowed ('solucao_aplicada' was unexpected); sem_explorar: True was expected |
| o script daria o número seguinte e as duas linhas | passa | passa | OK |     mapa-tres-frentes.md, seção 6: / 32, o script do mapa lê a 6A do brief por linhas fixas (exemplo da registrar-melhoria) / P; D / K-006 / |
| texto de insumo já anotado é recusado | reprova | reprova | OK (reprovou como esperado) |     - insumo: o mesmo texto já está anotado em trilhas/insumos-planejamento.md |
| insumo com e-mail de terceiro é recusado | reprova | reprova | OK (reprovou como esperado) |     - dado pessoal de terceiros: e-mail: [dado pessoal omitido] |

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
| v0.1: as 38 ausências conhecidas (37 até a D-029 + D-030) | reprova | reprova | OK (reprovou como esperado) | } |
| divergência real de 16/10: D-018 sem 'traduzível' | reprova | reprova | OK (reprovou como esperado) | } |
| D-018 correta | passa | passa | OK | } |
| Anexos A e B intactos (commit e868a98) | passa | passa | OK | IDÊNTICO: Anexos A e B (694 linhas) iguais ao commit e868a98 (fins de linha normalizados) |
| relatório de exemplo com achado confirmado | passa | passa | OK |  |
| achado de contradição sem linha nem trecho | reprova | reprova | OK (reprovou como esperado) | achados/0: 'linha' is a required property; achados/0: 'trecho' is a required property |

### contratos do §6 (esquemas/) (rodada B)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| termo: retirado só com o ID (exemplo de esquema) | passa | passa | OK |  |
| termo: retirado ainda com conteúdo | reprova | reprova | OK (reprovou como esperado) | (raiz): 'conceito' is not one of ['id', 'retirado', 'fundido_em', 'origem_registro', 'nota'] |
| termo: exemplo que passa (dado real) | passa | passa | OK |  |
| termo: atestado sem abonação | reprova | reprova | OK (reprovou como esperado) | abonacoes: [] should be non-empty |
| proposicao: exemplo que passa (dado real) | passa | passa | OK |  |
| proposicao: estado calculado sem μ | reprova | reprova | OK (reprovou como esperado) | lambda: None is not of type 'number'; mu: None is not of type 'number' |
| evidencia: exemplo que passa (dado real) | passa | passa | OK |  |
| evidencia: voz fora da lista | reprova | reprova | OK (reprovou como esperado) | voz/tipo: 'folclorista famoso' is not one of ['autor', 'pessoa citada em fala direta', 'instituição', 'anúncio'] |
| fonte: exemplo que passa (dado real) | passa | passa | OK |  |
| fonte: nome de pessoa na referência | reprova | reprova | OK (reprovou como esperado) | referencia: Additional properties are not allowed ('autor' was unexpected) |
| ambiente: exemplo que passa (dado real) | passa | passa | OK |  |
| ambiente: ambiente minerando sem ficha de acesso | reprova | reprova | OK (reprovou como esperado) | (raiz): 'ficha_de_acesso' is a required property |
| consulta: exemplo que passa (exemplo de esquema) | passa | passa | OK |  |
| consulta: consulta de termo sem termos | reprova | reprova | OK (reprovou como esperado) | termos: [] should be non-empty |
| recorte: exemplo que passa (dado real) | passa | passa | OK |  |
| recorte: sem total informado e dado como percorrido | reprova | reprova | OK (reprovou como esperado) | (raiz): 'faltas' is a required property; estado: 'percorrido pela busca' should not be valid under {'const': 'percorrido pela busca'} |
| entrada: exemplo que passa (exemplo de esquema) | passa | passa | OK |  |
| entrada: quarentena sem o selo | reprova | reprova | OK (reprovou como esperado) | (raiz): 'selo' is a required property |
| trecho: exemplo que passa (dado real) | passa | passa | OK |  |
| trecho: dado como localizado sem hash nem grau | reprova | reprova | OK (reprovou como esperado) | (raiz): 'hash' is a required property; (raiz): 'data_conferencia' is a required property; (raiz): 'grau_semelhanca' is a required property |
| clb: exemplo que passa (exemplo de esquema) | passa | passa | OK |  |
| clb: critério recusado em vez de Falta | reprova | reprova | OK (reprovou como esperado) | criterios/identidade_ou_memoria: {} should be non-empty |
| elemento: exemplo que passa (exemplo de esquema) | passa | passa | OK |  |
| elemento: W completada com texto em vez de Compreensão local ou Falta | reprova | reprova | OK (reprovou como esperado) | w: 'o povo acha que é tradição' is not valid under any of the given schemas |
| insumo-x: exemplo que passa (exemplo de esquema) | passa | passa | OK |  |
| insumo-x: status e Falta ao mesmo tempo | reprova | reprova | OK (reprovou como esperado) | (raiz): {'id': 'IN-900001', 'nome': 'pedúnculo do caju', 'tipo': 'fruto', 'falta_status': 'F-900005', 'proposicoes': [], 'nota': 'caso que reprova: status e Falta ao mesmo tempo', 'origem_registro': {'criado_por': 'curador (exemplo de esquema, K-104)', 'data': '2026-10-22', 'execucao': 'EX-900001'}, 'status_botanico_cultural': 'nativo'} is valid under each of {'required': ['falta_status']}, {'required': ['status_botanico_cultural']} |
| processo: exemplo que passa (exemplo de esquema) | passa | passa | OK |  |
| processo: sem nome | reprova | reprova | OK (reprovou como esperado) | nome: '' should be non-empty |
| compreensao-local: exemplo que passa (exemplo de esquema) | passa | passa | OK |  |
| compreensao-local: atestada sem Evidência | reprova | reprova | OK (reprovou como esperado) | evidencias: [] should be non-empty |
| transformacao: exemplo que passa (exemplo de esquema) | passa | passa | OK |  |
| transformacao: por interação sem dizer com quem | reprova | reprova | OK (reprovou como esperado) | (raiz): 'interacao_com' is a required property |
| aresta: exemplo que passa (exemplo de esquema) | passa | passa | OK |  |
| aresta: μ fora de [0, 1] | reprova | reprova | OK (reprovou como esperado) | mu: 1.4 is greater than the maximum of 1 |
| lugar: exemplo que passa (dado real) | passa | passa | OK |  |
| lugar: território tradicional sem fonte que o nomeie | reprova | reprova | OK (reprovou como esperado) | (raiz): 'fonte_nomeia' is a required property |
| pessoa: exemplo que passa (exemplo de esquema) | passa | passa | OK |  |
| pessoa: nome no registro | reprova | reprova | OK (reprovou como esperado) | (raiz): Additional properties are not allowed ('nome' was unexpected) |
| valores-provisorios: o registro real passa | passa | passa | OK |  |
| valores-provisorios: valor sem a linha da Fundação que o permite | reprova | reprova | OK (reprovou como esperado) | valores/lote_maquina: 'linha_fundacao' is a required property |

### scripts do núcleo (K-105, bloco 3) (rodada B)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| localizar_trecho: trecho exato | passa | passa | OK | estado: localizado · grau 1.0 · limiar 0.9 · normalizacao-0.1 |
| localizar_trecho: semelhança acima do limiar | passa | passa | OK | estado: localizado · grau 0.9412 · limiar 0.9 · normalizacao-0.1 |
| localizar_trecho: abaixo do limiar vira Falta | reprova | reprova | OK (reprovou como esperado) | estado: não verificável por máquina · grau 0.4468 · limiar 0.9 · normalizacao-0.1 |
| localizar_trecho: PDF sem texto legível vira Falta | reprova | reprova | OK (reprovou como esperado) | estado: não verificável por máquina · grau None · limiar 0.9 · normalizacao-0.1 |
| localizar_trecho: reconferência do Trecho localizado | passa | passa | OK | o Trecho se sustenta: localizado, grau 1.0, hash igual |
| localizar_trecho: trecho alterado marcado como localizado | reprova | reprova | OK (reprovou como esperado) | NÃO SE SUSTENTA: marcado como exato (1.0), mas o texto não está literal na fonte (grau 0.9016) |
| validar_acervo: acervo de teste completo | passa | passa | OK | acervo-0.1: 25 registros; válido |
| validar_acervo: forma de OCR registrada como variante | reprova | reprova | OK (reprovou como esperado) | acervo-0.1: 25 registros; 1 erro(s) |
| validar_acervo: Termo atestado sem abonação localizada | reprova | reprova | OK (reprovou como esperado) | acervo-0.1: 25 registros; 1 erro(s) |
| validar_acervo: W sem a voz de quem pratica | reprova | reprova | OK (reprovou como esperado) | acervo-0.1: 25 registros; 1 erro(s) |
| validar_acervo: frase da ficha sem marcação | reprova | reprova | OK (reprovou como esperado) | acervo-0.1: 25 registros; 1 erro(s) |
| validar_acervo: Evidência aponta para Trecho que não existe | reprova | reprova | OK (reprovou como esperado) | acervo-0.1: 25 registros; 2 erro(s) |
| validar_acervo: colisão de ID | reprova | reprova | OK (reprovou como esperado) | acervo-0.1: 25 registros; 1 erro(s) |
| validar_acervo: o acervo do repositório | passa | passa | OK | acervo-0.1: 69 registros; válido |
| calcular_mu_lambda: recálculo bate | passa | passa | OK | mu-lambda-0.1: 3 registros calculados; recálculo bate |
| calcular_mu_lambda: duas fontes da mesma linhagem contadas como duas | reprova | reprova | OK (reprovou como esperado) | mu-lambda-0.1: 3 registros calculados; 6 divergência(s) |
| triagem_fixa: casos óbvios viram Faltas jurídicas válidas | passa | passa | OK | triagem-fixa-0.1: 1 registro(s), 3 Falta(s) jurídica(s) |
| triagem_fixa: registro sem caso óbvio | passa | passa | OK | triagem-fixa-0.1: 1 registro(s), 0 Falta(s) jurídica(s) |
| triagem_fixa: norma sem trecho não gera Falta | reprova | reprova | OK (reprovou como esperado) | RECUSADO: o caso substancia_controlada tem norma incompleta (trecho); Falta jurídica sem norma não sai |
| falta: Falta jurídica sem caminho de liberação | reprova | reprova | OK (reprovou como esperado) | (raiz): 'caminho_de_liberacao' is a required property |
| gerar_termo: booleanos e Consulta nova | passa | passa | OK | termo-0.1: 1 Termo(s) |
| gerar_termo: Termo com forma de OCR como variante | reprova | reprova | OK (reprovou como esperado) | RECUSADO TE-900001: variante 'bebida-cxemplo' é forma de OCR ou truncada (forma de OCR): vai só em formas_de_busca |
| sortear_amostra: a amostra bate com a semente | passa | passa | OK | a amostra bate com a semente 20261022 (15 itens de 25) |
| sortear_amostra: itens escolhidos à mão | reprova | reprova | OK (reprovou como esperado) | NÃO BATE: a semente 20261022 sobre o universo gravado dá ['AR-900001', 'CL-900001', 'CP-900001', 'EV-900001', 'EV-900003', 'EV-900004', 'F-900001', 'FO-900002', 'IN-900001', 'P-900001', 'PC-900002', ' |
| semear_ambientes: os 69 ambientes validam e batem com o Anexo E | passa | passa | OK | 69 ambientes; Anexo E: 69; bate e valida |
| semear_ambientes: pasta incompleta | reprova | reprova | OK (reprovou como esperado) | 1 ambientes; Anexo E: 69; 1 erro(s) |
