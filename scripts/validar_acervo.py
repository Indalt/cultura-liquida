"""Valida o acervo inteiro: os esquemas e as ligações (bloco 3; l. 707). Regra acervo-0.2 (0.1 + achados A-003 a A-005, A-012 e A-014 do auditor no K-105).

Confere, em ambientes/, entrada/ e acervo/ (pasta ausente não é erro; l. 723):
  1. cada registro no esquema do seu prefixo (esquemas/<tipo>.schema.json);
  2. IDs: um ID num só arquivo (colisão reprova; valor numeracao_id); no acervo real,
     nenhum ID da faixa "exemplos de esquema";
  3. toda referência a outro ID aponta para um registro que existe (fora EX-, que é log);
  4. Evidência → Trecho → Fonte; a Evidência aponta para uma Proposição que a lista;
  5. Proposição com ao menos uma Evidência;
  6. Termo atestado só com abonação localizada (Evidência cujo Trecho está "localizado");
     forma de OCR ou grafia truncada nunca é variante, só forma de busca;
  7. W (Compreensão local) só com a voz de quem pratica, pelo papel da Pessoa
     (PAPEIS_DE_QUEM_PRATICA) ou pelo papel dito na voz da Evidência;
  8. nenhum dado pessoal (procurar_dado_pessoal.achar) nos registros;
  9. nas fichas (acervo/fichas/*.md), toda frase factual com a marcação de Proposição
     ([PR-nnnn] ao fim da frase; valor marcacao_frase_proposicao), apontando para uma
     Proposição que existe. Ficam fora: títulos, comentários e as seções de título exato
     Fontes, Como citar e Faltas. O formato da ficha se fecha no bloco 8 (montar-ficha);
  10. deriva_de sem auto-referência e sem ciclo;
  11. as pegadas (ambientes/pegadas/RC-nnnn.jsonl; D-045): cada linha no esquema da pegada, num
      Recorte que existe, sem dado pessoal; o EN-nnnn que só uma pegada guarda conta como registro
      existente nas referências (o item fora do escopo pela regra não se apaga).
  12. (acervo-0.4, K-111) a forma que nomeia mais de um Termo ativo é termo ambíguo (D-039): cada Termo
      que a usa o marca (insumos 26 e 88);
  13. (acervo-0.4, K-111) a Evidência ativa marcada por aviso, saúde ou política leva a marca à
      Proposição que ela sustenta (insumo 72, A3);
  14. (acervo-0.4, K-111) a camada Educação (acervo/fichas/educacao/*.md; insumo 80): cada item de
      lista das seções de conteúdo termina com a marca da Proposição; cada habilidade da BNCC com o
      código, o texto literal entre aspas e a página do PDF oficial (checar_educacao).
A Falta sem valor e a Falta jurídica com norma e caminho são do falta.schema.json (item 1).

Uso:
    python scripts/validar_acervo.py [--raiz <pasta>]
Código 0 = acervo válido; 1 = algum erro (lista arquivo: problema).
Gancho de pre-commit: .githooks/pre-commit (git config core.hooksPath .githooks).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _acervo import ESQUEMA_POR_PREFIXO, RE_ID, carregar_acervo, faixas, prefixo, textos  # noqa: E402
from _comum import RAIZ, carregar_esquema, carregar_valores, validar_objeto  # noqa: E402
from procurar_dado_pessoal import achar  # noqa: E402
from guarda import PASTA as PASTA_PEGADAS, ler as ler_pegadas  # noqa: E402

VERSAO = "acervo-0.4"
PAPEIS_DE_QUEM_PRATICA = {"detentor ou mestre", "quem ensinou", "comunidade, coletivo ou sujeito de direitos"}
RE_OCR = re.compile(r"\bocr\b|truncad|erro de (digitação|leitura|reconhecimento|transcrição|digitalização)", re.I)
RE_REF = re.compile(r"^[A-Z]{1,2}-[0-9]{4,}$")
SECOES_FORA = ("fontes", "como citar", "faltas")


def _ativo(r: dict) -> bool:
    return not r.get("retirado")


def checar_termo(t: dict) -> list[str]:
    """A regra das variantes, também usada por gerar_termo.py."""
    erros = []
    busca = {f.casefold() for f in t.get("formas_de_busca", [])}
    for v in t.get("variantes", []):
        if RE_OCR.search(v.get("tipo_variacao", "")):
            erros.append(f"variante {v['forma']!r} é forma de OCR ou truncada ({v['tipo_variacao']}): vai só em formas_de_busca")
        elif v.get("forma", "").casefold() in busca:
            erros.append(f"variante {v['forma']!r} também está em formas_de_busca: forma de busca não é variante")
    return erros


def checar_ambiguos(indice: dict, rel) -> list[str]:
    """Item 12 (acervo-0.4; K-111, insumos 26 e 88; D-039): a forma que nomeia mais de um Termo ativo
    (designação ou variante) é termo ambíguo, e cada Termo que a usa o diz: na variante, no
    tipo_variacao; na designação, na nota."""
    usos: dict[str, list[tuple[str, str]]] = {}
    for id_, t in indice.items():
        if prefixo(id_) != "TE" or not _ativo(t):
            continue
        for d in t.get("designacoes", []):
            usos.setdefault(d.get("forma", "").casefold(), []).append((id_, t.get("nota", "")))
        for v in t.get("variantes", []):
            usos.setdefault(v.get("forma", "").casefold(), []).append((id_, v.get("tipo_variacao", "")))
    erros = []
    for forma, lista in usos.items():
        if len({i for i, _ in lista}) < 2:
            continue
        outros = sorted({i for i, _ in lista})
        for i, marca in lista:
            if "ambígu" not in marca.casefold():
                erros.append(f"{rel(i)}: a forma {forma!r} nomeia também {', '.join(o for o in outros if o != i)}: "
                             "termo ambíguo (D-039) sem a marca (na variante, no tipo_variacao; na designação, na nota)")
    return erros


RE_BNCC = re.compile(r"^EM13[A-Z]{2,4}[0-9]{2,3}$")
URL_BNCC = "https://www.gov.br/mec/pt-br/cne/arquivos/bncc_ensino_medio.pdf"


def checar_educacao(arq: Path, indice: dict, padrao: str) -> list[str]:
    """Item 14 (acervo-0.4; K-111, insumo 80; regra educacao-0.1): a camada Educação
    (acervo/fichas/educacao/*.md). Nas seções de conteúdo (as de título numerado que não são de
    público, de habilidades, de Faltas nem de Fontes), cada item de lista sobre a CLB termina com a marca
    de uma Proposição que existe; a pergunta para a aula fica fora. Na seção das habilidades da BNCC,
    cada linha da tabela traz o código (EM13...), o texto literal entre aspas e a página do PDF (número),
    e a seção cita o PDF oficial do MEC."""
    erros, secao, tem_url = [], "", False
    fim = re.compile(f"({padrao})[.!?]?$")
    linhas = arq.read_text(encoding="utf-8").splitlines()
    for n, linha in enumerate(linhas, 1):
        s = linha.strip()
        if s.startswith("## "):
            secao = s[3:].casefold()
            continue
        if "bncc" in secao and "habilidade" in secao:
            tem_url = tem_url or URL_BNCC in s
            cel = [c.strip() for c in s.strip("|").split("|")] if s.startswith("|") else []
            if len(cel) >= 3 and cel[0] != "Código" and not re.fullmatch(r"[\s:-]*", cel[0]):
                if not RE_BNCC.match(cel[0]):
                    erros.append(f"l. {n}: código da BNCC fora do formato EM13...: {cel[0]!r}")
                if not (cel[1].startswith('"') and cel[1].rstrip(".").endswith('"')):
                    erros.append(f"l. {n}: habilidade {cel[0]} sem o texto literal entre aspas")
                if not re.fullmatch(r"(p\. ?)?[0-9]+", cel[2]):
                    erros.append(f"l. {n}: habilidade {cel[0]} sem a página do PDF (número): {cel[2]!r}")
            continue
        conteudo = re.match(r"\d+\.", secao) and not any(x in secao for x in ("para quem", "falta", "fonte"))
        if not conteudo or not s.startswith("- ") or s[2:].startswith("Pergunta para a aula"):
            continue
        for pr in re.findall(r"PR-[0-9]{4,}", s):
            if pr not in indice:
                erros.append(f"l. {n}: marca {pr} aponta para Proposição que não existe")
        if not fim.search(s):
            erros.append(f"l. {n}: item sobre a CLB sem a marca da Proposição ao fim: {s[:80]!r}")
    if any("bncc" in l.casefold() and "habilidade" in l.casefold() for l in linhas if l.startswith("## ")) and not tem_url:
        erros.append(f"seção das habilidades da BNCC sem o PDF oficial do MEC ({URL_BNCC})")
    return erros


def checar_ficha(arq: Path, indice: dict, padrao: str) -> list[str]:
    erros, secao, em_comentario = [], "", False
    fim = re.compile(f"({padrao})[.!?]?$")  # a marca ao fim da frase, antes ou depois do ponto
    for n, linha in enumerate(arq.read_text(encoding="utf-8").splitlines(), 1):
        s = linha.strip()
        if em_comentario or "<!--" in s:
            antes, _, resto = s.partition("<!--") if not em_comentario else ("", "", s)
            em_comentario = "-->" not in resto
            s = (antes + " " + (resto.split("-->", 1)[1] if "-->" in resto else "")).strip()
            if not s:
                continue
        if s.startswith("#"):
            secao = s.lstrip("#").strip().casefold()
            continue
        if not s or secao in SECOES_FORA or re.fullmatch(r"\|?[\s:|-]+\|?", s):
            continue
        s = re.sub(r"^([-*>]|\d+\.)\s+", "", s)
        for pr in re.findall(r"PR-[0-9]{4,}", s):
            if pr not in indice:
                erros.append(f"l. {n}: {pr} não existe no acervo")
        for frase in re.split(r"(?<=[.!?])\s+(?!\[PR-)", s):
            if frase.strip() and not fim.search(frase.strip()):
                erros.append(f"l. {n}: frase sem marcação de Proposição: {frase[:80]!r}")
    return erros


def checar_deriva(indice: dict, rel) -> list[str]:
    """deriva_de sem auto-referência e sem ciclo (busca em profundidade)."""
    erros, cor = [], {}
    viz = {i: [d for d in r.get("deriva_de", []) if d in indice] for i, r in indice.items() if prefixo(i) == "FO"}

    def visita(i, pilha):
        cor[i] = 1
        for d in viz.get(i, []):
            if d == i:
                erros.append(f"{rel(i)}: deriva de si mesma")
            elif cor.get(d) == 1:
                erros.append(f"{rel(i)}: ciclo em deriva_de ({' → '.join(pilha[pilha.index(d):] + [i, d])})")
            elif d not in cor:
                visita(d, pilha + [i])
        cor[i] = 2

    for i in sorted(viz):
        if i not in cor:
            visita(i, [])
    return erros


def checar_pegadas(raiz: Path, indice: dict) -> tuple[set[str], list[str]]:
    """Item 11: as linhas das pegadas e os EN-nnnn que elas guardam."""
    pasta, ens, erros = raiz / PASTA_PEGADAS, set(), []
    if not pasta.exists():
        return ens, erros
    esq = carregar_esquema("pegada")
    for arq in sorted(pasta.glob("*.jsonl")):
        rel = arq.relative_to(raiz)
        if arq.stem not in indice:
            erros.append(f"{rel}: pegadas de um Recorte que não existe ({arq.stem})")
        try:
            linhas = ler_pegadas(arq)
        except ValueError as e:
            erros.append(f"{rel}: linha ilegível ({e})")
            continue
        for n, p in enumerate(linhas, 1):
            erros += [f"{rel}:{n}: {e}" for e in validar_objeto(p, esq)]
            for cam, txt in textos(p):
                for _, tipo, _s in achar(txt):
                    erros.append(f"{rel}:{n}: {cam}: dado pessoal ({tipo})")
            if p.get("entrada"):
                ens.add(p["entrada"])
    return ens, erros


def validar(raiz: Path) -> list[str]:
    indice, onde, erros = carregar_acervo(raiz)
    rel = lambda i: str(onde[i][0].relative_to(raiz))  # noqa: E731
    exemplos = faixas()["exemplos de esquema"]
    real = raiz.resolve() == RAIZ.resolve()
    esquemas: dict[str, dict] = {}
    ens_pegada, erros_peg = checar_pegadas(raiz, indice)
    erros += erros_peg
    for id_, arqs in onde.items():
        if len(arqs) > 1:
            erros.append(f"colisão de ID {id_}: {', '.join(str(a.relative_to(raiz)) for a in arqs)}")
    for id_, r in indice.items():
        p = prefixo(id_)
        if p not in ESQUEMA_POR_PREFIXO:
            erros.append(f"{rel(id_)}: prefixo de ID desconhecido ({id_})")
            continue
        m = RE_ID.match(id_)
        if real and exemplos[0] <= int(m.group(2)) <= exemplos[1]:
            erros.append(f"{rel(id_)}: {id_} é da faixa de exemplos de esquema; nenhum registro real a usa")
        esq = esquemas.setdefault(p, carregar_esquema(ESQUEMA_POR_PREFIXO[p]))
        erros += [f"{rel(id_)}: {e}" for e in validar_objeto(r, esq)]
        for cam, txt in textos(r):
            if cam.endswith("/nota"):
                continue
            if RE_REF.match(txt) and txt != id_ and not txt.startswith("EX-") and txt not in indice and txt not in ens_pegada:
                erros.append(f"{rel(id_)}: {cam} aponta para {txt}, que não existe")
            for _, tipo, _s in achar(txt):
                erros.append(f"{rel(id_)}: {cam}: dado pessoal ({tipo})")
        if not _ativo(r):
            continue
        if p == "EV":
            tr = indice.get(r.get("trecho"), {})
            if tr and prefixo(tr.get("fonte", "")) != "FO":
                erros.append(f"{rel(id_)}: o Trecho {r['trecho']} não aponta para uma Fonte")
            pr = indice.get(r.get("proposicao"))
            if pr and id_ not in pr.get("evidencias", []):
                erros.append(f"{rel(id_)}: a Proposição {r['proposicao']} não lista esta Evidência")
        elif p == "PR" and not r.get("evidencias"):
            erros.append(f"{rel(id_)}: Proposição sem Evidência")
        elif p == "PR" and not r.get("sustenta_aviso_saude_politica"):
            # item 13 (acervo-0.4; K-111, insumo 72, achado A3 do K-109): a marca de aviso, saúde ou política
            # de uma Evidência ativa vale para a Proposição que ela sustenta
            marcadas = [ev for ev in r["evidencias"] if _ativo(indice.get(ev, {})) and indice.get(ev, {}).get("sustenta_aviso_saude_politica")]
            if marcadas:
                erros.append(f"{rel(id_)}: Evidência marcada por aviso, saúde ou política ({', '.join(marcadas)}) e a Proposição sem a marca")
        elif p == "TE":
            erros += [f"{rel(id_)}: {e}" for e in checar_termo(r)]
            if r.get("estado") == "atestado":
                loc = [ev for ev in r.get("abonacoes", [])
                       if indice.get(indice.get(ev, {}).get("trecho"), {}).get("estado") == "localizado"]
                if not loc:
                    erros.append(f"{rel(id_)}: Termo atestado sem abonação localizada")
        elif p == "CP":
            def pratica(ev: dict) -> bool:
                voz = ev.get("voz", {})
                papeis = set(indice.get(voz.get("pessoa"), {}).get("papeis", [])) | {voz.get("papel")}
                return bool(papeis & PAPEIS_DE_QUEM_PRATICA)
            if not any(pratica(indice.get(ev, {})) for ev in r.get("evidencias", [])):
                erros.append(f"{rel(id_)}: W sem a voz de quem pratica (papéis: {', '.join(sorted(PAPEIS_DE_QUEM_PRATICA))})")
    erros += checar_deriva(indice, rel)
    erros += checar_ambiguos(indice, rel)
    fichas = raiz / "acervo" / "fichas"
    if fichas.exists():
        padrao = carregar_valores()["valores"]["marcacao_frase_proposicao"]["valor"]["padrao"]
        for arq in sorted(fichas.glob("*.md")):
            erros += [f"{arq.relative_to(raiz)}: {e}" for e in checar_ficha(arq, indice, padrao)]
        for arq in sorted((fichas / "educacao").glob("*.md")):
            erros += [f"{arq.relative_to(raiz)}: {e}" for e in checar_educacao(arq, indice, padrao)]
    return erros


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--raiz", type=Path, default=RAIZ)
    a = ap.parse_args()
    raiz = a.raiz if a.raiz.is_absolute() else RAIZ / a.raiz
    erros = validar(raiz)
    for e in erros:
        print("ERRO", e)
    n = len(carregar_acervo(raiz)[0])
    print(f"{VERSAO}: {n} registros; {'válido' if not erros else f'{len(erros)} erro(s)'}")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
