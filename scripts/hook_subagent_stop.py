"""Hook SubagentStop: grava uma linha mínima de log a cada fim de subagente (rede de segurança).

Configurado em .claude/settings.json. Recebe pela entrada padrão o JSON do Claude Code
(campos oficiais conferidos em 16/10/2026: session_id, transcript_path, cwd, hook_event_name,
stop_hook_active, agent_id, agent_type, agent_transcript_path, last_assistant_message).
Esse JSON não traz tokens nem duração; o script tenta somar o uso e contar as chamadas de
ferramenta pelo transcript do subagente e anota isso como estimativa em `resultados`.
O campo `tokens` fica null: o número oficial é o do retorno do Agent, gravado pelo curador.

Nunca bloqueia o subagente: sai sempre com código 0 e sem saída.
Não grava o texto da última mensagem nem caminhos completos (só tamanhos e nomes de arquivo).
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))


def resumo_transcript(caminho: str) -> tuple[dict, list[str]]:
    info = {"tokens": 0, "chamadas": 0, "modelo": None, "inicio": None, "fim": None}
    erros: list[str] = []
    p = Path(caminho).expanduser() if caminho else None
    if not p or not p.is_file():
        return info, ["transcript do subagente não encontrado"]
    for linha in p.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            reg = json.loads(linha)
        except json.JSONDecodeError:
            continue
        ts = reg.get("timestamp")
        if ts:
            info["inicio"] = info["inicio"] or ts
            info["fim"] = ts
        msg = reg.get("message") or {}
        if not isinstance(msg, dict):
            continue
        if msg.get("model"):
            info["modelo"] = msg["model"]
        uso = msg.get("usage") or {}
        if isinstance(uso, dict):
            info["tokens"] += sum(v for k, v in uso.items() if k.endswith("tokens") and isinstance(v, int))
        conteudo = msg.get("content")
        if isinstance(conteudo, list):
            info["chamadas"] += sum(1 for c in conteudo if isinstance(c, dict) and c.get("type") == "tool_use")
    return info, erros


def segundos(inicio: str | None, fim: str | None):
    try:
        a = datetime.fromisoformat(inicio.replace("Z", "+00:00"))
        b = datetime.fromisoformat(fim.replace("Z", "+00:00"))
        return round((b - a).total_seconds(), 1)
    except Exception:
        return None


def main() -> None:
    try:
        dados = json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError:
        dados = {}
    tipo = str(dados.get("agent_type") or "desconhecido").lower()
    tipo = re.sub(r"[^a-z0-9-]+", "-", tipo).strip("-") or "desconhecido"
    info, erros = resumo_transcript(dados.get("agent_transcript_path", ""))
    ultima = dados.get("last_assistant_message") or ""
    linha = {
        "data_hora": datetime.now().astimezone().isoformat(timespec="seconds"),
        "agente": tipo,
        "habilidade": "n/a",
        "versao_harness": "n/a",
        "modelo": info["modelo"] or "não informado",
        "esforco": "n/a",
        "entrada_ref": Path(dados.get("agent_transcript_path") or "sem-transcript").name,
        "acoes": ["subagente terminou (hook SubagentStop)"],
        "resultados": [
            f"última mensagem: {len(ultima)} caracteres",
            f"estimativa pelo transcript: {info['tokens']} tokens somados (entrada, saída e cache), "
            f"{info['chamadas']} chamadas de ferramenta",
        ],
        "decisoes": [],
        "tokens": None,
        "chamadas": None,
        "duracao_s": segundos(info["inicio"], info["fim"]),
        "erros": erros,
        "sessao": str(dados.get("session_id") or ""),
        "agente_id": str(dados.get("agent_id") or ""),
        "fonte_do_registro": "hook-SubagentStop",
    }
    try:
        from registrar_log import conferir, gravar

        problemas = conferir(linha)
        if problemas:
            linha["resultados"] = ["linha reduzida: a conferência reprovou a versão completa"]
            linha["erros"] = [p[:200] for p in problemas if "dado pessoal" not in p]
        gravar(linha)
    except Exception as e:  # rede de segurança: nunca derrubar o subagente
        try:
            from _comum import RAIZ

            with (RAIZ / "trilhas" / "logs" / "hook-erros.txt").open("a", encoding="utf-8") as f:
                f.write(f"{datetime.now().isoformat()} {type(e).__name__}: {e}\n")
        except Exception:
            pass


if __name__ == "__main__":
    main()
    sys.exit(0)
