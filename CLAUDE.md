@AGENTS.md

# Notas do Claude Code

Só o Claude Code opera os agentes deste projeto (D-029): pasta `.claude/`, sem espelho `.agents/`.

## Ambiente Windows
- **Python real:** `C:/Users/alqui/AppData/Local/Programs/Python/Python312/python.exe`. O `python` do PATH é um atalho da Microsoft Store e falha (código 49).
- **Ambiente do projeto:** `.venv/Scripts/python.exe` (tem `jsonschema`). Os scripts de `scripts/` rodam com qualquer um dos dois.
- **UTF-8:** usar `PYTHONUTF8=1`; nunca imprimir acentos assumindo cp1252.
- **Buscas que podem não achar nada** (`grep`, `rg`, `ls` de caminho opcional): acrescentar `|| true`.
- **Git Bash e `gh api`:** caminhos de API sem a barra inicial (`repos/...`).
- Não usar `sleep` em primeiro plano.

## Modelos por agente (iniciais, provisórios até os testes do Passo 1; D-027)
- **Sessão principal (curador):** `claude-opus-5-5`, esforço médio, sem ultracode. Se o ID do modelo for outro, avisar e parar.
- **redator:** Opus 5.5, médio. **auditor, juridico, rastreador:** Sonnet 5.5, alto.
- **avaliador, arquivista, campo-de-acao:** a definir no Passo 1 (o arquivo traz Sonnet 5.5 como marcador; não chamar antes do caso-piloto).
- Subagentes **um por vez**, com teto de chamadas declarado no pedido. Sem Workflow sem pedido explícito.
- **Depois de cada Agent:** o curador grava o log completo com `scripts/registrar_log.py` (tokens e chamadas vêm do retorno do Agent) e soma o consumo no checklist. O hook `SubagentStop` grava só uma linha mínima de segurança.

## Commits
- Autor configurado **só neste repositório**: `Vicente <vicente@dacaatinga.com.br>` ("assinado" = autoria, não GPG).
- Mensagem em português, terminando com a linha de atribuição que o sistema indicar na sessão.
- Antes do commit: `scripts/procurar_dado_pessoal.py --git`. **Push depois de cada commit.**
- A proteção do `main` exige revisão, mas o dono grava direto (`enforce_admins: false`); o aviso "Bypassed rule violations" é esperado.
