"""Monta um programa de aulas do campo de ação a partir de blocos escritos pela IA (habilidade planejar-aulas; D-063).

A IA escreve só o texto dos blocos; este script faz o resto, sem IA:
  material  prepara, para cada bloco, o material fechado: só as afirmações do bloco, com o grau em
            palavras e a citação curta prontos (a IA não abre o acervo).
  montar    junta os blocos em N aulas (1, 3, 5... conforme as montagens do programa), põe as
            referências de cada aula, e grava a nota do educador (rastreio, cuidados, carimbo,
            espaço para anotar) e o kit do professor com as referências.
  conferir  barra a invenção: toda marca <!-- PR-nnnn --> existe no acervo e pertence ao material do
            bloco; toda data, número e nome próprio do bloco aparece no material; nenhum dado pessoal.

O programa é um JSON na pasta do programa (programa.json):
  {"clb": "CL-0001", "titulo": "...", "minutos_por_aula": 50,
   "carimbo": {"versao_ficha": "...", "nivel": "...", "data": "AAAA-MM-DD", "como_citar": "..."},
   "cuidados": ["texto simples", ...], "faltas": ["F-nnnn: o que falta", ...],
   "blocos": [{"id": "abertura", "titulo": "...", "minutos": 15, "proposicoes": ["PR-nnnn", ...]}, ...],
   "montagens": {"1": [["abertura", "b1"]], "3": [["abertura", "b1"], ["b2"], ["b3"]]}}
Os blocos ficam em <pasta>/blocos/<id>.md; o kit, em <pasta>/blocos/kit.md (opcional).
Cada frase com fato leva logo depois a marca invisível <!-- PR-nnnn --> da afirmação.

Uso:
    python scripts/montar_programa.py material <programa.json> [--saida DIR]
    python scripts/montar_programa.py montar   <programa.json> --aulas 3 [--saida DIR]
    python scripts/montar_programa.py conferir <programa.json>
Código 0 = feito ou conferido; 1 = reprovado (a conferência diz o quê); 2 = erro de entrada.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ  # noqa: E402
from procurar_dado_pessoal import achar  # noqa: E402

VERSAO = "montar-programa-0.1"
ACERVO = RAIZ / "acervo"
MARCA = re.compile(r"<!--\s*(PR-\d{4})\s*-->")
COMENTARIO = re.compile(r"<!--.*?-->", re.S)


def _registro(pasta: str, id_: str) -> dict:
    arq = ACERVO / pasta / f"{id_}.json"
    if not arq.exists():
        achados = list((ACERVO / pasta).rglob(f"{id_}.json"))
        if not achados:
            raise FileNotFoundError(f"{id_} não existe em acervo/{pasta}")
        arq = achados[0]
    return json.loads(arq.read_text(encoding="utf-8"))


def grau_em_palavras(pr: dict) -> str:
    if (pr.get("lambda") or 0) > 0:
        return "as fontes divergem"
    return {"verdadeiro": "fontes independentes concordam",
            "intermediário": "uma fonte só, ainda sem confirmação independente",
            "paracompleto": "as fontes não bastam para afirmar nem negar"}.get(pr.get("estado"), pr.get("estado", "?"))


def fontes_da(pr: dict) -> list[dict]:
    """[{fo, localizador, ref}] pelas Evidências da Proposição (Evidência -> Trecho -> Fonte)."""
    saida, vistos = [], set()
    for ev_id in pr.get("evidencias", []):
        ev = _registro("evidencias", ev_id)
        tr = _registro("trechos", ev["trecho"])
        fo = _registro("fontes", tr["fonte"])
        chave = (fo["id"], tr.get("localizador", ""))
        if chave in vistos:
            continue
        vistos.add(chave)
        saida.append({"fo": fo["id"], "localizador": tr.get("localizador", "").split(";")[0],
                      "trecho": tr.get("texto_exato", ""), "ref": fo["referencia"]})
    return saida


def citacao_curta(ref: dict) -> str:
    inst = ref.get("autor") or ref["instituicao"].split(" (")[0]
    return f"({inst}, {ref['ano']})"


def referencia_completa(ref: dict) -> str:
    quem = ref.get("autor") or ref["instituicao"]
    return f"{quem}. *{ref['titulo']}*. {ref['ano']}. Disponível em: {ref['link_permanente']}."


def carregar_programa(caminho: Path) -> dict:
    prog = json.loads(caminho.read_text(encoding="utf-8"))
    prog["_pasta"] = caminho.parent
    prog["_blocos"] = {b["id"]: b for b in prog["blocos"]}
    return prog


def material_do_bloco(bloco: dict) -> list[dict]:
    itens = []
    for pr_id in bloco["proposicoes"]:
        pr = _registro("proposicoes", pr_id)
        fs = fontes_da(pr)
        itens.append({"pr": pr_id, "valor": pr["valor"], "grau": grau_em_palavras(pr),
                      "aviso": bool(pr.get("sustenta_aviso_saude_politica")),
                      "citacao": "; ".join(dict.fromkeys(citacao_curta(f["ref"]) for f in fs)), "fontes": fs})
    return itens


def cmd_material(prog: dict, saida: Path | None = None) -> int:
    pasta = (saida or prog["_pasta"]) / "material"
    pasta.mkdir(parents=True, exist_ok=True)
    for b in prog["blocos"]:
        linhas = [f"# Material do bloco {b['id']}: {b['titulo']} ({b.get('minutos', '?')} min)", "",
                  "Só estas afirmações entram no bloco. O que não está aqui não entra na aula. "
                  "Depois de cada frase com fato, ponha a marca invisível <!-- PR-nnnn -->. "
                  "Use o grau em palavras e a citação como estão.", ""]
        for i in material_do_bloco(b):
            linhas.append(f"- **{i['pr']}** — {i['valor']}")
            linhas.append(f"  - grau: {i['grau']}; citação: {i['citacao']}")
            if i["aviso"]:
                linhas.append("  - sustenta aviso (saúde, norma ou risco): só \"a fonte diz\", sem conselho nem instrução")
        (pasta / f"{b['id']}.md").write_text("\n".join(linhas) + "\n", encoding="utf-8")
    print(f"{VERSAO}: material de {len(prog['blocos'])} bloco(s) em {pasta}")
    return 0


def _frase_antes(texto: str, pos: int) -> str:
    antes = COMENTARIO.sub("", texto[:pos]).rstrip()
    frase = re.split(r"(?<=[.!?])\s+|\n", antes)[-1].strip(" -*")
    palavras = frase.split()
    return " ".join(palavras[:12]) + (" ..." if len(palavras) > 12 else "")


def _ler_bloco(prog: dict, id_: str) -> str:
    arq = prog["_pasta"] / "blocos" / f"{id_}.md"
    if not arq.exists():
        raise FileNotFoundError(f"falta o bloco {arq}")
    return arq.read_text(encoding="utf-8")


def _referencias(textos: list[str]) -> list[str]:
    refs = {}
    for t in textos:
        for pr_id in MARCA.findall(t):
            for f in fontes_da(_registro("proposicoes", pr_id)):
                refs[f["fo"]] = referencia_completa(f["ref"])
    return [refs[k] for k in sorted(refs)]


def cmd_montar(prog: dict, n: int, saida: Path | None = None) -> int:
    montagem = prog.get("montagens", {}).get(str(n))
    if not montagem:
        print(f"erro: o programa não tem montagem para {n} aula(s); há: {sorted(prog.get('montagens', {}))}")
        return 2
    pasta, limite = (saida or prog["_pasta"]), prog.get("minutos_por_aula", 50)
    pasta.mkdir(parents=True, exist_ok=True)
    nota = [f"> Rascunho, não publicado. Nota do educador — {prog['titulo']} em {n} aula(s).", "",
            f"# Nota do educador: {prog['titulo']}", "",
            "Esta nota é só do educador: diz de onde vem cada frase das aulas, os cuidados e onde adaptar. "
            "As aulas não dependem dela para serem dadas.", "",
            "## Ajuste ao público e ao educador", "Público: ______________________________",
            "Educador (formação, lugar, pertencimento, língua; se é quem sabe fazer): ______________________________",
            "O que muda nas aulas: ______________________________", ""]
    avisos = 0
    for k, ids in enumerate(montagem, 1):
        textos = [_ler_bloco(prog, i) for i in ids]
        minutos = sum(prog["_blocos"][i].get("minutos", 0) for i in ids)
        if minutos > limite:
            print(f"aviso: a aula {k} soma {minutos} min, acima de {limite}")
            avisos += 1
        titulo = " · ".join(prog["_blocos"][i]["titulo"] for i in ids)
        corpo = [f"> Rascunho, não publicado.", "", f"# Aula {k} de {n} — {titulo}", "",
                 f"Duração prevista: {minutos} minutos.", ""]
        for i, t in zip(ids, textos):
            corpo += [t.rstrip(), ""]
        refs = _referencias(textos)
        if refs:
            corpo += ["## Referências", ""] + [f"- {r}" for r in refs]
        (pasta / f"aula-{k}.md").write_text("\n".join(corpo) + "\n", encoding="utf-8")
        nota += [f"## Aula {k}: {titulo}", "", "| Frase da aula | Afirmação | Grau | Fonte | Onde |", "|---|---|---|---|---|"]
        for t in textos:
            for m in MARCA.finditer(t):
                pr = _registro("proposicoes", m.group(1))
                for f in fontes_da(pr) or [{"fo": "—", "localizador": "—"}]:
                    nota.append(f"| {_frase_antes(t, m.start()).replace('|', '/')} | {m.group(1)} | "
                                f"{grau_em_palavras(pr)} | {f['fo']} | {f['localizador']} |")
        nota += ["", "**Anotações (à mão ou digitadas):**", ""]
        for _ in range(5):
            nota += ["______________________________________________", ""]
        nota += ["Digite aqui: ", ""]
    nota += ["## Cuidados", ""] + [f"- {c}" for c in prog.get("cuidados", [])]
    nota += ["", "## O que as fontes ainda não dizem", ""] + [f"- {f}" for f in prog.get("faltas", [])]
    c = prog.get("carimbo", {})
    nota += ["", "## Carimbo", f"- **Versão da ficha:** {c.get('versao_ficha', '?')}", f"- **Nível:** {c.get('nivel', '?')}",
             f"- **Faltas:** ver \"O que as fontes ainda não dizem\"", f"- **Data:** {c.get('data', '?')}",
             f"- **Como citar:** {c.get('como_citar', '?')}", "- **Aviso:** não é orientação jurídica nem sanitária.",
             f"- **Montado por:** scripts/montar_programa.py ({VERSAO})"]
    (pasta / "nota-do-educador.md").write_text("\n".join(nota) + "\n", encoding="utf-8")
    kit = prog["_pasta"] / "blocos" / "kit.md"
    if kit.exists():
        t = kit.read_text(encoding="utf-8")
        refs = _referencias([t])
        saida = ["> Rascunho, não publicado.", "", t.rstrip(), ""] + (["## Referências", ""] + [f"- {r}" for r in refs] if refs else [])
        (pasta / "kit-do-professor.md").write_text("\n".join(saida) + "\n", encoding="utf-8")
    for velho in sorted(pasta.glob("aula-*.md")):
        if int(re.search(r"\d+", velho.stem).group()) > n:
            velho.unlink()
    print(f"{VERSAO}: {n} aula(s), nota do educador{' e kit' if kit.exists() else ''} em {pasta}; avisos: {avisos}")
    return 0


# números que são da própria aula, não fato: minutos, faixas de roteiro, itens numerados, "aula 2", códigos P-1
NAO_FATO = re.compile(r"\d+\s*(?:[-–a]\s*\d+\s*)?min(?:utos)?\b|^\s*\|?\s*\d+\s*[-–]\s*\d+\s*\||^\s*\d+[.)]\s|"
                      r"[Aa]ulas?\s+\d+|\bP-\d+\b|\b\d+\s+aulas?\b", re.M)
NUMERO = re.compile(r"\b\d+(?:[.,]\d+)?\b")
NOME = re.compile(r"[A-ZÁÉÍÓÚÂÊÔÃÕÇ][a-záéíóúâêôãõç]+(?:\s+(?:d[aeo]s?\s+)?[A-ZÁÉÍÓÚÂÊÔÃÕÇ][a-záéíóúâêôãõç]+)*")


def nomes_proprios(texto: str) -> set[str]:
    """Palavras com maiúscula que não abrem frase, linha ou item (heurística: o que sobra é provável nome)."""
    achados = set()
    for m in NOME.finditer(texto):
        antes = texto[:m.start()].rstrip(" \t*_\"'(“")
        if not antes or antes[-1] in ".!?:\n|#->":
            continue
        achados.add(m.group(0))
    return achados


def _sem_acento(s: str) -> str:
    import unicodedata
    return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")


def conferir_bloco(bloco: dict, texto: str, permitidos: set[str]) -> list[str]:
    problemas = []
    for pr_id in MARCA.findall(texto):
        if pr_id not in permitidos:
            problemas.append(f"marca {pr_id} fora do material do bloco")
    itens = [i for i in material_do_bloco(bloco)] if bloco else []
    corpus = _sem_acento(" ".join([i["valor"] + " " + i["citacao"] + " " + " ".join(
        f["trecho"] + " " + f["ref"]["titulo"] + " " + f["ref"]["instituicao"] for f in i["fontes"]) for i in itens]))
    limpo = NAO_FATO.sub(" ", COMENTARIO.sub(" ", texto))
    for n in sorted(set(NUMERO.findall(limpo))):
        if _sem_acento(n) not in corpus:
            problemas.append(f"número ou data fora do material: {n}")
    for nome in sorted(nomes_proprios(limpo)):
        if _sem_acento(nome) not in corpus:
            problemas.append(f"nome próprio fora do material: {nome}")
    for linha, tipo, trecho in achar(texto):
        problemas.append(f"dado pessoal ({tipo}) na linha {linha}: {trecho}")
    return problemas


def cmd_conferir(prog: dict) -> int:
    todos, total = set(), 0
    for b in prog["blocos"]:
        for pr_id in b["proposicoes"]:
            try:
                _registro("proposicoes", pr_id)
                todos.add(pr_id)
            except FileNotFoundError as e:
                print(f"REPROVA  {b['id']}: {e}")
                total += 1
    for b in prog["blocos"]:
        try:
            texto = _ler_bloco(prog, b["id"])
        except FileNotFoundError as e:
            print(f"REPROVA  {b['id']}: {e}")
            total += 1
            continue
        probs = conferir_bloco(b, texto, set(b["proposicoes"]))
        total += len(probs)
        print(("REPROVA  " if probs else "PASSA    ") + b["id"] + "".join(f"\n  - {p}" for p in probs))
    kit = prog["_pasta"] / "blocos" / "kit.md"
    if kit.exists():
        t = kit.read_text(encoding="utf-8")
        probs = [f"marca {p} fora do programa" for p in MARCA.findall(t) if p not in todos]
        probs += [f"dado pessoal ({tp}) na linha {ln}: {tr}" for ln, tp, tr in achar(t)]
        total += len(probs)
        print(("REPROVA  " if probs else "PASSA    ") + "kit" + "".join(f"\n  - {p}" for p in probs))
    print(f"{VERSAO}: {'PASSA' if not total else f'REPROVA ({total} ponto(s) a corrigir)'}")
    return 0 if not total else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("acao", choices=["material", "montar", "conferir"])
    ap.add_argument("programa", type=Path)
    ap.add_argument("--aulas", type=int)
    ap.add_argument("--saida", type=Path, help="pasta de saída (padrão: a pasta do programa)")
    a = ap.parse_args()
    caminho = a.programa if a.programa.is_absolute() else RAIZ / a.programa
    try:
        prog = carregar_programa(caminho)
        saida = (a.saida if a.saida.is_absolute() else RAIZ / a.saida) if a.saida else None
        if a.acao == "material":
            return cmd_material(prog, saida)
        if a.acao == "montar":
            if not a.aulas:
                print("erro: montar pede --aulas N")
                return 2
            return cmd_montar(prog, a.aulas, saida)
        return cmd_conferir(prog)
    except (FileNotFoundError, KeyError, json.JSONDecodeError) as e:
        print(f"erro: {type(e).__name__}: {e}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
