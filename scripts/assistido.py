"""Modo assistido (l. 429): a busca manual de Vicente onde a fonte barra robôs (Hemeroteca, 403) ou a
via automática não existe, registrada como Recorte com "pessoa" como executor.

Dois passos:
1. `modelo`: escreve o formulário da busca (ambiente × Consulta × período), com a sintaxe já
   traduzida para a fonte (`ambientes/traducao-consultas.json`). O formulário fica fora da pasta
   versionada até ser registrado (padrão: a pasta temporária do layout).
2. `registrar`: confere o formulário preenchido e grava o Recorte (cursor = a última página vista;
   total informado e visto; estado) e uma Entrada por item, canal "busca assistida", cada uma com
   o link permanente da página e o localizador. O log da Execução é de pessoa (Vicente), sem IA.
   Reprova (código 1, nada gravado) se faltar o link permanente ou o localizador de um item, ou o
   link permanente de uma página.

Formulário:
    {"ambiente": "AM-0001", "consulta": "CO-0002", "periodo": "todo", "sintaxe": "...",
     "data": "AAAA-MM-DD", "total_informado": 12 | null, "terminou": true | false,
     "paginas": [{"pagina": 1, "link_permanente": "https://...", "resultados_vistos": 12,
                  "itens": [{"link_permanente": "https://...", "id_na_fonte": "opcional",
                             "localizador": "página 3, coluna 2"}]}],
     "observacoes": "texto livre, sem nome de pessoa"}

Uso:
    python scripts/assistido.py modelo --ambiente AM-0001 --consulta CO-0002 [--periodo todo] [--saida <arq>]
    python scripts/assistido.py registrar <formulario.json> [--raiz <pasta>] [--simular]
"""
from __future__ import annotations

import argparse
import json
import sys
import tempfile
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_json  # noqa: E402
from _coleta import Execucao  # noqa: E402
import deduplicar  # noqa: E402
from recorte import Registro, carregar_consulta, fechar, modo_da  # noqa: E402

VERSAO = "assistido-0.1"
EXECUTOR = "Vicente (pessoa), busca assistida"


def modelo(raiz: Path, ambiente: str, consulta: str, periodo: str) -> dict:
    t = carregar_json(raiz / "ambientes" / "traducao-consultas.json").get(consulta, {}).get(ambiente, {})
    return {
        "ambiente": ambiente, "consulta": consulta, "periodo": periodo,
        "sintaxe": t.get("sintaxe", "sem tradução: escrever a sintaxe usada"),
        "data": date.today().isoformat(), "total_informado": None, "terminou": False,
        "paginas": [{"pagina": 1, "link_permanente": "", "resultados_vistos": 0,
                     "itens": [{"link_permanente": "", "id_na_fonte": "", "localizador": ""}]}],
        "observacoes": "",
    }


def conferir(f: dict) -> list[str]:
    erros = []
    for k in ("ambiente", "consulta", "data", "paginas"):
        if not f.get(k):
            erros.append(f"sem {k}")
    for p in f.get("paginas", []):
        if not str(p.get("link_permanente", "")).startswith("http"):
            erros.append(f"página {p.get('pagina')}: sem link permanente")
        for i, it in enumerate(p.get("itens", []), 1):
            if not str(it.get("link_permanente", "")).startswith("http"):
                erros.append(f"página {p.get('pagina')}, item {i}: sem link permanente")
            if not str(it.get("localizador", "")).strip():
                erros.append(f"página {p.get('pagina')}, item {i}: sem localizador")
            if any(c.isspace() for c in str(it.get("id_na_fonte", "")).strip()):
                erros.append(f"página {p.get('pagina')}, item {i}: id_na_fonte com espaço (use o código da fonte, ou deixe vazio para usar o link)")
    return erros


def registrar(raiz: Path, f: dict, simular: bool) -> int:
    erros = conferir(f)
    if erros:
        print("REPROVA: o formulário não foi registrado.")
        for e in erros:
            print("    -", e)
        return 1
    ex = Execucao("assistido", f"busca assistida de Vicente: {f['ambiente']} × {f['consulta']} ({f.get('periodo', 'todo')}), {f['data']}", simular=simular)
    reg = Registro(raiz, ex, gravar=not simular)
    c = carregar_consulta(raiz, f["consulta"])
    r = reg.recorte(f["ambiente"], f["consulta"], f.get("periodo", "todo"), modo_da(c), {"chamadas": max(1, len(f["paginas"]))})
    r["origem_registro"] = ex.origem(EXECUTOR, VERSAO) if r["total_visto"] == 0 else r["origem_registro"]
    ex.ambientes.add(f["ambiente"])
    ex.consultas.add(f["consulta"])
    ex.recortes.add(r["id"])
    novas = rep = 0
    for p in f["paginas"]:
        for it in p.get("itens", []):
            ident = f"{f['ambiente']}:{(it.get('id_na_fonte') or it['link_permanente']).strip()}"
            _, nova = deduplicar.registrar(
                reg.indice, identificador=ident, url=it["link_permanente"], canal="busca assistida",
                origem=ex.origem(EXECUTOR, VERSAO), ambiente=f["ambiente"], recorte=r["id"],
                localizador=it["localizador"], gravar=not simular)
            novas += nova
            rep += not nova
    vistos = sum(int(p.get("resultados_vistos", 0)) for p in f["paginas"])
    r.update(total_informado=f.get("total_informado"), total_visto=r["total_visto"] + vistos,
             cursor=f"página {f['paginas'][-1]['pagina']}", data=f["data"], estado="em curso")
    acabou = bool(f.get("terminou"))
    fechar(reg, r, acabou=acabou, teto_estourado=None, erro=None)
    if not acabou:
        r["proxima_acao"] = f"busca assistida: seguir da {r['cursor']}"
        reg.salvar(r)
    ex.acoes.append(f"scripts/assistido.py registrar (formulário de {f['data']})")
    ex.olhado.append(f"{f['ambiente']} × {f['consulta']}: {len(f['paginas'])} página(s) da busca de Vicente, "
                     f"{vistos} resultado(s) vistos de {f.get('total_informado')}")
    if not acabou:
        ex.fora.append(f"{r['id']}: {r['proxima_acao']}")
    ex.resultados.insert(0, f"{r['id']}: {r['estado']}; {novas} Entrada(s) nova(s), {rep} repetida(s)")
    for x in ex.resultados:
        print(x)
    print(f"{VERSAO}: {ex.id}; {ex.gravar_log(fonte='pessoa')}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("modelo")
    m.add_argument("--ambiente", required=True)
    m.add_argument("--consulta", required=True)
    m.add_argument("--periodo", default="todo")
    m.add_argument("--saida", type=Path)
    m.add_argument("--raiz", type=Path, default=RAIZ)
    g = sub.add_parser("registrar")
    g.add_argument("formulario", type=Path)
    g.add_argument("--raiz", type=Path, default=RAIZ)
    g.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    raiz = a.raiz if a.raiz.is_absolute() else RAIZ / a.raiz
    if a.cmd == "modelo":
        f = modelo(raiz, a.ambiente, a.consulta, a.periodo)
        saida = a.saida or Path(tempfile.gettempdir()) / "cultura-liquida" / "assistido" / f"{a.ambiente}_{a.consulta}_{f['data']}.json"
        saida.parent.mkdir(parents=True, exist_ok=True)
        saida.write_text(json.dumps(f, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{VERSAO}: formulário em {saida}")
        return 0
    return registrar(raiz, carregar_json(a.formulario), a.simular)


if __name__ == "__main__":
    sys.exit(main())
