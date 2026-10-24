"""Pré-triagem por regra, sem IA, na coleta (D-045, item 2; K-108b).

Segue o item que traz no título ou no resumo o termo (uma das formas dos Termos da Consulta) ou um dos
descritores do processo da Consulta (P3). O resto fica só como pegada, "fora do escopo pela regra", com
a versão da regra: nunca se apaga (princípio 10), e a pegada reabre se a regra mudar. O item sem título
nem resumo na fonte segue (a regra não decide sem texto; hospitalidade com o vestígio, princípio 4).

O título e o resumo só servem à regra e ficam na memória: o motivo diz qual forma ou descritor bateu e
onde; a citação curta (até CITACAO_MAX caracteres em volta da ocorrência) só sai quando a ocorrência
está no resumo, para a Entrada que segue (padrão da F-0003).

A busca é por palavra inteira, sem caixa, com a forma em NFC: "caju" não acha "cajueiro"; as formas
sem acento entram só quando o Termo as lista (como "cajuina").

Uso como biblioteca (recorte.py, migrar_entradas.py): avaliar(), consultas_do().
"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

from _comum import carregar_json
from gerar_termo import formas

VERSAO = "pretriagem-0.1"
FORA = "fora do escopo pela regra"
SEGUE = "segue"
CITACAO_MAX = 240


def _norm(s: str) -> str:
    return unicodedata.normalize("NFC", s or "").casefold()


def _achar(texto: str, termo: str) -> re.Match | None:
    return re.search(rf"(?<!\w){re.escape(_norm(termo))}(?!\w)", _norm(texto))


def formas_e_descritores(raiz: Path, co: str) -> tuple[list[str], list[str]]:
    c = carregar_json(raiz / "ambientes" / "consultas" / f"{co}.json")
    fs: list[str] = []
    for te in c.get("termos", []):
        arq = raiz / "acervo" / "termos" / f"{te}.json"
        if arq.exists():
            fs += formas(carregar_json(arq))
    fs += c.get("variantes", [])
    return list(dict.fromkeys(fs)), list(c.get("descritores", []))


def citacao(resumo: str, m: re.Match) -> str:
    """Até CITACAO_MAX caracteres em volta da ocorrência, cortados em espaço, com reticências."""
    t = " ".join(resumo.split())
    m2 = _achar(t, m.group(0)) or m
    meio = (m2.start() + m2.end()) // 2
    a, b = max(0, meio - CITACAO_MAX // 2), min(len(t), meio + CITACAO_MAX // 2)
    if a > 0:
        a = t.find(" ", a) + 1 or a
    if b < len(t):
        b = t.rfind(" ", a, b) if t.rfind(" ", a, b) > a else b
    return ("…" if a > 0 else "") + t[a:b].strip() + ("…" if b < len(t) else "")


def avaliar(raiz: Path, titulo: str | None, resumo: str | None, consultas: list[str]) -> dict:
    """{estado, motivo, versao_regra, citacao?} para o item achado pelas Consultas dadas."""
    titulo, resumo = (titulo or "").strip(), (resumo or "").strip()
    if not titulo and not resumo:
        return {"estado": SEGUE, "motivo": "sem título nem resumo na fonte: a regra não decide sem texto",
                "versao_regra": VERSAO}
    for co in consultas:
        fs, ds = formas_e_descritores(raiz, co)
        for tipo, lista in (("forma", fs), ("descritor", ds)):
            for x in lista:
                if _achar(titulo, x):
                    return {"estado": SEGUE, "motivo": f"{tipo} '{x}' no título ({co})", "versao_regra": VERSAO}
        for tipo, lista in (("forma", fs), ("descritor", ds)):
            for x in lista:
                if m := _achar(resumo, x):
                    return {"estado": SEGUE, "motivo": f"{tipo} '{x}' no resumo ({co})", "versao_regra": VERSAO,
                            "citacao": citacao(resumo, m)}
    return {"estado": FORA, "motivo": f"{FORA}: nenhuma forma nem descritor de {', '.join(consultas)} no título nem no resumo",
            "versao_regra": VERSAO}
