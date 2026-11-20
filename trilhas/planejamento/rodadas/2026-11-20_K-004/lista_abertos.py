"""K-004, etapa 1 (D-058): lista dos insumos abertos, por script e sem IA.

Lê:
- trilhas/insumos-planejamento.md (tabela de insumos: #, data, origem, insumo, aonde);
- trilhas/planejamento/mapa-tres-frentes.md, seção 6 (cada insumo N: frente e 'vira');
- trilhas/planejamento/quadro.md (estado de cada cartão K-nnn[a-c]).

Regra mecânica (sem julgamento):
- fechado_por_cartao: o 'vira' cita cartões e todos estão Concluído;
- aberto_cartao: cita algum cartão que não está Concluído;
- a_definir: o 'vira' é 'a definir pelo planejamento' e não cita cartão;
- conferir: o 'vira' cita decisão (D-nnn) ou não tem cartão nem 'a definir' (leitura humana, não fecha por script);
- não encontrado: insumo sem linha na seção 6 (erro de dados, a corrigir).

Saída: lista_abertos.json e lista_abertos.md, nesta pasta. Não altera nenhum insumo.
Uso: python lista_abertos.py   (com PYTHONUTF8=1)
"""
import json
import pathlib
import re
from collections import Counter

RAIZ = pathlib.Path(__file__).resolve().parents[4]
PASTA = pathlib.Path(__file__).resolve().parent
INSUMOS = RAIZ / "trilhas" / "insumos-planejamento.md"
MAPA = RAIZ / "trilhas" / "planejamento" / "mapa-tres-frentes.md"
QUADRO = RAIZ / "trilhas" / "planejamento" / "quadro.md"

RE_CARTAO = re.compile(r"K-\d{3}[a-c]?")
RE_DECISAO = re.compile(r"\bD-\d{3}\b")


def ler_insumos():
    itens = {}
    for linha in INSUMOS.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\| (\d+) \| ([^|]*)\| ([^|]*)\| (.*)\| (.*) \|\s*$", linha)
        if m:
            n = int(m.group(1))
            itens[n] = {
                "data": m.group(2).strip(),
                "origem": m.group(3).strip(),
                "insumo": m.group(4).strip(),
                "aonde": m.group(5).strip(),
            }
    return itens


def ler_mapa():
    texto = MAPA.read_text(encoding="utf-8").splitlines()
    dentro = False
    vira = {}
    for linha in texto:
        if linha.startswith("## 6."):
            dentro = True
            continue
        if dentro and linha.startswith("## 7."):
            break
        if not dentro:
            continue
        m = re.match(r"^\| (\d+), (.*?) \| ([^|]*)\| (.*) \|\s*$", linha)
        if m:
            n = int(m.group(1))
            vira[n] = {
                "texto": m.group(2).strip(),
                "frente": m.group(3).strip(),
                "vira": m.group(4).strip(),
            }
    return vira


def ler_quadro():
    estado = {}
    for linha in QUADRO.read_text(encoding="utf-8").splitlines():
        if not linha.startswith("| "):
            continue
        colunas = [c.strip() for c in linha.split("|")[1:-1]]
        if len(colunas) < 2:
            continue
        status = colunas[0]
        for cartao in RE_CARTAO.findall(colunas[1]):
            pass
        m = re.search(r"\*\*(K-\d{3}[a-c]?)\*\*", colunas[1])
        if m:
            estado[m.group(1)] = "concluido" if status.startswith("Concluído") else "aberto"
    return estado


def classificar(n, vira, estado):
    if vira is None:
        return "nao_encontrado", []
    texto = vira["vira"]
    cartoes = RE_CARTAO.findall(texto)
    if cartoes:
        status = {c: estado.get(c, "sem_cartao_no_quadro") for c in cartoes}
        if all(s == "concluido" for s in status.values()):
            return "fechado_por_cartao", cartoes
        return "aberto_cartao", cartoes
    if texto.lower().startswith("respondido pela d-"):
        return "fechado_por_decisao", RE_DECISAO.findall(texto)
    if "a definir" in texto.lower():
        return "a_definir", []
    return "conferir", RE_DECISAO.findall(texto)


def main():
    insumos = ler_insumos()
    mapa = ler_mapa()
    estado = ler_quadro()
    resultado = []
    contagem = Counter()
    for n in sorted(insumos):
        cls, refs = classificar(n, mapa.get(n), estado)
        contagem[cls] += 1
        resultado.append({
            "insumo": n,
            "data": insumos[n]["data"],
            "classe": cls,
            "refs": refs,
            "vira": mapa[n]["vira"] if n in mapa else None,
            "frente": mapa[n]["frente"] if n in mapa else None,
        })
    total = len(insumos)
    abertos = [r for r in resultado if not r["classe"].startswith("fechado")]
    dados = {
        "total_insumos": total,
        "contagem": dict(contagem),
        "abertos_por_script": len(abertos),
        "itens": resultado,
    }
    (PASTA / "lista_abertos.json").write_text(
        json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")

    linhas = [
        "# Insumos abertos por script (K-004, etapa 1, D-058)",
        "",
        "Gerado por `lista_abertos.py`, sem IA. Nenhum insumo foi alterado.",
        "",
        f"- Total de insumos: {total}",
        f"- Contagem por classe: {dict(contagem)}",
        f"- Abertos para a proposta de limpeza (não fechados por script): {len(abertos)}",
        "",
        "## Fechados por cartão concluído (saem da fila, com o motivo)",
        "",
        "| Insumo | Cartão(ões) |",
        "|---|---|",
    ]
    for r in resultado:
        if r["classe"] == "fechado_por_cartao":
            linhas.append(f"| {r['insumo']} | {', '.join(r['refs'])} |")
    linhas += ["", "## Fechados por decisão vigente (respondidos, saem da fila)", "",
               "| Insumo | Decisão |", "|---|---|"]
    for r in resultado:
        if r["classe"] == "fechado_por_decisao":
            linhas.append(f"| {r['insumo']} | {', '.join(r['refs'])} |")
    for titulo, classe in [
        ("Abertos: apontam para cartão não concluído", "aberto_cartao"),
        ("A definir pelo planejamento", "a_definir"),
        ("Para conferir à mão (cita decisão ou sem destino claro)", "conferir"),
        ("Sem linha na seção 6 do mapa (erro a corrigir)", "nao_encontrado"),
    ]:
        linhas += ["", f"## {titulo}", "", "| Insumo | Cartão / decisão | Vira (mapa, seção 6) |", "|---|---|---|"]
        for r in resultado:
            if r["classe"] == classe:
                refs = ", ".join(r["refs"]) if r["refs"] else "—"
                vira = (r["vira"] or "").replace("|", "/")
                linhas.append(f"| {r['insumo']} | {refs} | {vira} |")
    (PASTA / "lista_abertos.md").write_text("\n".join(linhas) + "\n", encoding="utf-8")
    print(json.dumps({"total": total, "contagem": dict(contagem),
                      "abertos": len(abertos)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
