"""Checagem mecânica dos ajustes do K-003 (D-036 e D-037) no brief, no roteiro e no quadro, sem IA.

Uso:
    python checar_ajustes.py <raiz do repositório>                 -> confere os arquivos da pasta (tem de passar)
    python checar_ajustes.py <raiz do repositório> --commit 71dafff -> confere os arquivos de antes dos ajustes (tem de reprovar)
Código 0 = passa; 1 = reprova. As linhas de `.claude/` que o K-101 muda saem como informação, sem reprovar.
"""
import re
import subprocess
import sys
from pathlib import Path

BRIEF = "trilhas/2026-10-17_caminhos/brief-execucoes-v0.1.md"
ROTEIRO = "trilhas/2026-10-17_caminhos/caminhos.md"
QUADRO = "trilhas/planejamento/quadro.md"


def ler(raiz: Path, rel: str, commit: str | None) -> str:
    if commit:
        r = subprocess.run(["git", "-C", str(raiz), "show", f"{commit}:{rel}"],
                           capture_output=True, encoding="utf-8", check=True)
        return r.stdout
    return (raiz / rel).read_text(encoding="utf-8")


def secao(texto: str, inicio: str, fim: str | None = None) -> str:
    i = texto.find(inicio)
    if i < 0:
        return ""
    j = texto.find(fim, i + len(inicio)) if fim else -1
    return texto[i:j] if j > 0 else texto[i:]


def main() -> int:
    raiz = Path(sys.argv[1])
    commit = sys.argv[sys.argv.index("--commit") + 1] if "--commit" in sys.argv else None
    brief = ler(raiz, BRIEF, commit)
    roteiro = ler(raiz, ROTEIRO, commit)
    quadro = ler(raiz, QUADRO, commit)
    problemas: list[str] = []

    # 1. Expressões que a D-036 e a D-037 superaram: não podem ficar no brief (salvo a linha que diz que foram superadas)
    proibidas = [
        ("aprova ou devolve", None),
        ("O veredito de Vicente", None),
        ("Vicente a junta na revisão", None),
        ("na revisão de uma tela, como na camada 2", None),
        ("fila = itens à espera de juízo humano", None),
        ("o que sobra da cota semanal", None),
        ("Essência a registrar", None),
        ("Proposta, não registrada", None),
        ("revisões de uma tela, juízo de até 15 itens", None),
        ("Revisão de uma tela por lote", None),
        ("revisada antes de entrar na versão principal", None),
        ("mudar a Fundação fora dos blocos 0 e 14", "superou"),
        ("o curador a abre numa conversa de trabalho", "substitui"),
        # achados da verificação do K-003 (AUD-K003-01 e 02): regras que o texto tinha criado sem âncora
        ("não conta na fila até lá", None),
        ("ele confere a nossa leitura das Evidências em tensão", None),
    ]
    for n, linha in enumerate(brief.splitlines(), 1):
        for expr, permitido_se in proibidas:
            if expr in linha and not (permitido_se and permitido_se in linha):
                problemas.append(f"brief l. {n}: ainda diz '{expr}'")

    # 2. O quadro de ajustes e o que o cartão K-003 pede
    ajustes = secao(brief, "**Ajustes das D-036 e D-037", "\n---")
    if not ajustes:
        problemas.append("brief sem o quadro 'Ajustes das D-036 e D-037'")
    for a in ["A-01", "A-02", "A-03", "A-04", "A-05", "A-06", "A-07", "A-08", "A-09", "A-10", "A-11", "A-13"]:
        if ajustes and a not in ajustes:
            problemas.append(f"quadro de ajustes sem o {a}")
    s2 = secao(brief, "## 2. Decisões vigentes", "## 3.")
    for d in range(15, 38):
        if not re.search(rf"^\| D-0{d} \|", s2, re.M):
            problemas.append(f"seção 2 sem a linha da D-0{d}")
    retomada = secao(brief, "**Retomada:", "## 2.")
    for t in ["quadro.md", "estado-planejamento.md", "mover o cartão"]:
        if t not in retomada:
            problemas.append(f"retomada sem '{t}'")
    b1 = secao(brief, "### Bloco 1 ", "### Bloco 2 ")
    for t in ["curador.md", "avaliador.md", "extrair-evidencia", "executar-brief", "conferir-fato",
              "insumo 5", "insumo 7", "insumo 17", "--teto 300000", "A-01", "A-02", "A-05", "A-06"]:
        if t not in b1:
            problemas.append(f"bloco 1 sem '{t}'")
    b2 = secao(brief, "### Bloco 2 ", "### Bloco 3 ")
    for t in ["A-03", "A-04", "A-05", "A-09", "candidata"]:
        if t not in b2:
            problemas.append(f"bloco 2 sem '{t}'")
    b5 = secao(brief, "### Bloco 5 ", "### Bloco 6 ")
    for t in ["cartões de conflito", "Falta jurídica a liberar", "CLB candidata", "não se julga a prática", "A-05", "A-10", "D-032"]:
        if t not in b5:
            problemas.append(f"bloco 5 sem '{t}'")
    # cada padrão nos lugares onde o brief o aplica (achado AUD-K003-06)
    s3a = secao(brief, "### 3a.", "### 3b.")
    s3b = secao(brief, "### 3b.", "## 4.")
    b3 = secao(brief, "### Bloco 3 ", "### Bloco 4 ")
    b7 = secao(brief, "### Bloco 7 ", "### Bloco 8 ")
    b8 = secao(brief, "### Bloco 8 ", "### Entre os blocos 8 e 9")
    for nome, parte, padroes in [("seção 3a", s3a, ["A-04"]), ("seção 3b", s3b, ["A-10"]), ("bloco 3", b3, ["A-04"]),
                                 ("bloco 7", b7, ["A-04", "A-05"]), ("bloco 8", b8, ["A-04"])]:
        for p in padroes:
            if p not in parte:
                problemas.append(f"{nome} sem o {p}")
    if "D-017" not in b3:
        problemas.append("bloco 3: a lista do sorteio tem de vir como exemplo (D-017)")
    if "Script de menções incidentais (cartão K-102)" not in brief:
        problemas.append("brief sem a seção do script de menções incidentais (K-102)")
    b10 = secao(brief, "### Bloco 10 ", "### Bloco 11 ")
    if b10.count("A-10") < 3:
        problemas.append(f"bloco 10 cita o A-10 {b10.count('A-10')} vez(es); esperado: 3 ou mais")
    b13 = secao(brief, "### Bloco 13 ", "### Bloco 14 ")
    if "A-08" not in b13:
        problemas.append("bloco 13 sem o A-08 (horas relidas)")
    op = secao(brief, "### Depois do bloco 14", "## 5.")
    for t in ["A-09 b", "D-036", "K-102"]:
        if t not in op:
            problemas.append(f"'Depois do bloco 14' sem '{t}'")
    s5 = secao(brief, "## 5. Não fazer", "## 6.")
    for t in ["juntar a própria proposta", "D-037, diretriz 1", "D-035; cartão K-004"]:
        if t not in s5:
            problemas.append(f"seção 5 sem '{t}'")
    # termos-chave das essências na seção 2 (o sentido por inteiro ainda é leitura humana ou do auditor)
    chaves = {
        "D-033": ["repositório", "outra solução em nuvem"],
        "D-034": ["não se pergunta", "aonde se quer chegar", "valor provisório", "seção 6A"],
        "D-035": ["construir e testar", "versão nova", "não se explora", "Uma tarefa por vez"],
        "D-036": ["três frentes", "kanban", "cartão até Concluído", "teto de custo próprios", "sem precisar da IDE"],
        "D-037": ["revisão de rotina", "em tensão", "Falta jurídica pede liberação", "auditar a ferramenta",
                  "menções incidentais", "sem IA", "diretrizes de admissão"],
    }
    for d, termos in chaves.items():
        m = re.search(rf"^\| {d} \|(.*)$", s2, re.M)
        for t in termos:
            if m and t not in m.group(1):
                problemas.append(f"seção 2, {d}: falta o termo-chave '{t}'")

    # linhas da Fundação que o texto novo cita, por palavra-chave (só nos arquivos da pasta)
    if not commit:
        fund = (raiz / "00_Fundacao_Cultura_Liquida.md").read_text(encoding="utf-8").splitlines()
        citadas = [(112, "não admitida"), (114, "nunca recusa"), (133, "julgamento de Vicente"),
                   (394, "quarentena, com o seu selo"), (396, "o portão é combinado"),
                   (472, "uma semana de trabalho de curadoria"), (473, "quem propõe não aprova"),
                   (498, "cota de juízo humano"), (506, "claude/"), (512, "uma tela"), (575, "passa por profissional"),
                   (592, "Reabrem o Recorte"), (605, "nunca recusa"), (628, "Vicente, pelo portão"), (638, "em tensão"),
                   (733, "candidatos"), (787, "profissional habilitado"), (812, "PENDENTE_JULGAMENTO"),
                   (902, "Até 15 itens por semana")]
        for n, palavra in citadas:
            if palavra not in fund[n - 1]:
                problemas.append(f"Fundação l. {n}, citada nos ajustes, não traz '{palavra}'")

    # 3. A nota do roteiro e as linhas que ela cita (contadas com a nota no arquivo)
    if "**Nota de ajuste (22/10/2026" not in roteiro:
        problemas.append("roteiro sem a nota de ajuste do K-003")
    else:
        linhas = roteiro.splitlines()
        esperado = [(17, "claude/"), (18, "quarentena"), (19, "uma tela"), (85, "quarentena"), (86, "amostra"),
                    (92, "amostra"), (103, "fila"), (104, "ramificação"), (106, "amostra"), (122, "uma tela"),
                    (172, "quarentena"), (178, "juízo humano"), (187, "fila")]
        for n, palavra in esperado:
            if n > len(linhas) or palavra not in linhas[n - 1]:
                problemas.append(f"roteiro l. {n}, citada na nota, não traz '{palavra}'")

    # 4. O quadro
    if "Só os de conflito e os de Falta jurídica a liberar chamam Vicente" not in quadro:
        problemas.append("quadro: o texto da operação ainda não diz quais cartões chamam Vicente")
    if not re.search(r"^\| Fazendo[^|]*\| \*\*K-003\*\*", quadro, re.M):
        problemas.append("quadro: K-003 não está em Fazendo")

    # 5. O que o K-101 grava em .claude/: as linhas que o bloco 1 cita têm de trazer o que ele diz (achado AUD-K003-05)
    info = []
    citadas_claude = [
        (".claude/agents/curador.md", 20, "Começa pela retomada"),
        (".claude/agents/curador.md", 37, "relatório de uma tela"),
        (".claude/agents/curador.md", 43, "D-015 a D-030"),
        (".claude/agents/avaliador.md", 32, "vai para a quarentena com o selo"),
        (".claude/skills/extrair-evidencia/SKILL.md", 19, "quarentena com `PENDENTE_JULGAMENTO`"),
        (".claude/skills/extrair-evidencia/SKILL.md", 23, "vai para a quarentena"),
        (".claude/skills/extrair-evidencia/SKILL.md", 24, "para a cota humana"),
        (".claude/skills/executar-brief/SKILL.md", 18, "2026-10-15_pesquisa/clb-execucao-v0.2-brief.md"),
        (".claude/skills/executar-brief/SKILL.md", 26, "--teto 600000"),
        (".claude/skills/executar-brief/SKILL.md", 43, "600 mil"),
    ]
    for rel, n, e in citadas_claude:
        try:
            linhas_c = ler(raiz, rel, commit).splitlines()
        except Exception:
            problemas.append(f"{rel}: não abriu")
            continue
        if n > len(linhas_c) or e not in linhas_c[n - 1]:
            problemas.append(f"{rel}, l. {n}, citada no bloco 1, não traz '{e}'")
        else:
            info.append(f"{rel}, l. {n}: '{e}' (a gravar no K-101)")
    # outras linhas com a mesma expressão, que o bloco 1 não cita pelo número
    for rel, exprs in {".claude/skills/executar-brief/SKILL.md": ["relatório de uma tela"]}.items():
        for n, linha in enumerate(ler(raiz, rel, commit).splitlines(), 1):
            for e in exprs:
                if e in linha:
                    info.append(f"{rel}, l. {n}: '{e}' (a gravar no K-101, pelo ritual relido)")

    print("Base:", f"commit {commit}" if commit else "arquivos da pasta")
    print("PROBLEMAS:" if problemas else "Sem problemas.")
    for p in problemas:
        print(" -", p)
    print(f"Para o K-101 ({len(info)}):")
    for i in info:
        print(" -", i)
    return 1 if problemas else 0


if __name__ == "__main__":
    sys.exit(main())
