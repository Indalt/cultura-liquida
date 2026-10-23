"""Funções comuns aos scripts do núcleo (bloco 3): leitura do acervo, índice por ID,
esquema de cada prefixo e o próximo ID da faixa do gravador.

Layout (esquemas/valores-provisorios.json, valor "layout"; ambientes/adaptadores.json é configuração
dos adaptadores, K-107): ambientes/<id>.json,
ambientes/consultas/, ambientes/recortes/, entrada/, acervo/<tipo>/. As pastas nascem
no passo em que entram (l. 723): pasta ausente não é erro.
"""
from __future__ import annotations

import re
from pathlib import Path

from _comum import RAIZ, carregar_json, carregar_valores

# prefixo do ID → nome do esquema em esquemas/
ESQUEMA_POR_PREFIXO = {
    "AM": "ambiente", "CO": "consulta", "RC": "recorte", "EN": "entrada", "FO": "fonte",
    "TR": "trecho", "EV": "evidencia", "PR": "proposicao", "CL": "clb", "EL": "elemento",
    "IN": "insumo-x", "PC": "processo", "CP": "compreensao-local", "TF": "transformacao",
    "AR": "aresta", "TE": "termo", "LU": "lugar", "F": "falta", "P": "pessoa",
}
PASTAS_ACERVO = ["ambientes", "entrada", "acervo"]
RE_ID = re.compile(r"^([A-Z]{1,2})-([0-9]{4,})$")


def prefixo(id_: str) -> str | None:
    m = RE_ID.match(id_ or "")
    return m.group(1) if m else None


def id_do_registro(obj) -> str | None:
    """O ID de um registro: 'id' em todos, 'codigo' na Pessoa."""
    if not isinstance(obj, dict):
        return None
    return obj.get("id") or obj.get("codigo")


def arquivos_acervo(raiz: Path = RAIZ) -> list[Path]:
    """Os JSON do acervo, fora os arquivos de configuração do layout (tradução, rotinas)."""
    saida = []
    for nome in PASTAS_ACERVO:
        pasta = raiz / nome
        if pasta.exists():
            saida += sorted(p for p in pasta.rglob("*.json")
                            if p.name not in ("traducao-consultas.json", "rotinas.json", "adaptadores.json"))
    return saida


def onde_esta_no_layout(arq: Path, raiz: Path, pastas: tuple[str, ...]) -> bool:
    """O arquivo está numa das pastas de topo dadas (ex.: ("entrada", "acervo"))?"""
    return arq.relative_to(raiz).parts[0] in pastas


def carregar_acervo(raiz: Path = RAIZ) -> tuple[dict[str, dict], dict[str, list[Path]], list[str]]:
    """Devolve (índice id → registro, id → arquivos onde aparece, erros de leitura)."""
    indice: dict[str, dict] = {}
    onde: dict[str, list[Path]] = {}
    erros: list[str] = []
    for arq in arquivos_acervo(raiz):
        try:
            obj = carregar_json(arq)
        except Exception as e:
            erros.append(f"{arq.relative_to(raiz)}: JSON ilegível ({e})")
            continue
        id_ = id_do_registro(obj)
        if not id_:
            erros.append(f"{arq.relative_to(raiz)}: registro sem id")
            continue
        onde.setdefault(id_, []).append(arq)
        indice.setdefault(id_, obj)
    return indice, onde, erros


def faixas() -> dict[str, list[int]]:
    return carregar_valores()["valores"]["numeracao_id"]["valor"]["faixas"]


def proximo_id(prefixo_: str, ids_existentes, gravador: str = "conversa") -> str:
    """O maior número da faixa do gravador + 1 (valor numeracao_id)."""
    ini, fim = faixas()[gravador]
    nums = [int(m.group(2)) for i in ids_existentes
            if (m := RE_ID.match(i)) and m.group(1) == prefixo_ and ini <= int(m.group(2)) <= fim]
    n = max(nums) + 1 if nums else ini
    if n > fim:
        raise ValueError(f"faixa {gravador} de {prefixo_} esgotada")
    return f"{prefixo_}-{n:04d}"


def textos(obj, caminho: str = ""):
    """Percorre todas as cadeias de um registro: (caminho, texto)."""
    if isinstance(obj, str):
        yield caminho, obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from textos(v, f"{caminho}/{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from textos(v, f"{caminho}/{i}")
