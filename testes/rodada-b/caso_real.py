"""Roda um caso real da rodada B (bloco 9; K-111): uma cópia do real, com ou sem o erro injetado.

O caso é um JSON pequeno, gravado nos exemplos da habilidade (`.claude/skills/<h>/exemplos/real-*.json`).
Nada do acervo se duplica no Git: a cópia nasce a cada rodada numa pasta temporária fora do
repositório, a partir do acervo do momento, e se apaga no fim. Três modos:

- **fatia** (padrão): copia os registros das `sementes` e tudo o que eles apontam (o fecho das
  referências, como o `validar_acervo.py` as segue: campos com um ID inteiro, fora as notas), mais as
  `fichas` dadas (com as Proposições que elas marcam); aplica as `mudancas` e roda os `validadores`
  com `{raiz}` = a pasta da cópia. Código 0 se todos passam.
- **registro**: tira um registro (`registro`, e dentro dele `caminho`, se dado) ou um arquivo do
  repositório (`arquivo`), aplica as `mudancas` e o valida pelo `esquema` (scripts/validar.py, com as
  regras entre campos).
- **trecho**: a fonte reduzida à janela de citação do Trecho real (antes + texto exato + depois, já no
  Git como citação curta; o texto integral nunca entra no repositório, l. 100); o `localizar_trecho.py`
  localiza o texto exato nessa janela, as `mudancas` se aplicam ao Trecho gerado e o `conferir` o relê.

Mudanças: {"arquivo"|"registro", "op": "set"|"apagar"|"anexar"|"texto", "caminho": [...], "valor": ..., "de": "...", "para": "..."}.
"texto" troca `de` por `para` num arquivo de texto (a ficha); `de` tem de aparecer uma vez.

Uso:
    python testes/rodada-b/caso_real.py <caso.json> [--manter]
Código 0 = o caso passa; 1 = reprova (o motivo na última linha); 2 = caso mal escrito.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "scripts"))
from _acervo import arquivos_acervo, id_do_registro, textos  # noqa: E402

RE_REF = re.compile(r"^[A-Z]{1,2}-[0-9]{4,}$")
RE_MARCA = re.compile(r"\b[A-Z]{1,2}-[0-9]{4,}\b")


def indice() -> dict[str, Path]:
    saida = {}
    for arq in arquivos_acervo(RAIZ):
        try:
            i = id_do_registro(json.loads(arq.read_text(encoding="utf-8")))
        except Exception:
            continue
        if i:
            saida.setdefault(i, arq)
    return saida


def fecho(sementes: list[str], ind: dict[str, Path]) -> set[str]:
    vistos, fila = set(), list(sementes)
    while fila:
        i = fila.pop()
        if i in vistos or i not in ind:
            continue
        vistos.add(i)
        r = json.loads(ind[i].read_text(encoding="utf-8"))
        for cam, txt in textos(r):
            if not cam.endswith("/nota") and RE_REF.match(txt) and not txt.startswith("EX-"):
                fila.append(txt)
    return vistos


def pegar(obj, caminho):
    for k in caminho:
        obj = obj[k]
    return obj


def aplicar(obj, m: dict):
    *pai, ult = m["caminho"]
    alvo = pegar(obj, pai)
    if m["op"] == "set":
        alvo[ult] = m["valor"]
    elif m["op"] == "apagar":
        del alvo[ult]
    elif m["op"] == "anexar":
        alvo[ult].append(m["valor"])
    else:
        raise SystemExit(2)


def mudar_arquivo(arq: Path, ms: list[dict]):
    if arq.suffix == ".md":
        s = arq.read_text(encoding="utf-8")
        for m in ms:
            if s.count(m["de"]) != 1:
                print(f"CASO MAL ESCRITO: {m['de']!r} aparece {s.count(m['de'])} vez(es) em {arq.name}")
                raise SystemExit(2)
            s = s.replace(m["de"], m["para"])
        arq.write_text(s, encoding="utf-8")
        return
    obj = json.loads(arq.read_text(encoding="utf-8"))
    for m in ms:
        aplicar(obj, m)
    arq.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def rodar(cmd: list[str], raiz: Path) -> tuple[int, str]:
    cmd = [x.replace("{raiz}", str(raiz)) for x in cmd]
    r = subprocess.run([sys.executable, str(RAIZ / cmd[0]), *cmd[1:]], cwd=RAIZ, capture_output=True,
                       text=True, encoding="utf-8")
    saida = (r.stdout + r.stderr).strip().splitlines()
    # o motivo: as linhas que nomeiam o erro (achado A1 do auditor no K-111), não a última linha informativa
    marcas = ("NÃO BATE", "ERRO", "NÃO SE SUSTENTA", "BARRA", "    - ", "REPROVA (")
    erros = [l.strip() for l in saida if l.startswith(marcas) or l.lstrip().startswith(marcas)]
    return r.returncode, ("; ".join(erros[:2]) if erros and r.returncode else (saida[-1] if saida else ""))


def modo_fatia(caso: dict, tmp: Path) -> int:
    ind = indice()
    sementes = list(caso.get("sementes", []))
    for f in caso.get("fichas", []):
        sementes += RE_MARCA.findall((RAIZ / "acervo" / "fichas" / f).read_text(encoding="utf-8"))
    faltam = [s for s in caso.get("sementes", []) if s not in ind]
    if faltam:
        print(f"CASO MAL ESCRITO: sementes que não existem no acervo: {', '.join(faltam)}")
        return 2
    ids = fecho(sementes, ind)
    for i in ids:
        destino = tmp / ind[i].relative_to(RAIZ)
        destino.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ind[i], destino)
    for f in caso.get("fichas", []):
        (tmp / "acervo" / "fichas" / f).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(RAIZ / "acervo" / "fichas" / f, tmp / "acervo" / "fichas" / f)
    por_arq: dict[Path, list] = {}
    for m in caso.get("mudancas", []):
        arq = tmp / (m["arquivo"] if "arquivo" in m else ind[m["registro"]].relative_to(RAIZ))
        por_arq.setdefault(arq, []).append(m)
    for arq, ms in por_arq.items():
        mudar_arquivo(arq, ms)
    print(f"fatia: {len(ids)} registro(s) do acervo real, {len(caso.get('mudancas', []))} mudança(s)")
    for cmd in caso["validadores"]:
        cod, ult = rodar(cmd, tmp)
        print(f"{cmd[0]}: código {cod}: {ult}")
        if cod:
            return 1
    return 0


def modo_registro(caso: dict, tmp: Path) -> int:
    if "registro" in caso:
        obj = json.loads(indice()[caso["registro"]].read_text(encoding="utf-8"))
    else:
        obj = json.loads((RAIZ / caso["arquivo"]).read_text(encoding="utf-8"))
    obj = pegar(obj, caso.get("caminho", []))
    for m in caso.get("mudancas", []):
        aplicar(obj, m)
    arq = tmp / "registro.json"
    arq.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
    cod, ult = rodar(["scripts/validar.py", caso["esquema"], str(arq)], tmp)
    print(f"registro {caso.get('registro') or caso['arquivo']} pelo esquema {caso['esquema']}: código {cod}: {ult}")
    return 1 if cod else 0


def modo_trecho(caso: dict, tmp: Path) -> int:
    tr = json.loads(indice()[caso["trecho"]].read_text(encoding="utf-8"))
    fonte = tmp / "janela.txt"
    fonte.write_text(tr.get("antes", "") + tr["texto_exato"] + tr.get("depois", ""), encoding="utf-8")
    gerado = tmp / "trecho.json"
    cod, ult = rodar(["scripts/localizar_trecho.py", "localizar", "--fonte", str(fonte), "--trecho", tr["texto_exato"],
                      "--saida", str(gerado)], tmp)
    if cod:
        print(f"CASO MAL ESCRITO: o texto exato de {caso['trecho']} não se localiza na própria janela ({ult})")
        return 2
    if caso.get("mudancas"):
        obj = json.loads(gerado.read_text(encoding="utf-8"))
        alvo = obj.get("trecho", obj)
        for m in caso["mudancas"]:
            aplicar(alvo, m)
        gerado.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
    cod, ult = rodar(["scripts/localizar_trecho.py", "conferir", str(gerado), "--fonte", str(fonte)], tmp)
    print(f"{caso['trecho']} na janela de citação: conferir, código {cod}: {ult}")
    return 1 if cod else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("caso", type=Path)
    ap.add_argument("--manter", action="store_true", help="não apaga a cópia (para olhar)")
    a = ap.parse_args()
    caso = json.loads((a.caso if a.caso.is_absolute() else RAIZ / a.caso).read_text(encoding="utf-8"))
    tmp = Path(tempfile.mkdtemp(prefix="cl-rodada-b-"))
    try:
        modo = {"fatia": modo_fatia, "registro": modo_registro, "trecho": modo_trecho}[caso.get("modo", "fatia")]
        return modo(caso, tmp)
    finally:
        if a.manter:
            print(f"cópia mantida em {tmp}")
        else:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
