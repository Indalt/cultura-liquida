"""Banco de provas dos testes de modelos (bloco 12 do brief de execuções; K-115a; D-027, D-053). banco-0.1.

Os casos da rodada B (testes/rodada-b/caso_real.py) conferem os validadores sobre registros reais e não rodam
agente. Este banco roda o **agente**, em cada modelo candidato, sobre a **entrada real** de um par e passa a
saída pelos mesmos validadores, mais o confronto com a saída real do par (o gabarito).

- **Base congelada (insumo 119):** a entrada sai do acervo num commit fixo (`base_commit` da prova), por
  `git archive`, nunca do acervo do momento: a rotina diária muda registros (Entradas, Recortes) e o banco não
  pode depender deles. A cópia se extrai uma vez por commit numa pasta temporária fora do repositório.
- **Saída fora do acervo:** cada rodada trabalha numa pasta fora do repositório (`--pasta`), com `raiz/` (a
  fatia do acervo que o agente lê e onde grava, como se fosse o acervo) e `saida/` (o que a habilidade devolve
  ao curador). O gabarito nunca entra na pasta: o `avaliar` o lê da base.
- **Fonte:** só pela janela de citação que já está no Git (antes + texto exato + depois de cada Trecho real);
  nenhuma web nova.

Subcomandos:
    python testes/modelos/banco.py preparar <prova> --pasta <dir>      monta raiz/ e saida/ e grava pedido.md
    python testes/modelos/banco.py avaliar <prova> --pasta <dir> [--modelo m] [--rodada n] [--resumo]
                                                                        validadores + gabarito; código 0 = passa
    python testes/modelos/banco.py autoteste <prova> [--erro]           prepara, põe a saída real (ou a real com o
                                                                        erro da prova) e avalia: 0 = passa
    python testes/modelos/banco.py casos                                roda testes/modelos/casos.json
`<prova>` é o nome em testes/modelos/provas/<prova>.json. `--resumo` grava o resultado (só números e motivos,
nunca conteúdo) em testes/modelos/resultados/. Estes casos não entram no rodar_testes.py: a suíte é o portão
da rotina diária, que roda com outro checkout, e o banco extrai commits antigos (insumo 119).
"""
from __future__ import annotations

import argparse
import io
import json
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "scripts"))
sys.path.insert(0, str(RAIZ / "testes" / "rodada-b"))
from _acervo import arquivos_acervo, id_do_registro  # noqa: E402
from caso_real import aplicar, fecho  # noqa: E402

VERSAO = "banco-0.2"
PROVAS = RAIZ / "testes" / "modelos" / "provas"
RESULTADOS = RAIZ / "testes" / "modelos" / "resultados"
CACHE = Path(tempfile.gettempdir()) / "cultura-liquida-banco"
RE_MARCA = re.compile(r"\b(?:PR|EV|TR|EL|AR|F)-[0-9]{4,}\b")
SEP = "\n\n[…]\n\n"


def py() -> str:
    return sys.executable


def carregar_prova(nome: str) -> dict:
    return json.loads((PROVAS / f"{nome}.json").read_text(encoding="utf-8"))


def base(commit: str) -> Path:
    """A cópia do acervo no commit fixo (acervo, entrada, ambientes), extraída uma vez."""
    destino = CACHE / f"base-{commit}"
    if (destino / ".pronto").exists():
        return destino
    shutil.rmtree(destino, ignore_errors=True)
    destino.mkdir(parents=True)
    r = subprocess.run(["git", "archive", commit, "acervo", "entrada", "ambientes"], cwd=RAIZ, capture_output=True)
    if r.returncode:
        raise SystemExit(f"git archive {commit} falhou: {r.stderr.decode('utf-8', 'replace')[:200]}")
    with tarfile.open(fileobj=io.BytesIO(r.stdout)) as t:
        t.extractall(destino)
    (destino / ".pronto").write_text(commit, encoding="utf-8")
    return destino


def indice(raiz: Path) -> dict[str, Path]:
    saida = {}
    for arq in arquivos_acervo(raiz):
        try:
            i = id_do_registro(json.loads(arq.read_text(encoding="utf-8")))
        except Exception:
            continue
        if i:
            saida.setdefault(i, arq)
    return saida


def expandir(ids: list[str], ind: dict[str, Path]) -> list[str]:
    saida = []
    for i in ids:
        saida += sorted(k for k in ind if k.startswith(i[:-1])) if i.endswith("*") else [i]
    return saida


def ler(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def janela(tr: dict) -> str:
    return tr.get("antes", "") + tr["texto_exato"] + tr.get("depois", "")


def trocar_secao(texto: str, titulo: str, novo: str) -> str:
    linhas = texto.split("\n")
    ini = linhas.index(titulo)
    fim = next((k for k in range(ini + 1, len(linhas)) if linhas[k].startswith("## ")), len(linhas))
    return "\n".join(linhas[:ini + 1] + [novo, ""] + linhas[fim:])


def secao(texto: str, titulo: str) -> str:
    linhas = texto.split("\n")
    ini = linhas.index(titulo)
    fim = next((k for k in range(ini + 1, len(linhas)) if linhas[k].startswith("## ")), len(linhas))
    return "\n".join(linhas[ini + 1:fim])


def preparar(prova: dict, pasta: Path) -> Path:
    b = base(prova["base_commit"])
    ind = indice(b)
    raiz, saida = pasta / "raiz", pasta / "saida"
    shutil.rmtree(pasta, ignore_errors=True)
    raiz.mkdir(parents=True)
    saida.mkdir(parents=True)
    ids = expandir(prova.get("registros", []), ind)
    sementes = list(ids)
    for f in prova.get("fichas", []):
        sementes += RE_MARCA.findall((b / "acervo" / "fichas" / f).read_text(encoding="utf-8"))
    if prova.get("fecho"):
        ids = sorted(fecho(sementes, ind))
    faltam = [i for i in ids if i not in ind]
    if faltam:
        raise SystemExit(f"PROVA MAL ESCRITA: registros fora da base {prova['base_commit']}: {', '.join(faltam)}")
    retirar = set(prova.get("retirar", []))
    for i in ids:
        if i in retirar:
            continue
        destino = raiz / ind[i].relative_to(b)
        destino.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ind[i], destino)
    for c in prova.get("caminhos", []):
        orig = b / c
        if orig.is_dir():
            shutil.copytree(orig, raiz / c, dirs_exist_ok=True)
        else:
            (raiz / c).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(orig, raiz / c)
    for f in prova.get("fichas", []):
        (raiz / "acervo" / "fichas").mkdir(parents=True, exist_ok=True)
        shutil.copy2(b / "acervo" / "fichas" / f, raiz / "acervo" / "fichas" / f)
    rind = indice(raiz)
    for m in prova.get("mudancas", []):
        if m.get("op") == "secao":
            arq = raiz / m["arquivo"]
            arq.write_text(trocar_secao(arq.read_text(encoding="utf-8"), m["titulo"], m["para"]), encoding="utf-8")
            continue
        arq = raiz / m["arquivo"] if "arquivo" in m else rind[m["registro"]]
        obj = ler(arq)
        aplicar(obj, m)
        arq.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
    for en, trs in prova.get("janelas", {}).items():
        (raiz / "fonte").mkdir(exist_ok=True)
        (raiz / "fonte" / f"{en}.txt").write_text(SEP.join(janela(ler(ind[t])) for t in trs), encoding="utf-8")
    comum = (PROVAS / "_comum.md").read_text(encoding="utf-8")
    pedido = (comum + "\n" + (PROVAS / f"{prova['nome']}.md").read_text(encoding="utf-8"))
    pedido = pedido.replace("{raiz}", raiz.as_posix()).replace("{saida}", saida.as_posix()).replace(
        "{pasta}", pasta.as_posix()).replace("{teto}", str(prova["teto_chamadas"]))
    (pasta / "pedido.md").write_text(pedido, encoding="utf-8")
    print(f"{VERSAO}: preparada {prova['nome']} em {pasta} (base {prova['base_commit']}; "
          f"{len(indice(raiz))} registro(s) na raiz; retirados {len(retirar)})")
    return pasta


def rodar(cmd: list[str], raiz: Path, saida: Path) -> tuple[int, str]:
    cmd = [x.replace("{raiz}", str(raiz)).replace("{saida}", str(saida)) for x in cmd]
    r = subprocess.run([py(), str(RAIZ / cmd[0]), *cmd[1:]], cwd=RAIZ, capture_output=True, text=True, encoding="utf-8")
    linhas = (r.stdout + r.stderr).strip().splitlines()
    marcas = ("NÃO BATE", "ERRO", "NÃO SE SUSTENTA", "REPROVA", "    - ", "  ")
    erros = [l.strip() for l in linhas if l.startswith(marcas)]
    return r.returncode, ("; ".join(erros[:3]) if r.returncode and erros else (linhas[-1] if linhas else ""))


# ---------- checagens do gabarito (a saída real do par, lida da base) ----------

def ck_trechos(prova, g, raiz, saida, b, ind):
    """Cada Trecho real é coberto por um Trecho da saída que o script localizou na mesma janela."""
    res = []
    arqs = sorted((saida / "trechos").glob("*.json")) if (saida / "trechos").exists() else []
    gerados = []
    for a in arqs:
        en = a.name.rsplit("-", 1)[0]
        cod, ult = rodar(["scripts/localizar_trecho.py", "conferir", str(a), "--fonte", str(raiz / "fonte" / f"{en}.txt")], raiz, saida)
        res.append((cod == 0, f"conferir {a.name}: {ult}"))
        try:
            gerados.append((en, ler(a)["trecho"]["texto_exato"]))
        except Exception as e:
            res.append((False, f"{a.name} ilegível: {e}"))
    if not arqs:
        res.append((False, "nenhum Trecho em saida/trechos"))
    for en, trs in prova["janelas"].items():
        texto = (raiz / "fonte" / f"{en}.txt").read_text(encoding="utf-8")
        intervalos = [(texto.find(t), texto.find(t) + len(t)) for e, t in gerados if e == en and texto.find(t) >= 0]
        for t in trs:
            ex = ler(ind[t])["texto_exato"]
            i = texto.find(ex)
            ok = any(a < i + len(ex) and i < z for a, z in intervalos)
            res.append((ok, f"{t} ({en}) {'coberto' if ok else 'NÃO coberto'} por um Trecho da saída"))
    return res


def ck_termo(prova, g, raiz, saida, b, ind):
    res = []
    arq = raiz / "acervo" / "termos" / f"{g['id']}.json"
    if not arq.exists():
        return [(False, f"{g['id']} não gravado em raiz/acervo/termos")]
    te = ler(arq)
    real = ler(ind[g["id"]])
    res.append((te.get("estado") == real["estado"], f"estado {te.get('estado')!r} (real {real['estado']!r})"))
    formas = {d.get("forma") for d in te.get("designacoes", [])}
    res.append((g["designacao"] in formas, f"designação {g['designacao']!r} {'presente' if g['designacao'] in formas else 'ausente'}"))
    var = {v.get("forma"): v for v in te.get("variantes", [])}
    for f in g.get("variantes", []):
        res.append((f in var, f"variante {f!r} {'presente' if f in var else 'ausente'}"))
    abon = set(te.get("abonacoes", [])) | {e for v in te.get("variantes", []) for e in v.get("abonacoes", [])}
    fora = sorted(abon - set(g["evidencias_dadas"]))
    res.append((not fora, "abonações só das Evidências dadas" + (f"; fora: {fora}" if fora else "")))
    return res


def ck_secao(prova, g, raiz, saida, b, ind):
    res = []
    arq = raiz / "acervo" / "fichas" / g["ficha"]
    txt = secao(arq.read_text(encoding="utf-8"), g["titulo"])
    marcas = set(re.findall(r"PR-[0-9]{4,}", txt))
    dadas = set(g["proposicoes_dadas"])
    falta = sorted(dadas - marcas)
    fora = sorted(marcas - dadas)
    res.append((not falta, f"{len(dadas - set(falta))} de {len(dadas)} Proposições dadas marcadas" + (f"; faltam {falta}" if falta else "")))
    res.append((not fora, "nenhuma marca fora das dadas" + (f"; fora: {fora}" if fora else "")))
    erros_mu = []
    for linha in txt.splitlines():
        m = re.search(r"μ\s*([0-9]+(?:,[0-9]+)?)", linha)
        if not m:
            continue
        v = float(m.group(1).replace(",", "."))
        mus = [ler(ind[p]).get("mu") for p in re.findall(r"PR-[0-9]{4,}", linha) if p in ind]
        if mus and not any(x is not None and abs(x - v) < 1e-9 for x in mus):
            erros_mu.append(f"μ {m.group(1)} ≠ {mus}")
    res.append((not erros_mu, "μ citado bate com a Proposição" + (f"; {erros_mu[:3]}" if erros_mu else "")))
    return res


def ck_grafo(prova, g, raiz, saida, b, ind):
    rind = indice(raiz)
    props = set(g["proposicoes"])
    els = {i: ler(p) for i, p in rind.items() if i.startswith("EL-") and props & set(ler(p).get("proposicoes", []))}
    ars = [ler(p) for i, p in rind.items() if i.startswith("AR-") and ler(p).get("de") in els and ler(p).get("para") in els]
    seq = [a for a in ars if a.get("tipo") == g["tipo_aresta"]]
    prox = {a["de"]: a["para"] for a in seq}
    ini = [e for e in els if e in prox and e not in set(prox.values())]
    cadeia = []
    if len(ini) == 1:
        e = ini[0]
        while e and e not in cadeia:
            cadeia.append(e)
            e = prox.get(e)
    ys = [els[e].get("y") for e in cadeia]
    res = [(ys == g["ys"], f"cadeia de {len(cadeia)} Elemento(s) por '{g['tipo_aresta']}': Y {ys} (real {g['ys']})")]
    xs_ok = all(els[e].get("x") == g["x"] for e in cadeia) and cadeia
    res.append((bool(xs_ok), f"X de cada Elemento = {g['x']}"))
    ws = sorted({els[e].get("w") for e in cadeia})
    res.append((ws == [g["w"]], f"W da cadeia {ws} (real {g['w']})"))
    res.append((len(seq) == len(g["ys"]) - 1, f"{len(seq)} Aresta(s) '{g['tipo_aresta']}' (real {len(g['ys']) - 1})"))
    return res


def ck_faltas(prova, g, raiz, saida, b, ind):
    arq = saida / "faltas.json"
    if not arq.exists():
        return [(False, "saida/faltas.json ausente")]
    obj = ler(arq)
    faltas = obj.get("faltas", obj) if isinstance(obj, dict) else obj
    res = []
    tmp = saida / "_falta.json"
    for k, f in enumerate(faltas):
        tmp.write_text(json.dumps(f, ensure_ascii=False), encoding="utf-8")
        cod, ult = rodar(["scripts/validar.py", "falta", str(tmp)], raiz, saida)
        res.append((cod == 0, f"Falta {k + 1} pelo esquema: {ult}"))
    tmp.unlink(missing_ok=True)

    def alvos(f):
        return set(re.findall(r"TR-[0-9]{4,}", json.dumps(f.get("onde_aparece", []), ensure_ascii=False)))
    esperadas = [f for f in faltas if f.get("subtipo_juridico") == g["subtipo"] and f.get("vale_para") == g["vale_para"]
                 and g["item"] in alvos(f)]
    res.append((len(esperadas) >= 1, f"Falta {g['subtipo']} / {g['vale_para']} no {g['item']}: {len(esperadas)}"))
    agora = [f for f in faltas if f.get("vale_para") == "agora"]
    res.append((not agora, f"nenhuma Falta que barra agora ({len(agora)})"))
    sobre_controle = [sorted(alvos(f)) for f in faltas if alvos(f) and alvos(f) <= set(g["sem_falta"])]
    res.append((not sobre_controle, f"nenhuma Falta só sobre os itens sem Falta pela regra {g['sem_falta']}"
                + (f"; achadas: {sobre_controle}" if sobre_controle else "")))
    return res


CHECAGENS = {"trechos": ck_trechos, "termo": ck_termo, "secao": ck_secao, "grafo": ck_grafo, "faltas": ck_faltas}


def avaliar(prova: dict, pasta: Path) -> tuple[bool, list[tuple[bool, str]]]:
    b = base(prova["base_commit"])
    ind = indice(b)
    raiz, saida = pasta / "raiz", pasta / "saida"
    res: list[tuple[bool, str]] = []
    for cmd in prova.get("validadores", []):
        cod, ult = rodar(cmd, raiz, saida)
        res.append((cod == 0, f"{cmd[0]}: código {cod}: {ult}"))
    for g in prova.get("gabarito", []):
        res += CHECAGENS[g["tipo"]](prova, g, raiz, saida, b, ind)
    return all(ok for ok, _ in res), res


# ---------- autoteste: a saída real do par no lugar da do agente ----------

def por_saida_real(prova: dict, pasta: Path) -> None:
    b = base(prova["base_commit"])
    ind = indice(b)
    raiz, saida = pasta / "raiz", pasta / "saida"
    for i in prova.get("retirar", []):
        destino = raiz / ind[i].relative_to(b)
        destino.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ind[i], destino)
    for m in prova.get("mudancas", []):
        if m.get("op") == "secao":
            shutil.copy2(b / m["arquivo"], raiz / m["arquivo"])
    real = prova.get("saida_real", {})
    if real.get("tipo") == "extracao":  # o lote real do avaliador: os Trechos relocalizados na janela
        (saida / "trechos").mkdir(exist_ok=True)
        entradas = []
        for en, trs in prova["janelas"].items():
            evs = []
            for k, t in enumerate(trs, 1):
                arq = saida / "trechos" / f"{en}-{k}.json"
                cod, ult = rodar(["scripts/localizar_trecho.py", "localizar", "--fonte", str(raiz / "fonte" / f"{en}.txt"),
                                  "--trecho", ler(ind[t])["texto_exato"], "--saida", str(arq)], raiz, saida)
                if cod:
                    raise SystemExit(f"PROVA MAL ESCRITA: {t} não se localiza na janela ({ult})")
                ev = next(ler(p) for i, p in ind.items() if i.startswith("EV-") and ler(p).get("trecho") == t)
                pr = ler(ind[ev["proposicao"]])
                evs.append({"arquivo_trecho": str(arq), "atributo": pr["atributo"], "valor": pr["valor"],
                            "periodo_referido": pr.get("periodo", {}).get("referido"), "sentido": ev["sentido"],
                            "voz": ev["voz"], "lugares": {"pratica": None, "publicacao": None, "pesquisa": None},
                            "criterio_pratica_cultural": None,
                            "sustenta_aviso_saude_politica": ev.get("sustenta_aviso_saude_politica", False)})
            entradas.append({"entrada": en, "estado": "aceito", "valencias": real["valencias"],
                             "sustenta_aviso_saude_politica": any(e["sustenta_aviso_saude_politica"] for e in evs),
                             "fonte": {}, "evidencias": evs})
        (saida / "saida-avaliador.json").write_text(json.dumps({"lote": "autoteste", "entradas": entradas},
                                                               ensure_ascii=False, indent=1), encoding="utf-8")
    elif real.get("tipo") == "faltas":
        faltas = [ler(ind[i]) for i in real["faltas"]]
        (saida / "faltas.json").write_text(json.dumps({"faltas": faltas}, ensure_ascii=False, indent=1), encoding="utf-8")


def por_erro(prova: dict, pasta: Path) -> None:
    raiz, saida = pasta / "raiz", pasta / "saida"
    for m in prova["erro"]["mudancas"]:
        arq = (saida if m.get("onde") == "saida" else raiz) / m["arquivo"]
        if arq.suffix == ".md":
            s = arq.read_text(encoding="utf-8")
            if s.count(m["de"]) != 1:
                raise SystemExit(f"PROVA MAL ESCRITA: {m['de']!r} aparece {s.count(m['de'])} vez(es)")
            arq.write_text(s.replace(m["de"], m["para"]), encoding="utf-8")
        elif m.get("op") == "remover":
            arq.unlink()
        else:
            obj = ler(arq)
            aplicar(obj, m)
            arq.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def imprimir(nome: str, ok: bool, res: list[tuple[bool, str]]) -> None:
    for o, t in res:
        print(f"  {'ok ' if o else 'REPROVA:'} {t}")
    print(f"{VERSAO}: {nome}: {'PASSA' if ok else 'REPROVA'}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("acao", choices=["preparar", "avaliar", "autoteste", "casos"])
    ap.add_argument("prova", nargs="?")
    ap.add_argument("--pasta", type=Path)
    ap.add_argument("--modelo")
    ap.add_argument("--resumo", action="store_true")
    ap.add_argument("--erro", action="store_true")
    ap.add_argument("--rodada", type=int, default=1, help="o número da rodada da prova nesse modelo (depois de reforçar o harness)")
    a = ap.parse_args()
    if a.acao == "casos":
        casos = json.loads((RAIZ / "testes" / "modelos" / "casos.json").read_text(encoding="utf-8"))["casos"]
        falhas = 0
        for c in casos:
            r = subprocess.run([py(), str(Path(__file__)), "autoteste", c["prova"], *(["--erro"] if c.get("erro") else [])],
                               cwd=RAIZ, capture_output=True, text=True, encoding="utf-8")
            obtido = "passa" if r.returncode == 0 else ("reprova" if r.returncode == 1 else "erro")
            ok = obtido == c["espera"]
            falhas += not ok
            ult = (r.stdout + r.stderr).strip().splitlines()
            print(f"{'OK   ' if ok else 'FALHA'} {c['nome']}: esperado {c['espera']}, obtido {obtido}"
                  + ("" if ok else f" ({'; '.join(l.strip() for l in ult if 'REPROVA' in l or 'MAL' in l)[:300]})"))
        print(f"{VERSAO}: casos OK {len(casos) - falhas} · FALHA {falhas}")
        return 1 if falhas else 0
    prova = carregar_prova(a.prova)
    if a.acao == "preparar":
        preparar(prova, a.pasta)
        return 0
    if a.acao == "autoteste":
        pasta = Path(tempfile.mkdtemp(prefix="cl-banco-"))
        try:
            preparar(prova, pasta)
            por_saida_real(prova, pasta)
            if a.erro:
                por_erro(prova, pasta)
            ok, res = avaliar(prova, pasta)
            imprimir(prova["nome"] + (" (com o erro)" if a.erro else " (saída real)"), ok, res)
            return 0 if ok else 1
        finally:
            shutil.rmtree(pasta, ignore_errors=True)
    ok, res = avaliar(prova, a.pasta)
    imprimir(prova["nome"], ok, res)
    if a.resumo:
        RESULTADOS.mkdir(parents=True, exist_ok=True)
        arq = RESULTADOS / f"{prova['nome']}__{a.modelo or 'sem-modelo'}__r{a.rodada}.json"
        arq.write_text(json.dumps({"prova": prova["nome"], "habilidade": prova["habilidade"], "agente": prova["agente"],
                                   "modelo": a.modelo, "rodada": a.rodada, "data": date.today().isoformat(), "versao": VERSAO, "base_commit": prova["base_commit"],
                                   "passa": ok, "checagens": [{"ok": o, "texto": t} for o, t in res]},
                                  ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"resumo em {arq.relative_to(RAIZ)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
