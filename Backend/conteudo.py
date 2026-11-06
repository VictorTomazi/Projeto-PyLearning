"""
conteudo.py — Central de lições baseada no cronograma do Curso em Vídeo.
Padrão: 8 bolinhas por módulo (Teoria, Objetivas, Prática intercaladas).
"""

MODULOS_E_LICOES = [
    # ======================================================================
    # MÓDULO 1: Primeiros Comandos (Equivalente à Aula 4)
    # ======================================================================

    # --- Bolinha 1: 1 Aula ---
    {
        "id_modulo": 1, "id_etapa": 1, "tipo": "TEORIA",
        "titulo": "O que é o Python?",
        "enunciado": "O Python é uma linguagem super amigável. Para pedir que o computador mostre uma mensagem na tela, usamos a função `print()`. \n\nRegra de Ouro: Textos precisam estar sempre abraçados por aspas (simples ou duplas). \n\nExemplo: `print('Olá, Mundo!')`.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 2: 2 Objetivas ---
    {
        "id_modulo": 1, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "Comando de Saída",
        "enunciado": "Qual é a forma correta de fazer o Python exibir a palavra 'Brasil' na tela?",
        "opcoes": ["escreva(Brasil)", "print('Brasil')", "print(Brasil)", "mostrar 'Brasil'"],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 1, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "O Detalhe das Aspas",
        "enunciado": "O que acontece se você rodar o código `print(Olá)` sem aspas?",
        "opcoes": ["O texto aparece normalmente.", "Aparece em negrito.", "O Python dá erro, pois acha que 'Olá' não é um texto, mas sim uma variável que não existe.", "O código roda, mas a tela fica em branco."],
        "gabarito": "C", "xp_recompensa": 10
    },

    # --- Bolinha 3: 1 Aula ---
    {
        "id_modulo": 1, "id_etapa": 3, "tipo": "TEORIA",
        "titulo": "Guardando Informações",
        "enunciado": "Na programação, usamos **Variáveis** para guardar dados. Pense nelas como caixas com nomes. \n\nPara colocar algo na caixa, usamos o sinal `=`. \nExemplo: `idade = 20`. O Python guardou o número 20 na caixa chamada 'idade'. Se fizermos `print(idade)` (sem aspas!), ele mostra 20.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 4: 1 Escrever ---
    {
        "id_modulo": 1, "id_etapa": 4, "tipo": "PRATICA",
        "titulo": "Sua Primeira Variável",
        "enunciado": "Crie uma variável chamada `curso` e guarde o texto 'Python' dentro dela. Na linha de baixo, use o `print` para mostrar o conteúdo da sua variável.",
        "opcoes": None, "gabarito": "Python\n", "xp_recompensa": 20
    },

    # --- Bolinha 5: 1 Aula ---
    {
        "id_modulo": 1, "id_etapa": 5, "tipo": "TEORIA",
        "titulo": "Conversando com o Usuário",
        "enunciado": "Para perguntar algo a quem está usando o programa, usamos o `input()`. O programa pausa e espera a pessoa digitar.\n\nExemplo: `nome = input('Qual seu nome? ')`. \n\nO que for digitado no teclado será imediatamente guardado na variável 'nome'.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 6: 2 Objetivas ---
    {
        "id_modulo": 1, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "Entendendo o Input",
        "enunciado": "Qual é a principal diferença entre `print()` e `input()`?",
        "opcoes": ["Ambos fazem exatamente a mesma coisa.", "Print pergunta algo, input mostra a resposta.", "Print exibe mensagens na tela, input captura dados digitados no teclado.", "Input só aceita números matemáticos."],
        "gabarito": "C", "xp_recompensa": 10
    },
    {
        "id_modulo": 1, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "A Armadilha do Texto",
        "enunciado": "CUIDADO: Tudo que o `input()` captura vem em formato de texto. Se você fizer `x = input('Idade: ')` e a pessoa digitar 18, o que o Python guarda?",
        "opcoes": ["O número matemático 18", "O texto '18' (string)", "O número decimal 18.0", "Um erro estrutural"],
        "gabarito": "B", "xp_recompensa": 10
    },

    # --- Bolinha 7: 1 Aula ---
    {
        "id_modulo": 1, "id_etapa": 7, "tipo": "TEORIA",
        "titulo": "Convertendo Tipos",
        "enunciado": "Como o `input()` só devolve textos, não podemos fazer matemática com ele direto. O texto '5' mais o texto '2' vira '52'!\n\nPrecisamos converter o texto em número inteiro usando a função `int()`. \nFica assim: `idade = int(input('Qual sua idade? '))`. Agora o Python entende que é um número para calcular.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 8: 2 Objetivas + 1 Escrever ---
    {
        "id_modulo": 1, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "A Soma Bizarra",
        "enunciado": "Um aluno fez o seguinte:\na = input('Número 1: ')\nb = input('Número 2: ')\nprint(a + b)\n\nSe ele digitar 5 e 2, qual será o resultado na tela?",
        "opcoes": ["7", "Vai dar erro", "52", "0"],
        "gabarito": "C", "xp_recompensa": 10
    },
    {
        "id_modulo": 1, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "A Solução",
        "enunciado": "Qual função o aluno deveria ter usado ao redor do input para transformar o texto capturado em um número inteiro?",
        "opcoes": ["str()", "float()", "int()", "soma()"],
        "gabarito": "C", "xp_recompensa": 10
    },
    {
        "id_modulo": 1, "id_etapa": 8, "tipo": "PRATICA",
        "titulo": "O Grande Desafio (Sem input)",
        "enunciado": "Vamos testar variáveis e cálculos! \nCrie a variável `a` com o valor 10 e a variável `b` com o valor 5. \nDepois, use o comando print para mostrar a soma exata de `a + b`.",
        "opcoes": None, "gabarito": "15\n", "xp_recompensa": 25
    },

    # ======================================================================
    # ETAPA 9: TESTE FINAL DO MÓDULO 1 (O Troféu)
    # 7 Exercícios (2 Obj, 1 Prática, 3 Obj, 1 Prática)
    # ======================================================================

    # --- 2 Objetivas Iniciais ---
    {
        "id_modulo": 1, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão Geral: Saída",
        "enunciado": "Para que serve a função print() no Python?",
        "opcoes": ["Para capturar o que o usuário digita.", "Para exibir informações e textos na tela.",
                   "Para criar variáveis na memória.", "Para converter textos em números inteiros."],
        "gabarito": "B", "xp_recompensa": 15
    },
    {
        "id_modulo": 1, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão Geral: Variáveis",
        "enunciado": "Se criarmos `escola = 'CEUNSP'` e depois fizermos `print(escola)`, o que aparece na tela?",
        "opcoes": ["A palavra 'escola'", "CEUNSP", "Dá erro de aspas", "Nada"],
        "gabarito": "B", "xp_recompensa": 15
    },

    # --- 1 Prática Intermediária ---
    {
        "id_modulo": 1, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Prática de Fixação",
        "enunciado": "Crie uma variável chamada `pontos` e atribua a ela o valor numérico 100. Na linha seguinte, mostre o valor da variável na tela.",
        "opcoes": None, "gabarito": "100\n", "xp_recompensa": 30
    },

    # --- 3 Objetivas de Raciocínio ---
    {
        "id_modulo": 1, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão Geral: Entrada",
        "enunciado": "Por que precisamos usar a função int() quando pedimos a idade de alguém com o input() e queremos fazer cálculos depois?",
        "opcoes": ["Porque o input() sempre devolve textos (strings), e não podemos fazer matemática com textos.",
                   "Porque o int() deixa o texto mais bonito.", "Porque o Python não aceita números sem o int().",
                   "Para evitar que o programa trave se a pessoa digitar letras."],
        "gabarito": "A", "xp_recompensa": 20
    },
    {
        "id_modulo": 1, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Caça ao Bug",
        "enunciado": "Qual das alternativas abaixo possui um erro de sintaxe que faria o programa quebrar?",
        "opcoes": ["print('123')", "numero = 10", "print(Olá Mundo)", "nome = input('Nome: ')"],
        "gabarito": "C", "xp_recompensa": 20
    },
    {
        "id_modulo": 1, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Leitura de Código",
        "enunciado": "O que o código abaixo faz?\n\nx = '5'\ny = '5'\nprint(x + y)",
        "opcoes": ["Mostra 10", "Mostra 55", "Mostra x + y", "Dá erro matemático"],
        "gabarito": "B", "xp_recompensa": 20
    },

    # --- 1 Prática Final (O Chefe) ---
    {
        "id_modulo": 1, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Desafio Final do Módulo 1",
        "enunciado": "Mostre que você dominou o básico! Crie uma variável `saudacao` com o texto 'Bem-vindo, '. Crie uma variável `jogador` com o texto 'Victor'. Faça um único print que some (concatene) as duas variáveis para exibir a mensagem completa.",
        "opcoes": None, "gabarito": "Bem-vindo, Victor\n", "xp_recompensa": 50
    },

    # ======================================================================
    # MÓDULO 2: Operadores Aritméticos (Equivalente à Aula 7 do Curso em Vídeo)
    # ======================================================================

    # --- Bolinha 1: Teoria Introdutória ---
    {
        "id_modulo": 2, "id_etapa": 1, "tipo": "TEORIA",
        "titulo": "A Matemática do Python",
        "enunciado": "O Python é uma excelente calculadora. Para fazer operações básicas, usamos os operadores aritméticos padrão:\n\n`+` (Adição)\n`-` (Subtração)\n`*` (Multiplicação - usamos o asterisco!)\n`/` (Divisão)\n\nVocê pode fazer as contas diretamente no print. Se rodar `print(5 * 2)`, o Python fará a conta e exibirá apenas o resultado (10).",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 2: Objetiva Fácil ---
    {
        "id_modulo": 2, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "O Operador de Multiplicação",
        "enunciado": "Como você pediria para o Python multiplicar 4 por 3 corretamente?",
        "opcoes": ["print(4 x 3)", "print(4 * 3)", "print(4.3)", "print(4 X 3)"],
        "gabarito": "B", "xp_recompensa": 10
    },

    # --- Bolinha 3: Teoria Nível 2 (Operadores Especiais) ---
    {
        "id_modulo": 2, "id_etapa": 3, "tipo": "TEORIA",
        "titulo": "Os Três Operadores Diferentões",
        "enunciado": "Além das contas normais, o Python tem três operadores poderosos:\n\n1. `**` (Potência): Para fazer 5 elevado a 2 (5²), fazemos `5 ** 2`.\n2. `//` (Divisão Inteira): Divide, mas ignora a vírgula. `5 // 2` resulta em 2 (e não 2.5).\n3. `%` (Resto da Divisão/Módulo): Mostra o que 'sobrou'. `5 % 2` resulta em 1, porque 5 dividido por 2 dá 2 e sobra 1 inteiro.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 10
    },

    # --- Bolinha 4: Objetiva Média ---
    {
        "id_modulo": 2, "id_etapa": 4, "tipo": "OBJETIVA",
        "titulo": "Entendendo o Módulo",
        "enunciado": "Se você executar o código `print(10 % 3)`, qual será o número exato exibido na tela?",
        "opcoes": ["3.33", "3", "1", "0"],
        "gabarito": "C", "xp_recompensa": 15
    },

    # --- Bolinha 5: Objetiva Média (Ordem de Precedência) ---
    {
        "id_modulo": 2, "id_etapa": 5, "tipo": "OBJETIVA",
        "titulo": "Quem resolve primeiro?",
        "enunciado": "O Python segue uma Ordem de Precedência. Primeiro resolve-se o que está nos `()`, depois potências `**`, depois `* / // %`, e por último `+ e -`.\n\nSabendo disso, qual o resultado de: `print(5 + 3 * 2)`?",
        "opcoes": ["16", "11", "10", "15"],
        "gabarito": "B", "xp_recompensa": 15
    },

    # --- Bolinha 6: Prática Nível 1 ---
    {
        "id_modulo": 2, "id_etapa": 6, "tipo": "PRATICA",
        "titulo": "Calculadora de Frota",
        "enunciado": "Você está administrando uma frota no Euro Truck Simulator 2 e quer expandir. Crie um programa com um único comando `print()` que calcule o valor de 3 caminhões Volvo FH4 multiplicados pelo custo de 150000 cada.",
        "opcoes": None, "gabarito": "450000\n", "xp_recompensa": 20
    },

    # --- Bolinha 7: Teoria Nível 3 (O Segredo das Strings) ---
    {
        "id_modulo": 2, "id_etapa": 7, "tipo": "TEORIA",
        "titulo": "Multiplicando Palavras?",
        "enunciado": "No Python, os operadores de Adição e Multiplicação também funcionam com textos (strings)!\n\nSe você usar `+` entre textos, ele junta tudo: `'Py' + 'thon'` vira `'Python'`.\nSe você usar `*` com um texto e um número, ele repete: `'Oi' * 3` vira `'OiOiOi'`. Isso é muito útil para criar barras de design no terminal: `print('-' * 20)`.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 15
    },

    # --- Bolinha 8: Objetiva Difícil ---
    {
        "id_modulo": 2, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "Análise de Código Textual",
        "enunciado": "Leia o código abaixo:\n\ntexto = 'A'\nprint(texto * 4)\n\nO que será exibido na tela?",
        "opcoes": ["A * 4", "4A", "AAAA", "Dá erro matemático"],
        "gabarito": "C", "xp_recompensa": 20
    },

    # ======================================================================
    # ETAPA 9: TESTE FINAL DO MÓDULO 2 (O Troféu)
    # 7 Exercícios (2 Obj, 1 Prática, 3 Obj, 1 Prática)
    # ======================================================================

    # --- 2 Objetivas Iniciais ---
    {
        "id_modulo": 2, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: Divisão Inteira",
        "enunciado": "Qual a diferença prática entre usar `/` e `//` no Python?",
        "opcoes": [
            "O `/` é para textos e `//` para números.",
            "O `/` faz a divisão normal com casas decimais (float), enquanto o `//` corta a vírgula e retorna a parte inteira.",
            "Não existe diferença, ambos mostram o mesmo resultado.",
            "O `//` serve para calcular o resto da divisão."
        ],
        "gabarito": "B", "xp_recompensa": 15
    },
    {
        "id_modulo": 2, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: Potência",
        "enunciado": "Qual das opções abaixo calcula corretamente 4 elevado ao cubo (4³)?",
        "opcoes": ["print(4 * 3)", "print(4 ** 3)", "print(4 ^ 3)", "print(4 // 3)"],
        "gabarito": "B", "xp_recompensa": 15
    },

    # --- 1 Prática Intermediária ---
    {
        "id_modulo": 2, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Prática de Precedência",
        "enunciado": "O resultado de `5 + 2 * 3` é 11. Recrie essa conta no `print()`, mas adicione parênteses no lugar certo para forçar a adição a acontecer primeiro, de modo que o resultado final seja 21.",
        "opcoes": None, "gabarito": "21\n", "xp_recompensa": 30
    },

    # --- 3 Objetivas de Raciocínio ---
    {
        "id_modulo": 2, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: O Resto (%)",
        "enunciado": "Na programação, o operador de resto (`%`) é extremamente útil para descobrir se um número é Par ou Ímpar. Se fizermos `x % 2`, e o resultado for zero, o que sabemos sobre o número 'x'?",
        "opcoes": [
            "Sabemos que ele é um número ímpar.",
            "Sabemos que ele é um número par, pois toda divisão exata por 2 não deixa restos.",
            "Sabemos que houve um erro no código.",
            "Sabemos que 'x' vale zero."
        ],
        "gabarito": "B", "xp_recompensa": 20
    },
    {
        "id_modulo": 2, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "O Perigo do Texto",
        "enunciado": "Um aluno que esqueceu de usar o `int()` fez o seguinte código:\na = '5'\nb = '3'\nprint(a + b)\n\nQual será o resultado?",
        "opcoes": ["8", "53", "Erro de tipo", "5 + 3"],
        "gabarito": "B", "xp_recompensa": 20
    },
    {
        "id_modulo": 2, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Análise de Variáveis",
        "enunciado": "Qual será o valor final da variável 'resultado'?\n\nvalor = 10\nresultado = (valor // 3) + (valor % 3)",
        "opcoes": ["4", "3", "1", "3.33"],
        "gabarito": "A", "xp_recompensa": 20
    },

    # --- 1 Prática Final (O Chefe) ---
    {
        "id_modulo": 2, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Desafio Final do Módulo 2",
        "enunciado": "Você precisa calcular a sua média de Ciência da Computação no CEUNSP. A nota da P1 foi 7 e a nota da P2 foi 9. Crie uma variável `p1` e uma variável `p2` com esses valores. Depois, faça um único `print()` que use a ordem de precedência (parênteses) para somar as duas notas e dividir o total por 2.",
        "opcoes": None, "gabarito": "8.0\n", "xp_recompensa": 50
    },

    # ======================================================================
    # MÓDULO 3: Utilizando Módulos (Equivalente à Aula 8 do Curso em Vídeo)
    # ======================================================================

    # --- Bolinha 1: Teoria Introdutória ---
    {
        "id_modulo": 3, "id_etapa": 1, "tipo": "TEORIA",
        "titulo": "O que são Módulos?",
        "enunciado": "Até agora usamos as funções básicas que já vêm ligadas no Python (como o `print` e `int`). Mas o Python tem 'caixas de ferramentas' extras chamadas de **Módulos** ou Bibliotecas.\n\nPara usar as ferramentas matemáticas avançadas, precisamos importar a caixa inteira usando o comando `import`.\n\nExemplo:\n`import math`",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 2: Objetiva Fácil ---
    {
        "id_modulo": 3, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "Trazendo a Caixa de Ferramentas",
        "enunciado": "Qual é o comando correto para trazer TODAS as funcionalidades matemáticas extras para o seu programa?",
        "opcoes": ["include math", "import math", "math.import()", "use math"],
        "gabarito": "B", "xp_recompensa": 10
    },

    # --- Bolinha 3: Teoria Nível 2 (Importação Específica) ---
    {
        "id_modulo": 3, "id_etapa": 3, "tipo": "TEORIA",
        "titulo": "Pegando só uma ferramenta",
        "enunciado": "Se você importar a caixa inteira (`import math`), para usar a Raiz Quadrada precisa digitar `math.sqrt(81)`.\n\nMas se você quiser trazer SÓ a Raiz Quadrada para o seu código, economizando memória, você usa o comando `from`:\n\n`from math import sqrt`\n\nFazendo isso, você pode usar direto: `print(sqrt(81))`.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 10
    },

    # --- Bolinha 4: Objetiva Média ---
    {
        "id_modulo": 3, "id_etapa": 4, "tipo": "OBJETIVA",
        "titulo": "A Diferença do From",
        "enunciado": "Se um programador escrever `from math import ceil` (que arredonda números para cima), como ele deve usar essa função na linha de baixo?",
        "opcoes": ["math.ceil(4.2)", "ceil.math(4.2)", "ceil(4.2)", "import.ceil(4.2)"],
        "gabarito": "C", "xp_recompensa": 15
    },

    # --- Bolinha 5: Objetiva Média (Arredondamentos) ---
    {
        "id_modulo": 3, "id_etapa": 5, "tipo": "OBJETIVA",
        "titulo": "Teto e Chão",
        "enunciado": "Dentro da biblioteca `math`, temos o `ceil` (teto = arredonda para cima) e o `floor` (chão = arredonda para baixo). Se você rodar `math.floor(5.9)`, qual será o resultado?",
        "opcoes": ["6", "5", "5.9", "0"],
        "gabarito": "B", "xp_recompensa": 15
    },

    # --- Bolinha 6: Prática Nível 1 ---
    {
        "id_modulo": 3, "id_etapa": 6, "tipo": "PRATICA",
        "titulo": "Calculando a Raiz",
        "enunciado": "Vamos testar o seu primeiro import! Na primeira linha, faça a importação completa da biblioteca `math`. Na segunda linha, use o `print` com `math.sqrt()` para mostrar a raiz quadrada do número 144.",
        "opcoes": None, "gabarito": "12.0\n", "xp_recompensa": 20
    },

    # --- Bolinha 7: Teoria Nível 3 (Módulo Random) ---
    {
        "id_modulo": 3, "id_etapa": 7, "tipo": "TEORIA",
        "titulo": "Números Aleatórios",
        "enunciado": "Outra biblioteca muito famosa (especialmente para criar jogos) é a `random`, que gera coisas aleatórias.\n\nSe você quiser que o computador sorteie um número inteiro entre 1 e 10, você faz:\n\n`import random`\n`numero = random.randint(1, 10)`",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 15
    },

    # --- Bolinha 8: Objetiva Difícil ---
    {
        "id_modulo": 3, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "Lendo o Sorteio",
        "enunciado": "Um desenvolvedor escreveu `sorteio = random.randint(5, 7)`. Quais são os únicos números que podem aparecer nessa variável?",
        "opcoes": ["5 e 7 apenas", "5, 6 e 7", "Qualquer número de 1 a 7", "Nenhuma das anteriores"],
        "gabarito": "B", "xp_recompensa": 20
    },

    # ======================================================================
    # ETAPA 9: TESTE FINAL DO MÓDULO 3 (O Troféu)
    # 7 Exercícios (2 Obj, 1 Prática, 3 Obj, 1 Prática)
    # ======================================================================

    # --- 2 Objetivas Iniciais ---
    {
        "id_modulo": 3, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: A Regra do Import",
        "enunciado": "Em qual parte do seu código você deve colocar os comandos de `import`?",
        "opcoes": [
            "No final do código, para não pesar a memória.",
            "Sempre na primeira linha (topo) do código, antes de usar as funções.",
            "Dentro da função print().",
            "Não faz diferença, o Python procura sozinho."
        ],
        "gabarito": "B", "xp_recompensa": 15
    },
    {
        "id_modulo": 3, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: As duas formas",
        "enunciado": "Qual a principal vantagem de usar `from math import sqrt` em vez de `import math`?",
        "opcoes": [
            "Deixa o código mais colorido.",
            "O programa só carrega a funcionalidade da raiz quadrada para a memória, economizando espaço.",
            "Evita que o usuário precise digitar números decimais.",
            "O Python não permite usar 'import math' em computadores antigos."
        ],
        "gabarito": "B", "xp_recompensa": 15
    },

    # --- 1 Prática Intermediária ---
    {
        "id_modulo": 3, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Prática: Arredondamento",
        "enunciado": "Importe a biblioteca matemática por completo. Na linha de baixo, faça um `print()` que use a função de teto (`math.ceil`) para arredondar o número 8.1 para cima.",
        "opcoes": None, "gabarito": "9\n", "xp_recompensa": 30
    },

    # --- 3 Objetivas de Raciocínio ---
    {
        "id_modulo": 3, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Caça ao Bug: Módulos",
        "enunciado": "Por que o código abaixo vai quebrar?\n\nimport math\nprint(sqrt(25))",
        "opcoes": [
            "Porque 25 não tem raiz exata.",
            "Porque o print está escrito errado.",
            "Como ele usou a importação geral (import math), ele é obrigado a escrever 'math.sqrt(25)'.",
            "Faltou colocar o número 25 entre aspas."
        ],
        "gabarito": "C", "xp_recompensa": 20
    },
    {
        "id_modulo": 3, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Análise de Sorteio",
        "enunciado": "Você precisa que o seu jogo sorteie o dano de um ataque entre 10 e 50. Qual comando abaixo faz isso de forma exata?",
        "opcoes": ["random.randint(10, 50)", "random.sorteio(10, 50)", "math.randint(10, 50)", "random(10, 50)"],
        "gabarito": "A", "xp_recompensa": 20
    },
    {
        "id_modulo": 3, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Combinando Ferramentas",
        "enunciado": "Você pode importar mais de uma coisa na mesma linha separando por vírgulas. Sabendo disso, como você importa o Teto e o Chão da biblioteca math ao mesmo tempo, sem importar a biblioteca inteira?",
        "opcoes": ["import ceil, floor", "from math import ceil, floor", "import math(ceil, floor)", "from ceil, floor import math"],
        "gabarito": "B", "xp_recompensa": 20
    },

    # --- 1 Prática Final (O Chefe) ---
    {
        "id_modulo": 3, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Desafio Final: O Dano da Espada",
        "enunciado": "Vamos recriar a mecânica de dano do Minecraft! Importe a biblioteca `random`. Crie uma variável chamada `dano_espada` e use a função correta do `random` para gerar um número inteiro aleatório entre 1 e 7. Por fim, use o `print()` para exibir a variável na tela.",
        "opcoes": None, "gabarito": "", # Validação de range tratada no servidor/sandbox
        "xp_recompensa": 50
    },

    # ======================================================================
    # MÓDULO 4: Manipulando Textos (Equivalente à Aula 9 do Curso em Vídeo)
    # ======================================================================

    # --- Bolinha 1: Teoria Introdutória ---
    {
        "id_modulo": 4, "id_etapa": 1, "tipo": "TEORIA",
        "titulo": "Textos são Correntes",
        "enunciado": "No Python, um texto (chamado de String) é como uma corrente de letras. O computador guarda cada letra em uma 'gaveta' numerada, começando SEMPRE do zero.\n\nSe a variável for `nome = 'Python'`, a letra 'P' está na gaveta 0, o 'y' na 1, e assim por diante.\n\nPara pegar só a primeira letra, usamos colchetes: `print(nome[0])`.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 2: Objetiva Fácil ---
    {
        "id_modulo": 4, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "A Gaveta Zero",
        "enunciado": "Se você tem a variável `fruta = 'Banana'`, qual comando exibe apenas a letra 'n' (a primeira que aparece na palavra)?",
        "opcoes": ["print(fruta[3])", "print(fruta[2])", "print(fruta[n])", "print(fruta[1])"],
        "gabarito": "B", "xp_recompensa": 10
    },

    # --- Bolinha 3: Teoria Nível 2 (Fatiamento) ---
    {
        "id_modulo": 4, "id_etapa": 3, "tipo": "TEORIA",
        "titulo": "Fatiando a Pizza",
        "enunciado": "Podemos pegar pedaços maiores do texto usando o Fatiamento (Slicing): `[início:fim]`.\n\nMas cuidado: o Python corta no número final, ele NÃO inclui a última gaveta!\n\nSe `texto = 'CEUNSP'`, fazer `print(texto[0:4])` vai pegar as gavetas 0, 1, 2 e 3 (mostrando 'CEUN'). A gaveta 4 fica de fora.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 10
    },

    # --- Bolinha 4: Objetiva Média ---
    {
        "id_modulo": 4, "id_etapa": 4, "tipo": "OBJETIVA",
        "titulo": "Corte Preciso",
        "enunciado": "Considere a variável `jogo = 'Minecraft'`. Qual código você usaria para fatiar e mostrar apenas a palavra 'Mine' na tela?",
        "opcoes": ["print(jogo[1:4])", "print(jogo[0:3])", "print(jogo[0:4])", "print(jogo[1:5])"],
        "gabarito": "C", "xp_recompensa": 15
    },

    # --- Bolinha 5: Objetiva Média (Tamanho da String) ---
    {
        "id_modulo": 4, "id_etapa": 5, "tipo": "OBJETIVA",
        "titulo": "Qual o tamanho?",
        "enunciado": "O Python tem uma função nativa chamada `len()` (de length/tamanho) que conta quantas letras tem um texto.\n\nQual será o resultado de `print(len('Brasil'))`?",
        "opcoes": ["5", "6", "Brasil", "B"],
        "gabarito": "B", "xp_recompensa": 15
    },

    # --- Bolinha 6: Prática Nível 1 ---
    {
        "id_modulo": 4, "id_etapa": 6, "tipo": "PRATICA",
        "titulo": "Contador de Letras",
        "enunciado": "Vamos testar o `len()`! Crie uma variável chamada `curso` guardando o texto 'Ciencia da Computacao' (sem acentos). Use o `print()` junto com a função `len()` para exibir quantas letras (e espaços) essa frase possui no total.",
        "opcoes": None, "gabarito": "21\n", "xp_recompensa": 20
    },

    # --- Bolinha 7: Teoria Nível 3 (Transformações) ---
    {
        "id_modulo": 4, "id_etapa": 7, "tipo": "TEORIA",
        "titulo": "O Poder do Ponto",
        "enunciado": "Podemos transformar textos usando 'métodos' (funções que vêm grudadas na variável com um ponto).\n\n- `.upper()`: Deixa tudo MAIÚSCULO.\n- `.lower()`: Deixa tudo minúsculo.\n- `.replace('A', 'B')`: Troca a letra ou palavra A pela B.\n\nExemplo: `print(nome.upper())`.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 15
    },

    # --- Bolinha 8: Objetiva Difícil ---
    {
        "id_modulo": 4, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "Substituição Rápida",
        "enunciado": "Leia o código:\nfrase = 'Eu gosto de Java'\nprint(frase.replace('Java', 'Python'))\n\nO que aparecerá na tela?",
        "opcoes": ["Eu gosto de Java Python", "Eu gosto de Python", "Erro, replace não existe", "EU GOSTO DE PYTHON"],
        "gabarito": "B", "xp_recompensa": 20
    },

    # ======================================================================
    # ETAPA 9: TESTE FINAL DO MÓDULO 4 (O Troféu)
    # 7 Exercícios (2 Obj, 1 Prática, 3 Obj, 1 Prática)
    # ======================================================================

    # --- 2 Objetivas Iniciais ---
    {
        "id_modulo": 4, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: Fatiamento Aberto",
        "enunciado": "Se você omitir o número final no fatiamento, como em `texto[2:]`, o que o Python faz?",
        "opcoes": [
            "Dá um erro de sintaxe.",
            "Pega apenas a letra na posição 2 e para.",
            "Começa na gaveta 2 e vai até o final do texto, não importa o tamanho dele.",
            "Começa do zero e vai até a gaveta 2."
        ],
        "gabarito": "C", "xp_recompensa": 15
    },
    {
        "id_modulo": 4, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: Buscando Palavras",
        "enunciado": "A função `.count('A')` conta quantas vezes a letra 'A' aparece. Se fizermos `frase = 'Abacate'`, qual será o resultado de `frase.count('a')` (minúsculo)?",
        "opcoes": ["3", "2", "0", "1"],
        "gabarito": "B", "xp_recompensa": 15
    },

    # --- 1 Prática Intermediária ---
    {
        "id_modulo": 4, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Prática: Gritando no Terminal",
        "enunciado": "Crie uma variável `aviso` com o texto 'cuidado' (tudo em minúsculo). Na linha de baixo, use o `print()` combinado com o método `.upper()` para exibir a palavra em letras maiúsculas.",
        "opcoes": None, "gabarito": "CUIDADO\n", "xp_recompensa": 30
    },

    # --- 3 Objetivas de Raciocínio ---
    {
        "id_modulo": 4, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Caça ao Bug: Fatiamento",
        "enunciado": "Um aluno tentou inverter o texto, mas esqueceu um detalhe. Para fazer o fatiamento pular de trás para frente, usamos `[::-1]`. O que o `-1` representa nesse caso?",
        "opcoes": [
            "O número da gaveta final.",
            "O 'passo', dizendo para o Python andar de 1 em 1 para trás.",
            "Um erro matemático, índices não podem ser negativos.",
            "O método replace escondido."
        ],
        "gabarito": "B", "xp_recompensa": 20
    },
    {
        "id_modulo": 4, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "A Sujeira Invisível",
        "enunciado": "Ao usar o `input()`, um usuário pode digitar espaços sem querer, tipo: `'  Victor  '`. Qual método usamos para remover os espaços vazios das pontas de uma string?",
        "opcoes": [".remove()", ".clear()", ".strip()", ".delete()"],
        "gabarito": "C", "xp_recompensa": 20
    },
    {
        "id_modulo": 4, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "O Operador In",
        "enunciado": "O Python tem um operador mágico chamado `in` para checar se uma palavra está dentro da outra. Qual o resultado lógico (Verdadeiro ou Falso) do comando: `print('Valor' in 'Valorant')`?",
        "opcoes": ["True (Verdadeiro)", "False (Falso)", "Dá erro", "Valorant"],
        "gabarito": "A", "xp_recompensa": 20
    },

    # --- 1 Prática Final (O Chefe) ---
    {
        "id_modulo": 4, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Desafio Final: O Corretor Automático",
        "enunciado": "Mostre que você domina as strings! Crie uma variável chamada `mensagem` com o texto 'EU ODEIO PYTHON'. Você deve usar o método `.replace()` dentro do `print()` para exibir na tela a frase corrigida: 'EU AMO PYTHON'.",
        "opcoes": None, "gabarito": "EU AMO PYTHON\n", "xp_recompensa": 50
    },

# ======================================================================
    # MÓDULO 5: Condições Básicas (Equivalente à Aula 10 do Curso em Vídeo)
    # ======================================================================

    # --- Bolinha 1: Teoria Introdutória ---
    {
        "id_modulo": 5, "id_etapa": 1, "tipo": "TEORIA",
        "titulo": "Tomando Decisões",
        "enunciado": "Até agora, nossos programas rodavam de cima para baixo, lendo todas as linhas. Mas e se quisermos que o código só execute uma ação SE algo for verdade?\n\nUsamos a estrutura `if` (que significa 'Se').\nExemplo:\n`if idade == 18:`\n    `print('Você tem 18 anos!')`\n\nNote os dois-pontos `:` no final da condição. Eles são obrigatórios!",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 2: Objetiva Fácil ---
    {
        "id_modulo": 5, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "A Pergunta Certa",
        "enunciado": "Quando queremos PERGUNTAR ao Python se uma coisa é exatamente igual a outra na condição do `if`, qual sinal devemos usar?",
        "opcoes": ["=", "==", "===", "=>"],
        "gabarito": "B", "xp_recompensa": 10
    },

    # --- Bolinha 3: Teoria Nível 2 (O Plano B) ---
    {
        "id_modulo": 5, "id_etapa": 3, "tipo": "TEORIA",
        "titulo": "O Plano B (Senão)",
        "enunciado": "E se a condição do `if` for falsa? Podemos criar um 'Plano B' usando o `else` (que significa 'Senão').\n\nExemplo:\n`if dinheiro >= 50:`\n    `print('Vou ao cinema!')`\n`else:`\n    `print('Vou ficar em casa.')`\n\nO `else` também precisa dos dois-pontos `:`, mas ele não leva nenhuma condição ao lado dele.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 10
    },

    # --- Bolinha 4: Objetiva Média ---
    {
        "id_modulo": 5, "id_etapa": 4, "tipo": "OBJETIVA",
        "titulo": "O Caminho do Código",
        "enunciado": "Leia o código mentalmente:\n\nnota = 5\nif nota >= 6:\n    print('Aprovado')\nelse:\n    print('Reprovado')\n\nO que o Python vai mostrar na tela?",
        "opcoes": ["Aprovado", "Reprovado", "As duas palavras", "Dá erro"],
        "gabarito": "B", "xp_recompensa": 15
    },

    # --- Bolinha 5: Objetiva Média (A Magia do Espaço) ---
    {
        "id_modulo": 5, "id_etapa": 5, "tipo": "OBJETIVA",
        "titulo": "A Indentação",
        "enunciado": "No Python, como o computador sabe quais comandos estão DENTRO do `if` e quais comandos estão FORA dele?",
        "opcoes": [
            "Pelo uso de chaves { } no código.",
            "Pela palavra 'Fim'.",
            "Pela Indentação (os espaços ou 'Tab' no começo da linha). Tudo que estiver afastado da margem esquerda pertence ao bloco.",
            "Ele adivinha sozinho."
        ],
        "gabarito": "C", "xp_recompensa": 15
    },

    # --- Bolinha 6: Prática Nível 1 ---
    {
        "id_modulo": 5, "id_etapa": 6, "tipo": "PRATICA",
        "titulo": "Acesso Liberado",
        "enunciado": "Vamos testar o `if` simples! Crie uma variável `senha` com o número 1234. Na linha de baixo, crie um `if` que verifique se a senha é IGUAL a 1234. Se for, imprima na tela o texto 'Acesso Permitido'.",
        "opcoes": None, "gabarito": "Acesso Permitido\n", "xp_recompensa": 20
    },

    # --- Bolinha 7: Teoria Nível 3 (Operadores Relacionais) ---
    {
        "id_modulo": 5, "id_etapa": 7, "tipo": "TEORIA",
        "titulo": "Sinais de Comparação",
        "enunciado": "Para fazer comparações, usamos os Operadores Relacionais:\n\n`>` (Maior que)\n`<` (Menor que)\n`>=` (Maior ou igual)\n`<=` (Menor ou igual)\n`==` (Igual)\n`!=` (Diferente)\n\nSe você quiser checar se um número NÃO É igual a 10, você faz: `if numero != 10:`",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 15
    },

    # --- Bolinha 8: Objetiva Difícil ---
    {
        "id_modulo": 5, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "Analisando a Desigualdade",
        "enunciado": "O que acontece ao rodarmos o código abaixo?\n\nmoedas = 10\nif moedas != 10:\n    print('A')\nelse:\n    print('B')",
        "opcoes": ["Mostra A", "Mostra B", "Erro de sintaxe", "Mostra 10"],
        "gabarito": "B", "xp_recompensa": 20
    },

    # ======================================================================
    # ETAPA 9: TESTE FINAL DO MÓDULO 5 (O Troféu)
    # 7 Exercícios (2 Obj, 1 Prática, 3 Obj, 1 Prática)
    # ======================================================================

    # --- 2 Objetivas Iniciais ---
    {
        "id_modulo": 5, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: Recebendo valores",
        "enunciado": "Qual a diferença crítica entre o `=` (um igual) e o `==` (dois iguais) em Python?",
        "opcoes": [
            "Nenhuma, ambos fazem a mesma coisa.",
            "Um igual `=` faz contas de matemática, e dois iguais `==` criam variáveis.",
            "Um igual `=` serve para ATRIBUIR valor a uma variável. Dois iguais `==` servem para COMPARAR se duas coisas são iguais.",
            "O `==` não existe no Python, só em outras linguagens."
        ],
        "gabarito": "C", "xp_recompensa": 15
    },
    {
        "id_modulo": 5, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: A Regra do Else",
        "enunciado": "É obrigatório usar o `else` sempre que fizermos um `if`?",
        "opcoes": [
            "Sim, o Python dá erro se um 'if' não tiver seu 'else'.",
            "Não. Você pode ter um 'if' sozinho. O 'else' é opcional, usado apenas quando você precisa de um 'Plano B'.",
            "Sim, mas apenas quando trabalhamos com números.",
            "Não, o 'else' só funciona dentro de variáveis."
        ],
        "gabarito": "B", "xp_recompensa": 15
    },

    # --- 1 Prática Intermediária ---
    {
        "id_modulo": 5, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Prática: Multa de Velocidade",
        "enunciado": "Crie uma variável `velocidade` valendo 95. Faça um `if` que verifique se a velocidade é MAIOR que 80. Se for, exiba a mensagem 'Multado!'.",
        "opcoes": None, "gabarito": "Multado!\n", "xp_recompensa": 30
    },

    # --- 3 Objetivas de Raciocínio ---
    {
        "id_modulo": 5, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Caça ao Bug: Dois Pontos",
        "enunciado": "Por que o código abaixo está errado?\n\nif idade >= 18\n    print('Pode dirigir')\nelse\n    print('Não pode')",
        "opcoes": [
            "Porque faltam aspas nos números.",
            "Porque faltam os dois-pontos (:) no final da linha do 'if' e do 'else'.",
            "Porque a palavra 'else' deveria estar na mesma linha do 'if'.",
            "Não tem nenhum erro, vai rodar perfeito."
        ],
        "gabarito": "B", "xp_recompensa": 20
    },
    {
        "id_modulo": 5, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "O Comando Fora do Bloco",
        "enunciado": "Observe:\nif 5 > 10:\n    print('Gato')\nprint('Cachorro')\n\nO que o Python exibirá?",
        "opcoes": [
            "Apenas Gato",
            "Apenas Cachorro",
            "Gato e Cachorro",
            "Nada"
        ],
        "gabarito": "B", "xp_recompensa": 20
    },
    {
        "id_modulo": 5, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Misturando Módulos",
        "enunciado": "Como aprendemos no Módulo 4, `len()` conta o tamanho de um texto. Se `nome = 'Ana'`, qual é o resultado do código abaixo?\n\nif len(nome) < 5:\n    print('Nome curto')\nelse:\n    print('Nome longo')",
        "opcoes": ["Nome longo", "Nome curto", "Ana", "Erro"],
        "gabarito": "B", "xp_recompensa": 20
    },

    # --- 1 Prática Final (O Chefe) ---
    {
        "id_modulo": 5, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Desafio Final: O Radar de Par ou Ímpar",
        "enunciado": "Juntando Matemática (Mod. 2) com Condições (Mod. 5)! \nCrie a variável `numero` valendo 7. \nCrie um `if` para checar se o número é PAR (lembre-se: um número é par se o resto da divisão dele por 2 for igual a zero: `numero % 2 == 0`). \nSe for par, faça um print escrito 'PAR'. \nSenão (`else`), faça um print escrito 'IMPAR'.",
        "opcoes": None, "gabarito": "IMPAR\n", "xp_recompensa": 50
    },

# ======================================================================
    # MÓDULO 6: Condições Aninhadas (Equivalente à Aula 12 do Curso em Vídeo)
    # ======================================================================

    # --- Bolinha 1: Teoria Introdutória ---
    {
        "id_modulo": 6, "id_etapa": 1, "tipo": "TEORIA",
        "titulo": "O Caminho do Meio",
        "enunciado": "No Módulo 5, aprendemos o `if` (Sim) e o `else` (Não). Mas e se tivermos 3 ou mais opções?\n\nPara isso, o Python tem o `elif` (uma mistura de 'else' com 'if', que significa 'senão se').\n\nExemplo:\n`if cor == 'verde':`\n    `print('Siga')`\n`elif cor == 'amarelo':`\n    `print('Atenção')`\n`else:`\n    `print('Pare')`",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 2: Objetiva Fácil ---
    {
        "id_modulo": 6, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "A Palavra Mágica",
        "enunciado": "Qual é a palavra-chave que usamos em Python para adicionar uma terceira (ou quarta, ou quinta...) opção de caminho no nosso código?",
        "opcoes": ["elseif", "else if", "elif", "senão se"],
        "gabarito": "C", "xp_recompensa": 10
    },

    # --- Bolinha 3: Teoria Nível 2 (As Regras do Jogo) ---
    {
        "id_modulo": 6, "id_etapa": 3, "tipo": "TEORIA",
        "titulo": "As Regras do Elif",
        "enunciado": "Existem três regras de ouro para as condições aninhadas:\n\n1. O `if` sempre tem que ser o primeiro.\n2. Você pode usar quantos `elif` quiser no meio do caminho.\n3. O `else` (se você quiser usar) tem que ser sempre o último, para fechar a porta.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 10
    },

    # --- Bolinha 4: Objetiva Média ---
    {
        "id_modulo": 6, "id_etapa": 4, "tipo": "OBJETIVA",
        "titulo": "Quantas opções?",
        "enunciado": "Quantas vezes podemos usar o comando `elif` dentro de uma mesma estrutura condicional?",
        "opcoes": [
            "Apenas uma vez.",
            "No máximo duas vezes.",
            "Quantas vezes você quiser, dependendo de quantas opções seu programa precisa.",
            "Apenas se não tiver um 'else' no final."
        ],
        "gabarito": "C", "xp_recompensa": 15
    },

    # --- Bolinha 5: Objetiva Média (Comportamento de Execução) ---
    {
        "id_modulo": 6, "id_etapa": 5, "tipo": "OBJETIVA",
        "titulo": "A Corrida de Obstáculos",
        "enunciado": "Quando o Python encontra uma estrutura com `if`, `elif` e `else`, como ele a executa?",
        "opcoes": [
            "Ele executa todas as opções para garantir.",
            "Ele avalia de cima para baixo. Assim que encontra a PRIMEIRA condição verdadeira, ele executa aquele bloco, ignora todo o resto e sai da estrutura.",
            "Ele executa o 'if' e o 'else', mas ignora os 'elifs'.",
            "Ele roda o código de baixo para cima."
        ],
        "gabarito": "B", "xp_recompensa": 15
    },

    # --- Bolinha 6: Prática Nível 1 ---
    {
        "id_modulo": 6, "id_etapa": 6, "tipo": "PRATICA",
        "titulo": "O Caixa Eletrônico",
        "enunciado": "Crie uma variável `opcao` com o número 2. Faça uma estrutura onde: se a opção for 1, imprima 'Saque'; se a opção for 2 (usando elif), imprima 'Extrato'; senão, imprima 'Sair'.",
        "opcoes": None, "gabarito": "Extrato\n", "xp_recompensa": 20
    },

    # --- Bolinha 7: Teoria Nível 3 (O Else não é obrigatório) ---
    {
        "id_modulo": 6, "id_etapa": 7, "tipo": "TEORIA",
        "titulo": "O Final é Opcional",
        "enunciado": "Muitos alunos acham que toda estrutura grande precisa terminar com `else`. Isso é um mito!\n\nVocê pode ter um programa que seja apenas `if` e `elif`. Se nenhuma das condições for verdadeira, o Python simplesmente não faz nada e continua o código normalmente.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 15
    },

    # --- Bolinha 8: Objetiva Difícil ---
    {
        "id_modulo": 6, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "Leitura de Código",
        "enunciado": "nome = 'Pedro'\nif nome == 'Ana':\n    print('Menina')\nelif nome == 'João':\n    print('Menino')\n\nO que aparecerá na tela?",
        "opcoes": ["Menina", "Menino", "Erro, falta o else", "Não aparecerá nada (a tela ficará em branco)"],
        "gabarito": "D", "xp_recompensa": 20
    },

    # ======================================================================
    # ETAPA 9: TESTE FINAL DO MÓDULO 6 (O Troféu)
    # 7 Exercícios (2 Obj, 1 Prática, 3 Obj, 1 Prática)
    # ======================================================================

    # --- 2 Objetivas Iniciais ---
    {
        "id_modulo": 6, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: Anatomia do Comando",
        "enunciado": "Diferente do `else` (que fica sozinho), o `elif` sempre precisa de algo do lado dele. O que é?",
        "opcoes": [
            "Um número.",
            "Uma condição a ser testada (ex: elif idade > 10:).",
            "A palavra 'then'.",
            "Sempre a mesma condição que estava no 'if'."
        ],
        "gabarito": "B", "xp_recompensa": 15
    },
    {
        "id_modulo": 6, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: Estrutura",
        "enunciado": "Qual das opções abaixo apresenta uma estrutura condicional logicamente correta em Python?",
        "opcoes": [
            "if -> else -> elif",
            "elif -> if -> else",
            "if -> elif -> elif -> else",
            "else -> elif -> if"
        ],
        "gabarito": "C", "xp_recompensa": 15
    },

    # --- 1 Prática Intermediária ---
    {
        "id_modulo": 6, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Prática: Menu de Jogos",
        "enunciado": "Vamos fazer um seletor! Crie uma variável `jogo` valendo 'Valorant'. Usando `if` e `elif`, verifique: se jogo for 'Minecraft', imprima 'Blocos'. Se for 'Valorant', imprima 'Tiro'.",
        "opcoes": None, "gabarito": "Tiro\n", "xp_recompensa": 30
    },

    # --- 3 Objetivas de Raciocínio ---
    {
        "id_modulo": 6, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Caça ao Bug: Condições Aninhadas",
        "enunciado": "Por que o código abaixo vai dar erro de sintaxe?\n\nif valor > 10:\n    print('Maior')\nelif:\n    print('Menor')",
        "opcoes": [
            "Porque faltou o else.",
            "Porque o 'elif' foi escrito sem nenhuma condição para testar antes dos dois-pontos.",
            "Porque as palavras no print não têm aspas duplas.",
            "Porque a variável 'valor' não aceita números."
        ],
        "gabarito": "B", "xp_recompensa": 20
    },
    {
        "id_modulo": 6, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Sobreposição de Condições",
        "enunciado": "Observe com muita atenção:\n\nidade = 20\nif idade >= 10:\n    print('A')\nelif idade >= 18:\n    print('B')\n\nO número 20 é maior que 10 e também é maior que 18. O que o Python fará?",
        "opcoes": [
            "Vai mostrar A e B.",
            "Vai mostrar B, pois 18 é mais próximo de 20.",
            "Vai mostrar A, pois ele executa sempre a PRIMEIRA condição verdadeira que encontra e ignora o resto.",
            "Vai dar erro pois as condições entram em conflito."
        ],
        "gabarito": "C", "xp_recompensa": 20
    },
    {
        "id_modulo": 6, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "A Matemática do If",
        "enunciado": "Juntando Módulo 2 com Módulo 6:\n\nn = 9\nif n % 2 == 0:\n    print('P')\nelif n % 3 == 0:\n    print('T')\nelse:\n    print('N')\n\nQual será a saída na tela?",
        "opcoes": ["P", "T", "N", "T e N"],
        "gabarito": "B", "xp_recompensa": 20
    },

    # --- 1 Prática Final (O Chefe) ---
    {
        "id_modulo": 6, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Desafio Final: O Boletim Escolar",
        "enunciado": "Clássico exercício do Professor Guanabara! Crie uma variável `media` com o valor 5.5. \nCrie a seguinte estrutura condicional completa:\n- Se a média for maior ou igual a 7.0, imprima 'Aprovado'.\n- Senão se (elif) a média for maior ou igual a 5.0, imprima 'Recuperação'.\n- Senão (else), imprima 'Reprovado'.",
        "opcoes": None, "gabarito": "Recuperação\n", "xp_recompensa": 50
    },

# ======================================================================
    # MÓDULO 7: Estrutura de Repetição FOR (Equivalente à Aula 13 do Curso em Vídeo)
    # ======================================================================

    # --- Bolinha 1: Teoria Introdutória ---
    {
        "id_modulo": 7, "id_etapa": 1, "tipo": "TEORIA",
        "titulo": "O Laço de Repetição",
        "enunciado": "Imagine que você precisa escrever 'Oi' na tela 3 vezes. Em vez de fazer três `print('Oi')`, o Python tem os 'Laços de Repetição'.\n\nO mais famoso é o `for` (para). Usamos ele junto com a função `range()` (intervalo).\n\nExemplo:\n`for c in range(1, 4):`\n    `print('Oi')`\n\nO Python vai repetir o bloco indentado 3 vezes!",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 2: Objetiva Fácil ---
    {
        "id_modulo": 7, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "A Função do Laço",
        "enunciado": "Qual é a principal utilidade da estrutura `for` na programação?",
        "opcoes": [
            "Tomar decisões matemáticas complexas.",
            "Repetir um bloco de código várias vezes de forma automática.",
            "Criar variáveis de texto.",
            "Perguntar a idade do usuário."
        ],
        "gabarito": "B", "xp_recompensa": 10
    },

    # --- Bolinha 3: Teoria Nível 2 (O Segredo do Range) ---
    {
        "id_modulo": 7, "id_etapa": 3, "tipo": "TEORIA",
        "titulo": "O Segredo do Range",
        "enunciado": "A função `range(1, 4)` diz: 'Comece no 1 e vá até o 4'. Mas preste muita atenção a esta regra de ouro do Python:\n\n**O último número NUNCA é incluído!**\n\nOu seja, `range(1, 4)` vai contar: 1, 2 e 3. Quando chega no 4, ele para e sai do laço sem executar.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 10
    },

    # --- Bolinha 4: Objetiva Média ---
    {
        "id_modulo": 7, "id_etapa": 4, "tipo": "OBJETIVA",
        "titulo": "Contando nos dedos",
        "enunciado": "Se um programador escrever `for c in range(1, 10):`, quantas vezes o laço vai se repetir?",
        "opcoes": ["10 vezes", "9 vezes", "8 vezes", "1 vez"],
        "gabarito": "B", "xp_recompensa": 15
    },

    # --- Bolinha 5: Objetiva Média (A Variável de Controle) ---
    {
        "id_modulo": 7, "id_etapa": 5, "tipo": "OBJETIVA",
        "titulo": "A Variável Fantasma",
        "enunciado": "No código `for c in range(1, 4):`, a letra 'c' é uma variável que muda de valor a cada volta. Se rodarmos `print(c)` dentro desse laço, o que será exibido na tela?",
        "opcoes": [
            "A letra 'c' três vezes.",
            "Os números 1, 2, 3 e 4.",
            "Os números 1, 2 e 3 (um em cada linha).",
            "Dá erro pois 'c' não foi criado com =."
        ],
        "gabarito": "C", "xp_recompensa": 15
    },

    # --- Bolinha 6: Prática Nível 1 ---
    {
        "id_modulo": 7, "id_etapa": 6, "tipo": "PRATICA",
        "titulo": "Contando até 3",
        "enunciado": "Vamos ver isso funcionando! Crie um laço `for` usando uma variável `i` e a função `range()` para percorrer os números de 1 até 3 (lembre da regra do último número). Dentro do laço, dê um `print(i)` para exibir a contagem.",
        "opcoes": None, "gabarito": "1\n2\n3\n", "xp_recompensa": 20
    },

    # --- Bolinha 7: Teoria Nível 3 (Passo e Reverso) ---
    {
        "id_modulo": 7, "id_etapa": 7, "tipo": "TEORIA",
        "titulo": "Saltos e Marcha Ré",
        "enunciado": "O `range` pode receber um 3º número, que é o 'passo' (como ele conta).\n\n- Pular de 2 em 2: `range(0, 10, 2)` (Conta: 0, 2, 4...)\n- Contagem Regressiva: `range(5, 0, -1)` (Conta: 5, 4, 3, 2, 1. O -1 manda ele andar para trás!).",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 15
    },

    # --- Bolinha 8: Objetiva Difícil ---
    {
        "id_modulo": 7, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "Lendo a Marcha Ré",
        "enunciado": "O que será exibido se executarmos o código abaixo?\n\nfor n in range(3, 0, -1):\n    print(n)",
        "opcoes": ["0, 1, 2, 3", "3, 2, 1", "3, 2, 1, 0", "Dá erro"],
        "gabarito": "B", "xp_recompensa": 20
    },

    # ======================================================================
    # ETAPA 9: TESTE FINAL DO MÓDULO 7 (O Troféu)
    # 7 Exercícios (2 Obj, 1 Prática, 3 Obj, 1 Prática)
    # ======================================================================

    # --- 2 Objetivas Iniciais ---
    {
        "id_modulo": 7, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: A Sintaxe",
        "enunciado": "Qual caractere é totalmente OBRIGATÓRIO no final da linha do `for` para que ele funcione, assim como no `if`?",
        "opcoes": ["O ponto final (.)", "O ponto e vírgula (;)", "Os dois-pontos (:)", "As chaves {}"],
        "gabarito": "C", "xp_recompensa": 15
    },
    {
        "id_modulo": 7, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: Ocultando o Início",
        "enunciado": "Se você escrever apenas `range(3)` com apenas UM número dentro, o que o Python assume automaticamente?",
        "opcoes": [
            "Que é um erro.",
            "Ele assume que a contagem deve começar do zero. (Vai contar: 0, 1, 2)",
            "Ele assume que é o passo.",
            "Ele conta infinitamente."
        ],
        "gabarito": "B", "xp_recompensa": 15
    },

    # --- 1 Prática Intermediária ---
    {
        "id_modulo": 7, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Prática: Saltando",
        "enunciado": "Usando o laço `for` e o terceiro parâmetro do `range` (passo), exiba os números pares de 0 a 4 (ou seja, 0, 2 e 4, um em cada linha). Dica: lembre de até onde o range precisa ir para incluir o 4!",
        "opcoes": None, "gabarito": "0\n2\n4\n", "xp_recompensa": 30
    },

    # --- 3 Objetivas de Raciocínio ---
    {
        "id_modulo": 7, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "O Comando Fora do Laço",
        "enunciado": "Preste atenção na indentação:\n\nfor c in range(1, 3):\n    print('A')\nprint('B')",
        "opcoes": [
            "A B A B",
            "A A B",
            "B B",
            "Erro de sintaxe"
        ],
        "gabarito": "B", "xp_recompensa": 20
    },
    {
        "id_modulo": 7, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Acumuladores (Avançado)",
        "enunciado": "Um padrão muito comum é somar os valores do laço em uma variável de fora. Veja:\n\nsoma = 0\nfor i in range(1, 4):\n    soma = soma + i\n\nNo final, qual será o valor da variável 'soma'?",
        "opcoes": ["3", "4", "6", "0"],
        "gabarito": "C", "xp_recompensa": 20
    },
    {
        "id_modulo": 7, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Repetindo com Inputs",
        "enunciado": "O que acontece se colocarmos um `input()` DENTRO de um bloco `for` que repete 5 vezes?",
        "opcoes": [
            "Dá erro lógico.",
            "O Python vai perguntar 5 vezes seguidas para o usuário digitar algo.",
            "O Python pula o input e só faz os prints.",
            "O programa trava."
        ],
        "gabarito": "B", "xp_recompensa": 20
    },

    # --- 1 Prática Final (O Chefe) ---
    {
        "id_modulo": 7, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Desafio Final: Ano Novo!",
        "enunciado": "Junte tudo que aprendeu! Crie um laço `for` com uma contagem regressiva. O laço deve imprimir os números 3, 2 e 1 (usando a marcha ré no range). FORA DO LAÇO (sem indentação), imprima 'FOGO!'.",
        "opcoes": None, "gabarito": "3\n2\n1\nFOGO!\n", "xp_recompensa": 50
    },

# ======================================================================
    # MÓDULO 8: Estrutura de Repetição WHILE (Equivalente à Aula 14 do Curso em Vídeo)
    # ======================================================================

    # --- Bolinha 1: Teoria Introdutória ---
    {
        "id_modulo": 8, "id_etapa": 1, "tipo": "TEORIA",
        "titulo": "O Laço Condicional",
        "enunciado": "No Módulo 7, usamos o `for` para repetir quando SABEMOS o limite (ex: de 1 a 10).\n\nMas e se não soubermos quando a repetição vai acabar? Usamos o `while` (Enquanto).\nEle repete o bloco DE NOVO E DE NOVO enquanto uma condição for verdadeira.\n\nExemplo:\n`c = 1`\n`while c < 4:`\n    `print(c)`\n    `c = c + 1`",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 2: Objetiva Fácil ---
    {
        "id_modulo": 8, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "A Diferença de Ouro",
        "enunciado": "Qual é a principal diferença entre o `for` e o `while`?",
        "opcoes": [
            "O for é para matemática, o while é para textos.",
            "O for é usado quando sabemos o limite de repetições. O while é usado quando não sabemos o limite, dependendo de uma condição.",
            "Não existe diferença, os dois funcionam com a função range().",
            "O while só roda uma vez."
        ],
        "gabarito": "B", "xp_recompensa": 10
    },

    # --- Bolinha 3: Teoria Nível 2 (O Loop Infinito) ---
    {
        "id_modulo": 8, "id_etapa": 3, "tipo": "TEORIA",
        "titulo": "O Perigo do Loop Infinito",
        "enunciado": "Se você cria um `while` mas nunca altera a variável que ele está testando, o programa fica preso para sempre!\n\nSe você fizer:\n`c = 1`\n`while c < 4:`\n    `print(c)`\n\nComo o valor do `c` nunca muda, ele vai ser eternamente menor que 4. O computador vai imprimir o número 1 infinitamente até travar. Você SEMPRE precisa atualizar a variável dentro do laço (ex: `c = c + 1`).",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 10
    },

    # --- Bolinha 4: Objetiva Média ---
    {
        "id_modulo": 8, "id_etapa": 4, "tipo": "OBJETIVA",
        "titulo": "Identificando a Trava",
        "enunciado": "Observe o código:\nx = 0\nwhile x < 5:\n    print('Rodando')\n\nPor que este código é um loop infinito?",
        "opcoes": [
            "Porque faltaram os dois-pontos.",
            "Porque 0 sempre será menor que 5, e o código não atualiza o valor de x em nenhum momento.",
            "Porque a palavra Rodando é muito grande.",
            "Porque o x começou com zero."
        ],
        "gabarito": "B", "xp_recompensa": 15
    },

    # --- Bolinha 5: Objetiva Média (Comportamento) ---
    {
        "id_modulo": 8, "id_etapa": 5, "tipo": "OBJETIVA",
        "titulo": "Contando com While",
        "enunciado": "O que será exibido se rodarmos este código?\n\nx = 1\nwhile x <= 2:\n    print(x)\n    x = x + 1",
        "opcoes": ["Apenas 1", "Apenas 2", "1 e 2 (um em cada linha)", "Dá erro infinito"],
        "gabarito": "C", "xp_recompensa": 15
    },

    # --- Bolinha 6: Prática Nível 1 ---
    {
        "id_modulo": 8, "id_etapa": 6, "tipo": "PRATICA",
        "titulo": "O Seu Primeiro While",
        "enunciado": "Vamos testar o `while`! \n1. Crie uma variável `cont` com o valor 1.\n2. Crie um `while` que rode enquanto `cont` for menor ou igual a 3.\n3. Dentro do laço, imprima 'Loop'.\n4. Na linha seguinte (ainda dentro do laço), adicione 1 à variável `cont` (`cont = cont + 1`).",
        "opcoes": None, "gabarito": "Loop\nLoop\nLoop\n", "xp_recompensa": 20
    },

    # --- Bolinha 7: Teoria Nível 3 (A Flag de Parada) ---
    {
        "id_modulo": 8, "id_etapa": 7, "tipo": "TEORIA",
        "titulo": "A Condição de Parada (Flag)",
        "enunciado": "O maior poder do `while` é pedir dados ao usuário até que ele digite uma 'senha' de saída.\n\nExemplo:\n`r = 'S'`\n`while r == 'S':`\n    `r = input('Quer continuar? [S/N] ')`\n\nNeste caso, o programa não tem um limite fixo (como 10 ou 20 vezes). Ele vai repetir 1000 vezes se o usuário ficar digitando 'S'. Só vai parar quando ele digitar qualquer outra coisa.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 15
    },

    # --- Bolinha 8: Objetiva Difícil ---
    {
        "id_modulo": 8, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "O Limite Misterioso",
        "enunciado": "Imagine um programa com a seguinte linha: `while numero != 0:`.\nQuando o laço vai parar de repetir?",
        "opcoes": [
            "Quando o programa acabar o tempo.",
            "Quando o usuário finalmente digitar o número 0.",
            "Ele vai parar na primeira volta.",
            "Ele é um loop infinito por natureza."
        ],
        "gabarito": "B", "xp_recompensa": 20
    },

    # ======================================================================
    # ETAPA 9: TESTE FINAL DO MÓDULO 8 (O Troféu)
    # 7 Exercícios (2 Obj, 1 Prática, 3 Obj, 1 Prática)
    # ======================================================================

    # --- 2 Objetivas Iniciais ---
    {
        "id_modulo": 8, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: Significado",
        "enunciado": "O que a palavra `while` significa literalmente em português, e qual a sua lógica de funcionamento?",
        "opcoes": [
            "Significa 'Para'. Ele roda uma vez para cada item.",
            "Significa 'Enquanto'. Ele executa o bloco de código ENQUANTO uma condição for verdadeira.",
            "Significa 'Se'. Ele faz um teste lógico.",
            "Significa 'Repita'. Ele não precisa de condições."
        ],
        "gabarito": "B", "xp_recompensa": 15
    },
    {
        "id_modulo": 8, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: A Variável Externa",
        "enunciado": "Ao contrário do `for`, que cria a variável de contagem na mesma linha (ex: `for c in range...`), o que precisamos fazer no `while`?",
        "opcoes": [
            "Não precisamos usar variáveis no while.",
            "Precisamos CRIAR a variável de controle antes do while e ATUALIZAR ela dentro do bloco.",
            "Temos que usar a palavra range() dentro dele.",
            "O usuário que escolhe automaticamente."
        ],
        "gabarito": "B", "xp_recompensa": 15
    },

    # --- 1 Prática Intermediária ---
    {
        "id_modulo": 8, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Prática: Contagem do While",
        "enunciado": "Crie uma variável `i` igual a 0. Usando o laço `while`, repita um bloco enquanto `i` for menor que 2. Dentro do bloco, imprima o valor de `i` e some 1 a ele (`i = i + 1`).",
        "opcoes": None, "gabarito": "0\n1\n", "xp_recompensa": 30
    },

    # --- 3 Objetivas de Raciocínio ---
    {
        "id_modulo": 8, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Caça ao Bug: Loop Infinito",
        "enunciado": "Onde está o erro gravíssimo no código abaixo?\n\nvidas = 3\nwhile vidas > 0:\n    print('Ainda vivo!')",
        "opcoes": [
            "O while precisa de parênteses.",
            "Faltou o if antes.",
            "A variável 'vidas' não foi diminuída dentro do bloco, gerando um Loop Infinito.",
            "A variável deveria ser texto."
        ],
        "gabarito": "C", "xp_recompensa": 20
    },
    {
        "id_modulo": 8, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "A Condição Falsa Inicial",
        "enunciado": "O que acontece se a condição do `while` já for FALSA logo na primeira vez que o código passa por ele?\nEx:\nx = 10\nwhile x < 5:\n    print('Oi')",
        "opcoes": [
            "Dá um erro.",
            "Ele imprime 'Oi' pelo menos uma vez antes de perceber que é falso.",
            "O Python ignora o bloco inteiro e não imprime nada, continuando o código abaixo.",
            "Ele força o x a virar 5."
        ],
        "gabarito": "C", "xp_recompensa": 20
    },
    {
        "id_modulo": 8, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Leitura de Execução",
        "enunciado": "Analise o código abaixo:\n\nc = 10\nwhile c >= 8:\n    print(c)\n    c = c - 1\n\nQuais números serão exibidos na tela?",
        "opcoes": ["10, 9, 8", "10, 9", "10", "8"],
        "gabarito": "A", "xp_recompensa": 20
    },

    # --- 1 Prática Final (O Chefe) ---
    {
        "id_modulo": 8, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Desafio Final: O Foguete Manual",
        "enunciado": "Vamos recriar a contagem regressiva, mas usando apenas o `while`! \n1. Crie a variável `tempo` com o valor 3.\n2. Crie um `while` para rodar enquanto o tempo for MAIOR que 0.\n3. Dentro do laço: imprima o tempo, e depois diminua 1 do tempo (`tempo = tempo - 1`).\n4. Fora do laço (sem indentação), imprima 'FOGO!'.",
        "opcoes": None, "gabarito": "3\n2\n1\nFOGO!\n", "xp_recompensa": 50
    },

]

