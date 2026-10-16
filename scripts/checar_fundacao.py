"""Verificação mecânica da Fundação (olhar "mecanico" da habilidade verificar-fundacao).

Confere, por busca exata:
  1. marcadores de status ([VIGENTE], [PROPOSTA], [PENDENTE], [ABERTO], [ADIADO]);
  2. "Versão 0.2", "Anexo D", "Anexo E", "C.3" e a legenda das P-refs ("buscar `#### Pn`");
  3. cada decisão D-015 a D-029;
  4. cada entidade do §6 (lista do plano, Implementação, passo 4, mais Recorte, Lugar e papéis);
  5. opcional (--essencias): para cada D-nnn, a linha que a registra contém os termos-chave da
     essência confirmada; e não contém transcrição literal da fala original (--falas).

Saída: relatório JSON no formato de esquemas/achado-verificacao.schema.json (stdout ou --saida).
Código 0 = nenhum achado; 1 = há achados (o que é esperado na v0.1).

Uso:
    python scripts/checar_fundacao.py [arquivo] [--essencias E.json] [--falas F.json] [--saida R.json]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_json  # noqa: E402

MARCADORES = ["[VIGENTE]", "[PROPOSTA]", "[PENDENTE]", "[ABERTO]", "[ADIADO]"]
EXIGIDOS = {
    "versao-0.2": "Versão 0.2",
    "anexo-d": "Anexo D",
    "anexo-e": "Anexo E",
    "anexo-c3": "C.3",
    "legenda-pref": "#### Pn",
    "falta": "Falta",
}
DECISOES = [f"D-{n:03d}" for n in range(15, 30)]
ENTIDADES_6 = [
    "Ambiente", "Consulta", "Execução", "Entrada", "Fonte", "Trecho", "Evidência", "Proposição",
    "Termo", "CLB situada", "Elemento de prática", "Compreensão local", "Transformação", "Falta",
    "Insumo", "Aresta", "Recorte", "Lugar", "papéis", "eixos de status", "IDs imutáveis",
    "campos de proteção",
]


def sem_acento(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")


def secao(linhas: list[str], inicio: str, fim_prefixo: str = "## ") -> tuple[int, list[str]]:
    ini = next((i for i, l in enumerate(linhas) if l.startswith(inicio)), None)
    if ini is None:
        return 0, []
    fim = next((i for i in range(ini + 1, len(linhas)) if linhas[i].startswith(fim_prefixo)), len(linhas))
    return ini, linhas[ini:fim]


def achado(n: int, tipo: str, descricao: str, comando: str, linha=None, trecho=None) -> dict:
    a = {"id": f"M-{n:03d}", "tipo": tipo, "descricao": descricao,
         "confirmacao": {"metodo": "script", "comando": comando}, "estado": "confirmado"}
    if linha is not None:
        a["linha"] = linha
    if trecho is not None:
        a["trecho"] = trecho[:300]
    return a


def checar(caminho: Path, essencias: Path | None = None, falas: Path | None = None) -> dict:
    texto = caminho.read_text(encoding="utf-8").replace("\r\n", "\n")
    linhas = texto.split("\n")
    achados: list[dict] = []
    presentes: dict[str, int] = {}
    cmd = f"python scripts/checar_fundacao.py {caminho.name}"

    def primeira(s: str, base: list[str] = linhas, desloc: int = 0):
        return next((i + 1 + desloc for i, l in enumerate(base) if s in l), None)

    for m in MARCADORES:
        ln = primeira(m)
        if ln:
            presentes[m] = ln
        else:
            achados.append(achado(len(achados) + 1, "ausencia", f"marcador {m} ausente", cmd))
    for chave, s in EXIGIDOS.items():
        ln = primeira(s)
        if ln:
            presentes[s] = ln
        else:
            achados.append(achado(len(achados) + 1, "ausencia", f"'{s}' ausente ({chave})", cmd))
    for d in DECISOES:
        ln = primeira(d)
        if ln:
            presentes[d] = ln
        else:
            achados.append(achado(len(achados) + 1, "ausencia", f"decisão {d} ausente", cmd))

    ini6, sec6 = secao(linhas, "## 6.")
    if not sec6:
        achados.append(achado(len(achados) + 1, "ausencia", "seção '## 6.' não encontrada", cmd))
    for ent in ENTIDADES_6:
        rx = re.compile(r"(?<!\w)" + re.escape(ent) + r"(?!\w)")
        ln = next((ini6 + i + 1 for i, l in enumerate(sec6) if rx.search(l)), None)
        if ln:
            presentes[f"§6:{ent}"] = ln
        else:
            achados.append(achado(len(achados) + 1, "ausencia", f"entidade '{ent}' ausente do §6", cmd))

    if essencias:
        for e in carregar_json(essencias)["essencias"]:
            ln = primeira(e["id"])
            if not ln:
                continue  # a ausência já foi registrada acima
            # a linha da decisão e as continuações (até a próxima linha vazia ou próximo D-)
            bloco = [linhas[ln - 1]]
            for l in linhas[ln:]:
                if not l.strip() or re.match(r"^\s*[-*|]?\s*\**D-\d{3}", l):
                    break
                bloco.append(l)
            alvo = sem_acento(" ".join(bloco))
            faltam = [t for t in e["termos_chave"] if sem_acento(t) not in alvo]
            if faltam:
                achados.append(achado(len(achados) + 1, "divergencia_de_essencia",
                                      f"{e['id']}: faltam termos da essência confirmada: {', '.join(faltam)}",
                                      cmd + f" --essencias {essencias.as_posix()}", ln, linhas[ln - 1]))
    if falas:
        norm = lambda s: re.sub(r"\s+", " ", sem_acento(s)).strip()  # noqa: E731
        corpo = norm(texto)
        for f in carregar_json(falas)["falas"]:
            for frase in f["frases"]:
                if len(frase.split()) >= 6 and norm(frase) in corpo:
                    ln = next((i + 1 for i, l in enumerate(linhas) if norm(frase)[:40] in norm(l)), None)
                    achados.append(achado(len(achados) + 1, "transcricao_no_lugar_da_essencia",
                                          f"{f['id']}: transcrição literal da fala original, em vez da essência",
                                          cmd + f" --falas {falas.as_posix()}", ln, frase))

    return {
        "arquivo": caminho.name,
        "data": date.today().isoformat(),
        "verificador": "scripts/checar_fundacao.py",
        "olhar": "mecanico",
        "achados": achados,
        "resumo": {"achados": len(achados), "presentes": presentes},
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("arquivo", nargs="?", default=str(RAIZ / "00_Fundacao_Cultura_Liquida.md"))
    ap.add_argument("--essencias", type=Path)
    ap.add_argument("--falas", type=Path)
    ap.add_argument("--saida", type=Path)
    a = ap.parse_args()
    rel = checar(Path(a.arquivo), a.essencias, a.falas)
    js = json.dumps(rel, ensure_ascii=False, indent=2)
    if a.saida:
        a.saida.write_text(js + "\n", encoding="utf-8")
        print(f"{len(rel['achados'])} achado(s); relatório em {a.saida}")
    else:
        print(js)
    return 1 if rel["achados"] else 0


if __name__ == "__main__":
    sys.exit(main())
