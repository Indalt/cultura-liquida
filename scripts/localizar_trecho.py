"""Localiza um trecho na fonte, pela regra versionada (bloco 3; l. 130, 598; valor
normalizacao_e_limiar de esquemas/valores-provisorios.json).

Lê a fonte (arquivo local, URL ou a captura datada do Wayback) em memória ou na pasta
temporária fora do repositório (padrão <TEMP>/cultura-liquida/fontes/). Extrai o texto do
PDF (pypdf) ou do HTML, normaliza, calcula o hash SHA-256 do texto lido e acha o trecho
exato ou mede a semelhança (difflib.SequenceMatcher.ratio com a melhor janela). Devolve o
trecho, um pedaço antes e outro depois (seletor de citação da W3C), o localizador e o grau.
Abaixo do limiar, o estado é "não verificável por máquina" e sai a Falta "trecho não
verificável por máquina", dita e nunca completada. Pela D-041 (normalizacao-0.2), a semelhança
tolera só OCR e grafia: se uma palavra de negação ou de sentido contrário (palavras_exatas do
registro) não bate entre o trecho e a janela achada, o trecho nunca passa por semelhança e sai
a mesma Falta, com o motivo. PDF sem texto legível vira essa Falta;
a transcrição por IA entra marcada (--transcricao-ia, com --link-imagem).
Nunca grava o texto integral no repositório (l. 100): a pasta temporária precisa ficar fora dele.

Uso:
    python scripts/localizar_trecho.py localizar --fonte <arquivo|URL> --trecho "..." \\
        [--wayback AAAAMMDDhhmmss] [--id TR-nnnn --id-fonte FO-nnnn --execucao EX-nnnn] \\
        [--id-falta F-nnnn] [--saida trecho.json]
    python scripts/localizar_trecho.py conferir <trecho.json> --fonte <arquivo|URL> [--wayback ...]
"localizar": código 0 = localizado (exato ou por semelhança); 2 = abaixo do limiar (Falta emitida).
"conferir": relê a mesma captura, compara o hash e relocaliza; código 0 = o Trecho se sustenta;
1 = não se sustenta (hash diferente, texto que não está na fonte, estado ou grau que não batem).
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import html
import io
import json
import os
import re
import sys
import tempfile
import unicodedata
import urllib.request
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _acervo import carregar_acervo, proximo_id  # noqa: E402
from _comum import RAIZ, carregar_esquema, carregar_valores, validar_objeto  # noqa: E402

REGRA = carregar_valores()["valores"]["normalizacao_e_limiar"]["valor"]
VERSAO = REGRA["versao_regra"]
LIMIAR = REGRA["limiar_semelhanca"]
EXATAS = {p for k in ("negacao", "sentido_contrario") for p in REGRA["palavras_exatas"][k]}
CONTEXTO = 60  # caracteres de "antes" e "depois" no seletor
MIN_TEXTO_LEGIVEL = 20  # menos que isso de texto extraído = PDF sem texto legível
USER_AGENT = "cultura-liquida/0.1 (+https://github.com/Indalt/cultura-liquida)"


def normalizar(t: str) -> str:
    """A regra normalizacao-0.1, na ordem do registro."""
    t = unicodedata.normalize("NFC", t)
    t = re.sub(r"([^\W\d_])-[ \t]*\r?\n[ \t]*([^\W\d_])", r"\1\2", t)  # hífen de fim de linha entre letras
    t = re.sub(r"\s+", " ", t)
    t = t.translate(str.maketrans({"“": '"', "”": '"', "„": '"', "«": '"', "»": '"',
                                   "‘": "'", "’": "'", "‚": "'", "´": "'"}))
    return t.strip()


def sha256(t: str) -> str:
    return hashlib.sha256(t.encode("utf-8")).hexdigest()


class _Texto(HTMLParser):
    def __init__(self):
        super().__init__()
        self.partes, self._pula = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript"):
            self._pula += 1
        elif tag in ("p", "br", "div", "li", "h1", "h2", "h3", "h4", "tr"):
            self.partes.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript") and self._pula:
            self._pula -= 1

    def handle_data(self, data):
        if not self._pula:
            self.partes.append(data)


def pasta_temporaria() -> Path:
    p = Path(os.environ.get("CL_FONTES_TMP") or Path(tempfile.gettempdir()) / "cultura-liquida" / "fontes")
    if p.resolve().is_relative_to(RAIZ.resolve()):
        raise SystemExit("a pasta temporária das fontes não pode ficar dentro do repositório (l. 100)")
    p.mkdir(parents=True, exist_ok=True)
    return p


def ler_bytes(fonte: str, wayback: str | None) -> tuple[bytes, str, str]:
    """Devolve (bytes, tipo 'pdf'|'html'|'texto', origem 'fonte'|'wayback')."""
    if wayback:
        if not fonte.startswith("http"):
            raise SystemExit("--wayback pede a URL original em --fonte")
        fonte = f"https://web.archive.org/web/{wayback}id_/{fonte}"
    if fonte.startswith("http"):
        pedido = urllib.request.Request(fonte, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(pedido, timeout=60) as r:  # 403 e captcha não se contornam: o erro sobe
            dados, ctype = r.read(), r.headers.get("Content-Type", "")
        (pasta_temporaria() / sha256(fonte)[:16]).write_bytes(dados)
    else:
        dados, ctype = Path(fonte).read_bytes(), ""
    if dados[:5] == b"%PDF-" or "pdf" in ctype:
        tipo = "pdf"
    elif "html" in ctype or re.search(rb"<html|<body|<p[ >]", dados[:4000], re.I):
        tipo = "html"
    else:
        tipo = "texto"
    return dados, tipo, "wayback" if wayback else "fonte"


def extrair_texto(dados: bytes, tipo: str) -> tuple[str, list[int]]:
    """Texto normalizado e, no PDF, o deslocamento de início de cada página."""
    if tipo == "pdf":
        from pypdf import PdfReader  # dependência do requirements.txt
        paginas, inicios, texto = PdfReader(io.BytesIO(dados)).pages, [], ""
        for pg in paginas:
            inicios.append(len(texto) + (1 if texto else 0))
            parte = normalizar(pg.extract_text() or "")
            texto = f"{texto} {parte}" if texto else parte
        return texto, inicios
    bruto = dados.decode("utf-8", errors="replace")
    if tipo == "html":
        p = _Texto()
        p.feed(bruto)
        bruto = html.unescape("".join(p.partes))
    return normalizar(bruto), []


def melhor_janela(texto: str, alvo: str) -> tuple[float, int, int]:
    """(grau, início, fim) da melhor janela do texto para o alvo."""
    i = texto.find(alvo)
    if i >= 0:
        return 1.0, i, i + len(alvo)
    n = len(alvo)
    if not n or not texto:
        return 0.0, 0, 0
    passo = max(1, n // 4)
    melhor = (0.0, 0, min(n, len(texto)))
    sm = difflib.SequenceMatcher(autojunk=False)
    sm.set_seq2(alvo)
    for ini in range(0, max(1, len(texto) - n + 1), passo):
        sm.set_seq1(texto[ini:ini + n])
        if sm.quick_ratio() <= melhor[0]:
            continue
        r = sm.ratio()
        if r > melhor[0]:
            melhor = (r, ini, ini + n)
    _, b0, _ = melhor  # refina em volta da melhor, variando início e tamanho
    for ini in range(max(0, b0 - passo), min(len(texto), b0 + passo) + 1):
        for tam in range(max(1, n - passo // 2), n + passo // 2 + 1):
            sm.set_seq1(texto[ini:ini + tam])
            if sm.quick_ratio() <= melhor[0]:
                continue
            r = sm.ratio()
            if r > melhor[0]:
                melhor = (r, ini, ini + tam)
    return melhor


def _sem_acento(t: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", t.casefold()) if unicodedata.category(c) != "Mn")


_EXATAS_SA = {_sem_acento(p) for p in EXATAS}


def palavras_exatas_diferentes(alvo: str, janela: str) -> list[str]:
    """As palavras de negação e de sentido contrário cuja contagem difere entre o trecho e a
    janela (sem maiúsculas e sem acentos: a perda de acento é OCR ou grafia; D-041)."""
    def conta(t: str) -> dict[str, int]:
        c: dict[str, int] = {}
        for w in re.findall(r"[^\W\d_]+", _sem_acento(t)):
            if w in _EXATAS_SA:
                c[w] = c.get(w, 0) + 1
        return c
    a, j = conta(alvo), conta(janela)
    return sorted(w for w in set(a) | set(j) if a.get(w, 0) != j.get(w, 0))


def localizar(texto: str, inicios: list[int], trecho: str) -> dict:
    alvo = normalizar(trecho)
    if not alvo:
        raise SystemExit("trecho vazio: nada a localizar")
    grau, ini, fim = melhor_janela(texto, alvo)
    grau = round(grau, 4)
    loc = f"car. {ini}-{fim} do texto normalizado ({VERSAO})"
    if inicios:
        pg = max(k for k, s in enumerate(inicios) if s <= ini) + 1 if ini >= inicios[0] else 1
        loc = f"p. {pg} do PDF; " + loc
    r = {"grau_semelhanca": grau, "localizador": loc, "hash": sha256(texto),
         "versao_normalizacao": VERSAO, "data_conferencia": date.today().isoformat()}
    difere = palavras_exatas_diferentes(alvo, texto[ini:fim]) if grau < 1.0 else []
    if difere:
        r["palavras_exatas_diferentes"] = difere
    if grau >= LIMIAR and not difere:
        r.update(estado="localizado", texto_exato=texto[ini:fim],
                 antes=texto[max(0, ini - CONTEXTO):ini], depois=texto[fim:fim + CONTEXTO])
    else:
        r.update(estado="não verificável por máquina", texto_exato=alvo, antes="", depois="")
    return r


def falta_trecho(id_falta: str, onde: str, motivo: str) -> dict:
    return {"id": id_falta, "tipo": "trecho_nao_verificavel",
            "o_que_falta": "trecho não verificável por máquina",
            "por_que": motivo, "onde_aparece": [onde],
            "criada_por": f"scripts/localizar_trecho.py ({VERSAO})", "data": date.today().isoformat()}


def cmd_localizar(a) -> int:
    dados, tipo, origem = ler_bytes(a.fonte, a.wayback)
    if a.transcricao_ia:
        if not a.link_imagem:
            raise SystemExit("transcrição por IA pede --link-imagem (l. 598)")
        texto, inicios, origem = normalizar(Path(a.transcricao_ia).read_text(encoding="utf-8")), [], "transcrição por IA"
    else:
        texto, inicios = extrair_texto(dados, tipo)
    if len(texto) < MIN_TEXTO_LEGIVEL:
        r = {"estado": "não verificável por máquina", "texto_exato": normalizar(a.trecho), "antes": "", "depois": "",
             "localizador": "sem texto legível", "grau_semelhanca": None, "versao_normalizacao": VERSAO}
        motivo = f"{tipo.upper()} sem texto legível por máquina; caminho: transcrição por IA marcada, com o link da imagem"
    else:
        r = localizar(texto, inicios, a.trecho)
        difere = r.pop("palavras_exatas_diferentes", [])
        if difere:
            motivo = (f"palavra de negação ou de sentido contrário diferente da fonte ({', '.join(difere)}): "
                      f"não passa por semelhança, grau {r['grau_semelhanca']} ({VERSAO}; D-041)")
        else:
            motivo = f"semelhança {r['grau_semelhanca']} abaixo do limiar {LIMIAR} ({VERSAO})"
    r["origem_texto"] = origem
    if a.link_imagem:
        r["link_imagem"] = a.link_imagem
    saida: dict = {"trecho": r}
    if a.id and a.id_fonte and a.execucao:
        if not a.protecao:
            raise SystemExit("o registro completo pede --protecao (l. 586)")
        reg = {"id": a.id, "fonte": a.id_fonte, **r, "protecao": json.loads(a.protecao),
               "origem_registro": {"criado_por": "scripts/localizar_trecho.py", "data": date.today().isoformat(),
                                   "execucao": a.execucao, "versao_regra": VERSAO}}
        if r["estado"] != "localizado":
            if not a.id_falta:
                raise SystemExit("abaixo do limiar: informe --id-falta para a Falta")
            reg["falta"] = a.id_falta
        saida = {"trecho": reg}
        erros = validar_objeto(reg, carregar_esquema("trecho"))
        if erros:
            print("Trecho não valida:", "; ".join(erros), file=sys.stderr)
            return 1
    if r["estado"] != "localizado":
        saida["falta"] = falta_trecho(a.id_falta or proximo_id("F", carregar_acervo(RAIZ)[0]), a.id or a.fonte, motivo)
    js = json.dumps(saida, ensure_ascii=False, indent=2)
    if a.saida:
        Path(a.saida).write_text(js + "\n", encoding="utf-8")
    print(js)
    print(f"estado: {r['estado']} · grau {r['grau_semelhanca']} · limiar {LIMIAR} · {VERSAO}")
    return 0 if r["estado"] == "localizado" else 2


def cmd_conferir(a) -> int:
    reg = json.loads(Path(a.arquivo).read_text(encoding="utf-8"))
    reg = reg.get("trecho", reg)
    dados, tipo, _ = ler_bytes(a.fonte, a.wayback)
    texto, inicios = extrair_texto(dados, tipo)
    problemas = []
    if reg.get("versao_normalizacao") not in (None, VERSAO):
        problemas.append(f"normalização {reg['versao_normalizacao']} ≠ {VERSAO}: refazer pela regra nova")
    if reg.get("hash") and reg["hash"] != sha256(texto):
        problemas.append("hash do texto lido diferente: não é a mesma captura")
    novo = localizar(texto, inicios, reg.get("texto_exato", ""))
    if reg.get("estado") == "localizado":
        if novo.get("palavras_exatas_diferentes"):
            problemas.append("marcado como localizado, mas palavra de negação ou de sentido contrário difere da fonte: "
                             + ", ".join(novo["palavras_exatas_diferentes"]) + " (D-041)")
        elif novo["estado"] != "localizado":
            problemas.append(f"marcado como localizado, mas o grau relido é {novo['grau_semelhanca']} (< {LIMIAR})")
        elif reg.get("grau_semelhanca") == 1.0 and novo["grau_semelhanca"] < 1.0:
            problemas.append(f"marcado como exato (1.0), mas o texto não está literal na fonte (grau {novo['grau_semelhanca']})")
        elif abs((reg.get("grau_semelhanca") or 0) - novo["grau_semelhanca"]) > 0.001:
            problemas.append(f"grau registrado {reg.get('grau_semelhanca')} ≠ relido {novo['grau_semelhanca']}")
    for p in problemas:
        print("NÃO SE SUSTENTA:", p)
    if not problemas:
        print(f"o Trecho se sustenta: {novo['estado']}, grau {novo['grau_semelhanca']}, hash igual")
    return 1 if problemas else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    l = sub.add_parser("localizar")
    l.add_argument("--fonte", required=True)
    l.add_argument("--trecho", required=True)
    l.add_argument("--wayback")
    l.add_argument("--transcricao-ia")
    l.add_argument("--link-imagem")
    l.add_argument("--id")
    l.add_argument("--id-fonte")
    l.add_argument("--id-falta")
    l.add_argument("--execucao")
    l.add_argument("--protecao", help="JSON dos campos de proteção (comum.schema.json#/$defs/protecao)")
    l.add_argument("--saida")
    c = sub.add_parser("conferir")
    c.add_argument("arquivo")
    c.add_argument("--fonte", required=True)
    c.add_argument("--wayback")
    a = ap.parse_args()
    return cmd_localizar(a) if a.cmd == "localizar" else cmd_conferir(a)


if __name__ == "__main__":
    sys.exit(main())
