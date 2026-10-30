"""Nomes prováveis de pessoa nos Trechos (K-111, insumo 76). Sem IA. Regra nomes-0.1.

O `gravar_extracao.py` barra o nome que está na tabela privada e corta o contexto num tratamento
seguido de nome ("Dona", "seu"...). O nome de quem a fonte cita sem falar e sem tratamento escapa às
duas e só a leitura o pegava. Este script não depende da leitura: aponta, no texto exato, no antes e no
depois de cada Trecho, as sequências de duas ou mais palavras com maiúscula (com "de", "da", "do",
"dos", "das" e "e" no meio) que não são lugar da tabela do IBGE de 2024, nome de UF nem palavra da
lista de instituições e termos comuns (abaixo). Não decide nada: a lista vai a quem grava (curador) ou
ao auditor, que olha cada uma. O nome do autor citado com a obra não é dado pessoal a barrar (D-042).

Uso:
    python scripts/nomes_provaveis.py [<TR-nnnn.json> ...] [--raiz <pasta>] [--falhar]
Sem arquivos, olha todos os Trechos de <raiz>/acervo/trechos/. Código 0 = lista impressa (ou nada achado);
com --falhar, código 1 quando acha algo (para o portão de quem grava).
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ  # noqa: E402

VERSAO = "nomes-0.1"
MAI = "A-ZÁÉÍÓÚÂÊÔÃÕÇ"
RE_SEQ = re.compile(rf"(?<![\w.])[{MAI}][\wÀ-ÿ'-]+(?:\s+(?:(?:de|da|do|dos|das|e)\s+)?[{MAI}][\wÀ-ÿ'-]+)+")
# instituições, lugares maiores e termos que aparecem com maiúscula nas fontes do piloto
COMUNS = {
    "iphan", "embrapa", "emater", "sebrae", "ufc", "ufpi", "uespi", "mec", "bncc", "dpi", "divtec", "bcr",
    "brasil", "nordeste", "piauí", "ceará", "maranhão", "rio", "grande", "norte", "sul", "delta", "parnaíba",
    "universidade", "federal", "estadual", "instituto", "departamento", "superintendência", "patrimônio",
    "histórico", "artístico", "nacional", "imaterial", "cultural", "programa", "pós-graduação", "ciência",
    "tecnologia", "alimentos", "agroindústria", "tropical", "meio-norte", "centro", "pesquisa", "ministério",
    "agricultura", "secretaria", "governo", "estado", "associação", "cooperativa", "produtores", "cajuína",
    "caju", "livro", "registro", "saberes", "bens", "culturais", "registrados", "conselho", "consultivo",
    "parecer", "técnico", "dossiê", "lei", "decreto", "instrução", "normativa", "portaria", "resolução",
    "indicação", "geográfica", "procedência", "festival", "feira", "festa", "semana", "dia", "mercado",
    "público", "praça", "avenida", "rua", "igreja", "nossa", "senhora", "são", "santo", "santa", "deus",
    "tremembé", "tremembés", "tabela", "figura", "quadro", "gráfico", "anexo", "capítulo", "seção", "a", "o",
    "os", "as", "em", "no", "na", "para", "com", "por", "que", "se", "mas", "quando", "como", "ela", "ele",
}


def chave(t: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", t.casefold()) if unicodedata.category(c) != "Mn")


def lugares() -> set[str]:
    saida = set()
    for arq in (RAIZ / "acervo" / "lugares" / "ibge").glob("*.csv"):
        with arq.open(encoding="utf-8-sig", newline="") as f:
            for l in csv.DictReader(f, delimiter=";"):
                saida.add(chave(l["Nome do município"]))
                saida.add(chave(l.get("Nome da UF") or ""))
    return saida


def provaveis(texto: str, lugs: set[str]) -> list[str]:
    achados = []
    for m in RE_SEQ.finditer(texto or ""):
        seq = m.group(0)
        palavras = [p for p in re.split(r"\s+", seq) if p not in ("de", "da", "do", "dos", "das", "e")]
        if chave(seq) in lugs or all(chave(p) in COMUNS or chave(p) in lugs for p in palavras):
            continue
        achados.append(seq)
    return achados


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("arquivos", nargs="*", type=Path)
    ap.add_argument("--raiz", type=Path, default=RAIZ)
    ap.add_argument("--falhar", action="store_true")
    a = ap.parse_args()
    arqs = a.arquivos or sorted((a.raiz / "acervo" / "trechos").glob("TR-*.json"))
    lugs = lugares()
    total = 0
    for arq in arqs:
        tr = json.loads(arq.read_text(encoding="utf-8"))
        for campo in ("texto_exato", "antes", "depois"):
            for seq in provaveis(tr.get(campo, ""), lugs):
                total += 1
                print(f"{tr.get('id', arq.stem)} ({campo}): {seq}")
    print(f"{VERSAO}: {len(arqs)} Trecho(s) olhado(s); {total} nome(s) provável(is) para conferir (a lista não decide)")
    return 1 if (a.falhar and total) else 0


if __name__ == "__main__":
    sys.exit(main())
