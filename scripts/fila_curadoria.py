"""Fila de curadoria (l. 512; D-037; D-038; D-039): o relatório de cada lote e os cartões da frente de
operação, sem pedir aprovação.

- **Relatório do lote** (uma tela): o que entrou (Entradas da Execução ou da data), o que ficou em
  quarentena e as Faltas novas. Grava-se na trilha (`--saida`), sem pedir aprovação.
- **Cartões** na tabela da frente de operação do quadro (`--abrir-cartoes`), um por item, nunca
  repetidos (o cartão leva o ID do item):
  - de conflito: Proposição com estado "inconsistente" (de `calcular_mu_lambda.py`), a tensão da
    l. 638. Chama Vicente, que confere a nossa leitura das Evidências em tensão (se cada trecho diz
    o que dissemos que diz; eixo 3), nunca a prática (D-038); as duas documentações convivem (P29);
  - de Falta jurídica a liberar: Falta `impedimento_juridico` com o caminho de liberação não
    liberado. Chama Vicente, salvo a Falta que só vale para publicar (`"vale_para": "publicar"`),
    que espera a decisão de publicar (K-010) e não o chama antes dela (D-032);
  - de lista das CLB candidatas de outro termo: um só cartão, com uma linha por CLB em
    `trilhas/planejamento/clb-candidatas.md`, de baixa prioridade, que não chama Vicente (D-037,
    diretriz 4; A-09 b, D-038, com a D-039).
- **Fila:** os cartões da frente de operação em "A fazer" que chamam Vicente, contra o valor
  `fila_curadoria` do registro (15 por semana): acima dele, a fila passa de uma semana.
- `--conferir` reprova (código 1) se um cartão de conflito aponta para Proposição que não existe ou
  que não está mais inconsistente, ou se há dois cartões abertos para o mesmo item.
A ação de Vicente num cartão vira Execução com executor "pessoa" e fecha o cartão (à mão, na fase 1).
A saída da quarentena não passa por aqui: é a regra, pelo portão (A-05, D-038).

Uso:
    python scripts/fila_curadoria.py [--execucao EX-0020 | --data AAAA-MM-DD] [--saida <relatorio.md>]
        [--abrir-cartoes] [--conferir] [--termos-piloto TE-0001,TE-0002] [--raiz <pasta>] [--quadro <arq>]
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ, carregar_json, carregar_valores  # noqa: E402

VERSAO = "fila-curadoria-0.1"
LIMITE = carregar_valores()["valores"]["fila_curadoria"]["valor"]["cartoes_por_semana"]
TERMOS_PILOTO = ("TE-0001", "TE-0002")
CAB_OPERACAO = "## Operação"


def registros(raiz: Path, pasta: str) -> list[dict]:
    p = raiz / pasta
    return [carregar_json(a) for a in sorted(p.glob("*.json"))] if p.exists() else []


def pendencias(raiz: Path, termos_piloto) -> list[dict]:
    """Os itens que pedem cartão: conflito, Falta jurídica a liberar, CLB candidata de outro termo."""
    itens = []
    for pr in registros(raiz, "acervo/proposicoes"):
        if pr.get("estado") == "inconsistente" and not pr.get("retirado"):
            itens.append({"tipo": "conflito", "id": pr["id"], "chama": True,
                          "titulo": f"Conflito: {pr['id']} (Proposição inconsistente; conferir a nossa leitura das Evidências em tensão, nunca a prática)"})
    for f in registros(raiz, "acervo/faltas"):
        if f.get("tipo") == "impedimento_juridico" and f.get("caminho_de_liberacao", {}).get("estado") != "liberado":
            so_publicar = f.get("vale_para") == "publicar"
            itens.append({"tipo": "falta", "id": f["id"], "chama": not so_publicar,
                          "titulo": f"Falta jurídica a liberar: {f['id']} ({f.get('subtipo_juridico', '?')})"
                                    + (". *Espera a decisão de publicar (K-010)*" if so_publicar else "")})
    candidatas = [c for c in registros(raiz, "acervo/clb")
                  if c.get("estado") == "candidata" and c.get("termo") not in termos_piloto and not c.get("retirado")]
    if candidatas:
        itens.append({"tipo": "lista", "id": "clb-candidatas", "chama": False, "candidatas": candidatas,
                      "titulo": "Lista das CLB candidatas de outro termo (uma linha por CLB em `trilhas/planejamento/clb-candidatas.md`; baixa prioridade, não chama Vicente)"})
    return itens


def tabela_operacao(texto: str) -> tuple[int, int, list[str]]:
    """(início, fim) das linhas da tabela da frente de operação e as linhas."""
    ini = texto.index(CAB_OPERACAO)
    linhas = texto[ini:].splitlines(keepends=True)
    pos, i0, i1 = ini, None, None
    for ln in linhas:
        if ln.startswith("| ") and i0 is None and "Coluna" not in ln and not ln.startswith("|---"):
            i0 = pos
        if i0 is not None and not ln.startswith("|"):
            i1 = pos
            break
        pos += len(ln)
    i1 = i1 if i1 is not None else len(texto)
    if i0 is None:
        i0 = i1
    return i0, i1, [x for x in texto[i0:i1].splitlines() if x.startswith("| ")]


def abertos(linhas: list[str]) -> list[str]:
    return [x for x in linhas if x.startswith("| A fazer") or x.startswith("| Fazendo")]


def chama_vicente(linha: str) -> bool:
    """Conflito ou Falta jurídica a liberar, sem estar à espera de outra coisa (ex.: a decisão de publicar)."""
    return ("Conflito:" in linha or "a liberar" in linha) and "Espera" not in linha


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--execucao")
    ap.add_argument("--data")
    ap.add_argument("--saida", type=Path)
    ap.add_argument("--abrir-cartoes", action="store_true")
    ap.add_argument("--conferir", action="store_true")
    ap.add_argument("--termos-piloto", default=",".join(TERMOS_PILOTO))
    ap.add_argument("--raiz", type=Path, default=RAIZ)
    ap.add_argument("--quadro", type=Path)
    a = ap.parse_args()
    raiz = a.raiz if a.raiz.is_absolute() else RAIZ / a.raiz
    quadro = a.quadro or raiz / "trilhas" / "planejamento" / "quadro.md"
    quadro = quadro if quadro.is_absolute() else RAIZ / quadro
    texto = quadro.read_text(encoding="utf-8")
    i0, i1, linhas = tabela_operacao(texto)
    itens = pendencias(raiz, tuple(x.strip() for x in a.termos_piloto.split(",")))

    # --- conferência dos cartões abertos ---
    problemas = []
    props = {p["id"]: p for p in registros(raiz, "acervo/proposicoes")}
    for ln in abertos(linhas):
        if m := re.search(r"Conflito: (PR-\d{4,})", ln):
            p = props.get(m.group(1))
            if not p or p.get("estado") != "inconsistente":
                problemas.append(f"cartão de conflito aberto para {m.group(1)}, que {'não existe' if not p else 'não está inconsistente'}")
    for it in itens:
        n = sum(1 for ln in abertos(linhas) if re.search(rf"(?<![\w-]){re.escape(it['id'])}(?![\w-])", ln))
        if n > 1:
            problemas.append(f"{n} cartões abertos para {it['id']}")

    # --- cartões novos ---
    novos = [it for it in itens if not any(re.search(rf"(?<![\w-]){re.escape(it['id'])}(?![\w-])", ln) for ln in linhas)]
    nums = [int(n) for n in re.findall(r"\*\*K-(2\d\d)\*\*", texto)]
    prox = max(nums, default=200) + 1
    linhas_novas = []
    for it in novos:
        origem = {"conflito": "calcular_mu_lambda.py; D-037, diretriz 1; D-038", "falta": "triagem do juridico; D-037, diretriz 1",
                  "lista": "D-037, diretriz 4; D-039"}[it["tipo"]]
        destino = {"conflito": "a leitura conferida: certa, as duas documentações lado a lado e o cartão fecha; errada, a leitura se corrige e a ferramenta ganha um insumo",
                   "falta": "a Falta liberada pelo caminho do guia, ou mantida com o porquê",
                   "lista": "cada CLB candidata vista, sem pressa; nenhuma chamada a Vicente"}[it["tipo"]]
        linhas_novas.append(f"| A fazer | **K-{prox}** {it['titulo']} | {origem} | {destino} |")
        prox += 1
    fila = [ln for ln in abertos(linhas) if chama_vicente(ln)] + [ln for ln, it in zip(linhas_novas, novos) if it["chama"]]

    # --- relatório do lote ---
    hoje = a.data or date.today().isoformat()
    def do_lote(r: dict) -> bool:
        o = r.get("origem_registro", {})
        return o.get("execucao") == a.execucao if a.execucao else (o.get("data") or r.get("data")) == hoje
    ents = [e for e in registros(raiz, "entrada") if do_lote(e)]
    quar = [e for e in registros(raiz, "entrada") if e.get("estado") == "quarentena" and do_lote(e)]
    falts = [f for f in registros(raiz, "acervo/faltas")
             if (a.execucao and a.execucao in f.get("criada_por", "")) or (not a.execucao and f.get("data") == hoje)]
    alvo = f"Execução {a.execucao}" if a.execucao else f"dia {hoje}"
    rel = [f"# Relatório do lote ({alvo})", "",
           f"Gerado por `scripts/fila_curadoria.py` ({VERSAO}), sem pedir aprovação (l. 512 relida pela D-037).", "",
           f"- **Entraram:** {len(ents)} Entrada(s)" + (": " + ", ".join(e["id"] for e in ents[:30]) + (" …" if len(ents) > 30 else "") if ents else "."),
           f"- **Em quarentena:** {len(quar)}" + (": " + ", ".join(f"{e['id']} ({e.get('motivo_quarentena', '')})" for e in quar) if quar else "."),
           f"- **Faltas novas:** {len(falts)}" + (": " + "; ".join(f"{f['id']} ({f['o_que_falta']})" for f in falts) if falts else "."),
           f"- **Cartões novos na frente de operação:** {len(novos)}" + (": " + "; ".join(it["titulo"] for it in novos) if novos else "."),
           f"- **Fila de curadoria:** {len(fila)} cartão(ões) à espera de Vicente, para {LIMITE} por semana"
           + (" — **a fila passa de uma semana**" if len(fila) > LIMITE else "") + "."]
    print("\n".join(rel))
    if a.saida:
        s = a.saida if a.saida.is_absolute() else RAIZ / a.saida
        s.parent.mkdir(parents=True, exist_ok=True)
        s.write_text("\n".join(rel) + "\n", encoding="utf-8")
    if a.abrir_cartoes and linhas_novas:
        texto = texto[:i1] + "".join(x + "\n" for x in linhas_novas) + texto[i1:]
        quadro.write_text(texto, encoding="utf-8")
        lista = next((it for it in novos if it["tipo"] == "lista"), None) or next((it for it in itens if it["tipo"] == "lista"), None)
        if lista:
            arq = raiz / "trilhas" / "planejamento" / "clb-candidatas.md"
            arq.parent.mkdir(parents=True, exist_ok=True)
            arq.write_text("# CLB candidatas de outro termo (D-039)\n\n" + "".join(
                f"- {c['id']}: termo {c.get('termo')}; origem {', '.join(c.get('origem_mencao', [])) or c.get('origem_registro', {}).get('execucao', '?')}\n"
                for c in lista["candidatas"]), encoding="utf-8")
    for p in problemas:
        print("PROBLEMA", p)
    print(f"{VERSAO}: {len(novos)} cartão(ões) novo(s){' gravado(s)' if a.abrir_cartoes and novos else ''}; fila {len(fila)} de {LIMITE}; "
          f"{'cartões conferidos' if not problemas else f'{len(problemas)} problema(s)'}")
    return 1 if a.conferir and problemas else 0


if __name__ == "__main__":
    sys.exit(main())
