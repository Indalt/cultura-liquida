"""Checagem mecânica de completude do mapa das três frentes (K-001), sem IA."""
import re
import sys
from pathlib import Path

RAIZ = Path(sys.argv[1])
P = RAIZ / "trilhas" / "planejamento"
mapa = (P / "mapa-tres-frentes.md").read_text(encoding="utf-8")
quadro = (P / "quadro.md").read_text(encoding="utf-8")
prox = (P / "proxima-versao.md").read_text(encoding="utf-8")
fund = (RAIZ / "00_Fundacao_Cultura_Liquida.md").read_text(encoding="utf-8").splitlines()

problemas = []

def secao(texto, inicio, fim=None):
    i = texto.index(inicio)
    j = texto.index(fim, i) if fim else len(texto)
    return texto[i:j]

# 1. decisões D-001 a D-037 na seção 7
s7 = secao(mapa, "## 7. Decisões", "## 8.")
for n in range(1, 38):
    if not re.search(rf"^\| D-{n:03d} \|", s7, re.M):
        problemas.append(f"seção 7 sem linha para D-{n:03d}")

# 2. insumos 1 a 14 na seção 6
s6 = secao(mapa, "## 6. Insumos", "## 7.")
for n in range(1, 15):
    if not re.search(rf"^\| {n}, ", s6, re.M):
        problemas.append(f"seção 6 sem linha para o insumo {n}")

# 3. blocos 0 a 14 (10a e 10b) na tabela de blocos
s5 = secao(mapa, "### Blocos", "## 6.")
for b in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10a", "10b", "11", "12", "13", "14"]:
    if not re.search(rf"^\| {b} \|", s5, re.M):
        problemas.append(f"tabela de blocos sem o bloco {b}")

# 4. subseções da Fundação citadas na seção 3
s3 = secao(mapa, "## 3. Fundação", "## 4.")
heads = [l for l in fund if l.startswith("### ")]
for h in heads:
    m = re.match(r"### (\d+\.\d+)", h)
    if m and m.group(1) not in s3:
        problemas.append(f"seção 3 não cita §{m.group(1)} ({h[:50]})")
    m = re.match(r"### Passo (\d+)", h)
    if m and f"Passo {m.group(1)} " not in s3 and f"Passo {m.group(1)}," not in s3 and f"Passo {m.group(1)}\n" not in s3 and f"| Passo {m.group(1)} |" not in s3:
        problemas.append(f"seção 3 não cita o Passo {m.group(1)}")
for a in "ABCDE":
    if not re.search(rf"\| {a}[ ,]", s3) and f"| A e B" not in s3:
        problemas.append(f"seção 3 sem o Anexo {a}")

# 5. linhas do §8 (807-824) na tabela do §8
s8 = secao(mapa, "### §8 Decisões pendentes", "### §9")
for i, l in enumerate(fund, 1):
    if 805 <= i <= 824 and l.startswith("| **") or (805 <= i <= 824 and l.startswith("| ") and not l.startswith("| Decisão") and not l.startswith("|---")):
        if f"| {i} " not in s8:
            problemas.append(f"tabela do §8 sem a l. {i}: {l[:60]}")

# 6. perguntas 1 a 22 do §10
s10 = secao(mapa, "| Pergunta | Frente | Destino |", "- **§11")
for n in range(1, 23):
    if not re.search(rf"(\| |; |, | e ){n}(,| |;)", s10):
        problemas.append(f"tabela do §10 sem a pergunta {n}")

# 7. cartões: citados no mapa x existentes no quadro
cart_quadro = set(re.findall(r"\*\*(K-\d{3})\*\*", quadro))
cart_mapa = set(re.findall(r"K-\d{3}", mapa))
def expandir(texto):
    out = set()
    for a, b in re.findall(r"K-(\d{3}) a K-(\d{3})", texto):
        out |= {f"K-{n:03d}" for n in range(int(a), int(b) + 1)}
    return out
cart_mapa |= expandir(mapa)
for k in sorted(cart_mapa - cart_quadro):
    problemas.append(f"o mapa cita {k}, que não está no quadro")
for k in sorted(cart_quadro - cart_mapa):
    problemas.append(f"o quadro tem {k}, que o mapa não cita")

# 8. V citados no mapa x existentes na lista
v_lista = set(re.findall(r"^\| (V-\d{2}) \|", prox, re.M))
v_mapa = set(re.findall(r"V-\d{2}", mapa))
for a, b in re.findall(r"V-(\d{2}) a V-(\d{2})", mapa):
    v_mapa |= {f"V-{n:02d}" for n in range(int(a), int(b) + 1)}
for v in sorted(v_mapa - v_lista):
    problemas.append(f"o mapa cita {v}, que não está na lista")
nao_citados = sorted(v_lista - v_mapa)

# 9. A citados x existentes
a_tab = set(re.findall(r"^\| (A-\d{2}) \|", mapa, re.M))
a_cit = set(re.findall(r"A-\d{2}", mapa + prox + quadro))
for a, b in re.findall(r"A-(\d{2}) a A-(\d{2})", mapa + prox + quadro):
    a_cit |= {f"A-{n:02d}" for n in range(int(a), int(b) + 1)}
for a in sorted(a_cit - a_tab):
    problemas.append(f"citado {a}, que não está na tabela de atritos")
# atritos citados na lista como "atrito n"
for n in re.findall(r"atritos? (\d+)", prox):
    if f"A-{int(n):02d}" not in a_tab:
        problemas.append(f"a lista cita 'atrito {n}', sem par na tabela")

# 10. linhas 6A do brief cobertas pela lista (pelas linhas citadas)
brief = (RAIZ / "trilhas" / "2026-10-17_caminhos" / "brief-execucoes-v0.1.md").read_text(encoding="utf-8").splitlines()
for i in range(400, 417):
    l = brief[i - 1]
    if l.startswith("| ") and not l.startswith("| O que muda") and not l.startswith("|---"):
        celulas = [c.strip() for c in l.strip("|").split("|")]
        linhas = re.findall(r"\d{2,4}", celulas[1]) if len(celulas) > 1 else []
        cobertas = [x for x in linhas if re.search(rf"\b{x}\b", prox)]
        if linhas and not cobertas:
            problemas.append(f"6A, brief l. {i}: nenhuma das linhas {linhas} aparece na lista")

print(f"cartões no quadro: {len(cart_quadro)}; V na lista: {len(v_lista)}; atritos: {len(a_tab)}")
print(f"V que o mapa não cita (podem ser só da lista): {', '.join(nao_citados) or 'nenhum'}")
print("PROBLEMAS:" if problemas else "Sem problemas.")
for p in problemas:
    print(" -", p)
sys.exit(1 if problemas else 0)
