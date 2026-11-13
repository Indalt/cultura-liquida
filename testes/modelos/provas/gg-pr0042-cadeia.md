# Prova: gerar-grafo (arquivista)

No grafo 4D da CLB cajuína (CL-0001), faltam os Elementos e as Arestas que descrevem as etapas de produção dadas pela **PR-0042** e pela **PR-0059** (em `{raiz}/acervo/proposicoes/`, com as Evidências e os Trechos). Monte-os pela habilidade gerar-grafo: um Elemento por etapa (X = insumo, Y = processo, Z = o período que a Proposição diz, W = a compreensão local ou a Falta), ligando cada etapa à seguinte por uma Aresta, com as Proposições que sustentam cada um. Use os registros que já existem em `{raiz}`: os insumos (`acervo/insumos-x/`), os processos (`acervo/processos/`), as compreensões locais (`acervo/compreensoes-locais/`), as Faltas, e os outros Elementos e Arestas do grafo, como modelo do formato e da convenção. IDs novos: o próximo livre de cada prefixo na raiz. Esquemas: `esquemas/elemento.schema.json` e `esquemas/aresta.schema.json`.

μ e λ só por script: `.venv/Scripts/python.exe scripts/calcular_mu_lambda.py --raiz {raiz} --gravar --sem-grafo`.

Validação (as duas têm de passar): `.venv/Scripts/python.exe scripts/validar_acervo.py --raiz {raiz}` e `.venv/Scripts/python.exe scripts/calcular_mu_lambda.py --raiz {raiz} --conferir --sem-grafo`.
