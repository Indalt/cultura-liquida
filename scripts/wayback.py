"""Cópia no Wayback (l. 509), no piloto só a captura que já existe (D-043, K-124): consulta a
Availability API do Internet Archive para as Entradas sem cópia e grava na Entrada o endereço da captura
existente. **Não pede captura nova** ao Save Page Now: a captura nova é cópia além da citação, barra agora
(F-0004, D-042) e volta no K-010.

- Sem captura existente, a Entrada fica com o link permanente, e o script grava uma Falta "sem cópia
  arquivada", dita (tipo "outro", uma por Entrada, nunca repetida); o trecho, o hash e a data vêm no
  Trecho do §6 (hash e data_conferencia). Com `--simular`, nada se grava.
- Antes de consultar, olha a proteção da Entrada (insumo 49): restrição comunitária conhecida, dado
  sensível, criança ou adolescente, pedido de retirada ou Entrada retirada → pula, sem consulta.
- Não consulta Entrada de ambiente cuja ficha registra 403, captcha ou verificação de navegador (l. 419;
  ler a cópia de quem barra robôs seria contornar a barreira por outro caminho).
- Nunca roda sem a triagem do juridico sobre a política de cópias arquivadas (Lei 9.610; l. 740): o
  `--triagem` aponta o arquivo dela. Com uma Falta `impedimento_juridico` aberta (caminho não liberado)
  que aponte `scripts/wayback.py` e não valha só para publicar ("agora", ou "captura", o nome antigo),
  nada se consulta (D-020, D-025).
- O robots.txt do archive.org é respeitado como o de qualquer host; 1 pedido por segundo, no máximo
  `--max` consultas por rodada (padrão 20).

Uso:
    python scripts/wayback.py --triagem <arquivo da triagem> [--entrada EN-0001,...] [--max 20]
        [--fixtures <pasta>] [--raiz <pasta>] [--simular]
Código 0 = rodou; 1 = sem triagem, Falta inválida ou erro de uso.
"""
from __future__ import annotations

import argparse
import json
import re
import urllib.parse
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _acervo import carregar_acervo, proximo_id  # noqa: E402
from _comum import RAIZ, carregar_esquema, carregar_json, validar_objeto  # noqa: E402
from _coleta import BloqueioAntiRobo, BloqueioRobos, Cliente, Execucao, gravar_json  # noqa: E402

VERSAO = "wayback-0.2"
DISPONIVEL = "https://archive.org/wayback/available?url="
BARREIRAS = re.compile(r"\b403\b|captcha|cloudflare|verificação de navegador", re.I)
RE_COPIA = re.compile(r"/web/(\d{14})/")
SEM_COPIA = "sem cópia arquivada"


def triagem_valida(tri: Path | None) -> bool:
    """A triagem do juridico sobre esta política: JSON com o item que cita o wayback.py e as oito perguntas (A-010)."""
    if not tri or not tri.is_file():
        return False
    try:
        t = carregar_json(tri)
    except Exception:
        return False
    return "wayback.py" in str(t.get("item", "")) and len(t.get("perguntas", [])) == 8


def _ficha(raiz: Path, ambiente: str) -> dict:
    arq = raiz / "ambientes" / f"{ambiente}.json"
    return carregar_json(arq).get("ficha_de_acesso", {}) if arq.exists() else {}


def _motivo(ficha: dict) -> str | None:
    texto = " ".join(str(ficha.get(k, "")) for k in ("acesso", "robots", "como_buscar", "decisao"))
    m = BARREIRAS.search(texto)
    return m.group(0) if m else None


def barrado(raiz: Path, ambiente: str | None, url: str = "") -> str | None:
    """O motivo, se a ficha do ambiente registra 403, captcha ou verificação de navegador; sem ambiente,
    pelo host do link, contra os hosts das fichas com barreira (A-012)."""
    if ambiente and (m := _motivo(_ficha(raiz, ambiente))):
        return f"a ficha de {ambiente} registra {m!r}"
    host = (urllib.parse.urlsplit(url).hostname or "").removeprefix("www.")
    if not host:
        return None
    for arq in sorted((raiz / "ambientes").glob("AM-*.json")) if (raiz / "ambientes").exists() else []:
        ficha = carregar_json(arq).get("ficha_de_acesso", {})
        if (m := _motivo(ficha)) and host in {(urllib.parse.urlsplit(u).hostname or "").removeprefix("www.")
                                              for u in re.findall(r"https?://[^\s)<>\"']+", json.dumps(
                                                  [ficha.get(k, "") for k in ("endpoint", "link_permanente", "acesso", "como_buscar")],
                                                  ensure_ascii=False))}:  # só os campos de via, não o robô nem as notas
            return f"o link é do host de {arq.stem}, cuja ficha registra {m!r}"
    return None


def falta_que_barra(raiz: Path) -> str | None:
    """A Falta jurídica aberta que barra a captura em si, se houver."""
    pasta = raiz / "acervo" / "faltas"
    for arq in sorted(pasta.glob("*.json")) if pasta.exists() else []:
        f = carregar_json(arq)
        if (f.get("tipo") == "impedimento_juridico" and "scripts/wayback.py" in f.get("onde_aparece", [])
                and f.get("vale_para") != "publicar" and f.get("caminho_de_liberacao", {}).get("estado") != "liberado"):
            return f["id"]
    return None


def protecao_barra(e: dict) -> str | None:
    """O motivo, se a proteção da Entrada pede que nada se consulte nem se registre (insumo 49; D-043)."""
    if e.get("retirado"):
        return "Entrada retirada"
    p = {k: ("" if v is None else v) for k, v in (e.get("protecao") or {}).items()}
    if str(p.get("restricao_comunitaria", "")).strip() not in ("", "nenhuma conhecida"):
        return "restrição comunitária conhecida"
    if p.get("dado_sensivel") is True:
        return "dado sensível"
    if p.get("crianca_ou_adolescente") is True:
        return "criança ou adolescente"
    if str(p.get("pedido_de_retirada", "")).strip() not in ("", "nenhum"):
        return "pedido de retirada"
    return None


def captura_existente(cli: Cliente, url: str) -> str | None:
    """O endereço da captura que já existe no Wayback, ou None. Nunca pede captura nova (D-043)."""
    r = cli.pedir(DISPONIVEL + urllib.parse.quote(url, safe=""))
    if not 200 <= r.status < 300:
        raise RuntimeError(f"HTTP {r.status} na Availability API")
    try:
        perto = (r.json().get("archived_snapshots") or {}).get("closest") or {}
    except ValueError:
        raise RuntimeError("resposta ilegível da Availability API")
    if not perto.get("available") or str(perto.get("status", "200")) != "200":
        return None
    m = RE_COPIA.search(perto.get("url", ""))
    return f"https://web.archive.org/web/{m.group(1)}/{url}" if m else None


def faltas_sem_copia(raiz: Path) -> set[str]:
    """As Entradas que já têm a Falta 'sem cópia arquivada' (não se repete)."""
    pasta = raiz / "acervo" / "faltas"
    feitas = set()
    for arq in sorted(pasta.glob("*.json")) if pasta.exists() else []:
        f = carregar_json(arq)
        if f.get("o_que_falta", "").startswith(SEM_COPIA):
            feitas.update(o for o in f.get("onde_aparece", []) if o.startswith("entrada/"))
    return feitas


def falta_sem_copia(fid: str, entrada: str, hoje: str, execucao: str) -> dict:
    return {"id": fid, "tipo": "outro",
            "o_que_falta": f"{SEM_COPIA}: o Wayback não tem captura da página do item (consulta de {hoje})",
            "por_que": "No piloto, o wayback.py só registra a captura que já existe e não pede captura nova "
                       "(D-043; a captura nova é cópia além da citação e barra agora, F-0004). A Availability API "
                       "não achou captura. Fica o link permanente; o trecho, o hash e a data vêm no Trecho do §6. "
                       "A captura nova volta no K-010.",
            "onde_aparece": [f"entrada/{entrada}.json"],
            "criada_por": f"scripts/wayback.py ({VERSAO})", "data": hoje,
            "nota": f"Execução {execucao}; dita, nunca completada (D-018)."}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--triagem", type=Path)
    ap.add_argument("--entrada", help="uma ou mais, separadas por vírgula; sem ela, as Entradas sem cópia")
    ap.add_argument("--max", type=int, default=20)
    ap.add_argument("--fixtures", type=Path)
    ap.add_argument("--raiz", type=Path, default=RAIZ)
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    raiz = a.raiz if a.raiz.is_absolute() else RAIZ / a.raiz
    tri = (a.triagem if a.triagem.is_absolute() else RAIZ / a.triagem) if a.triagem else None
    if not triagem_valida(tri):
        print("REPROVA: sem a triagem do juridico sobre a política de cópias arquivadas (Lei 9.610; l. 740): "
              "o arquivo tem de ser a triagem do wayback.py, com as oito perguntas")
        return 1
    if barra := falta_que_barra(raiz):
        print(f"BARRADO: a Falta jurídica {barra} está aberta e vale agora para o wayback.py; nada se consulta, "
              "e as Entradas ficam com o link permanente (D-020, D-025)")
        return 0
    fx = (a.fixtures if a.fixtures.is_absolute() else RAIZ / a.fixtures) if a.fixtures else None
    cli = Cliente(fixtures=fx)
    ex = Execucao("wayback", f"captura existente no Wayback (D-043), triagem {tri.relative_to(RAIZ).as_posix() if tri.is_relative_to(RAIZ) else tri.name}", simular=a.simular)
    hoje = date.today().isoformat()
    ja_ditas = faltas_sem_copia(raiz)
    ids = set(carregar_acervo(raiz)[0])
    esq = carregar_esquema("falta")
    pasta = raiz / "entrada"
    alvos = [x.strip() for x in (a.entrada or "").split(",") if x.strip()]
    entradas = []
    for arq in sorted(pasta.glob("*.json")) if pasta.exists() else []:
        e = carregar_json(arq)
        if e.get("wayback") or not e.get("url_ou_arquivo", "").startswith("http"):
            continue
        if f"entrada/{e['id']}.json" in ja_ditas and not alvos:
            continue
        if alvos and e["id"] not in alvos:
            continue
        entradas.append((arq, e))
    achadas = sem = puladas = consultas = 0
    faltas = []
    for arq, e in entradas:
        if consultas >= a.max:
            ex.fora.append(f"{len(entradas) - consultas - puladas} Entrada(s) além do máximo de {a.max} consultas por rodada")
            break
        if motivo := protecao_barra(e):
            puladas += 1
            ex.fora.append(f"{e['id']}: não consulta: proteção da Entrada ({motivo}); fica o link permanente (insumo 49)")
            continue
        if motivo := barrado(raiz, e.get("ambiente"), e["url_ou_arquivo"]):
            puladas += 1
            ex.fora.append(f"{e['id']}: não consulta: {motivo}; fica o link permanente (l. 419)")
            continue
        consultas += 1
        try:
            copia = captura_existente(cli, e["url_ou_arquivo"])
        except (BloqueioRobos, BloqueioAntiRobo, RuntimeError) as err:
            ex.erros.append(f"{e['id']}: {err}")
            ex.fora.append(f"{e['id']}: consulta sem resposta ({err}); nada se registra")
            continue
        if copia:
            e["wayback"] = copia
            achadas += 1
            if not a.simular:
                gravar_json(arq, e)
            ex.saidas.append(f"entrada/{e['id']}.json")
            ex.resultados.append(f"{e['id']}: captura existente {copia}")
            continue
        sem += 1
        if f"entrada/{e['id']}.json" in ja_ditas:
            ex.resultados.append(f"{e['id']}: {SEM_COPIA} (a Falta já está dita)")
            continue
        fid = proximo_id("F", ids)
        ids.add(fid)
        f = falta_sem_copia(fid, e["id"], hoje, ex.id)
        if erros := validar_objeto(f, esq):
            print(f"FALTA INVÁLIDA ({fid}): {'; '.join(erros)}")
            return 1
        faltas.append(f)
        ex.resultados.append(f"{e['id']}: {SEM_COPIA} → {fid}")
    if not a.simular:
        pf = raiz / "acervo" / "faltas"
        for f in faltas:
            pf.mkdir(parents=True, exist_ok=True)
            gravar_json(pf / f"{f['id']}.json", f)
            ex.saidas.append(f"acervo/faltas/{f['id']}.json")
    ex.decisoes += [{"item": f["onde_aparece"][0], "decisao": "falta", "motivo": f"{SEM_COPIA} ({f['id']}; D-043)"} for f in faltas]
    ex.acoes.append(f"scripts/wayback.py --max {a.max}" + (" (fixtures)" if fx else "") + (" --simular" if a.simular else ""))
    ex.olhado.append(f"{len(entradas)} Entrada(s) sem cópia; {consultas} consulta(s) à Availability API: {achadas} com captura "
                     f"existente, {sem} sem; {puladas} pulada(s); {cli.pedidos} pedido(s) HTTP, robots.txt incluído; "
                     "nenhuma captura nova pedida (D-043)")
    for x in ex.resultados + ex.fora:
        print(x)
    for x in ex.erros:
        print("ERRO", x)
    print(f"{VERSAO}: {ex.id}; {achadas} captura(s) existente(s) registrada(s), {len(faltas)} Falta(s) '{SEM_COPIA}'; {ex.gravar_log()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
