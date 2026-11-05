"""Portão da camada 1 (bloco 10a; D-048; padrão A-10, D-038): as checagens por script que a
ramificação das rotinas passa antes de a ferramenta juntá-la ao main, sem esperar Vicente.

Checagens (todas sem IA, com log): `validar_acervo.py` (o acervo e as Entradas no contrato),
`deduplicar.py --conferir` (nenhuma Entrada duplicada; pegadas ligadas), `procurar_dado_pessoal.py --git`
(nenhum dado pessoal de terceiros no que o Git versiona) e, com `--testes`, `rodar_testes.py` (a suíte
inteira). O alarme da guarda (D-045) não reprova: vai ao relatório do dia.
Quem propõe não aprova (D-038): o portão é script, e a versão dele vai no log de cada junção.

Uso:
    python scripts/portao.py [--testes] [--entrada-ref "..."] [--simular]
Código 0 = passa (pode juntar); 1 = reprova (não junta; o workflow falha e o GitHub avisa).
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import RAIZ  # noqa: E402
from _coleta import Execucao  # noqa: E402
from procurar_dado_pessoal import nomes_privados  # noqa: E402

VERSAO = "portao-camada1-0.1"
PY = sys.executable
S = Path(__file__).resolve().parent


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--testes", action="store_true")
    ap.add_argument("--entrada-ref", default="portão da camada 1 da rotina diária (K-112, bloco 10a)")
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    checagens = [("validar_acervo", [PY, str(S / "validar_acervo.py")]),
                 ("deduplicar --conferir", [PY, str(S / "deduplicar.py"), "--conferir"]),
                 ("procurar_dado_pessoal --git", [PY, str(S / "procurar_dado_pessoal.py"), "--git"])]
    if a.testes:
        checagens.append(("rodar_testes", [PY, str(S / "rodar_testes.py")]))
    ex = Execucao("portao", a.entrada_ref, simular=a.simular)
    reprovou = []
    for nome, cmd in checagens:
        r = subprocess.run(cmd, cwd=RAIZ, capture_output=True, text=True, encoding="utf-8")
        cauda = ((r.stdout or "") + (r.stderr or "")).strip().splitlines()[-3:]
        ex.acoes.append(f"scripts/{nome}")
        ex.olhado.append(f"{nome}: código {r.returncode}")
        if r.returncode != 0:
            reprovou.append(nome)
            ex.erros.append(f"{nome} reprovou: {' | '.join(cauda)[:400]}")
        print(f"{'PASSA' if r.returncode == 0 else 'REPROVA'} {nome}: {' | '.join(cauda)[:300]}")
    ex.resultados.append(f"{VERSAO}: {'reprova (' + ', '.join(reprovou) + ')' if reprovou else 'passa'}")
    ex.decisoes.append({"item": "junção da ramificação das rotinas", "decisao": "falta" if reprovou else "aceito",
                        "motivo": f"regra {VERSAO}: " + ("checagem reprovada" if reprovou else "todas as checagens passaram"),
                        "versao_regra": VERSAO})
    if not a.testes:
        ex.fora.append("a suíte rodar_testes.py (só com --testes)")
    if not nomes_privados():  # na rotina, a tabela de pessoas não existe (D-048)
        ex.fora.append("os nomes da tabela privada de pessoas, que não está nesta máquina: a busca de dado "
                       "pessoal olhou e-mail, telefone, CPF e @perfil, não os nomes")
    print(f"{VERSAO}: {'REPROVA' if reprovou else 'PASSA'}; {ex.gravar_log()}")
    return 1 if reprovou else 0


if __name__ == "__main__":
    sys.exit(main())
