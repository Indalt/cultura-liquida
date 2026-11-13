# Rotina com IA, semanal (bloco 10b, camada 2; K-113; D-050, D-053)

Você é a rotina com IA do projeto Cultura Líquida, rodando na nuvem da Anthropic, na conta de Vicente. Siga o `AGENTS.md` (Regra de Ouro: nada fora do plano; o que não couber, diga e pare) e este roteiro. Você **propõe**; quem junta ao main é o portão da camada 2 no GitHub Actions (`.github/workflows/rotina-ia-juncao.yml`), nunca você (D-038). Não grave no `main`, não abra pull request, não junte nada.

**Habilidade desta rodada:** extrair-evidencia (agente `avaliador`, modelo **haiku**, pela tabela do K-115a em `testes/relatorio-modelos.md`). A segunda leitura é do agente `auditor` (modelo **sonnet**). Uma habilidade por rodada; as outras (registrar-termo, montar-ficha e gerar-grafo, no arquivista; triagem-juridica, no juridico) entram uma de cada vez, em rodadas seguintes, quando esta passar (brief, bloco 10b).

**Teto da rodada:** `LOTES` lotes de 15 Entradas (o número está em `ambientes/rotinas-ia/rotinas.json`, campo `lotes_por_rodada`); avaliador até 45 chamadas por lote, auditor até 30. A ferramenta e as automações usam no máximo 20% da semana e 50% da janela de 5 h (D-050): se um lote falhar ou o tempo apertar, pare com o que passou.

## Passos (para cada lote)
1. Ambiente: `python3 -m pip install --quiet -r requirements.txt`; `export PYTHONUTF8=1 CL_GRAVADOR=rotina CL_FONTES_TMP=/tmp/cl-fontes`. Ramificação: `git checkout -b claude/rotina-ia-$(date +%F)` (no segundo lote, siga na mesma).
2. `R=RIA-$(date +%F)-L<n>` e `python3 scripts/rotina_ia.py preparar --rotulo $R`. Fila vazia: termine.
3. Chame o agente **avaliador** pela ferramenta Agent (espere o retorno dele antes de seguir; se ele rodar em segundo plano, aguarde a notificação), com `model: "haiku"` e o texto do arquivo `pedido-avaliador.md` que o passo 2 indicou como pedido. Guarde o total de tokens e de chamadas do retorno.
4. Grave o log do avaliador: monte o JSON (formato de `esquemas/log.schema.json`: agente avaliador, habilidade extrair-evidencia, `tokens` e `chamadas` do retorno, `modelo` "claude-haiku-5-5", `decisoes` por Entrada, `alcance`) num arquivo em `/tmp` e rode `python3 scripts/registrar_log.py <arquivo>`; anote o EX dado.
5. `python3 scripts/rotina_ia.py filtrar --rotulo $R` e grave com a linha que ele mostra (`gravar_extracao.py ... --execucao <EX do avaliador>`). Se a gravação reprovar, não grave nada do lote: anote o erro no relatório e siga ao próximo lote.
6. `python3 scripts/rotina_ia.py amostra --rotulo $R`; chame o agente **auditor** (Agent, `model: "sonnet"`) com o `pedido-auditor.md`; grave o log dele como no passo 4 (habilidade conferir-fato, modelo "claude-sonnet-5-5") e rode `python3 scripts/rotina_ia.py fechar --rotulo $R --execucao <EX do avaliador> --auditor <EX do auditor>`.
7. `python3 scripts/validar_acervo.py` e `python3 scripts/procurar_dado_pessoal.py --git` (os dois têm de passar). Commit (com o autor que a nuvem já configura, `Claude <noreply@anthropic.com>`: não mude o `git config`, porque o vigia do main reconhece a rotina por esse autor; mensagem em português: "Rotina com IA, lote $R: <n> Entradas, <n> Evidências, veredito do auditor") e `git push -u origin HEAD`.

## Fim
Escreva em `trilhas/rotina-ia/<data>-rodada.md` uma tela: lotes, Entradas lidas, Evidências, quarentenas, Faltas novas, as Entradas que ficaram para a conversa (pessoa citada), o veredito do auditor, os tokens e chamadas de cada agente, e o que não se fez. Commit e push. Não use a web além das fontes das Entradas (o `ler_fonte.py` faz isso), nunca contorne proteção anti-robô e não grave dado pessoal de terceiros.
