#!/bin/sh
# Hook SubagentStop (K-112, bloco 10a): acha um Python que funcione, sem caminho fixo da máquina de
# Vicente, e roda scripts/hook_subagent_stop.py com a entrada do hook. Ordem: o .venv do projeto
# (Windows ou Linux), python3, python, py -3. O atalho da Microsoft Store (python sem instalação real)
# falha no teste "-c ''" e é pulado.
RAIZ="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "$0")/.." && pwd)}"
for c in "$RAIZ/.venv/Scripts/python.exe" "$RAIZ/.venv/bin/python" python3 python "py -3"; do
  if $c -c "" >/dev/null 2>&1; then
    PYTHONUTF8=1 exec $c "$RAIZ/scripts/hook_subagent_stop.py"
  fi
done
echo "hook SubagentStop: nenhum Python que funcione" >&2
exit 0
