# Teste de modelo (bloco 12 do brief de execuções; K-115a; D-027, D-053)

Esta chamada é uma prova do banco de testes de modelos: a mesma prova roda em cada modelo candidato, e a sua saída passa pelos validadores do projeto e pelo confronto com a saída real do par. Na **primeira linha** da resposta, diga o ID do modelo que você é. O modelo foi escolhido pelo curador para o teste; não pare por ele diferir do frontmatter.

**Onde trabalhar.** Tudo nesta prova está em `{pasta}`:
- `{raiz}` é a fatia do acervo desta prova; trate-a como o acervo (os scripts aceitam `--raiz {raiz}`). Os registros que a habilidade cria ou muda se gravam aí.
- `{saida}` é o que a habilidade devolve ao curador.
- **Não leia o acervo real do repositório** (`acervo/`, `entrada/`, `ambientes/`, `grafo/`, `wiki-local/`, `testes/modelos/`) nem `trilhas/`, salvo o que o pedido abaixo liberar: a prova tirou de lá a saída real, e lê-la anula o teste. Pode ler o seu harness (`.claude/agents/`, `.claude/skills/`), `esquemas/`, `scripts/`, `AGENTS.md` e `00_Fundacao_Cultura_Liquida.md` (por `grep -n` e faixas de linhas).
- Sem web.

**Teto:** {teto} chamadas, contadas como o harness conta (cada ferramenta e cada pedido, mesmo agrupados num comando), com margem. Ao chegar perto do teto, grave o que tiver, valide e devolva.

**Gravar.** Sem a ferramenta Write: grave por Bash, um arquivo pequeno por vez (comando acima de uns 8 mil caracteres falha no Windows; nada de heredoc longo com texto de fonte). Python: `.venv/Scripts/python.exe`, a partir da raiz do repositório, com `PYTHONUTF8=1`. Nenhum dado pessoal de terceiros.

**Harness.** Antes de tudo, leia do disco o `SKILL.md` da habilidade da prova (`.claude/skills/<habilidade>/SKILL.md`): é a versão em teste, que pode ser mais nova que a carregada com o agente.

**Fim.** Rode a validação indicada abaixo, diga o resultado e termine com o bloco LOG do seu agente.

---
