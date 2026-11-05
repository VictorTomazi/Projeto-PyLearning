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
    # MÓDULO 2: Operadores Aritméticos (Equivalente à Aula 7 do Curso em Vídeo)
    # ======================================================================

    # --- Bolinha 1: Teoria Introdutória Profunda ---
    {
        "id_modulo": 2, "id_etapa": 1, "tipo": "TEORIA",
        "titulo": "A Matemática do Python",
        "enunciado": "O Python é uma excelente calculadora. Para fazer operações básicas, usamos os operadores aritméticos padrão:\n\n`+` (Adição)\n`-` (Subtração)\n`*` (Multiplicação - usamos o asterisco!)\n`/` (Divisão)\n\nVocê pode fazer as contas diretamente no print, por exemplo: `print(5 * 2)`. O Python fará a conta e exibirá apenas o resultado (10).",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 2: Objetiva Fácil ---
    {
        "id_modulo": 2, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "O Operador de Multiplicação",
        "enunciado": "Como você pediria para o Python multiplicar 4 por 3?",
        "opcoes": ["print(4 x 3)", "print(4 * 3)", "print(4.3)", "print(4 X 3)"],
        "gabarito": "B", "xp_recompensa": 10
    },

    # --- Bolinha 3: Teoria Nível 2 (Operadores Especiais) ---
    {
        "id_modulo": 2, "id_etapa": 3, "tipo": "TEORIA",
        "titulo": "Os Três Operadores Diferentões",
        "enunciado": "Além das contas normais, o Python tem três operadores muito poderosos:\n\n1. `**` (Potência): Para fazer 5 elevado a 2 (5²), fazemos `5 ** 2`.\n2. `//` (Divisão Inteira): Divide, mas ignora a vírgula. Se fizermos `5 // 2`, a resposta será 2 (e não 2.5).\n3. `%` (Resto da Divisão/Módulo): Ele mostra o que 'sobrou' da divisão. Ex: `5 % 2` resulta em 1, porque 5 dividido por 2 dá 2 e sobra 1.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 10
    },

    # --- Bolinha 4: Objetiva Média ---
    {
        "id_modulo": 2, "id_etapa": 4, "tipo": "OBJETIVA",
        "titulo": "Entendendo o Módulo",
        "enunciado": "Se você executar o código `print(10 % 3)`, qual será o número exato exibido na tela do usuário?",
        "opcoes": ["3.33", "3", "1", "0"],
        "gabarito": "C", "xp_recompensa": 15
    },

    # --- Bolinha 5: Objetiva Média (Ordem de Precedência) ---
    {
        "id_modulo": 2, "id_etapa": 5, "tipo": "OBJETIVA",
        "titulo": "Quem resolve primeiro?",
        "enunciado": "Assim como na matemática da escola, o Python tem ordem de precedência (PEMDAS). Primeiro Parênteses, depois Potências, depois Multiplicação/Divisão e por último Adição/Subtração.\n\nQual o resultado de: `print(5 + 3 * 2)`?",
        "opcoes": ["16", "11", "10", "15"],
        "gabarito": "B", "xp_recompensa": 15
    },

    # --- Bolinha 6: Prática Nível 1 ---
    {
        "id_modulo": 2, "id_etapa": 6, "tipo": "PRATICA",
        "titulo": "Calculadora Simples",
        "enunciado": "Crie um programa com um único comando `print()` que calcule o resultado de 10 elevado a 3 (10³).",
        "opcoes": None, "gabarito": "1000\n", "xp_recompensa": 20
    },

    # --- Bolinha 7: Teoria Nível 3 (Trabalhando com Variáveis) ---
    {
        "id_modulo": 2, "id_etapa": 7, "tipo": "TEORIA",
        "titulo": "Contas com Variáveis",
        "enunciado": "A verdadeira magia acontece quando fazemos cálculos com variáveis. Veja o exemplo:\n\npreco = 50\ndesconto = 10\nnovo_preco = preco - desconto\nprint(novo_preco)\n\nA variável `novo_preco` faz a conta usando os valores guardados nas outras variáveis e guarda o resultado final (40).",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 15
    },

    # --- Bolinha 8: Objetiva Difícil ---
    {
        "id_modulo": 2, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "Análise de Código",
        "enunciado": "Leia o código abaixo:\na = 4\nb = 2\nc = (a + b) ** b\n\nQual será o valor guardado na variável 'c'?",
        "opcoes": ["12", "16", "36", "10"],
        "gabarito": "C", "xp_recompensa": 20
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

]