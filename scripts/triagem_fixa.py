"""Triagem fixa do Jurídico para os casos óbvios (bloco 3; Fundação l. 695; D-020; D-042).

Para cada registro (Entrada, Fonte, Trecho, Evidência ou outro com campos de proteção), aplica
as regras de esquemas/triagem-fixa.json (versão da regra no próprio arquivo), para o ato pedido
(`--ato`: "ler", o padrão, que é ler, localizar, linkar e citar trecho curto com autor e origem;
"copiar", cópia além da citação; "publicar"). Cada caso só vale para os atos que lista:
  - cópia além da citação (ato copiar, sem licença registrada; barra agora);
  - licença ausente (atos copiar e publicar; barra só a publicação);
  - pessoa identificável e dado pessoal (procurar_dado_pessoal.achar nos textos; ou pessoa por
    código sem referência de consentimento, fora a pessoa com papel de autor citado; barra agora);
  - dado sensível (protecao.dado_sensivel = true; barra agora);
  - possível conhecimento tradicional (palavras da regra; restrição comunitária conhecida; barra
    só a publicação, com a nota do art. 9º da Lei 13.123);
  - substância controlada (substâncias e plantas da Lista E) e dúvida de substância (ayahuasca,
    jurema): barram só a publicação, e agora quando o registro traz também o modo de obter ou de
    preparar (Lei 11.343, art. 33);
  - criança ou adolescente (protecao.crianca_ou_adolescente = true; palavras da regra; barra agora).
Ler, localizar, linkar e citar trecho curto de informação pública e acessível não gera Falta (regra
de Vicente, D-042, não parecer de licitude): sem caso, a saída diz "sem Falta pela regra".
Cada caso vira uma Falta jurídica válida no falta.schema.json, com a norma citada (referência,
trecho literal, URL e nível), o vale_para e o caminho de liberação (o guia da habilidade
guia-de-liberacao, estado "não iniciado"). Cria Faltas e nunca autoriza. Norma sem trecho, sem URL
ou "não conferido" não sai: o script recusa (código 1).

Uso:
    python scripts/triagem_fixa.py <registro.json> [...] [--ato ler|copiar|publicar] [--raiz <pasta>]
        [--normas <arquivo>] [--gravar] [--portao]
--gravar grava as Faltas em <raiz>/acervo/faltas/ com IDs da faixa da conversa.
--portao: o portão do ato (K-124): código 1 se alguma Falta barra o ato agora (vale_para "agora"; no
ato publicar, qualquer Falta).
Código 0 = triagem feita (com ou sem Faltas, todas válidas) e, com --portao, nada barra o ato;
1 = regra ou Falta inválida, ou, com --portao, ato barrado.
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


def palavras_achadas(lista: list[str], texto: str) -> list[str]:
    return sorted({p for p in lista if casa(p, texto)})


def casos_do_registro(r: dict, regras: dict, ato: str = "ler") -> list[tuple[str, str, str]]:
    """Lista (caso, por que, vale_para) para um registro, no ato pedido."""
    c = {k: v for k, v in regras["casos"].items() if ato in v.get("atos", ["ler", "copiar", "publicar"])}
    prot = {k: ("" if v is None else v) for k, v in (r.get("protecao") or {}).items()}  # null vale como ausente
    corpo = [(cam, t) for cam, t in textos(r) if not cam.startswith("/origem_registro")]
    texto = sem_acento(" ".join(t for _, t in corpo))
    achou = []
    licenca = str(prot.get("licenca", "")).strip()
    if "copia_alem_da_citacao" in c and licenca in c["copia_alem_da_citacao"]["valores_sem_licenca"]:
        achou.append(("copia_alem_da_citacao", f"ato {ato}: cópia além da citação, licença: {licenca or 'ausente'}",
                      c["copia_alem_da_citacao"]["vale_para"]))
    if "licenca_ausente" in c and licenca in c["licenca_ausente"]["valores_sem_licenca"]:
        achou.append(("licenca_ausente", f"ato {ato}: licença: {licenca or 'ausente'}", c["licenca_ausente"]["vale_para"]))
    if "dado_pessoal" in c:
        fora = c["dado_pessoal"].get("papeis_fora", [])
        pessoas = [p for p in (r.get("pessoa"), (r.get("voz") or {}).get("pessoa")) if p]
        pessoas = [p for p in pessoas
                   if not (isinstance(p, dict) and any(casa(x, sem_acento(str(p.get("papel", "")))) for x in fora))]
        pessoais = sorted({tipo for _, t in corpo for _, tipo, _ in achar(t)})
        if pessoais:
            achou.append(("dado_pessoal", f"dado pessoal no registro ({', '.join(pessoais)}; o valor não se repete aqui)",
                          c["dado_pessoal"]["vale_para"]))
        elif pessoas and str(prot.get("consentimento", "")).strip() in c["dado_pessoal"]["consentimento_ausente"]:
            achou.append(("dado_pessoal", "pessoa por código sem referência ao termo de consentimento",
                          c["dado_pessoal"]["vale_para"]))
    if "dado_sensivel" in c and prot.get("dado_sensivel") is True:
        achou.append(("dado_sensivel", "protecao.dado_sensivel = true", c["dado_sensivel"]["vale_para"]))
    for caso in ("conhecimento_tradicional", "substancia_controlada", "substancia_duvida", "crianca_ou_adolescente"):
        if caso not in c:
            continue
        palavras = palavras_achadas(c[caso]["palavras"], texto)
        motivo = []
        if palavras:
            motivo.append(f"palavras da regra: {', '.join(palavras)}")
        if caso == "conhecimento_tradicional" and str(prot.get("restricao_comunitaria", "nenhuma conhecida")).strip() not in ("", "nenhuma conhecida"):
            motivo.append("restrição comunitária conhecida")
        if caso == "crianca_ou_adolescente" and prot.get("crianca_ou_adolescente") is True:
            motivo.append("protecao.crianca_ou_adolescente = true")
        if not motivo:
            continue
        vale = c[caso]["vale_para"]
        if palavras and (modo := palavras_achadas(c[caso].get("palavras_modo", []), texto)):
            vale = c[caso].get("vale_para_com_modo", vale)
            motivo.append(f"modo de obter ou de preparar: {', '.join(modo)}")
        achou.append((caso, "; ".join(motivo), vale))
    return achou


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("registros", nargs="+", type=Path)
    ap.add_argument("--raiz", type=Path, default=RAIZ)
    ap.add_argument("--normas", type=Path, default=ESQUEMAS / "triagem-fixa.json")
    ap.add_argument("--ato", choices=("ler", "copiar", "publicar"), default="ler")
    ap.add_argument("--gravar", action="store_true")
    ap.add_argument("--portao", action="store_true",
                    help="código 1 se alguma Falta barra o ato agora (no ato publicar, qualquer Falta)")
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
        for caso, motivo, vale in casos_do_registro(r, regras, a.ato):
            c = regras["casos"][caso]
            fid = proximo_id("F", ids)
            ids.add(fid)
            f = {"id": fid, "tipo": "impedimento_juridico", "subtipo_juridico": c["subtipo"],
                 "o_que_falta": c["o_que_falta"],
                 "por_que": f"{motivo}. Precaução pela norma citada; apoio: {'; '.join(c.get('apoio', [])) or 'nenhum'}. "
                            + (f"{c['nota']} " if c.get("nota") else "")
                            + f"Regra {versao}, ato {a.ato}; o script não autoriza (D-020).",
                 "vale_para": vale,
                 "onde_aparece": [onde],
                 "norma": {k: c["norma"][k] for k in ("referencia", "trecho", "url", "nivel")},
                 "caminho_de_liberacao": {"guia": c["guia"], "estado": "não iniciado"},
                 "criada_por": f"scripts/triagem_fixa.py ({versao})", "data": date.today().isoformat()}
            erros = validar_objeto(f, esq)
            if erros:
                invalidas += 1
                print(f"FALTA INVÁLIDA ({caso}): {'; '.join(erros)}")
            faltas.append(f)
            print(f"{onde}: {caso} → {fid} ({c['subtipo']}; vale para {vale}; {c['norma']['referencia']})")
    if a.gravar and not invalidas:
        pasta = raiz / "acervo" / "faltas"
        pasta.mkdir(parents=True, exist_ok=True)
        for f in faltas:
            (pasta / f"{f['id']}.json").write_text(json.dumps(f, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(faltas, ensure_ascii=False, indent=2))
    if not faltas:
        print(f"sem Falta pela regra {versao} (ato: {a.ato}; D-042)")
    print(f"{versao}: {len(a.registros)} registro(s), {len(faltas)} Falta(s) jurídica(s)"
          f"{'' if not invalidas else f', {invalidas} inválida(s)'}")
    if invalidas:
        return 1
    if a.portao:
        barra = [f for f in faltas if f["vale_para"] == "agora" or a.ato == "publicar"]
        if barra:
            print(f"BARRA: o ato {a.ato} fica parado pelas Faltas {', '.join(f['id'] for f in barra)} "
                  "(a Falta é dita e o caminho de liberação, apontado; D-020, D-025)")
            return 1
        print(f"PORTÃO: nenhuma Falta barra o ato {a.ato} agora"
              + (f"; {len(faltas)} Falta(s) só para a publicação, ditas" if faltas else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
