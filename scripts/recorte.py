"""Recorte (l. 427, 432): roda um ambiente × Consulta × período pelo adaptador do protocolo e grava o
estado a cada página (cursor, total informado e visto, saturação, erros, próxima ação, teto).

- O adaptador vem de `ambientes/adaptadores.json` (uma linha por ambiente; l. 430). "assistido" não
  roda aqui: é a busca de Vicente, registrada por `scripts/assistido.py` (l. 429).
- Cada item achado vai à Entrada pela deduplicação (`deduplicar.py`): uma Entrada por item, com os
  Recortes de origem (l. 435).
- **Resposta saturada** (o total passa do limite da fonte): divide a janela do período em duas e
  repete; só a passada completa e não saturada conta como pegada. Ao estourar o teto de chamadas ou
  de divisões, salva o estado e registra a Falta "busca interrompida por teto" (l. 427, 432).
- **Total desconhecido** (a fonte não informa): a Falta "total desconhecido", e o Recorte nunca
  fica "percorrido pela busca" (contrato do Recorte).
- **robots.txt ou proteção anti-robô:** nunca se contorna; o Recorte guarda o erro, a próxima ação
  é a via humana (modo assistido) e nasce a Falta "fonte inacessível" (l. 419).
- Um Recorte já percorrido roda de novo do começo (monitoramento): só o não visto vira Entrada nova.
- O alcance calculado vai ao log (D-030): Recortes previstos e rodados, páginas vistas e total
  informado, ambientes com erro.

Uso:
    python scripts/recorte.py --ambiente AM-0021 --consulta CO-0002[,CO-0001] [--periodo todo|1900-1950]
        [--teto-chamadas 50] [--teto-divisoes 4] [--fixtures <pasta>] [--gravar-fixtures <pasta>]
        [--raiz <pasta>] [--simular] [--entrada-ref "K-107 ..."]
Código 0 = rodou (mesmo com teto ou erro registrados no Recorte); 1 = erro de uso ou de contrato.
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_esquema, carregar_json, validar_objeto  # noqa: E402
from _acervo import carregar_acervo, proximo_id  # noqa: E402
from _coleta import BloqueioAntiRobo, BloqueioRobos, Cliente, Execucao, gravar_json  # noqa: E402
import adaptador_oai  # noqa: E402
import adaptador_vufind  # noqa: E402
import deduplicar  # noqa: E402
from gerar_termo import formas  # noqa: E402

VERSAO = "recorte-0.1"
ADAPTADORES = {m.PROTOCOLO: m for m in (adaptador_vufind, adaptador_oai)}
INICIO_PERIODO = 1900  # desde 1900 (propósito; §0)
FINAIS = ("percorrido pela busca", "lido por inteiro")


# --- configuração e registros ------------------------------------------------------------------
def carregar_cfg(raiz: Path, ambiente: str) -> dict:
    arq = raiz / "ambientes" / "adaptadores.json"
    cfg = carregar_json(arq).get(ambiente) if arq.exists() else None
    if not cfg:
        raise SystemExit(f"{ambiente}: sem linha em ambientes/adaptadores.json")
    return cfg


def ids_usados(raiz: Path, prefixo: str) -> set[str]:
    """IDs já usados: os do acervo e, para a Falta, também os citados na trilha (F-0001 a F-0003
    nasceram em trilhas/ antes do acervo). Um ID nunca se reaproveita (numeracao_id)."""
    ids = {i for i in carregar_acervo(raiz)[0] if i.startswith(prefixo + "-")}
    if prefixo == "F" and (raiz / "trilhas").exists():
        for arq in (raiz / "trilhas").rglob("*.json"):
            ids |= set(re.findall(r'"(F-[0-9]{4,})"', arq.read_text(encoding="utf-8", errors="replace")))
    return ids


class Registro:
    """O que a rodada grava: Recortes, Faltas e Entradas (estas pelo deduplicar.Indice)."""

    def __init__(self, raiz: Path, ex: Execucao, gravar: bool):
        self.raiz, self.ex, self.gravar = raiz, ex, gravar
        self.pasta_rc = raiz / "ambientes" / "recortes"
        self.recortes: dict[str, dict] = {}
        if self.pasta_rc.exists():
            for arq in self.pasta_rc.glob("*.json"):
                r = carregar_json(arq)
                self.recortes[r["id"]] = r
        self.faltas_ids = ids_usados(raiz, "F")
        self.indice = deduplicar.Indice(raiz)

    def salvar(self, r: dict) -> None:
        erros = validar_objeto(r, carregar_esquema("recorte"))
        if erros:
            raise SystemExit(f"{r['id']}: Recorte inválido: {'; '.join(erros)}")
        self.recortes[r["id"]] = r
        if self.gravar:
            gravar_json(self.pasta_rc / f"{r['id']}.json", r)
        saida = f"ambientes/recortes/{r['id']}.json"
        if saida not in self.ex.saidas:
            self.ex.saidas.append(saida)

    def falta(self, tipo: str, o_que: str, por_que: str, onde: list[str]) -> str:
        f = {"id": proximo_id("F", self.faltas_ids), "tipo": tipo, "o_que_falta": o_que, "por_que": por_que,
             "onde_aparece": onde, "criada_por": f"scripts/recorte.py ({self.ex.id})",
             "data": date.today().isoformat()}
        erros = validar_objeto(f, carregar_esquema("falta"))
        if erros:
            raise SystemExit(f"Falta inválida: {'; '.join(erros)}")
        self.faltas_ids.add(f["id"])
        if self.gravar:
            gravar_json(self.raiz / "acervo" / "faltas" / f"{f['id']}.json", f)
        self.ex.saidas.append(f"acervo/faltas/{f['id']}.json")
        self.ex.resultados.append(f"{f['id']}: {o_que}")
        return f["id"]

    def recorte(self, ambiente: str, consulta: str, periodo: str, modo: str, teto: dict) -> dict:
        """O Recorte de ambiente × Consulta × período × modo: o que existe, ou um novo (sob demanda)."""
        for r in self.recortes.values():
            if (r.get("ambiente"), r.get("consulta"), r.get("periodo", "todo"), r.get("modo")) == (ambiente, consulta, periodo, modo) and not r.get("retirado"):
                r = dict(r)
                if r["estado"] in FINAIS:  # nova passada (monitoramento): do começo, só o não visto é novo
                    r.update(cursor=None, total_visto=0, estado="aberto")
                    r.pop("explicacao_total_visto", None)
                r["teto"] = teto
                return r
        novo = {"id": proximo_id("RC", set(self.recortes)), "ambiente": ambiente, "consulta": consulta,
                "periodo": periodo, "modo": modo, "cursor": None, "total_informado": None, "total_visto": 0,
                "saturacao": "nada visto ainda", "erros": [], "proxima_acao": "rodar a primeira página",
                "teto": teto, "estado": "aberto", "data": date.today().isoformat(),
                "origem_registro": self.ex.origem("scripts/recorte.py", VERSAO)}
        self.recortes[novo["id"]] = novo  # o id fica tomado já na criação
        return novo


# --- Consulta ------------------------------------------------------------------------------------
def carregar_consulta(raiz: Path, co: str) -> dict:
    return carregar_json(raiz / "ambientes" / "consultas" / f"{co}.json")


def modo_da(c: dict) -> str:
    return "descritores" if c["tipo"] == "só descritores" else "termo"


def formas_da(raiz: Path, c: dict) -> list[str]:
    fs = []
    for te in c.get("termos", []):
        arq = raiz / "acervo" / "termos" / f"{te}.json"
        if arq.exists():
            fs += formas(carregar_json(arq))
    fs += c.get("variantes", [])
    return list(dict.fromkeys(fs))


def traducao(raiz: Path, co: str, ambiente: str) -> dict:
    t = carregar_json(raiz / "ambientes" / "traducao-consultas.json").get(co, {}).get(ambiente)
    if not t:
        raise SystemExit(f"{co} × {ambiente}: sem tradução em ambientes/traducao-consultas.json")
    return t


# --- estado --------------------------------------------------------------------------------------
def anotar_pagina(r: dict, total, vistos: int, proximo, data: str) -> None:
    r["total_informado"] = total
    r["total_visto"] = r.get("total_visto", 0) + vistos
    r["cursor"] = proximo
    r["estado"] = "em curso"
    r["data"] = data
    if total is not None and r["total_visto"] > total:
        r["explicacao_total_visto"] = ("a fonte mudou o total entre as páginas: o visto soma o que cada "
                                       "página trouxe")
    else:
        r.pop("explicacao_total_visto", None)


def fechar(reg: Registro, r: dict, *, acabou: bool, teto_estourado: str | None, erro: str | None) -> None:
    faltas = list(r.get("faltas", []))
    if erro:
        r["erros"] = r.get("erros", []) + [erro]
        r["proxima_acao"] = "via humana: busca assistida de Vicente (scripts/assistido.py); a via automática não se contorna"
        r["saturacao"] = f"não exaurido: {r['total_visto']} visto(s) até o erro"
        if r["estado"] == "em curso" and r["cursor"] is None:
            r["estado"] = "aberto"
        faltas.append(reg.falta("fonte_inacessivel", f"fonte inacessível pela via automática: {r['ambiente']} × {r['consulta']}",
                                erro, [r["id"], r["ambiente"]]))
    elif teto_estourado:
        r["estado"] = "interrompido por teto"
        r["saturacao"] = f"não exaurido: {r['total_visto']} de {r['total_informado'] if r['total_informado'] is not None else '?'} visto(s)"
        r["proxima_acao"] = f"retomar do cursor {r['cursor']!r} com teto novo" if r["cursor"] else "dividir a janela com teto novo"
        faltas.append(reg.falta("outro", f"busca interrompida por teto: {r['id']} ({r['ambiente']} × {r['consulta']}, {r.get('periodo', 'todo')})",
                                teto_estourado, [r["id"]]))
    elif acabou:
        if r["total_informado"] is None:
            r["estado"] = "em curso"
            r["saturacao"] = f"total desconhecido: {r['total_visto']} visto(s) até o fim da lista"
            r["proxima_acao"] = "repetir no monitoramento; o total não se conhece"
            faltas.append(reg.falta("outro", f"total desconhecido: {r['id']} ({r['ambiente']} × {r['consulta']})",
                                    "a fonte não informou o total da consulta", [r["id"]]))
        else:
            r["estado"] = "percorrido pela busca"
            r["saturacao"] = (f"exaurido: {r['total_visto']} de {r['total_informado']} visto(s), passada completa e não saturada")
            r["proxima_acao"] = "monitoramento: repetir e anotar só o não visto"
    if faltas:
        r["faltas"] = list(dict.fromkeys(faltas))
    if r["total_informado"] is None and not r.get("faltas"):
        r["faltas"] = [reg.falta("outro", f"total desconhecido: {r['id']} ({r['ambiente']} × {r['consulta']})",
                                 "a fonte ainda não informou o total", [r["id"]])]
    reg.salvar(r)


# --- rodadas -------------------------------------------------------------------------------------
def entradas(reg: Registro, r: dict, itens: list[dict]) -> tuple[int, int]:
    novas = repetidas = 0
    for it in itens:
        _, nova = deduplicar.registrar(
            reg.indice, identificador=it["identificador"], url=it["url"], canal="monitoramento e escavação",
            origem=reg.ex.origem("scripts/recorte.py", deduplicar.VERSAO), ambiente=r["ambiente"],
            recorte=r["id"], gravar=reg.gravar)
        novas += nova
        repetidas += not nova
    return novas, repetidas


def dividir(periodo: str, cfg: dict) -> tuple[str, str] | None:
    """Divide a janela ao meio. "todo" vai de 1900 ao ano corrente, ou ao "periodo" da linha do ambiente."""
    a, b = (cfg.get("periodo") or [INICIO_PERIODO, date.today().year]) if periodo == "todo" else map(int, periodo.split("-"))
    if a >= b:
        return None
    m = (a + b) // 2
    return f"{a}-{m}", f"{m + 1}-{b}"


def rodar_busca(reg, cli, mod, cfg, ambiente, co, periodo, teto, resumo) -> None:
    c = carregar_consulta(reg.raiz, co)
    consulta = mod.lookfor(traducao(reg.raiz, co, ambiente))
    r = reg.recorte(ambiente, co, periodo, modo_da(c), teto)
    reg.ex.recortes.add(r["id"])
    pags = novas = rep = 0
    while True:
        if pags >= teto["chamadas"]:
            fechar(reg, r, acabou=False, teto_estourado=f"teto de {teto['chamadas']} chamadas da rodada", erro=None)
            break
        try:
            p = mod.pagina(cli, cfg, ambiente, consulta, periodo, r["cursor"])
        except (BloqueioRobos, BloqueioAntiRobo, RuntimeError) as e:
            reg.ex.erros.append(f"{r['id']}: {e}")
            fechar(reg, r, acabou=False, teto_estourado=None, erro=str(e))
            break
        pags += 1
        if p["saturada"] and r["total_visto"] == 0:
            partes = dividir(periodo, cfg)
            if partes and teto.get("divisoes_janela", 0) > 0:
                r.update(total_informado=p["total_informado"], estado="aberto",
                         saturacao=f"saturada: {p['total_informado']} acima do limite da fonte ({cfg.get('limite_fonte')}); janela dividida em {partes[0]} e {partes[1]}",
                         proxima_acao="não conta como pegada: valem os Recortes da janela dividida")
                reg.salvar(r)
                resumo.append(f"{r['id']} {ambiente} {co} {periodo}: saturada, dividida em {partes[0]} e {partes[1]}")
                filho = dict(teto, divisoes_janela=teto["divisoes_janela"] - 1)
                for parte in partes:
                    rodar_busca(reg, cli, mod, cfg, ambiente, co, parte, filho, resumo)
                return
            fechar(reg, r, acabou=False, teto_estourado=f"resposta saturada e teto de divisões da janela ({teto.get('divisoes_janela', 0)}) esgotado", erro=None)
            break
        anotar_pagina(r, p["total_informado"], len(p["itens"]), p["proximo"], date.today().isoformat())
        n, k = entradas(reg, r, p["itens"])
        novas, rep = novas + n, rep + k
        if p.get("curta"):
            r["erros"] = r.get("erros", []) + [f"página {pags} curta: {len(p['itens'])} itens antes do fim"]
        if p["proximo"] is None:
            fechar(reg, r, acabou=True, teto_estourado=None, erro=None)
            break
        reg.salvar(r)
    reg.ex.olhado.append(f"{ambiente} × {co} ({periodo}): {pags} página(s), visto {r['total_visto']} de {r['total_informado']}")
    if r["estado"] not in FINAIS:
        reg.ex.fora.append(f"{r['id']}: {r['proxima_acao']}")
    resumo.append(f"{r['id']} {ambiente} {co} {periodo}: {r['estado']}; visto {r['total_visto']} de {r['total_informado']}; {novas} Entrada(s) nova(s), {rep} repetida(s)")


def rodar_colheita(reg, cli, mod, cfg, ambiente, cos, teto, resumo) -> None:
    alvos = []
    for co in cos:
        c = carregar_consulta(reg.raiz, co)
        r = reg.recorte(ambiente, co, "todo", modo_da(c), teto)
        reg.ex.recortes.add(r["id"])
        alvos.append((r, formas_da(reg.raiz, c), c.get("descritores", []), c["tipo"], [0, 0]))
    cursores = {r["cursor"] for r, *_ in alvos}
    if len(cursores) > 1:  # colheita comum: todos do mesmo ponto
        for r, *_ in alvos:
            r.update(cursor=None, total_visto=0)
    cursor, pags = alvos[0][0]["cursor"], 0
    while True:
        if pags >= teto["chamadas"]:
            for r, *_ in alvos:
                fechar(reg, r, acabou=False, teto_estourado=f"teto de {teto['chamadas']} chamadas da colheita", erro=None)
            break
        try:
            p = mod.pagina(cli, cfg, ambiente, cursor)
        except (BloqueioRobos, BloqueioAntiRobo, RuntimeError) as e:
            reg.ex.erros.append(f"{ambiente}: {e}")
            for r, *_ in alvos:
                fechar(reg, r, acabou=False, teto_estourado=None, erro=str(e))
            break
        pags += 1
        cursor = p["proximo"]
        for r, fs, ds, tipo, cont in alvos:
            anotar_pagina(r, p["total_informado"], p["vistos"], cursor, date.today().isoformat())
            achados = [it for it in p["itens"] if mod.casa(it["texto"], fs, ds, tipo)]
            n, k = entradas(reg, r, achados)
            cont[0] += n
            cont[1] += k
            if cursor is None:
                fechar(reg, r, acabou=True, teto_estourado=None, erro=None)
            else:
                reg.salvar(r)
        if cursor is None:
            break
    for r, _, _, _, cont in alvos:
        reg.ex.olhado.append(f"{ambiente} × {r['consulta']} (colheita OAI-PMH, filtro local): {pags} página(s), colhido {r['total_visto']} de {r['total_informado']}")
        if r["estado"] not in FINAIS:
            reg.ex.fora.append(f"{r['id']}: {r['proxima_acao']}")
        resumo.append(f"{r['id']} {ambiente} {r['consulta']} todo: {r['estado']}; colhido {r['total_visto']} de {r['total_informado']}; {cont[0]} Entrada(s) nova(s), {cont[1]} repetida(s)")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ambiente", required=True)
    ap.add_argument("--consulta", required=True, help="uma ou mais, separadas por vírgula")
    ap.add_argument("--periodo", default="todo")
    ap.add_argument("--teto-chamadas", type=int, default=50)
    ap.add_argument("--teto-divisoes", type=int, default=4)
    ap.add_argument("--fixtures", type=Path)
    ap.add_argument("--gravar-fixtures", type=Path)
    ap.add_argument("--raiz", type=Path, default=RAIZ)
    ap.add_argument("--simular", action="store_true", help="roda sem gravar registros nem log")
    ap.add_argument("--entrada-ref", default="K-107, bloco 5 do brief de execuções")
    ap.add_argument("--execucao", help="id da Execução já reservado (senão, o próximo livre)")
    a = ap.parse_args()
    raiz = a.raiz if a.raiz.is_absolute() else RAIZ / a.raiz
    fx = (a.fixtures if a.fixtures.is_absolute() else RAIZ / a.fixtures) if a.fixtures else None
    cfg = carregar_cfg(raiz, a.ambiente)
    if cfg["adaptador"] == "assistido":
        print(f"{a.ambiente}: modo assistido ({cfg.get('motivo', '')}); use scripts/assistido.py")
        return 1
    mod = ADAPTADORES.get(cfg["adaptador"])
    if not mod:
        print(f"{a.ambiente}: adaptador {cfg['adaptador']!r} não existe")
        return 1
    ex = Execucao("recorte", a.entrada_ref, id_=a.execucao, simular=a.simular)
    reg = Registro(raiz, ex, gravar=not a.simular)
    cli = Cliente(fixtures=fx, gravar_fixtures=a.gravar_fixtures)
    teto = {"chamadas": a.teto_chamadas, "divisoes_janela": a.teto_divisoes}
    cos = [x.strip() for x in a.consulta.split(",") if x.strip()]
    ex.ambientes.add(a.ambiente)
    ex.consultas |= set(cos)
    ex.acoes.append(f"scripts/recorte.py --ambiente {a.ambiente} --consulta {','.join(cos)} --periodo {a.periodo} "
                    f"--teto-chamadas {a.teto_chamadas} --teto-divisoes {a.teto_divisoes}"
                    + (" (fixtures)" if fx else "") + (" --simular" if a.simular else ""))
    resumo: list[str] = []
    if mod.TIPO == "colheita":
        rodar_colheita(reg, cli, mod, cfg, a.ambiente, cos, teto, resumo)
    else:
        for co in cos:
            rodar_busca(reg, cli, mod, cfg, a.ambiente, co, a.periodo, teto, resumo)
    ex.resultados = resumo + ex.resultados
    ex.olhado.append(f"{cli.pedidos} pedido(s) HTTP, robots.txt incluído, robô identificado, 1 por segundo")
    for d in reg.indice.duplicatas:
        ex.erros.append(f"duplicata em entrada/: {d}")
    for x in ex.resultados:
        print(x)
    for x in ex.erros:
        print("ERRO", x)
    print(f"{VERSAO}: {ex.id}; {cli.pedidos} pedido(s); {ex.gravar_log()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
