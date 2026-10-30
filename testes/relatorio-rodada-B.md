# Relatório de testes da rodada B

Gerado por `scripts/rodar_testes.py` em 2026-10-30T15:53:12-03:00.
Validador: `jsonschema` se instalado (.venv), senão o validador mínimo de `scripts/_comum.py`. Python: 3.12.10.

**Totais:** OK: 146 · FALHA: 0 · PENDENTE: 1.

"OK (reprovou como esperado)" = o caso com erro foi recusado pelo validador, como deve ser.

### consulta (rodada B)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| Recorte RC-0010 da primeira coleta real (K-108) | passa | passa | OK | registro RC-0010 pelo esquema recorte: código 0: PASSA  C:\Users\alqui\AppData\Local\Temp\cl-rodada-b-7pzrelko\registro.json |
| Recorte RC-0010 com o total visto acima do informado, sem explicação | reprova | reprova | OK (reprovou como esperado) | registro RC-0010 pelo esquema recorte: código 1: - (raiz): total_visto 999999 maior que total_informado 1305 sem explicacao_total_visto |

### consulta (rodada B)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| 'cauim' em quatro bases + bola de neve do Boletim Goeldi | passa | passa | OK |  |
| total_visto maior que total_informado sem explicação | reprova | reprova | OK (reprovou como esperado) | consultas/1: total_visto 14 maior que total_informado 10 sem explicacao_total_visto |

### extrair-evidencia (rodada B)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| TR-0001 (EV-0001, conferida pelo auditor) relocalizado na janela de citação | passa | passa | OK | TR-0001 na janela de citação: conferir, código 0: o Trecho se sustenta: localizado, grau 1.0, hash igual |
| TR-0034 com 'fresco', palavra de outro trecho, marcado como localizado | reprova | reprova | OK (reprovou como esperado) | TR-0034 na janela de citação: conferir, código 1: NÃO SE SUSTENTA: marcado como exato (1.0), mas o texto não está literal na fonte (grau 0.9815) |
| TR-0101 com a ligadura 'ﬁ' no texto exato e o grau gravado da leitura com 'fi' (0,9746) | passa | passa | OK | TR-0101 na janela de citação: conferir, código 0: o Trecho se sustenta: localizado, grau 1.0, hash igual |
| PR-0001 com a EV-0004 (leitura divergente) fora da conta de μ e λ | passa | passa | OK | scripts/calcular_mu_lambda.py: código 0: mu-lambda-0.2: 67 registros calculados; recálculo bate |
| PR-0001 gravada sem a EV-0004 em fora_da_conta (a leitura divergente contada) | reprova | reprova | OK (reprovou como esperado) | scripts/calcular_mu_lambda.py: código 1: NÃO BATE: PR-0001: fora_da_conta gravado {} ≠ recalculado {'EV-0004': 'leitura divergente'} |
| PR-0002 com a marca de saúde da EV-0002 | passa | passa | OK | scripts/validar_acervo.py: código 0: acervo-0.4: 798 registros; válido |
| PR-0002 sem a marca de saúde que a EV-0002 tem | reprova | reprova | OK (reprovou como esperado) | scripts/validar_acervo.py: código 1: ERRO acervo\proposicoes\PR-0002.json: Evidência marcada por aviso, saúde ou política (EV-0002) e a Proposição sem a marca |
| 'mocororó' declarado num trecho da p. 100 que não traz a palavra | reprova | reprova | OK (reprovou como esperado) | mencoes-0.1: nada gravado |

### ficha-de-acesso (rodada B)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| ficha da Hemeroteca (AM-0001) do K-106: 403 e via humana | passa | passa | OK | registro AM-0001 pelo esquema ficha-acesso: código 0: PASSA  C:\Users\alqui\AppData\Local\Temp\cl-rodada-b-qe9ogf1j\registro.json |
| ficha da Hemeroteca com o 403 e a decisão 'aceito' | reprova | reprova | OK (reprovou como esperado) | registro AM-0001 pelo esquema ficha-acesso: código 1: - decisao: 'aceito como via automática' does not match '^falta' |

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
| PR-0016 com duas linhagens a favor (FO-0008 e FO-0009), μ 1,0 | passa | passa | OK | scripts/calcular_mu_lambda.py: código 0: mu-lambda-0.2: 68 registros calculados; recálculo bate |
| PR-0016 com a FO-0009 derivada da FO-0008 e o μ gravado contando duas | reprova | reprova | OK (reprovou como esperado) | scripts/calcular_mu_lambda.py: código 1: NÃO BATE: PR-0016: mu gravado 1.0 ≠ recalculado 0.5; NÃO BATE: PR-0016: estado gravado 'verdadeiro' ≠ recalculado 'intermediário' |
| PR-0065 com tensão interna de linhagem (FO-0032 e FO-0034), fora de μ e λ | passa | passa | OK | scripts/calcular_mu_lambda.py: código 0: mu-lambda-0.2: 68 registros calculados; recálculo bate |
| PR-0065 gravada sem a tensão interna sinalizada | reprova | reprova | OK (reprovou como esperado) | scripts/calcular_mu_lambda.py: código 1: NÃO BATE: PR-0065: tensao_interna gravado [] ≠ recalculado ['FO-0032', 'FO-0034'] |

### guia-de-liberacao (rodada B)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| guia da licença de uso (Lei 9.610), rascunho do K-109 | passa | passa | OK | registro trilhas/2026-10-29_K-109/guias/G-licenca-lei-9610.json pelo esquema guia-liberacao: código 0: PASSA  C:\Users\alqui\AppData\Local\Temp\cl-rodada-b-hb44nolg\registro.json |
| guia da Lei 9.610 sem os limites | reprova | reprova | OK (reprovou como esperado) | registro trilhas/2026-10-29_K-109/guias/G-licenca-lei-9610.json pelo esquema guia-liberacao: código 1: - (raiz): 'limites' is a required property |
| guia da Lei 9.610 com passo 'oficial' sem URL | reprova | reprova | OK (reprovou como esperado) | registro trilhas/2026-10-29_K-109/guias/G-licenca-lei-9610.json pelo esquema guia-liberacao: código 1: - passos/0: 'url' is a required property |

### kit-fonte-primaria (rodada B)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| exemplos do caso-piloto | pendente | pendente | PENDENTE | pendente: caso-piloto (Passo 1). O primeiro pedido real de Vicente e os critérios de aceitação dele. |

### montar-ficha (rodada B)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| ficha CL-0001 (cajuína) com as Proposições que ela marca | passa | passa | OK | scripts/validar_acervo.py: código 0: acervo-0.4: 1298 registros; válido |
| ficha CL-0001 com uma frase factual sem a marca da Proposição | reprova | reprova | OK (reprovou como esperado) | scripts/validar_acervo.py: código 1: ERRO acervo\fichas\CL-0001.md: l. 136: frase sem marcação de Proposição: 'Uma fonte descreve a cajuína como relativa novidade histórica, que viceja nos es' |
| camada Educação da CL-0001 (K-110), com as marcas e as habilidades da BNCC | passa | passa | OK | scripts/validar_acervo.py: código 0: acervo-0.4: 1116 registros; válido |
| camada Educação com uma habilidade da BNCC sem a página do PDF | reprova | reprova | OK (reprovou como esperado) | scripts/validar_acervo.py: código 1: ERRO acervo\fichas\educacao\CL-0001.md: l. 70: habilidade EM13LP31 sem a página do PDF (número): 'não conferida' |

### registrar-termo (rodada B)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| TE-0002 cajuína, atestado, com o termo ambíguo marcado (e o TE-0004 que divide a forma) | passa | passa | OK | scripts/gerar_termo.py: código 0: termo-0.2: 3 Termo(s) |
| TE-0002 com a forma de busca 'cajuyna' registrada como variante de OCR | reprova | reprova | OK (reprovou como esperado) | scripts/validar_acervo.py: código 1: ERRO acervo\termos\TE-0002.json: variante 'cajuina' é forma de OCR ou truncada (grafia sem acento vinda do OCR das bases): vai só em formas_de_busca |
| TE-0002 com 'mocororó' como designação local, sem a marca de termo ambíguo | reprova | reprova | OK (reprovou como esperado) | scripts/validar_acervo.py: código 1: ERRO acervo\termos\TE-0002.json: a forma 'mocororó' nomeia também TE-0004: termo ambíguo (D-039) sem a marca (na variante, no tipo_variacao; na designação, na nota |

### triagem-juridica (rodada B)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| F-0033 (mocororó dos Tremembé, só para publicar), do K-110 | passa | passa | OK | registro F-0033 pelo esquema falta: código 0: PASSA  C:\Users\alqui\AppData\Local\Temp\cl-rodada-b-6pwak2zb\registro.json |
| F-0024 (dúvida de conhecimento tradicional, só para publicar), do K-109 | passa | passa | OK | registro F-0024 pelo esquema falta: código 0: PASSA  C:\Users\alqui\AppData\Local\Temp\cl-rodada-b-paggjk4q\registro.json |
| F-0033 sem o caminho de liberação | reprova | reprova | OK (reprovou como esperado) | registro F-0033 pelo esquema falta: código 1: - (raiz): 'caminho_de_liberacao' is a required property |
| F-0024 completada por inferência | reprova | reprova | OK (reprovou como esperado) | registro F-0024 pelo esquema falta: código 1: - (raiz): {'id': 'F-0024', 'tipo': 'impedimento_juridico', 'subtipo_juridico': 'conhecimento_tradicional', 'vale_para': 'publicar', 'o_que_falta': "Defini |
| regra fixa: ler, localizar, linkar e citar a Entrada real EN-0009 (BDTD) | passa | passa | OK | PORTÃO: nenhuma Falta barra o ato ler agora |
| regra fixa: copiar além da citação a Entrada real EN-0009 barra agora | reprova | reprova | OK (reprovou como esperado) | BARRA: o ato copiar fica parado pelas Faltas F-0034 (a Falta é dita e o caminho de liberação, apontado; D-020, D-025) |

### contratos do §6 (esquemas/) (rodada B)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| termo: retirado só com o ID (exemplo de esquema) | passa | passa | OK |  |
| termo: retirado ainda com conteúdo | reprova | reprova | OK (reprovou como esperado) | (raiz): 'conceito' is not one of ['id', 'retirado', 'fundido_em', 'origem_registro', 'nota'] |
| termo: exemplo que passa (dado real) | passa | passa | OK |  |
| termo: atestado sem abonação | reprova | reprova | OK (reprovou como esperado) | abonacoes: [] should be non-empty |
| termo: designação e variante com a língua e de onde ela veio (insumo 30) | passa | passa | OK |  |
| termo: língua sem a fonte (insumo 30) | reprova | reprova | OK (reprovou como esperado) | designacoes/0: 'lingua_fonte' is a required property |
| termo: designação como texto solto (formato 0.1.0) | reprova | reprova | OK (reprovou como esperado) | designacoes/0: 'cajuína' is not of type 'object' |
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
| entrada: quarentena sem o selo | reprova | reprova | OK (reprovou como esperado) | (raiz): 'selo' is a required property; (raiz): 'localizador' is a required property |
| entrada: item coletado com o identificador e dois Recortes (K-107) | passa | passa | OK |  |
| entrada: item coletado sem o identificador (K-107) | reprova | reprova | OK (reprovou como esperado) | (raiz): 'identificador' is a required property |
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
| pessoa: retirada só com o código (exemplo de esquema) | passa | passa | OK |  |
| pessoa: retirada ainda com conteúdo | reprova | reprova | OK (reprovou como esperado) | (raiz): 'papeis' is not one of ['codigo', 'retirado', 'fundido_em', 'origem_registro', 'nota'] |
| pegada: item que segue, com a Entrada | passa | passa | OK |  |
| pegada: item fora do escopo pela regra, sem Entrada | passa | passa | OK |  |
| pegada: com o título | reprova | reprova | OK (reprovou como esperado) | (raiz): Additional properties are not allowed ('titulo' was unexpected) |
| pegada: 'segue' sem a Entrada | reprova | reprova | OK (reprovou como esperado) | (raiz): 'entrada' is a required property |

### scripts do núcleo (K-105, bloco 3) (rodada B)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| localizar_trecho: trecho exato | passa | passa | OK | estado: localizado · grau 1.0 · limiar 0.9 · normalizacao-0.2 |
| localizar_trecho: semelhança acima do limiar | passa | passa | OK | estado: localizado · grau 0.9412 · limiar 0.9 · normalizacao-0.2 |
| localizar_trecho: abaixo do limiar vira Falta | reprova | reprova | OK (reprovou como esperado) | estado: não verificável por máquina · grau 0.4468 · limiar 0.9 · normalizacao-0.2 |
| localizar_trecho: PDF sem texto legível vira Falta | reprova | reprova | OK (reprovou como esperado) | estado: não verificável por máquina · grau None · limiar 0.9 · normalizacao-0.2 |
| localizar_trecho: reconferência do Trecho localizado | passa | passa | OK | o Trecho se sustenta: localizado, grau 1.0, hash igual |
| localizar_trecho: trecho alterado marcado como localizado | reprova | reprova | OK (reprovou como esperado) | NÃO SE SUSTENTA: marcado como exato (1.0), mas o texto não está literal na fonte (grau 0.9016) |
| validar_acervo: acervo de teste completo | passa | passa | OK | acervo-0.4: 25 registros; válido |
| validar_acervo: forma de OCR registrada como variante | reprova | reprova | OK (reprovou como esperado) | acervo-0.4: 25 registros; 1 erro(s) |
| validar_acervo: Termo atestado sem abonação localizada | reprova | reprova | OK (reprovou como esperado) | acervo-0.4: 25 registros; 1 erro(s) |
| validar_acervo: W sem a voz de quem pratica | reprova | reprova | OK (reprovou como esperado) | acervo-0.4: 25 registros; 1 erro(s) |
| validar_acervo: frase da ficha sem marcação | reprova | reprova | OK (reprovou como esperado) | acervo-0.4: 25 registros; 1 erro(s) |
| validar_acervo: Evidência aponta para Trecho que não existe | reprova | reprova | OK (reprovou como esperado) | acervo-0.4: 25 registros; 2 erro(s) |
| validar_acervo: colisão de ID | reprova | reprova | OK (reprovou como esperado) | acervo-0.4: 25 registros; 1 erro(s) |
| validar_acervo: o acervo do repositório | passa | passa | OK | acervo-0.4: 2858 registros; válido |
| calcular_mu_lambda: recálculo bate | passa | passa | OK | mu-lambda-0.2: 3 registros calculados; recálculo bate |
| calcular_mu_lambda: duas fontes da mesma linhagem contadas como duas | reprova | reprova | OK (reprovou como esperado) | mu-lambda-0.2: 3 registros calculados; 6 divergência(s) |
| triagem_fixa: casos óbvios viram Faltas jurídicas válidas | passa | passa | OK | triagem-fixa-0.3: 1 registro(s), 2 Falta(s) jurídica(s) |
| triagem_fixa: registro sem caso óbvio | passa | passa | OK | triagem-fixa-0.3: 1 registro(s), 0 Falta(s) jurídica(s) |
| triagem_fixa: norma sem trecho não gera Falta | reprova | reprova | OK (reprovou como esperado) | RECUSADO: o caso substancia_controlada tem norma incompleta (trecho); Falta jurídica sem norma não sai |
| falta: Falta jurídica sem caminho de liberação | reprova | reprova | OK (reprovou como esperado) | (raiz): 'caminho_de_liberacao' is a required property |
| gerar_termo: booleanos e Consulta nova | passa | passa | OK | termo-0.2: 1 Termo(s) |
| gerar_termo: Termo com forma de OCR como variante | reprova | reprova | OK (reprovou como esperado) | RECUSADO TE-900001: variante 'bebida-cxemplo' é forma de OCR ou truncada (forma de OCR): vai só em formas_de_busca |
| sortear_amostra: a amostra bate com a semente | passa | passa | OK | a amostra bate com a semente 20261022 (15 itens de 25) |
| sortear_amostra: itens escolhidos à mão | reprova | reprova | OK (reprovou como esperado) | NÃO BATE: a semente 20261022 sobre o universo gravado dá ['AR-900001', 'CL-900001', 'CP-900001', 'EV-900001', 'EV-900003', 'EV-900004', 'F-900001', 'FO-900002', 'IN-900001', 'P-900001', 'PC-900002', ' |
| semear_ambientes: os 69 ambientes validam e batem com o Anexo E | passa | passa | OK | 69 ambientes; Anexo E: 69; bate e valida |
| semear_ambientes: pasta incompleta | reprova | reprova | OK (reprovou como esperado) | 1 ambientes; Anexo E: 69; 1 erro(s) |
| localizar_trecho: trecho vazio | reprova | reprova | OK (reprovou como esperado) | trecho vazio: nada a localizar |
| validar_acervo: marca no meio da frase | reprova | reprova | OK (reprovou como esperado) | acervo-0.4: 25 registros; 1 erro(s) |
| validar_acervo: fato depois de comentário na mesma linha | reprova | reprova | OK (reprovou como esperado) | acervo-0.4: 25 registros; 1 erro(s) |
| validar_acervo: ciclo em deriva_de | reprova | reprova | OK (reprovou como esperado) | acervo-0.4: 25 registros; 1 erro(s) |
| triagem_fixa: 'cocada' não é substância controlada | passa | passa | OK | triagem-fixa-0.3: 1 registro(s), 0 Falta(s) jurídica(s) |
| triagem_fixa: licença null vira licença ausente | passa | passa | OK | triagem-fixa-0.3: 1 registro(s), 1 Falta(s) jurídica(s) |
| triagem_fixa: link e citação curta com o autor citado, sem Falta pela regra | passa | passa | OK | PORTÃO: nenhuma Falta barra o ato ler agora |
| triagem_fixa: cópia da página inteira barra agora | reprova | reprova | OK (reprovou como esperado) | BARRA: o ato copiar fica parado pelas Faltas F-0034 (a Falta é dita e o caminho de liberação, apontado; D-020, D-025) |
| triagem_fixa: quem ensinou, sem consentimento, barra agora | reprova | reprova | OK (reprovou como esperado) | BARRA: o ato ler fica parado pelas Faltas F-0034 (a Falta é dita e o caminho de liberação, apontado; D-020, D-025) |
| triagem_fixa: receita detalhada de substância listada barra agora | reprova | reprova | OK (reprovou como esperado) | BARRA: o ato ler fica parado pelas Faltas F-0034 (a Falta é dita e o caminho de liberação, apontado; D-020, D-025) |
| triagem_fixa: conhecimento tradicional de origem identificável não barra a leitura | passa | passa | OK | PORTÃO: nenhuma Falta barra o ato ler agora; 1 Falta(s) só para a publicação, ditas |
| triagem_fixa: conhecimento tradicional de origem identificável, sem consentimento, barra a publicação | reprova | reprova | OK (reprovou como esperado) | BARRA: o ato publicar fica parado pelas Faltas F-0034, F-0035 (a Falta é dita e o caminho de liberação, apontado; D-020, D-025) |
| localizar_trecho: 'nunca' inserido não passa por semelhança (A-015 do K-105; D-041) | reprova | reprova | OK (reprovou como esperado) | estado: não verificável por máquina · grau 0.9545 · limiar 0.9 · normalizacao-0.2 |
| localizar_trecho: 'não' sem acento é OCR e passa (D-041) | passa | passa | OK | estado: localizado · grau 0.9615 · limiar 0.9 · normalizacao-0.2 |
| localizar_trecho: 'não' tirado não passa por semelhança (D-041) | reprova | reprova | OK (reprovou como esperado) | estado: não verificável por máquina · grau 0.96 · limiar 0.9 · normalizacao-0.2 |
| localizar_trecho: reconferência do Trecho com 'nunca' marcado como localizado | reprova | reprova | OK (reprovou como esperado) | NÃO SE SUSTENTA: marcado como localizado, mas palavra de negação ou de sentido contrário difere da fonte: nunca (D-041) |
| calcular_mu_lambda: linhagem mista sinalizada e fora da conta (A-010 do K-105; D-041) | passa | passa | OK | mu-lambda-0.2: 5 registros calculados; recálculo bate |
| calcular_mu_lambda: linhagem mista contada nos dois lados | reprova | reprova | OK (reprovou como esperado) | mu-lambda-0.2: 5 registros calculados; 4 divergência(s) |
| calcular_mu_lambda: trecho não verificável e leitura divergente contados (A-009 do K-105) | reprova | reprova | OK (reprovou como esperado) | mu-lambda-0.2: 5 registros calculados; 4 divergência(s) |
| calcular_mu_lambda: Proposição gravada pela regra antiga | reprova | reprova | OK (reprovou como esperado) | mu-lambda-0.2: 3 registros calculados; 1 divergência(s) |
| validar_acervo: o acervo da D-041 é válido | passa | passa | OK | acervo-0.4: 35 registros; válido |

### script de menções incidentais (K-102) (rodada B)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| menções: a CLB registrada vira ligação, o termo ambíguo vai marcado, a candidata tem linha com a origem | passa | passa | OK | mencoes-0.1: 1 texto(s), 2 Termo(s), 3 forma(s); 1 ligação(ões); 1 menção(ões) ambígua(s); conferido |
| menções: menção a outra CLB sem ligação | reprova | reprova | OK (reprovou como esperado) | mencoes-0.1: 1 texto(s), 2 Termo(s), 3 forma(s); 1 ligação(ões); 1 menção(ões) ambígua(s); 1 problema(s) |
| menções: linha do cartão de lista sem a menção de origem | reprova | reprova | OK (reprovou como esperado) | mencoes-0.1: 1 texto(s), 2 Termo(s), 3 forma(s); 1 ligação(ões); 1 menção(ões) ambígua(s); 1 problema(s) |
| menções: um cartão por CLB no lugar da linha no cartão de lista | reprova | reprova | OK (reprovou como esperado) | mencoes-0.1: 1 texto(s), 2 Termo(s), 3 forma(s); 1 ligação(ões); 1 menção(ões) ambígua(s); 1 problema(s) |
| menções: o termo ambíguo declarado se desdobra em Termo e CLB candidatos | passa | passa | OK | mencoes-0.1: 1 candidata(s) simulada(s) |
| menções: forma declarada que o trecho não traz | reprova | reprova | OK (reprovou como esperado) | mencoes-0.1: nada gravado |

### scripts do harness 0.2.0 (K-111) (rodada B)

| Caso | Esperado | Obtido | Resultado | Detalhe |
|---|---|---|---|---|
| juntar_saida: itens em arquivos pequenos viram um JSON que passa no esquema | passa | passa | OK | 2 item(ns) em - |
| juntar_saida: arquivo com aspas quebradas | reprova | reprova | OK (reprovou como esperado) |   001.json: JSON ilegível (Invalid control character at: line 1 column 62 (char 61)) |
| nomes_provaveis: o TR-0001 real sem nome de pessoa | passa | passa | OK | nomes-0.1: 1 Trecho(s) olhado(s); 0 nome(s) provável(is) para conferir (a lista não decide) |
| nomes_provaveis: nome sem tratamento e fora da tabela no contexto | reprova | reprova | OK (reprovou como esperado) | nomes-0.1: 1 Trecho(s) olhado(s); 1 nome(s) provável(is) para conferir (a lista não decide) |
