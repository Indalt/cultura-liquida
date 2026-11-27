"""Trava dos testes (trava-testes-0.1; sem IA): caso de teste mudado ou tirado só entra com confirmação.

Por quê (D-059, 20/11/2026): quando uma mudança faz um teste deixar de passar, ela não entra sem
verificação e confirmação. O caminho circular é mudar o teste para ele passar: o conserto por cima
esconde o problema e faz nascer outro. A suíte (rodar_testes.py) já reprova o caso que falha; esta
trava fecha o outro caminho: guarda a impressão digital de cada caso e reprova quando um caso muda ou
sai sem uma confirmação registrada.

O que é o caso, para a trava: o objeto do caso no casos.json (todos os campos, inclusive "espera" e
"criterio") e o conteúdo de cada arquivo ou pasta que ele cita dentro das pastas de teste (testes/,
esquemas/exemplos/, .claude/skills/<habilidade>/exemplos/). O código de scripts/ não entra: é o que o
teste confere, rodando. Fim de linha CRLF conta como LF (a mesma impressão no Windows e no runner).

- Caso novo: entra na trava com --gravar-novos. Acrescentar teste fortalece; não pede confirmação.
- Caso mudado ou tirado: reprova até haver confirmação em testes/confirmacoes-testes.jsonl, gravada
  por --confirmar: o motivo, quem verificou (não quem mudou; D-038) e a confirmação de Vicente, com
  onde ele confirmou. A confirmação grava a impressão nova na trava; a linha antiga fica (nada se apaga).
- --pre-commit: além de conferir, olha o que vai no commit: impressão da trava mudada ou tirada sem
  linha nova de confirmação no mesmo commit reprova (a trava não se muda à mão); e linha nova em
  testes/falhas-conhecidas.txt reprova (a lista das falhas de antes da trava só diminui).

Uso:
    python scripts/trava_testes.py                     # confere; código 1 se algo mudou sem confirmação
    python scripts/trava_testes.py --gravar-novos      # põe na trava só os casos novos
    python scripts/trava_testes.py --confirmar --caso "<arquivo>::<nome>" --motivo "..." \\
        --verificado-por "<quem conferiu por que mudou>" --confirmado-por vicente --onde "<onde Vicente confirmou>"
    python scripts/trava_testes.py --pre-commit        # o que o gancho de pre-commit roda
    python scripts/trava_testes.py --raiz <pasta>      # outra pasta (os casos de teste da própria trava)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

VERSAO = "trava-testes-0.1"
RAIZ_PADRAO = Path(__file__).resolve().parent.parent
TRAVA = Path("testes") / "trava-testes.json"
CONFIRMACOES = Path("testes") / "confirmacoes-testes.jsonl"
PASTAS_DE_TESTE = ("testes/", "esquemas/exemplos/", ".claude/skills/")


def arquivos_de_casos(raiz: Path) -> list[Path]:
    """Os casos.json que a suíte roda (a mesma lista do rodar_testes.py, que a importa daqui)."""
    fixos = ["esquemas/exemplos", "testes/nucleo", "testes/coleta", "testes/extracao", "testes/mencoes",
             "testes/rodada-b", "testes/rotinas", "testes/manutencao", "testes/trava", "testes/cabecalhos"]
    arqs = sorted((raiz / ".claude" / "skills").glob("*/exemplos/casos*.json"))
    arqs += [raiz / p / "casos.json" for p in fixos]
    return [a for a in arqs if a.exists()]


def _bytes(p: Path) -> bytes:
    return p.read_bytes().replace(b"\r\n", b"\n")


def _hash_caminho(p: Path) -> str:
    h = hashlib.sha256()
    if p.is_file():
        h.update(_bytes(p))
    else:
        # Chave sem caixa por partes: a mesma ordem no Windows (onde a trava foi gravada) e no Linux.
        for f in sorted((x for x in p.rglob("*") if x.is_file() and "__pycache__" not in x.parts),
                        key=lambda x: tuple(s.lower() for s in x.relative_to(p).parts)):
            h.update(f.relative_to(p).as_posix().encode())
            h.update(hashlib.sha256(_bytes(f)).digest())
    return h.hexdigest()


def _citados(caso: dict) -> list[str]:
    """Os caminhos que o caso cita dentro das pastas de teste."""
    cands = [caso.get("entrada")] if caso.get("entrada") else []
    for arg in (caso.get("comando") or [])[1:]:
        cands.append(arg.split("=", 1)[-1] if "=" in arg else arg)
    return [c for c in cands if isinstance(c, str) and c.replace("\\", "/").startswith(PASTAS_DE_TESTE)]


def impressoes(raiz: Path) -> dict[str, str]:
    saida = {}
    for arq in arquivos_de_casos(raiz):
        rel = arq.relative_to(raiz).as_posix()
        vistos = {}
        for caso in json.loads(arq.read_text(encoding="utf-8")).get("casos", []):
            nome = caso.get("nome", "?")
            vistos[nome] = vistos.get(nome, 0) + 1
            chave = f"{rel}::{nome}" + (f"#{vistos[nome]}" if vistos[nome] > 1 else "")
            h = hashlib.sha256(json.dumps(caso, ensure_ascii=False, sort_keys=True).encode())
            for c in _citados(caso):
                p = raiz / c
                h.update(c.encode())
                h.update((_hash_caminho(p) if p.exists() else "ausente").encode())
            saida[chave] = h.hexdigest()[:16]
    return saida


def ler_trava(raiz: Path) -> dict[str, str]:
    p = raiz / TRAVA
    return json.loads(p.read_text(encoding="utf-8"))["casos"] if p.exists() else {}


def gravar_trava(raiz: Path, casos: dict[str, str]) -> None:
    dados = {"versao": VERSAO,
             "nota": "Impressão de cada caso de teste. Não se edita à mão: casos novos entram por "
                     "trava_testes.py --gravar-novos; caso mudado ou tirado, por --confirmar (D-059).",
             "casos": dict(sorted(casos.items()))}
    (raiz / TRAVA).write_text(json.dumps(dados, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def diferencas(raiz: Path) -> tuple[list[str], list[str], list[str]]:
    atual, trava = impressoes(raiz), ler_trava(raiz)
    novos = sorted(k for k in atual if k not in trava)
    mudados = sorted(k for k in atual if k in trava and trava[k] != atual[k])
    tirados = sorted(k for k in trava if k not in atual)
    return novos, mudados, tirados


def conferir(raiz: Path) -> list[str]:
    """Os problemas da trava, um por linha (lista vazia = em ordem). O rodar_testes.py chama isto."""
    novos, mudados, tirados = diferencas(raiz)
    p = [f"caso mudado sem confirmação: {k}" for k in mudados]
    p += [f"caso tirado sem confirmação: {k}" for k in tirados]
    p += [f"caso novo fora da trava: {k} (rode trava_testes.py --gravar-novos)" for k in novos]
    return p


def _git(raiz: Path, *args: str) -> str | None:
    r = subprocess.run(["git", *args], cwd=raiz, capture_output=True, text=True, encoding="utf-8")
    return r.stdout if r.returncode == 0 else None


def conferir_commit(raiz: Path) -> list[str]:
    """No commit: impressão da trava mudada ou tirada exige linha nova de confirmação no mesmo commit."""
    antes_txt = _git(raiz, "show", f"HEAD:{TRAVA.as_posix()}")
    agora_txt = _git(raiz, "show", f":{TRAVA.as_posix()}")
    if antes_txt is None or agora_txt is None:
        return []  # a trava ainda não existe no HEAD ou não vai no commit: nada a comparar
    antes, agora = json.loads(antes_txt)["casos"], json.loads(agora_txt)["casos"]
    conf_antes = set((_git(raiz, "show", f"HEAD:{CONFIRMACOES.as_posix()}") or "").splitlines())
    novas = [json.loads(x) for x in (_git(raiz, "show", f":{CONFIRMACOES.as_posix()}") or "").splitlines()
             if x.strip() and x not in conf_antes]
    cobertos = {(c["caso"], c["depois"]) for c in novas}
    p = []
    for k, v in antes.items():
        if agora.get(k) != v and (k, agora.get(k)) not in cobertos:
            p.append(f"a trava mudou para {k} sem confirmação nova neste commit (a trava não se muda à mão)")
    return p


FALHAS_CONHECIDAS = Path("testes") / "falhas-conhecidas.txt"


def conferir_falhas_conhecidas(raiz: Path) -> list[str]:
    """A lista de falhas conhecidas só diminui: linha nova no commit reprova (D-059)."""
    antes = _git(raiz, "show", f"HEAD:{FALHAS_CONHECIDAS.as_posix()}")
    agora = _git(raiz, "show", f":{FALHAS_CONHECIDAS.as_posix()}")
    if antes is None or agora is None:
        return []
    linhas = lambda s: {x.strip() for x in s.splitlines() if x.strip() and not x.startswith("#")}
    return [f"falha conhecida nova (a lista só diminui): {x}" for x in sorted(linhas(agora) - linhas(antes))]


def confirmar(raiz: Path, a: argparse.Namespace) -> int:
    if (a.confirmado_por or "").strip().lower() != "vicente":
        print("a confirmação de mudança de teste é de Vicente (D-059): --confirmado-por vicente e --onde")
        return 1
    if not (a.motivo and a.verificado_por and a.onde):
        print("faltam --motivo, --verificado-por ou --onde")
        return 1
    atual, trava = impressoes(raiz), ler_trava(raiz)
    if a.caso not in trava and a.caso not in atual:
        print(f"caso desconhecido: {a.caso}")
        return 1
    linha = {"data": datetime.now().astimezone().isoformat(timespec="seconds"), "versao": VERSAO,
             "caso": a.caso, "antes": trava.get(a.caso), "depois": atual.get(a.caso),
             "motivo": a.motivo, "verificado_por": a.verificado_por, "confirmado_por": "vicente", "onde": a.onde}
    with (raiz / CONFIRMACOES).open("a", encoding="utf-8") as f:
        f.write(json.dumps(linha, ensure_ascii=False) + "\n")
    if atual.get(a.caso) is None:
        trava.pop(a.caso, None)
    else:
        trava[a.caso] = atual[a.caso]
    gravar_trava(raiz, trava)
    print(f"{VERSAO}: confirmação gravada para {a.caso} ({'tirado' if linha['depois'] is None else 'mudado'})")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--raiz", type=Path, default=RAIZ_PADRAO)
    ap.add_argument("--gravar-novos", action="store_true")
    ap.add_argument("--pre-commit", action="store_true")
    ap.add_argument("--confirmar", action="store_true")
    ap.add_argument("--caso")
    ap.add_argument("--motivo")
    ap.add_argument("--verificado-por")
    ap.add_argument("--confirmado-por")
    ap.add_argument("--onde")
    a = ap.parse_args()
    raiz = a.raiz if a.raiz.is_absolute() else (Path.cwd() / a.raiz)
    if a.confirmar:
        return confirmar(raiz, a)
    if a.gravar_novos:
        novos, _, _ = diferencas(raiz)
        trava = ler_trava(raiz)
        atual = impressoes(raiz)
        trava.update({k: atual[k] for k in novos})
        gravar_trava(raiz, trava)
        print(f"{VERSAO}: {len(novos)} caso(s) novo(s) na trava; {len(trava)} no total")
        return 0
    problemas = conferir(raiz) + (conferir_commit(raiz) + conferir_falhas_conhecidas(raiz) if a.pre_commit else [])
    for p in problemas:
        print("TRAVA:", p)
    n = len(impressoes(raiz))
    print(f"{VERSAO}: {n} casos; " + (f"{len(problemas)} problema(s): verificar e confirmar antes de admitir "
                                       "a mudança (D-059), ou desfazer a mudança" if problemas else "em ordem"))
    return 1 if problemas else 0


if __name__ == "__main__":
    sys.exit(main())
