"""Portão da camada 2 (bloco 10b, K-113; padrão A-10, D-038; D-050): as checagens sem IA que a proposta
da rotina com IA (uma ramificação `claude/...`) passa antes de a ferramenta juntá-la ao main.

Quem propõe não aprova (D-038): a rotina propõe; este script, rodado pelo GitHub Actions a partir do
**main** (nunca da cópia da proposta), decide; a junção é do workflow `rotina-ia-juncao.yml`. O portão
não depende de registro que a rotina muda (insumo 119): o código e as regras vêm do main, e a suíte de
casos com registros reais (`rodar_testes.py`) não entra; no lugar, checagens sobre a própria proposta.

Checagens (todas sem IA, com a versão gravada):
  1. **alcance**: a proposta só toca o que a camada 2 pode tocar: `acervo/` (sem `acervo/lugares/`),
     as Entradas já existentes em `entrada/` (nenhuma nova), `trilhas/logs/`, `trilhas/rotina-ia/` e
     `trilhas/amostras/`; nada em `scripts/`, `esquemas/`, `.claude/`, `.github/`, `ambientes/` nem
     nos textos do plano. Nenhum arquivo apagado;
  2. **faixa**: todo registro novo do acervo tem número na faixa do gravador `rotina` (numeracao_id; as
     duas camadas gravam nela, e a colisão entre elas o `validar_acervo.py` pega na árvore já juntada
     ao main, que o workflow monta antes de rodar o portão);
  3. `validar_acervo.py --raiz <proposta>` (o acervo e as Entradas no contrato, sem colisão de ID);
  4. `deduplicar.py --conferir --raiz <proposta>`;
  5. `procurar_dado_pessoal.py` nos arquivos que a proposta muda (nenhum dado pessoal de terceiros);
  6. **segunda leitura** (D-026): `trilhas/rotina-ia/<lote>/segunda-leitura.json` com o auditor
     (a Execução dele em `trilhas/logs/`), a semente da amostra gravada (`trilhas/amostras/`) e
     `sortear_amostra.py --conferir` batendo; o veredito do auditor "serve" ou "serve com ressalvas"
     (com ressalvas, os achados vão ao insumo; "não serve" reprova).

Uso:
    python scripts/portao_camada2.py --proposta <pasta da ramificação> --base <commit do main>
       
Código 0 = passa (pode juntar); 1 = reprova (não junta; a ramificação fica, com o motivo no log).
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_valores  # noqa: E402

VERSAO = "portao-camada2-0.1"
PY = sys.executable
S = Path(__file__).resolve().parent
PODE = (re.compile(r"^acervo/(?!lugares/)"), re.compile(r"^entrada/EN-\d+\.json$"),
        re.compile(r"^trilhas/logs/"), re.compile(r"^trilhas/rotina-ia/"), re.compile(r"^trilhas/amostras/"))
VEREDITOS_QUE_PASSAM = {"serve", "serve com ressalvas"}


def git(pasta: Path, *args: str) -> list[str]:
    r = subprocess.run(["git", *args], cwd=pasta, capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        raise SystemExit(f"git {' '.join(args)}: {r.stderr.strip()[:300]}")
    return [x for x in r.stdout.splitlines() if x]


def mudancas(prop: Path, base: str) -> list[tuple[str, str]]:
    """(estado, caminho) de cada arquivo que a proposta muda em relação ao main."""
    out = []
    for linha in git(prop, "diff", "--name-status", "--no-renames", f"{base}...HEAD"):
        estado, caminho = linha.split("\t", 1)
        out.append((estado[0], caminho))
    return out


def checar_alcance(ms: list[tuple[str, str]]) -> list[str]:
    erros = []
    for estado, c in ms:
        if not any(p.search(c) for p in PODE):
            erros.append(f"fora do alcance da camada 2: {c}")
        elif estado == "D":
            erros.append(f"apaga arquivo (nada se apaga; princípio 10): {c}")
        elif c.startswith("entrada/") and estado == "A":
            erros.append(f"Entrada nova (a camada 2 não cria Entrada): {c}")
    return erros


def checar_faixa(ms: list[tuple[str, str]]) -> list[str]:
    ini, fim = carregar_valores()["valores"]["numeracao_id"]["valor"]["faixas"]["rotina"]
    erros = []
    for estado, c in ms:
        if estado == "A" and c.startswith("acervo/"):
            m = re.search(r"/[A-Z]{1,3}-(\d+)\.json$", c)
            if m and not ini <= int(m.group(1)) <= fim:
                erros.append(f"registro novo fora da faixa rotina ({ini}-{fim}): {c}")
    return erros


def checar_segunda_leitura(prop: Path, ms: list[tuple[str, str]]) -> list[str]:
    leituras = [c for e, c in ms if re.match(r"^trilhas/rotina-ia/[^/]+/segunda-leitura\.json$", c)]
    if not leituras:
        return ["sem segunda leitura (trilhas/rotina-ia/<lote>/segunda-leitura.json)"]
    erros = []
    for c in leituras:
        d = json.loads((prop / c).read_text(encoding="utf-8"))
        if d.get("veredito") not in VEREDITOS_QUE_PASSAM:
            erros.append(f"{c}: veredito do auditor '{d.get('veredito')}'")
        ex = d.get("execucao_auditor", "")
        logs = list((prop / "trilhas" / "logs").glob("*.jsonl"))
        if not ex or not any(f'"id": "{ex}"' in p.read_text(encoding="utf-8") or f'"id":"{ex}"' in p.read_text(encoding="utf-8")
                             for p in logs):
            erros.append(f"{c}: a Execução do auditor '{ex}' não está em trilhas/logs/")
        am = d.get("amostra")
        if not am or not (prop / am).exists():
            erros.append(f"{c}: sem a amostra gravada (semente) em trilhas/amostras/")
        else:
            r = subprocess.run([PY, str(S / "sortear_amostra.py"), "--raiz", str(prop), "--conferir", str(prop / am)],
                               capture_output=True, text=True, encoding="utf-8")
            if r.returncode != 0:
                erros.append(f"{c}: sortear_amostra --conferir não bate: {(r.stdout + r.stderr).strip()[-200:]}")
    return erros


def rodar(nome: str, cmd: list[str]) -> list[str]:
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    cauda = " | ".join(((r.stdout or "") + (r.stderr or "")).strip().splitlines()[-3:])[:600]
    return [] if r.returncode == 0 else [f"{nome} reprovou: {cauda}"]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--proposta", type=Path, required=True)
    ap.add_argument("--base", required=True)
    ap.add_argument("--saida", type=Path, help="grava o resultado (JSON) para o log da junção")
    a = ap.parse_args()
    prop = a.proposta.resolve()
    ms = mudancas(prop, a.base)
    checagens = {
        "alcance": checar_alcance(ms),
        "faixa": checar_faixa(ms),
        "validar_acervo": rodar("validar_acervo", [PY, str(S / "validar_acervo.py"), "--raiz", str(prop)]),
        "deduplicar --conferir": rodar("deduplicar", [PY, str(S / "deduplicar.py"), "--conferir", "--raiz", str(prop)]),
        "procurar_dado_pessoal": rodar("procurar_dado_pessoal", [PY, str(S / "procurar_dado_pessoal.py"),
                                       *[str(prop / c) for e, c in ms if e != "D" and (prop / c).is_file()]]) if ms else [],
        "segunda leitura": checar_segunda_leitura(prop, ms),
    }
    if not ms:
        checagens["alcance"].append("proposta vazia")
    passa = not any(checagens.values())
    for nome, erros in checagens.items():
        print(f"{'PASSA' if not erros else 'REPROVA'} {nome}")
        for e in erros[:15]:
            print(f"  {e[:300]}")
    res = {"versao_regra": VERSAO, "base": a.base, "arquivos": len(ms), "passa": passa,
           "checagens": {k: v for k, v in checagens.items()}}
    if a.saida:
        a.saida.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{VERSAO}: {'passa' if passa else 'reprova'} ({len(ms)} arquivo(s))")
    return 0 if passa else 1


if __name__ == "__main__":
    sys.exit(main())
