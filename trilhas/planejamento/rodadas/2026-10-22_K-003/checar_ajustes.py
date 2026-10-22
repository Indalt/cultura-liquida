"""Checagem mecânica dos ajustes do K-003 (D-036 e D-037), aprovados pela D-038 e com a D-039, no brief, no roteiro e no quadro, sem IA.

Uso:
    python checar_ajustes.py <raiz do repositório>                 -> confere os arquivos da pasta (tem de passar)
    python checar_ajustes.py <raiz do repositório> --commit 71dafff -> confere os arquivos de antes dos ajustes (tem de reprovar)
    python checar_ajustes.py <raiz do repositório> --commit 4e7b3fd -> confere os arquivos de antes da aprovação (tem de reprovar)
Código 0 = passa; 1 = reprova. As linhas de `.claude/` que o K-101 muda saem como informação, sem reprovar.
Histórico: 22/10/2026, primeira versão (ajustes, verificação e releitura); 22/10/2026, fechamento (D-038 e D-039:
sem marcas de aprovação pendente, K-003 em Concluído, as decisões no brief, no AGENTS.md e nos arquivos da rodada).
"""
import re
import subprocess
import sys
from pathlib import Path

BRIEF = "trilhas/2026-10-17_caminhos/brief-execucoes-v0.1.md"
ROTEIRO = "trilhas/2026-10-17_caminhos/caminhos.md"
QUADRO = "trilhas/planejamento/quadro.md"
AGENTS = "AGENTS.md"
PONTOS = "trilhas/planejamento/rodadas/2026-10-22_K-003/pontos-em-aberto.md"
ESTADO = "trilhas/planejamento/estado-planejamento.md"
DECISOES = ["trilhas/decisoes/D-038.json", "trilhas/decisoes/D-039.json"]


def ler(raiz: Path, rel: str, commit: str | None) -> str:
    if commit:
        r = subprocess.run(["git", "-C", str(raiz), "show", f"{commit}:{rel}"],
                           capture_output=True, encoding="utf-8")
        if r.returncode != 0:
            raise FileNotFoundError(f"{rel} não existe no commit {commit}")
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

    # 1. Expressões que a D-036 e a D-037 superaram, e as marcas de aprovação pendente que a D-038 fechou
    #    (permitido_se: a expressão pode ficar na linha que traz essa outra)
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
        ("o curador a abria numa conversa de trabalho", "substitui"),
        ("o curador a abre numa conversa de trabalho", None),
        # achados da verificação do K-003 (AUD-K003-01 e 02); a leitura do cartão de conflito vale desde a D-038
        ("não conta na fila até lá", None),
        ("ele confere a nossa leitura das Evidências em tensão", "D-038"),
        # releitura de 22/10: ambiguidades de redação corrigidas
        ("Prioridade entre frentes**", None),
        ("relatório calculado das frentes (l. 512)", None),
        ("o relatório calculado das frentes e do dia", None),
        ("a traz por acaso", None),
        ("até 15 itens por amostra", None),
        ("o que falha no portão é revertido com trilha", None),
        ("valor provisório novo (D-034)", None),
        ("que junta o que a amostra achou", None),
        ("uma semana de curadoria são até 15", None),
        ("uma semana de curadoria = até 15", None),
        ("depois da aprovação de Vicente.**", None),
        ("só até a v0.2.1, muda o plano", None),
        ("D-034 ou decisão própria (pendente)", None),
        ("Vicente aprova a v0.3 (acordo 5). Sem a aprovação, valem a v0.2.1", None),
        ("teto de 15; padrão proposto A-04", None),
        # fechamento (D-038): marcas de aprovação pendente
        ("a aprovar por Vicente", None),
        ("padrão proposto", None),
        ("padrões propostos", None),
        ("ponto levado a Vicente no K-003", None),
        ("ponto levado a ele no K-003", None),
        ("que vale com a aprovação", None),
        ("valem só com a aprovação de Vicente", None),
        ("Até ela, nenhum cartão do desenvolvimento começa", None),
        ("que ele confirma ao aprovar", None),
        ("salvo outro valor que Vicente indicar ao aprovar", None),
        ("que Vicente pode trocar ao aprovar", None),
        ("só depois do registro no bloco 0, com a aprovação de Vicente", None),
        # fechamento (D-039): um cartão de lista único; a CLB pelo termo
        ("cartão de CLB candidata", None),
        ("o da CLB situada nova", None),
        ("Qual é a CLB situada do piloto", None),
    ]
    for n, linha in enumerate(brief.splitlines(), 1):
        baixa = linha.lower()
        for expr, permitido_se in proibidas:
            if expr.lower() in baixa and not (permitido_se and permitido_se in linha):
                problemas.append(f"brief l. {n}: ainda diz '{expr}'")
        # a leitura proposta da Actions (bloco 10) segue como parada; as do K-003 (A-03 e A-06) não
        if ("leitura proposta" in baixa or "leituras propostas" in baixa) and ("A-03" in linha or "A-06" in linha):
            problemas.append(f"brief l. {n}: ainda chama de proposta a leitura A-03 ou A-06")

    # 2. O quadro de ajustes: o que vale quando, com as D-038 e D-039
    ajustes = secao(brief, "**Ajustes das D-036 e D-037", "\n---")
    if not ajustes:
        problemas.append("brief sem o quadro 'Ajustes das D-036 e D-037'")
    for a in ["A-01", "A-02", "A-03", "A-04", "A-05", "A-06", "A-07", "A-08", "A-09", "A-10", "A-11", "A-13"]:
        if ajustes and a not in ajustes:
            problemas.append(f"quadro de ajustes sem o {a}")
    for t in ["O que vale quando", "commit 71dafff", "4e7b3fd", "D-038", "D-039", "Vicente decide as regras",
              "K-005", "cartão de lista", "papel trocável", "fonte de verdade única", "nunca a prática",
              "fora da amostra"]:
        if ajustes and t not in ajustes:
            problemas.append(f"quadro de ajustes sem '{t}'")
    s2 = secao(brief, "## 2. Decisões vigentes", "## 3.")
    for d in range(15, 40):
        if not re.search(rf"^\| D-0{d} \|", s2, re.M):
            problemas.append(f"seção 2 sem a linha da D-0{d}")
    retomada = secao(brief, "**Retomada:", "## 2.")
    for t in ["quadro.md", "estado-planejamento.md", "mover o cartão"]:
        if t not in retomada:
            problemas.append(f"retomada sem '{t}'")
    b1 = secao(brief, "### Bloco 1 ", "### Bloco 2 ")
    for t in ["curador.md", "avaliador.md", "extrair-evidencia", "executar-brief", "conferir-fato",
              "insumo 5", "insumo 7", "insumo 17", "--teto 300000", "A-01", "A-02", "A-05", "A-06",
              "versão da regra", "D-038", "D-039"]:
        if t not in b1:
            problemas.append(f"bloco 1 sem '{t}'")
    b2 = secao(brief, "### Bloco 2 ", "### Bloco 3 ")
    for t in ["A-03", "A-04", "A-05", "A-09", "candidata", "D-038", "D-039", "unidade da ficha",
              "identificada pelo termo", "institucional", "lastro, trecho localizado e voz", "versão da regra",
              "K-005", "aviso, saúde ou política", "outro termo"]:
        if t not in b2:
            problemas.append(f"bloco 2 sem '{t}'")
    b5 = secao(brief, "### Bloco 5 ", "### Bloco 6 ")
    for t in ["cartões de conflito", "Falta jurídica a liberar", "CLB candidata", "não se julga a prática", "A-05", "A-10",
              "D-032", "D-038", "D-039", "cartão de lista", "confere a nossa leitura", "nunca a prática"]:
        if t not in b5:
            problemas.append(f"bloco 5 sem '{t}'")
    # cada padrão nos lugares onde o brief o aplica (achado AUD-K003-06), e as decisões do fechamento
    s3a = secao(brief, "### 3a.", "### 3b.")
    s3b = secao(brief, "### 3b.", "## 4.")
    b3 = secao(brief, "### Bloco 3 ", "### Bloco 4 ")
    b7 = secao(brief, "### Bloco 7 ", "### Bloco 8 ")
    b8 = secao(brief, "### Bloco 8 ", "### Entre os blocos 8 e 9")
    k102 = secao(brief, "### Entre os blocos 8 e 9", "### Bloco 9 ")
    b11 = secao(brief, "### Bloco 11 ", "### Bloco 12 ")
    for nome, parte, padroes in [("seção 3a", s3a, ["A-04", "D-038", "aviso, saúde ou política"]),
                                 ("seção 3b", s3b, ["A-10", "D-038"]),
                                 ("bloco 3", b3, ["A-04"]),
                                 ("bloco 7", b7, ["A-04", "A-05", "D-038", "D-039", "aviso, saúde ou política",
                                                  "institucional"]),
                                 ("bloco 8", b8, ["A-04", "D-038", "D-039", "aviso, saúde ou política",
                                                  "identificada pelo termo"]),
                                 ("seção do K-102", k102, ["A-09 (b)", "D-039", "cartão de lista"]),
                                 ("bloco 11", b11, ["K-114", "D-038", "insumo 25"])]:
        for p in padroes:
            if p not in parte:
                problemas.append(f"{nome} sem '{p}'")
    if "D-017" not in b3:
        problemas.append("bloco 3: a lista do sorteio tem de vir como exemplo (D-017)")
    if "Script de menções incidentais (cartão K-102)" not in brief:
        problemas.append("brief sem a seção do script de menções incidentais (K-102)")
    b10 = secao(brief, "### Bloco 10 ", "### Bloco 11 ")
    if b10.count("A-10") < 3:
        problemas.append(f"bloco 10 cita o A-10 {b10.count('A-10')} vez(es); esperado: 3 ou mais")
    for t in ["D-038", "D-039", "cartão de lista", "outro termo"]:
        if t not in b10:
            problemas.append(f"bloco 10 sem '{t}'")
    b13 = secao(brief, "### Bloco 13 ", "### Bloco 14 ")
    if "A-08" not in b13:
        problemas.append("bloco 13 sem o A-08 (horas relidas)")
    op = secao(brief, "### Depois do bloco 14", "## 5.")
    for t in ["A-09 b", "D-036", "K-102", "D-038", "D-039", "cartão de lista", "outro termo"]:
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
        "D-038": ["Regra-mãe", "Vicente decide as regras", "nunca a prática", "fora da amostra",
                  "versão da regra", "quem propõe não aprova", "papel trocável", "K-005", "K-114"],
        "D-039": ["pelo termo", "ambíguo", "fonte de verdade única", "institucional", "lastro, trecho localizado e voz",
                  "nasce candidata", "outro termo", "único cartão de lista", "todas as CLB"],
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
                   (473, "aviso, saúde ou política"),
                   (498, "cota de juízo humano"), (506, "claude/"), (512, "uma tela"), (516, "unidade da ficha"),
                   (575, "passa por profissional"), (592, "Reabrem o Recorte"), (597, "perspectiva"),
                   (605, "nunca recusa"), (605, "bebida × Lugar × grupo × período"), (613, "conceito"),
                   (624, "agentes e Vicente"), (626, "confere a nossa leitura"),
                   (628, "Vicente, pelo portão"), (638, "em tensão"),
                   (733, "candidatos"), (787, "profissional habilitado"), (811, "Unidade da ficha"),
                   (812, "PENDENTE_JULGAMENTO"), (880, "relação entre um nome"),
                   (902, "Até 15 itens por semana")]
        for n, palavra in citadas:
            if palavra not in fund[n - 1]:
                problemas.append(f"Fundação l. {n}, citada nos ajustes, não traz '{palavra}'")

    # 3. A nota do roteiro e as linhas que ela cita (contadas com a nota no arquivo)
    if "**Nota de ajuste (22/10/2026" not in roteiro:
        problemas.append("roteiro sem a nota de ajuste do K-003")
    else:
        nota = next((l for l in roteiro.splitlines() if l.startswith("**Nota de ajuste (22/10/2026")), "")
        if "a aprovar" in nota or "padrões propostos" in nota:
            problemas.append("roteiro: a nota de ajuste ainda tem marca de aprovação pendente")
        for t in ["D-038", "D-039"]:
            if t not in nota:
                problemas.append(f"roteiro: a nota de ajuste sem a {t}")
        linhas = roteiro.splitlines()
        esperado = [(17, "claude/"), (18, "quarentena"), (19, "uma tela"), (85, "quarentena"), (86, "amostra"),
                    (91, "CLB situada"), (92, "amostra"), (103, "fila"), (104, "ramificação"), (106, "amostra"),
                    (122, "uma tela"), (172, "quarentena"), (173, "Unidade da ficha"), (178, "juízo humano"),
                    (187, "fila")]
        for n, palavra in esperado:
            if n > len(linhas) or palavra not in linhas[n - 1]:
                problemas.append(f"roteiro l. {n}, citada na nota, não traz '{palavra}'")

    # 4. O quadro
    if "Só os de conflito e os de Falta jurídica a liberar chamam Vicente" not in quadro:
        problemas.append("quadro: o texto da operação ainda não diz quais cartões chamam Vicente")
    if re.search(r"^\| Fazendo[^|]*\| \*\*K-003\*\*", quadro, re.M):
        problemas.append("quadro: K-003 ainda em Fazendo")
    if not re.search(r"^\| Concluído[^|]*\| \*\*K-003\*\*", quadro, re.M):
        problemas.append("quadro: K-003 não está em Concluído")
    for t in ["cartão de lista", "D-038", "D-039"]:
        if t not in quadro:
            problemas.append(f"quadro sem '{t}'")

    # 5. As decisões registradas e o que as leva adiante
    for rel in DECISOES:
        try:
            dec = ler(raiz, rel, commit)
        except Exception:
            problemas.append(f"{rel}: não existe")
            continue
        if '"confirmada_por_vicente": true' not in dec or '"marcador": "VIGENTE"' not in dec:
            problemas.append(f"{rel}: sem a confirmação de Vicente ou sem o marcador VIGENTE")
    for rel, termos, proibido in [(AGENTS, ["**D-038:**", "**D-039:**", "Cartão K-003 feito"], "a aprovar por Vicente"),
                                  (PONTOS, ["D-038", "D-039", "Decidido em 22/10"], "a aprovar por Vicente"),
                                  (ESTADO, ["K-003 concluído", "D-039"], "a aprovar por Vicente")]:
        try:
            texto = ler(raiz, rel, commit)
        except Exception:
            problemas.append(f"{rel}: não abriu")
            continue
        for t in termos:
            if t not in texto:
                problemas.append(f"{rel} sem '{t}'")
        if proibido in texto:
            problemas.append(f"{rel} ainda diz '{proibido}'")

    # 6. O que o K-101 grava em .claude/: as linhas que o bloco 1 cita têm de trazer o que ele diz (achado AUD-K003-05)
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
