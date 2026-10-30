"""Roda os casos de teste de todas as habilidades (.claude/skills/*/exemplos/casos.json e, da rodada B, casos-rodada-b.json)
e dos contratos do §6 (esquemas/exemplos/casos.json) e dos scripts do núcleo (testes/nucleo/casos.json) da coleta (testes/coleta/casos.json) do bloco 7 (testes/extracao/casos.json) e das menções incidentais (testes/mencoes/casos.json, K-102) e dos scripts do harness 0.2.0 (testes/rodada-b/casos.json, K-111).

Formato de casos.json:
    {"habilidade": "...", "rodada": "A"|"B", "casos": [
       {"nome": "...", "espera": "passa"|"reprova"|"pendente",
        "esquema": "conferencia", "entrada": "caminho/relativo/a/raiz.json"}          # validação por esquema
       ou
        "comando": ["scripts/x.py", "arg", ...], "saida_contem": "texto opcional"}   # script: código 0 = passa
       "criterio": "o que o caso demonstra"}]}

Um caso dá OK quando o resultado é o esperado (inclusive "reprova" esperado).
Uso:
    python scripts/rodar_testes.py [--rodada A] [--relatorio testes/relatorio-rodada-A.md]
Código 0 = todos OK (pendentes não contam como falha); 1 = algum resultado inesperado.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_esquema, carregar_json  # noqa: E402
from procurar_dado_pessoal import achar  # noqa: E402
from validar import validar_arquivo  # noqa: E402


def rodar_caso(c: dict) -> tuple[str, str]:
    """Devolve (obtido, detalhe): obtido em {passa, reprova, pendente, erro}."""
    if c["espera"] == "pendente":
        return "pendente", c.get("criterio", "")
    try:
        if "esquema" in c:
            erros = validar_arquivo(RAIZ / c["entrada"], carregar_esquema(c["esquema"]))
            return ("passa" if not erros else "reprova"), "; ".join(erros[:3])
        cmd = [sys.executable, *[str(RAIZ / x) if i == 0 else x for i, x in enumerate(c["comando"])]]
        r = subprocess.run(cmd, cwd=RAIZ, capture_output=True, text=True, encoding="utf-8")
        saida = (r.stdout + r.stderr).strip()
        obtido = "passa" if r.returncode == 0 else "reprova"
        if c.get("saida_contem") and c["saida_contem"] not in saida:
            return "erro", f"saída não contém {c['saida_contem']!r}: {saida[:200]}"
        return obtido, saida.splitlines()[-1][:200] if saida else ""
    except Exception as e:  # caso mal escrito
        return "erro", f"{type(e).__name__}: {e}"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--rodada")
    ap.add_argument("--relatorio", type=Path)
    a = ap.parse_args()
    linhas_rel = []
    cont = {"ok": 0, "falha": 0, "pendente": 0}
    arquivos = sorted((RAIZ / ".claude" / "skills").glob("*/exemplos/casos*.json")) + [RAIZ / "esquemas" / "exemplos" / "casos.json", RAIZ / "testes" / "nucleo" / "casos.json", RAIZ / "testes" / "coleta" / "casos.json", RAIZ / "testes" / "extracao" / "casos.json", RAIZ / "testes" / "mencoes" / "casos.json", RAIZ / "testes" / "rodada-b" / "casos.json"]
    for arq in [x for x in arquivos if x.exists()]:
        spec = carregar_json(arq)
        if a.rodada and spec.get("rodada") != a.rodada:
            continue
        linhas_rel.append(f"\n### {spec['habilidade']} (rodada {spec.get('rodada', '?')})\n")
        linhas_rel.append("| Caso | Esperado | Obtido | Resultado | Detalhe |")
        linhas_rel.append("|---|---|---|---|---|")
        for c in spec["casos"]:
            obtido, det = rodar_caso(c)
            if obtido == "pendente":
                res = "PENDENTE"
                cont["pendente"] += 1
            elif obtido == c["espera"]:
                res = "OK" + (" (reprovou como esperado)" if obtido == "reprova" else "")
                cont["ok"] += 1
            else:
                res = "FALHA"
                cont["falha"] += 1
            det = det.replace("|", "/").replace("\n", " ")
            for _, _, s in achar(det):  # o relatório vai para o Git: nunca repetir dado pessoal, nem fictício
                det = det.replace(s, "[dado pessoal omitido]")
            linhas_rel.append(f"| {c['nome']} | {c['espera']} | {obtido} | {res} | {det} |")
            print(f"{res:<28} {spec['habilidade']}: {c['nome']}")
    total = f"OK: {cont['ok']} · FALHA: {cont['falha']} · PENDENTE: {cont['pendente']}"
    print(total)
    if a.relatorio:
        cab = [
            f"# Relatório de testes{' da rodada ' + a.rodada if a.rodada else ''}",
            "",
            f"Gerado por `scripts/rodar_testes.py` em {datetime.now().astimezone().isoformat(timespec='seconds')}.",
            f"Validador: `jsonschema` se instalado (.venv), senão o validador mínimo de `scripts/_comum.py`. Python: {sys.version.split()[0]}.",
            "",
            f"**Totais:** {total}.",
            "",
            "\"OK (reprovou como esperado)\" = o caso com erro foi recusado pelo validador, como deve ser.",
        ]
        a.relatorio.parent.mkdir(parents=True, exist_ok=True)
        a.relatorio.write_text("\n".join(cab + linhas_rel) + "\n", encoding="utf-8")
        print(f"relatório: {a.relatorio}")
    return 1 if cont["falha"] else 0


if __name__ == "__main__":
    sys.exit(main())
