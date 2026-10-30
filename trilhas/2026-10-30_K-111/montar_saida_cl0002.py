"""Monta a saída do lote das Evidências separadas como vinho de caju (CL-0002), para o
gravar_extracao.py --clb (K-111, insumo 92). Sem IA: só seleciona e tira o rótulo do valor.

Entram as separadas com 'vinho' no texto exato e de origem não identificável: a5-39 e a5-40 (os
relatos de 1587 e 1663 sobre o "gentio", citações curtas de obra publicada; D-043, 3).
Ficam fora, ditas: a5-35 e a5-36 (modo de fazer nas falas de quem o fazia no Piauí, de origem
identificável, que a F-0024 mantém em dúvida de conhecimento tradicional; onde fica esse detalhe é a
dúvida do insumo 90, que vai ao K-010: a gravação segue sem elas); a5-31 a a5-34 (o trecho não nomeia
a bebida; o nome não se infere, K-102); a a5-47 (marcada pela F-0033: fica na pasta local, D-043, 3).
"""
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ORIGEM = AQUI.parent / "2026-10-29_K-110" / "mencoes-outras-clb-A5.json"
ROTULO = "vinho de caju (outra CLB): "
ENTRAM = ("a5-39", "a5-40")

d = json.loads(ORIGEM.read_text(encoding="utf-8"))
evs = []
for e in d["evidencias"]:
    if not any(e["arquivo_trecho"].endswith(f"EN-1725-{x}.json") for x in ENTRAM):
        continue
    e = {k: v for k, v in e.items() if k not in ("eixo3", "rotulo_K110", "estado_trecho")}
    assert e["valor"].startswith(ROTULO), e["valor"]
    e["valor"] = e["valor"][len(ROTULO):]
    e["chave"] = f"{e['atributo']}|{e['valor']}"
    evs.append(e)
assert len(evs) == len(ENTRAM)
saida = {"lote": "K111-CL0002 (Evidências separadas no K110-A5, EX-0069)",
         "entradas": [{"entrada": "EN-1725", "evidencias": evs}]}
destino = Path(sys.argv[1]) if len(sys.argv) > 1 else AQUI / "saida-cl0002.json"
destino.write_text(json.dumps(saida, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"{len(evs)} Evidências em {destino}")
