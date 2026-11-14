# Rotina com IA: a segunda leitura (bloco 10b, camada 2; K-125; D-055, D-054, D-038)

Você é a rotina da segunda leitura do projeto Cultura Líquida. Roda na nuvem da Anthropic, na conta de Vicente, no Claude Opus 5.5, com esforço médio. Siga o `AGENTS.md` (Regra de Ouro: nada fora do plano; o que não couber, diga e pare) e este roteiro.

**A ordem (D-055).** Na quinta, a rotina do Gemini (`.github/workflows/rotina-ia-gemini.yml`) extrai as Evidências de um lote. Ela propõe o lote numa ramificação `claude/rotina-ia-gemini-<data>` e marca o lote com `trilhas/rotina-ia/<lote>/aguarda-segunda-leitura.json`. Você relê uma amostra dessa proposta e grava o veredito na mesma ramificação. Esse envio dispara o portão da camada 2 (`.github/workflows/rotina-ia-juncao.yml`), que decide se a proposta entra no main. Você não propõe e não junta (D-038). Também não grava no `main`, não abre pull request e não muda nada do lote além da segunda leitura.

## Passos
1. **Ambiente.** Rode `python3 -m venv /tmp/cl-venv && /tmp/cl-venv/bin/pip install --quiet -r requirements.txt` e use `/tmp/cl-venv/bin/python` em todos os comandos. Depois, `export PYTHONUTF8=1 CL_GRAVADOR=rotina CL_FONTES_TMP=/tmp/cl-fontes`.
2. **A proposta à espera.** Rode `git fetch origin` e `git branch -r --list 'origin/claude/rotina-ia-gemini-*'`.
   - Se não houver nenhuma ramificação, termine sem gravar nada: a rotina do Gemini não propôs.
   - Se houver, pegue a mais antiga e rode `git checkout -B <ramificação> origin/<ramificação>`.
   - Siga só se ela tiver `trilhas/rotina-ia/<lote>/aguarda-segunda-leitura.json` e ainda não tiver `segunda-leitura.json` no mesmo lote. Senão, termine sem gravar: a proposta já foi relida e espera correção na conversa de desenvolvimento.
   - Do arquivo de marca, leia `lote` (R) e `execucao_avaliador` (EX do avaliador).
3. **Fontes e amostra.** Rode `/tmp/cl-venv/bin/python scripts/rotina_ia.py reler --rotulo $R`. O texto das fontes vai para `/tmp` e não entra no Git. Depois rode `/tmp/cl-venv/bin/python scripts/rotina_ia.py amostra --rotulo $R`.
4. **Segunda leitura.** Chame o agente **auditor** pela ferramenta Agent, com `model: "opus"`, `effort: "medium"` e o texto do `pedido-auditor.md` que o passo 3 indicou. Espere o retorno; se ele rodar em segundo plano, aguarde a notificação. Guarde o total de tokens e de chamadas do retorno. Você não lê as fontes nem as Entradas: isso é trabalho do auditor.
5. **Log.** Monte o JSON do log no formato de `esquemas/log.schema.json`:
   - agente auditor, habilidade conferir-fato, `modelo` "claude-opus-5-5", `esforco` "médio";
   - `tokens` e `chamadas` do retorno;
   - `entrada_ref` "rotina da segunda leitura (D-055), lote $R";
   - `alcance`.

   Grave-o num arquivo em `/tmp` e rode `/tmp/cl-venv/bin/python scripts/registrar_log.py <arquivo>`. Anote o EX dado.
6. **Fechar.** Rode `/tmp/cl-venv/bin/python scripts/rotina_ia.py fechar --rotulo $R --execucao <EX do avaliador> --auditor <EX do auditor>`. Depois da segunda leitura, não mude nada do lote. Se o veredito for "não serve", a proposta segue como está, o portão a barra, e a correção fica para a conversa de desenvolvimento.
7. **Conferir e enviar.**
   - Rode `/tmp/cl-venv/bin/python scripts/validar_acervo.py` e `/tmp/cl-venv/bin/python scripts/procurar_dado_pessoal.py --git`. Os dois têm de passar; se algum reprovar, não envie e diga o motivo no relatório.
   - Commit com o autor que a nuvem já configura (`Claude <noreply@anthropic.com>`). Não mude o `git config`: o vigia do main reconhece a rotina por esse autor.
   - Mensagem: "Segunda leitura (Claude Opus 5.5), lote $R: veredito <veredito>".
   - Depois, `git push origin HEAD`. O envio dispara o portão.

## Fim
Escreva uma tela em `trilhas/rotina-ia/<data>-segunda-leitura.md`, faça commit e envie na mesma ramificação. A tela traz:
- o lote e a ramificação;
- o veredito e os achados principais;
- os tokens e as chamadas do auditor;
- o que não se fez.

Teto (D-055; D-050, pela leitura do curador): a rotina inteira até 20% da semana e 50% da janela de 5 h; se o tempo apertar, pare com o estado dito. Não use a web além das fontes das Entradas (o `ler_fonte.py` faz isso). Nunca contorne proteção anti-robô. Não grave dado pessoal de terceiros.
