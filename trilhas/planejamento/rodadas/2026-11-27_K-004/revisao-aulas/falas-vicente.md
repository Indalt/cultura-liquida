# Revisão das aulas do caju (O3, K-121): falas de Vicente, 27 e 28/11/2026

Trilha da conversa em que Vicente revisou as 5 aulas (`campo_de_acao/aulas-caju/`, commit 3b11877). As falas ficam aqui como fala original (o `fala_original_ref` da D-063). **Não se copiam para as instruções de geração** (habilidades, agentes, prompts): lá vai só a regra (fala 6).

## Fala 1 (27/11)
"sobre as aulas-caju, dei uma revisada com a ajuda de outra llm. a aula 1 me parece uma aula sobre o sistema cultura liquida e nao sobre as culturas liquidas do caju. ficaria melhor se falassemos da ciencia que o sistema usa e nem precisa mencionar o sistema em nenhuma aula. em outro lugar pode-se dar uma aula sobre o sistema e como ele age sobre as culturas liquidas. alias, pode-se fazer uma aula a parte, separada do programa como a ferramenta desenvolvida para as aulas dizendo que como ja se usa ia em tudo no mundo, resolvi usar a ia do jeito que acho que a ciencia poderia usar (ou outra defesa humilde tb para nao hiperdimensionar a importancia disso porque vou falar que todo mundo pode usar os metodos das ciencias para usar em suas areas de conhecimento)."

Depois, a 1ª crítica de outra LLM (em [critica-llm-1.md](critica-llm-1.md)).

## Fala 2 (27/11)
"para dar uma aula sobre como montei esse sistema eu teria de explicar o porque de usar cada escolha da ciencia? eu tive receio disso porque nao sou seguro 100%, apenas sei que os metodos existem e que aplicar metodo reforça o conhecimento."

## Fala 3 (27/11)
"nao. aula sobre o sistema vai para campo de ação e pode existir como pratica pedagogica do campo de ação. isso talvez entre pro backlog, mas essa especifica do caju ja entra na pasta aulas-caju"

## Fala 4 (27/11)
"sim, deve-se citar as fontes. eu nao consigo ler o kit agora. me entregue o que outra llm deve ler para criticar"

Depois, a 2ª crítica de outra LLM, sobre o kit (em [critica-llm-2-kit.md](critica-llm-2-kit.md)).

## Fala 5 (28/11)
"a primeira aula ainda traz conteudo sobre o programa. e pior, nao explica o que é programa e nao explica o que é μ. a aula 2 começa o que a aula 1 poderia fazer e pior, nao fala sobre a ciencia e sobre o programa que tb poderia ser tratada na aula 1 em 5 minutos. pelo jeito todas as aulas estao contaminadas com as ideias do sistema. é importante que o produz a aula seja revisto. o programa poderia ser uma apresentação do conjunto de aulas e ser uma aula em si tirando da aula 1 essas obrigações. não precisa explicar como o que proziu as aulas foi feito. isso seria o papel apenas do kit fonte que pode ser uma aula completa e didatica, e sem ter nem de mencionar o programa. o programa (sistema - essa palavra deve ser usada ao inves de programa porque programa pode ser programa de aulas por exemplo) nao colocar as minhas palavras nos codigos de geracao de aula. tudo isso me parece bem simples e intuititvo, me preocupa eu ter de falar isso. planejar como e o que mudar antes de agir"

## Fala 6 (28/11)
"1. desnecessario eu dizer que programa é uma palavra polissemica. 2. neste caso o programa sempre fará parte da aula 1 - será breve para ser dado em no maximo 15 minutos por tratar de topicos. precisa encantar quem vai acompanhar as proximas aulas. desnecessario colocar um script de conferencia para procurar o que nao foi produzido. se as aulas nao dizem pra fazer nao vai encontrar. ja deve ter scripts de conferencia do campo de acao e este talvez precise ser atualizado. desnecessario tb fazer dupla conferencia se o agente for bem pensado. Caso nao tenha, esse agente deveria ser responsavel por todo o campo de acao e carregar as habilidades necessarias para cada acao. o kit é uma explicacao breve e simples para o professor e no final uma aula que qualquer professor poderia dar para o grande publico para explicar como o programa de aulas foi feito com base nas ciencias. isso pode incluir um breve comentario sobre a didatica. 3. nota de educador pode incluir espaço para digitar anotacoes ou manuscrito. vamos fazer isso agora e com um prompt em uma nova sessao se nao houver mais um sprint O1 o2 ou 3para liberar o sistema. me traga sugestoes e modelos pedagogicos, assim como para as outras tarefas do campo de ação."

## Fala 7 (28/11)
"O guia para salvaguarda é algo que tb vai mudar. é muito pretensioso criar uma guia para um orgao que faz guias há decadas. isso foi passando para nao gerar muitas tarefas, mas ainda nao toquei nele por isso. e nao vamos tocar agora. nao precisa usar agente pra isso agora. apenas anote isso ao criar ou mudar o agente. o programa de aula nao é fixo em 5, pode ser 3, 1 etc. esse do caju ja pode se adequar a isso e ao inves de caju falamos da cajuina tornando o caju como parte do que se fala da cajuina, obviamente. topo olhar o que o agente se propoe a fazer de forma resumida antes de mudar novamente. pode ser interessante, mas tem de ser capaz de se adaptar ao publico, certo? se adaptar tb ao educador que poderia ser um indigena."

## Fala 8 (28/11)
"1 esse agente pode ser um script? 2 corresponde e vale para qualquer educador, tem de ser adaptavel e nao apenas para educador indigena."

## Fala 9 (28/11)
"entao se depender de IA, deve-se incluir nas habilidades dos respectivos agentes (que devem estar conectados e serem necessarias para os agentes) o que um script faria para nao gastar tokens fazendo, isso é possivel? ajudaria na economia? e como nao deixar a IA criar coisas que nao estao no cultura liquida? sim, o educador pode fazer na nota se nao atrapalhar o programa. acho que nao atrapalha. o programa é da CLB, no grupo de aulas que estamos trabalhando cajuina."

## Fala 10 (28/11)
"pode" (ao resumo: D-063 ampliada, agente com a nota do guia, habilidade só com blocos, `scripts/montar_programa.py`, Prompt 2b acertado, a regra geral para todos os agentes no backlog).

## O que a sessão reconheceu como causa (28/11)
1. A encomenda do O3 (`sprint-1.md`, seção 3, "O pedido") mandava o fio das aulas seguir as dimensões da ferramenta, praticar "o rigor da casa" com códigos de decisão, dizer o μ em aula e marcar cada frase com PR. O agente cumpriu a encomenda.
2. O campo-de-acao só tinha a habilidade do kit, escrita na língua interna do sistema; não havia habilidade de planejar aula.
3. A conferência do O3 olhou marcas, dado pessoal e carimbo; não olhou se a aula tratava do assunto. Não havia script próprio do campo de ação: a conferência estava escrita no prompt.
