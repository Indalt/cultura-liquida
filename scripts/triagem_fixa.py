"""Triagem fixa do Jurídico para os casos óbvios (bloco 3; Fundação l. 695; D-020).

Para cada registro (Entrada, Fonte, Trecho, Evidência ou outro com campos de proteção), aplica
as regras de esquemas/triagem-fixa.json (versão da regra no próprio arquivo):
  - licença ausente (protecao.licenca ausente, vazia ou "não conferido");
  - pessoa identificável e dado pessoal (procurar_dado_pessoal.achar nos textos; ou pessoa
    por código sem referência de consentimento);
  - dado sensível (protecao.dado_sensivel = true);
  - possível conhecimento tradicional (palavras da regra; restrição comunitária conhecida);
  - substância controlada (palavras da regra);
  - criança ou adolescente (protecao.crianca_ou_adolescente = true; palavras da regra).
Cada caso vira uma Falta jurídica válida no falta.schema.json, com a norma citada (referência,
trecho literal, URL e nível, do lote C5) e o caminho de liberação (o guia da habilidade
guia-de-liberacao, estado "não iniciado"). Cria Faltas e nunca autoriza. Norma sem trecho,
sem URL ou "não conferido" não sai: o script recusa (código 1).

Uso:
    python scripts/triagem_fixa.py <registro.json> [...] [--raiz <pasta>] [--normas <arquivo>] [--gravar]
--gravar grava as Faltas em <raiz>/acervo/faltas/ com IDs da faixa da conversa.
Código 0 = triagem feita (com ou sem Faltas, todas válidas); 1 = regra ou Falta inválida.
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
from _acervo import carregar_acervo, id_do_registro, proximo_id, textos  # noqa: E402
from _comum import ESQUEMAS, RAIZ, carregar_esquema, carregar_json, validar_objeto  # noqa: E402
from procurar_dado_pessoal import achar  # noqa: E402


def sem_acento(t: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", t.casefold()) if unicodedata.category(c) != "Mn")


def casa(palavra: str, texto: str) -> bool:
    """Palavra inteira; com '*' no fim, radical (ex.: 'raizeir*' casa raizeiro e raizeira)."""
    radical = palavra.endswith("*")
    p = re.escape(sem_acento(palavra.rstrip("*")))
    return re.search(r"\b" + p + ("" if radical else r"\b"), texto) is not None


def norma_ok(n: dict) -> list[str]:
    falta = [k for k in ("referencia", "trecho", "url", "nivel") if not n.get(k)]
    if n.get("nivel") == "não conferido":
        falta.append("nível 'não conferido'")
    return falta


def casos_do_registro(r: dict, regras: dict) -> list[tuple[str, str]]:
    """Lista (caso, por que) para um registro."""
    c = regras["casos"]
    prot = {k: ("" if v is None else v) for k, v in (r.get("protecao") or {}).items()}  # null vale como ausente
    corpo = [(cam, t) for cam, t in textos(r) if not cam.startswith("/origem_registro")]
    texto = sem_acento(" ".join(t for _, t in corpo))
    achou = []
    if prot.get("licenca", "").strip() in c["licenca_ausente"]["valores_sem_licenca"]:
        achou.append(("licenca_ausente", f"licença: {prot.get('licenca') or 'ausente'}"))
    pessoais = sorted({tipo for _, t in corpo for _, tipo, _ in achar(t)})
    tem_pessoa = bool(r.get("pessoa") or (r.get("voz") or {}).get("pessoa"))
    if pessoais:
        achou.append(("dado_pessoal", f"dado pessoal no registro ({', '.join(pessoais)}; o valor não se repete aqui)"))
    elif tem_pessoa and prot.get("consentimento", "").strip() in c["dado_pessoal"]["consentimento_ausente"]:
        achou.append(("dado_pessoal", "pessoa por código sem referência ao termo de consentimento"))
    if prot.get("dado_sensivel") is True:
        achou.append(("dado_sensivel", "protecao.dado_sensivel = true"))
    for caso in ("conhecimento_tradicional", "substancia_controlada", "crianca_ou_adolescente"):
        palavras = sorted({p for p in c[caso]["palavras"] if casa(p, texto)})
        motivo = []
        if palavras:
            motivo.append(f"palavras da regra: {', '.join(palavras)}")
        if caso == "conhecimento_tradicional" and prot.get("restricao_comunitaria", "nenhuma conhecida").strip() not in ("", "nenhuma conhecida"):
            motivo.append("restrição comunitária conhecida")
        if caso == "crianca_ou_adolescente" and prot.get("crianca_ou_adolescente") is True:
            motivo.append("protecao.crianca_ou_adolescente = true")
        if motivo:
            achou.append((caso, "; ".join(motivo)))
    return achou


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("registros", nargs="+", type=Path)
    ap.add_argument("--raiz", type=Path, default=RAIZ)
    ap.add_argument("--normas", type=Path, default=ESQUEMAS / "triagem-fixa.json")
    ap.add_argument("--gravar", action="store_true")
    a = ap.parse_args()
    raiz = a.raiz if a.raiz.is_absolute() else RAIZ / a.raiz
    regras = carregar_json(a.normas)
    versao = regras["versao_regra"]
    ruins = {k: norma_ok(v["norma"]) for k, v in regras["casos"].items()}
    ruins = {k: v for k, v in ruins.items() if v}
    if ruins:
        for k, v in ruins.items():
            print(f"RECUSADO: o caso {k} tem norma incompleta ({', '.join(v)}); Falta jurídica sem norma não sai")
        return 1
    indice, _, _ = carregar_acervo(raiz)
    ids = set(indice)
    esq = carregar_esquema("falta")
    faltas, invalidas = [], 0
    for arq in a.registros:
        r = carregar_json(arq if arq.is_absolute() else RAIZ / arq)
        onde = id_do_registro(r) or str(arq)
        for caso, motivo in casos_do_registro(r, regras):
            c = regras["casos"][caso]
            fid = proximo_id("F", ids)
            ids.add(fid)
            f = {"id": fid, "tipo": "impedimento_juridico", "subtipo_juridico": c["subtipo"],
                 "o_que_falta": c["o_que_falta"],
                 "por_que": f"{motivo}. Precaução pela norma citada; apoio: {'; '.join(c.get('apoio', [])) or 'nenhum'}. "
                            f"Regra {versao}; o script não autoriza (D-020).",
                 "onde_aparece": [onde],
                 "norma": {k: c["norma"][k] for k in ("referencia", "trecho", "url", "nivel")},
                 "caminho_de_liberacao": {"guia": c["guia"], "estado": "não iniciado"},
                 "criada_por": f"scripts/triagem_fixa.py ({versao})", "data": date.today().isoformat()}
            erros = validar_objeto(f, esq)
            if erros:
                invalidas += 1
                print(f"FALTA INVÁLIDA ({caso}): {'; '.join(erros)}")
            faltas.append(f)
            print(f"{onde}: {caso} → {fid} ({c['subtipo']}; {c['norma']['referencia']})")
    if a.gravar and not invalidas:
        pasta = raiz / "acervo" / "faltas"
        pasta.mkdir(parents=True, exist_ok=True)
        for f in faltas:
            (pasta / f"{f['id']}.json").write_text(json.dumps(f, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(faltas, ensure_ascii=False, indent=2))
    print(f"{versao}: {len(a.registros)} registro(s), {len(faltas)} Falta(s) jurídica(s)"
          f"{'' if not invalidas else f', {invalidas} inválida(s)'}")
    return 1 if invalidas else 0


if __name__ == "__main__":
    sys.exit(main())
