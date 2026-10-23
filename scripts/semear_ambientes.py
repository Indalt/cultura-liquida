"""Semeia ambientes/ com um arquivo por linha do Anexo E, em estado "proposto" (bloco 3; l. 415).

Lê os mesmos dados do gerar_anexo_e.py (o catálogo da pesquisa de 15/10), na mesma ordem e com
a mesma junção das repetidas, e grava ambientes/AM-nnnn.json (esquemas/ambiente.schema.json):
nome, tipo (o enum do contrato quando o tipo do catálogo cabe nele; senão "outro"), o tipo do
catálogo em tipo_detalhe, via de acesso, estado_escavacao "proposto", estado_monitoramento
"não iniciado" e a linha do Anexo E. Uso, nível, link e termos de uso do catálogo vão na nota,
até a ficha de acesso testada (bloco 4). A contagem tem de bater com a tabela do Anexo E da
Fundação.

Uso:
    python scripts/semear_ambientes.py --execucao EX-nnnn [--gravar]
    python scripts/semear_ambientes.py --conferir [--pasta <pasta>]
Sem --gravar, só mostra. --gravar recusa sobrescrever ambiente que já não esteja "proposto".
--conferir: os ambientes da pasta validam e a contagem bate com o Anexo E; código 1 se não.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_esquema, carregar_json, validar_objeto  # noqa: E402
from gerar_anexo_e import ARQUIVOS, PASTA, celula, fontes  # noqa: E402

FUNDACAO = RAIZ / "00_Fundacao_Cultura_Liquida.md"
TIPOS = [  # (padrão no tipo do catálogo, tipo do contrato); o primeiro que casa vale
    (r"^hemeroteca", "hemeroteca"),
    (r"^rede social", "rede social"),
    (r"teses e dissertações|repositório.*tese", "repositório de teses"),
    (r"^diário oficial|^diários oficiais|^legislação|^documentos oficiais|^normas e registro|^proposições", "documento oficial"),
    (r"^periódico", "periódico científico"),
    (r"blogs?\b", "blog"),
]


def linhas_anexo_e_fundacao() -> int:
    t = FUNDACAO.read_text(encoding="utf-8").splitlines()
    ini = next(i for i, l in enumerate(t) if l.startswith("## Anexo E"))
    fim = next((i for i in range(ini + 1, len(t)) if t[i].startswith("## ")), len(t))
    return sum(1 for l in t[ini:fim] if l.startswith("| ")) - 1  # menos o cabeçalho


def catalogo() -> list[dict]:
    saida, vistos = [], set()
    for nome, origem in ARQUIVOS:
        achadas: list[dict] = []
        fontes(json.loads((PASTA / nome).read_text(encoding="utf-8")), achadas)
        for f in achadas:
            chave = celula(f.get("name")).lower()
            if chave not in vistos:
                vistos.add(chave)
                saida.append({**f, "_origem": origem})
    return saida


def ambiente(n: int, f: dict, execucao: str) -> dict:
    kind = celula(f.get("kind"))
    tipo = next((t for p, t in TIPOS if re.search(p, kind, re.I)), "outro")
    link = f.get("url") or f.get("permalink") or f.get("endpoint")
    return {"id": f"AM-{n:04d}", "nome": celula(f.get("name")), "tipo": tipo, "tipo_detalhe": kind,
            "via_protocolo": celula(f.get("access")), "estado_escavacao": "proposto",
            "estado_monitoramento": "não iniciado", "linha_anexo_e": n,
            "origem_registro": {"criado_por": "scripts/semear_ambientes.py", "data": date.today().isoformat(),
                                "execucao": execucao},
            "nota": (f"Anexo E, linha {n} ({f['_origem']}): uso {celula(f.get('use'))}; nível {celula(f.get('level'))}; "
                     f"link {celula(link)}; termos de uso {celula(f.get('terms'))}; como buscar {celula(f.get('how_to_search'))}. "
                     "Dados do catálogo de 15/10, a conferir na ficha de acesso (bloco 4).")}


def conferir(pasta: Path) -> int:
    esq = carregar_esquema("ambiente")
    arqs = sorted(pasta.glob("AM-*.json"))
    erros = [f"{p.name}: {e}" for p in arqs for e in validar_objeto(carregar_json(p), esq)]
    esperado = linhas_anexo_e_fundacao()
    if len(arqs) != esperado:
        erros.append(f"{len(arqs)} ambientes em {pasta}, e o Anexo E da Fundação tem {esperado}")
    for e in erros:
        print("ERRO", e)
    print(f"{len(arqs)} ambientes; Anexo E: {esperado}; {'bate e valida' if not erros else f'{len(erros)} erro(s)'}")
    return 1 if erros else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--execucao")
    ap.add_argument("--gravar", action="store_true")
    ap.add_argument("--conferir", action="store_true")
    ap.add_argument("--pasta", type=Path, default=RAIZ / "ambientes")
    a = ap.parse_args()
    pasta = a.pasta if a.pasta.is_absolute() else RAIZ / a.pasta
    if a.conferir:
        return conferir(pasta)
    if not a.execucao or not re.fullmatch(r"EX-[0-9]{4,}", a.execucao):
        raise SystemExit("informe --execucao EX-nnnn (o id do log da semeadura)")
    esq = carregar_esquema("ambiente")
    regs = [ambiente(n, f, a.execucao) for n, f in enumerate(catalogo(), 1)]
    for r in regs:
        erros = validar_objeto(r, esq)
        if erros:
            print(f"{r['id']} inválido: {'; '.join(erros)}")
            return 1
        print(f"{r['id']} · {r['tipo']} · {r['nome']}")
    if a.gravar:
        pasta.mkdir(exist_ok=True)
        for r in regs:
            p = pasta / f"{r['id']}.json"
            if p.exists() and carregar_json(p).get("estado_escavacao") != "proposto":
                print(f"{p.name} já saiu de 'proposto': não sobrescrevo")
                continue
            p.write_text(json.dumps(r, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return conferir(pasta)
    print(f"{len(regs)} ambientes (Anexo E da Fundação: {linhas_anexo_e_fundacao()}); nada gravado sem --gravar")
    return 0


if __name__ == "__main__":
    sys.exit(main())
