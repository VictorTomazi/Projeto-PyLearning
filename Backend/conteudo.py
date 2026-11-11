"""
conteudo.py — Central de lições.
Padrão: 8 bolinhas por módulo (Teoria, Objetivas, Prática intercaladas).
"""

MODULOS_E_LICOES = [
    # ======================================================================
    # MÓDULO 1: Primeiros Comandos
    # ======================================================================

    # --- Bolinha 1: Texto Introdutório ---
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

    # --- Bolinha 3: Texto de Aprofundamento ---
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

    # --- Bolinha 5: Texto de Aprofundamento ---
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

    # --- Bolinha 7: Texto finalizador ---
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

    # --- 2 Objetivas Iniciais (Intermediárias) ---
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

    # --- 3 Objetivas de Raciocínio (Difíceis) ---
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

    # --- Prática Final ---
    {
        "id_modulo": 1, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Desafio Final do Módulo 1",
        "enunciado": "Mostre que você dominou o básico! Crie uma variável `saudacao` com o texto 'Bem-vindo, '. Crie uma variável `jogador` com o texto 'Victor'. Faça um único print que some (concatene) as duas variáveis para exibir a mensagem completa.",
        "opcoes": None, "gabarito": "Bem-vindo, Victor\n", "xp_recompensa": 50
    },

    # ======================================================================
    # MÓDULO 2: Operadores Aritméticos
    # ======================================================================

    # --- Bolinha 1: Texto Introdutório ---
    {
        "id_modulo": 2, "id_etapa": 1, "tipo": "TEORIA",
        "titulo": "A Matemática do Python",
        "enunciado": "O Python é uma excelente calculadora. Para fazer operações básicas, usamos:\n\n`+` (Adição)\n`-` (Subtração)\n`*` (Multiplicação)\n`/` (Divisão)\n\nVocê pode fazer as contas diretamente dentro de um print. Exemplo: se rodar `print(5 * 2)`, o Python fará a conta silenciosamente e exibirá apenas o resultado (10) na tela.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 2: 2 Objetivas ---
    {
        "id_modulo": 2, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "O Símbolo da Multiplicação",
        "enunciado": "Qual é a forma correta de pedir para o Python multiplicar 4 por 3?",
        "opcoes": ["print(4 x 3)", "print(4 * 3)", "print(4.3)", "print(4 X 3)"],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 2, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "Matemática Simples",
        "enunciado": "O que aparecerá na tela do usuário se executarmos o código `print(10 - 2)`?",
        "opcoes": ["8", "10 - 2", "O código dá erro", "-8"],
        "gabarito": "A", "xp_recompensa": 10
    },

    # --- Bolinha 3: Texto de Aprofundamento ---
    {
        "id_modulo": 2, "id_etapa": 3, "tipo": "TEORIA",
        "titulo": "Operadores Diferentões",
        "enunciado": "Além das contas normais, o Python tem três operadores muito poderosos:\n\n1. `**` (Potência): Para fazer 5 elevado a 2 (5²), fazemos `5 ** 2`.\n2. `//` (Divisão Inteira): Divide, mas ignora a vírgula. `5 // 2` resulta em 2 (e não 2.5).\n3. `%` (Resto da Divisão): Mostra o que 'sobrou' de uma divisão inteira. `5 % 2` resulta em 1, porque 5 dividido por 2 dá 2 e sobra 1.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 4: 1 Escrever ---
    {
        "id_modulo": 2, "id_etapa": 4, "tipo": "PRATICA",
        "titulo": "Calculando Potências",
        "enunciado": "Vamos testar os operadores novos! Crie um código com um único `print()` que calcule o valor de 10 elevado ao cubo (10³).",
        "opcoes": None, "gabarito": "1000\n", "xp_recompensa": 20
    },

    # --- Bolinha 5: Texto de Aprofundamento ---
    {
        "id_modulo": 2, "id_etapa": 5, "tipo": "TEORIA",
        "titulo": "Quem resolve primeiro?",
        "enunciado": "Assim como na matemática da escola, o Python tem uma **Ordem de Precedência** (quem manda mais). Ele resolve os cálculos nesta ordem:\n\n1º: Tudo que estiver entre parênteses `()`\n2º: Potências `**`\n3º: Multiplicações e Divisões `*`, `/`, `//`, `%`\n4º: Adições e Subtrações `+`, `-`\n\nSe houver empate (tipo uma multiplicação e uma divisão juntas), ele resolve da esquerda para a direita.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 6: 2 Objetivas ---
    {
        "id_modulo": 2, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "Regra Matemática",
        "enunciado": "Sabendo da regra de precedência, qual será o resultado exato de `print(5 + 3 * 2)`?",
        "opcoes": ["16", "11", "10", "15"],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 2, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "Alterando o Passado",
        "enunciado": "Se quisermos FORÇAR o Python a resolver a soma do exercício anterior primeiro, como devemos reescrever o código?",
        "opcoes": ["print((5 + 3) * 2)", "print(5 + (3 * 2))", "print([5 + 3] * 2)", "print(5 + 3 * 2 primeiro)"],
        "gabarito": "A", "xp_recompensa": 10
    },

    # --- Bolinha 7: Texto Finalizador ---
    {
        "id_modulo": 2, "id_etapa": 7, "tipo": "TEORIA",
        "titulo": "Matemática com Textos?",
        "enunciado": "Surpresa! No Python, alguns operadores também funcionam com textos (strings).\n\n- O `+` junta textos (chamamos de concatenação): `'Py' + 'thon'` vira `'Python'`.\n- O `*` repete textos: `'Oi' * 3` vira `'OiOiOi'`.\n\nIsso é excelente para criar divisórias em menus: `print('-' * 20)` criará uma linha com 20 tracinhos na tela.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 8: 2 Objetivas + 1 Escrever ---
    {
        "id_modulo": 2, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "O Multiplicador de Strings",
        "enunciado": "O que será exibido na tela se rodarmos o comando `print('A' * 4)`?",
        "opcoes": ["A * 4", "4A", "AAAA", "Dá erro matemático"],
        "gabarito": "C", "xp_recompensa": 10
    },
    {
        "id_modulo": 2, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "A Soma Falsa",
        "enunciado": "Preste muita atenção às aspas. O que o Python faz ao executar `print('1' + '1')`?",
        "opcoes": ["Soma matematicamente, resultando em 2", "Junta os textos, resultando em 11",
                   "Dá erro por somar textos", "Subtrai, resultando em 0"],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 2, "id_etapa": 8, "tipo": "PRATICA",
        "titulo": "Enfeitando a Tela",
        "enunciado": "Vamos usar a multiplicação de textos! Faça um `print()` que multiplique o sinal de igual `=` por 15 vezes, para gerar uma barra separadora na tela.",
        "opcoes": None, "gabarito": "===============\n", "xp_recompensa": 25
    },

    # ======================================================================
    # ETAPA 9: TESTE FINAL DO MÓDULO 2 (O Troféu)
    # 7 Exercícios (2 Obj, 1 Prática, 3 Obj, 1 Prática)
    # ======================================================================

    # --- 2 Objetivas Iniciais (Intermediárias) ---
    {
        "id_modulo": 2, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: A Divisão Justa",
        "enunciado": "Qual a diferença prática entre usar `/` e `//` no Python?",
        "opcoes": [
            "O `/` é para textos e `//` para números.",
            "O `/` faz a divisão normal (podendo dar número quebrado), enquanto o `//` corta a vírgula e retorna apenas a parte inteira.",
            "Não existe diferença, ambos mostram o mesmo resultado.",
            "O `//` serve para calcular o resto da divisão."
        ],
        "gabarito": "B", "xp_recompensa": 15
    },
    {
        "id_modulo": 2, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: Par ou Ímpar",
        "enunciado": "Na programação, o operador de resto (`%`) é muito usado para descobrir se um número é Par ou Ímpar. Se fizermos `x % 2` e o resultado for zero, o que sabemos sobre 'x'?",
        "opcoes": [
            "Sabemos que ele é um número ímpar.",
            "Sabemos que ele é um número par, pois uma divisão exata por 2 não deixa restos.",
            "Sabemos que houve um erro no código.",
            "Sabemos que 'x' vale zero."
        ],
        "gabarito": "B", "xp_recompensa": 15
    },

    # --- 1 Prática Intermediária ---
    {
        "id_modulo": 2, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Prática de Precedência",
        "enunciado": "Você sabe que o resultado natural de `5 + 2 * 3` é 11. Recrie essa conta dentro de um `print()`, mas adicione parênteses no lugar certo para FORÇAR a adição a acontecer primeiro, de modo que o resultado exibido seja 21.",
        "opcoes": None, "gabarito": "21\n", "xp_recompensa": 30
    },

    # --- 3 Objetivas de Raciocínio (Difíceis) ---
    {
        "id_modulo": 2, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Análise de Variáveis",
        "enunciado": "Leia o código mentalmente:\na = 4\nb = 2\nc = (a + b) ** b\n\nQual será o valor numérico que ficará guardado na variável 'c'?",
        "opcoes": ["12", "16", "36", "10"],
        "gabarito": "C", "xp_recompensa": 20
    },
    {
        "id_modulo": 2, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "O Perigo do Tipo Sanguíneo",
        "enunciado": "Um aluno que esqueceu de converter dados com o `int()` fez o seguinte código:\na = '5'\nb = '3'\nprint(a + b)\n\nQual será o resultado na tela?",
        "opcoes": ["8", "53", "Erro de tipo (TypeError)", "5 + 3"],
        "gabarito": "B", "xp_recompensa": 20
    },
    {
        "id_modulo": 2, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "A Matemática Completa",
        "enunciado": "Qual será o valor final da variável 'resultado' no código abaixo?\n\nvalor = 10\nresultado = (valor // 3) + (valor % 3)",
        "opcoes": ["4", "3", "1", "3.33"],
        "gabarito": "A", "xp_recompensa": 20
    },

    # --- Prática Final ---
    {
        "id_modulo": 2, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Desafio Final: O Boletim",
        "enunciado": "Você precisa calcular a sua média do semestre. A nota da P1 foi 7.5 e a nota da P2 foi 9.0. \n1. Crie a variável `p1` e a variável `p2` com esses valores (use ponto no lugar da vírgula!).\n2. Crie a variável `media` que recebe a soma das notas dividida por 2. (Dica: Lembra dos parênteses?).\n3. Use o `print()` para exibir apenas a variável `media`.",
        "opcoes": None, "gabarito": "8.25\n", "xp_recompensa": 50
    },

    # ======================================================================
    # MÓDULO 3: Utilizando Módulos
    # ======================================================================

    # --- Bolinha 1: Texto Introdutório ---
    {
        "id_modulo": 3, "id_etapa": 1, "tipo": "TEORIA",
        "titulo": "O que são Módulos?",
        "enunciado": "Até agora usamos as funções básicas que já vêm ligadas no Python (como o `print` e `int`). Mas o Python tem 'caixas de ferramentas' extras chamadas de **Módulos** ou Bibliotecas.\n\nPara usar as ferramentas matemáticas avançadas, precisamos importar a caixa inteira usando o comando `import` no topo do seu código.\n\nExemplo:\n`import math`",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 2: 2 Objetivas ---
    {
        "id_modulo": 3, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "Trazendo a Caixa de Ferramentas",
        "enunciado": "Qual é o comando correto para trazer TODAS as funcionalidades matemáticas extras para o seu programa?",
        "opcoes": ["include math", "import math", "math.import()", "use math"],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 3, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "A Analogia dos Módulos",
        "enunciado": "Podemos dizer que importar um módulo no Python é como:",
        "opcoes": [
            "Apagar todo o código escrito antes.",
            "Mudar a cor da tela do programa.",
            "Trazer uma caixa de ferramentas nova com funcionalidades que não estavam disponíveis originalmente.",
            "Desligar o computador."
        ],
        "gabarito": "C", "xp_recompensa": 10
    },

    # --- Bolinha 3: Texto de Aprofundamento ---
    {
        "id_modulo": 3, "id_etapa": 3, "tipo": "TEORIA",
        "titulo": "Pegando só uma ferramenta",
        "enunciado": "Se você importar a caixa inteira (`import math`), para usar a Raiz Quadrada você é obrigado a digitar `math.sqrt(81)`.\n\nMas se você quiser trazer SÓ a Raiz Quadrada para o seu código, economizando memória, você usa o comando `from`:\n\n`from math import sqrt`\n\nFazendo isso, você pode usar a ferramenta direto pelo nome dela: `print(sqrt(81))`.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 4: 1 Escrever ---
    {
        "id_modulo": 3, "id_etapa": 4, "tipo": "PRATICA",
        "titulo": "Calculando a Raiz",
        "enunciado": "Vamos testar o seu primeiro import! Na primeira linha, faça a importação completa da biblioteca `math` usando o comando `import math`. Na segunda linha, use o `print()` com `math.sqrt(144)` para mostrar a raiz quadrada do número 144.",
        "opcoes": None, "gabarito": "12.0\n", "xp_recompensa": 20
    },

    # --- Bolinha 5: Texto de Aprofundamento ---
    {
        "id_modulo": 3, "id_etapa": 5, "tipo": "TEORIA",
        "titulo": "Teto e Chão",
        "enunciado": "Dentro da biblioteca `math`, além da raiz, temos ferramentas muito úteis de arredondamento:\n\n1. `math.ceil()` (Teto): Arredonda o número sempre para CIMA. Exemplo: `math.ceil(4.2)` vira 5.\n2. `math.floor()` (Chão): Arredonda o número sempre para BAIXO. Exemplo: `math.floor(4.9)` vira 4.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 6: 2 Objetivas ---
    {
        "id_modulo": 3, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "Forçando para Cima",
        "enunciado": "Se um programador escrever `print(math.ceil(7.1))`, qual será o resultado exibido na tela?",
        "opcoes": ["7.1", "7", "8", "Dá erro"],
        "gabarito": "C", "xp_recompensa": 10
    },
    {
        "id_modulo": 3, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "Forçando para Baixo",
        "enunciado": "Qual será o resultado se o código for `print(math.floor(9.9))`?",
        "opcoes": ["10", "9", "9.9", "0"],
        "gabarito": "B", "xp_recompensa": 10
    },

    # --- Bolinha 7: Texto Finalizador ---
    {
        "id_modulo": 3, "id_etapa": 7, "tipo": "TEORIA",
        "titulo": "Números Aleatórios",
        "enunciado": "Outra biblioteca muito famosa no Python é a `random`, que serve para gerar coisas aleatórias (excelente para jogos!).\n\nSe você quiser que o computador sorteie um número inteiro entre 1 e 10, você faz:\n\n`import random`\n`numero = random.randint(1, 10)`",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 8: 2 Objetivas + 1 Escrever ---
    {
        "id_modulo": 3, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "Lendo o Sorteio",
        "enunciado": "Um desenvolvedor escreveu `sorteio = random.randint(5, 7)`. Quais são os únicos números que podem aparecer nessa variável?",
        "opcoes": ["Apenas 5 e 7", "5, 6 e 7", "Qualquer número de 1 a 7", "Nenhuma das anteriores"],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 3, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "A Ferramenta Certa",
        "enunciado": "Se você precisar criar um dado de 6 lados para o seu RPG de texto, qual biblioteca e função você usará?",
        "opcoes": ["math.ceil(1, 6)", "random.randint(1, 6)", "math.random(1, 6)", "sorteio.dado(6)"],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 3, "id_etapa": 8, "tipo": "PRATICA",
        "titulo": "O Arredondamento Prático",
        "enunciado": "Como o `random` gera números imprevisíveis, vamos praticar com o `math` que tem resultado exato! Importe o módulo `math` inteiro. Na linha de baixo, use o `print()` junto com a ferramenta de CHÃO `math.floor()` para arredondar o número 8.8 para baixo.",
        "opcoes": None, "gabarito": "8\n", "xp_recompensa": 25
    },

    # ======================================================================
    # ETAPA 9: TESTE FINAL DO MÓDULO 3 (O Troféu)
    # 7 Exercícios (2 Obj, 1 Prática, 3 Obj, 1 Prática)
    # ======================================================================

    # --- 2 Objetivas Iniciais (Intermediárias) ---
    {
        "id_modulo": 3, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: A Regra do Import",
        "enunciado": "Em qual parte do seu código você deve, obrigatoriamente, colocar os seus comandos de `import`?",
        "opcoes": [
            "No final do código, para não pesar a memória.",
            "Sempre na primeira linha (topo) do código, antes de tentar usar as funções deles.",
            "Dentro da função print().",
            "Não faz diferença a ordem das linhas."
        ],
        "gabarito": "B", "xp_recompensa": 15
    },
    {
        "id_modulo": 3, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: As duas formas",
        "enunciado": "Qual a principal vantagem de usar `from math import sqrt` em vez de simplesmente `import math`?",
        "opcoes": [
            "Deixa o código mais colorido no editor.",
            "O programa carrega APENAS a funcionalidade da raiz quadrada para a memória, economizando espaço.",
            "Evita que o usuário precise digitar números decimais.",
            "O Python trava se você usar 'import math' em códigos longos."
        ],
        "gabarito": "B", "xp_recompensa": 15
    },

    # --- 1 Prática Intermediária ---
    {
        "id_modulo": 3, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Prática: Arredondamento para Cima",
        "enunciado": "Importe a biblioteca matemática por completo (`import math`). Na linha de baixo, faça um `print()` que use a função de teto (`math.ceil()`) para forçar o arredondamento do número 3.1 para cima.",
        "opcoes": None, "gabarito": "4\n", "xp_recompensa": 30
    },

    # --- 3 Objetivas de Raciocínio (Difíceis) ---
    {
        "id_modulo": 3, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Caça ao Bug: Importação",
        "enunciado": "Por que o código abaixo vai quebrar imediatamente?\n\nimport math\nprint(sqrt(25))",
        "opcoes": [
            "Porque 25 não tem raiz exata.",
            "Porque o print está escrito errado.",
            "Como ele usou a importação geral (import math), ele é obrigado a referenciar a caixa escrevendo 'math.sqrt(25)'.",
            "Faltou colocar o número 25 entre aspas."
        ],
        "gabarito": "C", "xp_recompensa": 20
    },
    {
        "id_modulo": 3, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Combinando Ferramentas",
        "enunciado": "Você pode importar mais de uma ferramenta específica na mesma linha separando-as por vírgulas. Sabendo disso, como você importa o Teto e o Chão da biblioteca math de uma só vez, sem importar a biblioteca inteira?",
        "opcoes": ["import ceil, floor", "from math import ceil, floor", "import math(ceil, floor)", "from ceil, floor import math"],
        "gabarito": "B", "xp_recompensa": 20
    },
    {
        "id_modulo": 3, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Leitura de Código de Módulos",
        "enunciado": "Se um programador rodar perfeitamente o código abaixo, o que aparecerá na tela?\n\nfrom math import sqrt\nprint(sqrt(16))",
        "opcoes": ["4.0", "math.sqrt(16)", "Erro de importação", "16"],
        "gabarito": "A", "xp_recompensa": 20
    },

    # --- Prática Final ---
    {
        "id_modulo": 3, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Desafio Final: O Teorema",
        "enunciado": "O módulo `math` tem a função `math.hypot(a, b)` que calcula a hipotenusa (o lado maior) de um triângulo retângulo.\n\n1. Importe o módulo `math`.\n2. Crie a variável `ca` valendo 3 e a variável `co` valendo 4.\n3. Faça um `print()` chamando a função `math.hypot(ca, co)` para ver a mágica da matemática pronta acontecer!",
        "opcoes": None, "gabarito": "5.0\n", "xp_recompensa": 50
    },

    # ======================================================================
    # MÓDULO 4: Manipulando Textos
    # ======================================================================

    # --- Bolinha 1: Texto Introdutório ---
    {
        "id_modulo": 4, "id_etapa": 1, "tipo": "TEORIA",
        "titulo": "Textos são Correntes",
        "enunciado": "No Python, um texto (chamado de String) é como uma corrente de letras. O computador guarda cada letra em uma 'gaveta' numerada, começando SEMPRE do zero.\n\nSe a variável for `nome = 'Python'`, a letra 'P' está na gaveta 0, o 'y' na gaveta 1, e assim por diante.\n\nPara pegar só a primeira letra, colocamos o número da gaveta entre colchetes: `print(nome[0])`.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 2: 2 Objetivas ---
    {
        "id_modulo": 4, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "A Gaveta Zero",
        "enunciado": "Em qual gaveta (índice) o Python sempre guarda a PRIMEIRA letra de qualquer texto?",
        "opcoes": ["Na gaveta 1", "Na gaveta 0", "Na gaveta -1", "Depende do tamanho da palavra"],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 4, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "Buscando Letras",
        "enunciado": "Se você tem a variável `fruta = 'Banana'`, qual comando exibe apenas a letra 'n' (a primeira que aparece na palavra)?",
        "opcoes": ["print(fruta[3])", "print(fruta[2])", "print(fruta[n])", "print(fruta[1])"],
        "gabarito": "B", "xp_recompensa": 10
    },

    # --- Bolinha 3: Texto de Aprofundamento ---
    {
        "id_modulo": 4, "id_etapa": 3, "tipo": "TEORIA",
        "titulo": "Fatiando a Pizza",
        "enunciado": "Podemos pegar pedaços maiores do texto usando o Fatiamento (Slicing): `[início:fim]`.\n\nMas cuidado com a regra de ouro do Python: ele corta no número final, ou seja, **ele NÃO inclui a última gaveta!**\n\nSe `texto = 'CEUNSP'`, fazer `print(texto[0:4])` vai pegar as gavetas 0, 1, 2 e 3 (mostrando 'CEUN'). A gaveta 4 fica de fora.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 4: 1 Escrever ---
    {
        "id_modulo": 4, "id_etapa": 4, "tipo": "PRATICA",
        "titulo": "O Fatiador",
        "enunciado": "Crie a variável `jogo = 'Minecraft'`. Na linha de baixo, use o `print()` com o fatiamento `[0:4]` para exibir as 4 primeiras letras do texto e mostrar apenas a palavra 'Mine'.",
        "opcoes": None, "gabarito": "Mine\n", "xp_recompensa": 20
    },

    # --- Bolinha 5: Texto de Aprofundamento ---
    {
        "id_modulo": 4, "id_etapa": 5, "tipo": "TEORIA",
        "titulo": "Analisando a Corrente",
        "enunciado": "Podemos pedir para o Python analisar a nossa string!\n\n1. `len(nome)`: O 'len' vem de length (tamanho). Ele conta quantas letras (e espaços) existem no total da palavra.\n2. `nome.count('A')`: Conta quantas vezes uma letra específica (como a letra 'A' maiúscula) aparece dentro daquela variável.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 6: 2 Objetivas ---
    {
        "id_modulo": 4, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "Qual o tamanho?",
        "enunciado": "O que será exibido na tela se você rodar o comando `print(len('Brasil'))`?",
        "opcoes": ["5", "6", "Brasil", "B"],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 4, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "O Contador",
        "enunciado": "Se a variável é `frase = 'Abacate'`, qual será o número exibido pelo comando `print(frase.count('a'))` (minúsculo)?",
        "opcoes": ["3", "2", "0", "1"],
        "gabarito": "B", "xp_recompensa": 10
    },

    # --- Bolinha 7: Texto Finalizador ---
    {
        "id_modulo": 4, "id_etapa": 7, "tipo": "TEORIA",
        "titulo": "Transformações Mágicas",
        "enunciado": "O Python tem funções que vêm coladas no texto, chamadas de Métodos. Nós ativamos elas usando um ponto final.\n\n- `.upper()`: Transforma tudo em MAIÚSCULAS.\n- `.lower()`: Transforma tudo em minúsculas.\n- `.replace('A', 'B')`: Troca a letra ou palavra 'A' pela 'B' dentro do texto.\n\nExemplo: `print(texto.upper())`.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 8: 2 Objetivas + 1 Escrever ---
    {
        "id_modulo": 4, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "Gritando na Tela",
        "enunciado": "Qual dos comandos abaixo faria a palavra 'python' ser exibida inteiramente em letras maiúsculas ('PYTHON')?",
        "opcoes": ["print(upper('python'))", "print('python'.upper())", "print('python'.UPPER)", "print('python' + upper)"],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 4, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "Substituição Rápida",
        "enunciado": "Leia o código: \nfrase = 'Eu gosto de Java'\nprint(frase.replace('Java', 'Python'))\n\nO que aparecerá na tela?",
        "opcoes": ["Eu gosto de Java Python", "Eu gosto de Python", "Erro, replace não existe", "EU GOSTO DE PYTHON"],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 4, "id_etapa": 8, "tipo": "PRATICA",
        "titulo": "O Corretor Automático",
        "enunciado": "Crie a variável `frase = 'Eu odeio bugs'`. Na linha de baixo, use o `print()` junto com o método `.replace()` para trocar a palavra 'odeio' por 'amo' e exibir a nova frase.",
        "opcoes": None, "gabarito": "Eu amo bugs\n", "xp_recompensa": 25
    },

    # ======================================================================
    # ETAPA 9: TESTE FINAL DO MÓDULO 4 (O Troféu)
    # 7 Exercícios (2 Obj, 1 Prática, 3 Obj, 1 Prática)
    # ======================================================================

    # --- 2 Objetivas Iniciais (Intermediárias) ---
    {
        "id_modulo": 4, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: Fatiamento Aberto",
        "enunciado": "Se você omitir o número final no fatiamento, como no código `texto[2:]`, o que o Python faz?",
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
        "titulo": "Revisão: O Operador In",
        "enunciado": "O Python tem um operador mágico chamado `in` para checar se uma palavra está dentro da outra. Qual o resultado lógico (Verdadeiro ou Falso) do comando: `print('Valor' in 'Valorant')`?",
        "opcoes": ["True (Verdadeiro)", "False (Falso)", "Dá erro", "Valorant"],
        "gabarito": "A", "xp_recompensa": 15
    },

    # --- 1 Prática Intermediária ---
    {
        "id_modulo": 4, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Prática: Contando Letras",
        "enunciado": "Crie a variável `escola = 'CEUNSP'`. Na linha de baixo, use um `print()` combinado com a função `len()` para exibir o tamanho dessa palavra, ou seja, quantas letras ela possui.",
        "opcoes": None, "gabarito": "6\n", "xp_recompensa": 30
    },

    # --- 3 Objetivas de Raciocínio (Difíceis) ---
    {
        "id_modulo": 4, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "A Sujeira Invisível",
        "enunciado": "Ao usar o `input()`, um usuário pode digitar espaços sem querer, tipo: `'  Victor  '`. Qual método nativo do Python usamos para remover exclusivamente esses espaços vazios das pontas de uma string?",
        "opcoes": [".remove()", ".clear()", ".strip()", ".delete()"],
        "gabarito": "C", "xp_recompensa": 20
    },
    {
        "id_modulo": 4, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Caça ao Bug: Fatiamento",
        "enunciado": "Um aluno tentou inverter o texto. Para fazer o fatiamento pular de trás para frente, ele usou `[::-1]`. O que o `-1` representa nesse caso do fatiamento?",
        "opcoes": [
            "O número da gaveta final.",
            "O 'passo', dizendo para o Python andar de 1 em 1 para trás (reverso).",
            "Um erro matemático, índices não podem ser negativos.",
            "O método replace escondido."
        ],
        "gabarito": "B", "xp_recompensa": 20
    },
    {
        "id_modulo": 4, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Comandos Encadeados",
        "enunciado": "No Python, podemos ligar métodos como uma corrente. O que o comando `print(nome.upper().count('A'))` fará com o texto guardado na variável 'nome'?",
        "opcoes": [
            "Vai dar um erro de sintaxe.",
            "Vai contar os 'A's primeiro, e depois tentar deixar o número maiúsculo.",
            "Vai transformar tudo em maiúsculo primeiro, e depois contar quantas letras 'A' existem, garantindo que ele ache todos os 'A's independente de como o usuário digitou.",
            "Vai apagar a letra A."
        ],
        "gabarito": "C", "xp_recompensa": 20
    },

    # --- Prática Final ---
    {
        "id_modulo": 4, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Desafio Final: O Scanner Implacável",
        "enunciado": "O usuário digitou com espaços e letras minúsculas: `alerta = '  cuidado  '`.\nNa linha de baixo, faça um único `print()` que use dois métodos ao mesmo tempo: primeiro remova os espaços inúteis das pontas (usando o `.strip()`) e, logo em seguida, transforme tudo em MAIÚSCULO (com o `.upper()`).\nDica: Você pode 'correntar' os dois métodos juntos, como vimos na questão anterior!",
        "opcoes": None, "gabarito": "CUIDADO\n", "xp_recompensa": 50
    },

    # ======================================================================
    # MÓDULO 5: Condições Básicas
    # ======================================================================

    # --- Bolinha 1: Texto Introdutório ---
    {
        "id_modulo": 5, "id_etapa": 1, "tipo": "TEORIA",
        "titulo": "Tomando Decisões",
        "enunciado": "Até agora, nossos programas rodavam de cima para baixo em linha reta. Mas e se quisermos que o código só execute uma ação SE algo for verdade?\n\nUsamos a estrutura `if` (que significa 'Se').\n\nExemplo:\n`if idade >= 18:`\n    `print('Maior de idade')`\n\nNote os dois-pontos `:` no final da condição. Eles são totalmente obrigatórios para avisar o Python que a sua pergunta acabou!",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 2: 2 Objetivas ---
    {
        "id_modulo": 5, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "A Pergunta Certa",
        "enunciado": "Quando queremos PERGUNTAR ao Python se uma coisa é exatamente igual a outra na condição do `if`, qual sinal devemos usar?",
        "opcoes": ["=", "==", "===", "=>"],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 5, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "O Fim da Pergunta",
        "enunciado": "O que acontece se você esquecer de colocar os dois-pontos (`:`) no final da linha do `if`?",
        "opcoes": [
            "O código roda normalmente.",
            "O Python adiciona os dois-pontos sozinho.",
            "O programa quebra imediatamente com um Erro de Sintaxe (SyntaxError).",
            "Ele pula para a próxima linha sem executar o if."
        ],
        "gabarito": "C", "xp_recompensa": 10
    },

    # --- Bolinha 3: Texto de Aprofundamento ---
    {
        "id_modulo": 5, "id_etapa": 3, "tipo": "TEORIA",
        "titulo": "O Plano B (Senão)",
        "enunciado": "E se a condição do `if` for falsa? Podemos criar um 'Plano B' usando o `else` (que significa 'Senão').\n\nExemplo:\n`if dinheiro >= 50:`\n    `print('Vou ao cinema!')`\n`else:`\n    `print('Vou ficar em casa.')`\n\nO `else` também precisa dos dois-pontos `:`, mas atenção: ele NUNCA leva nenhuma condição ao lado dele, pois ele é a sobra de tudo que deu falso no if.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 4: 1 Escrever ---
    {
        "id_modulo": 5, "id_etapa": 4, "tipo": "PRATICA",
        "titulo": "Acesso Liberado",
        "enunciado": "Crie a variável `senha` com o número 123 (sem aspas). Na linha de baixo, crie um `if` para testar se a senha é IGUAL (`==`) a 123. Se for, imprima 'Liberado'. Na linha seguinte, crie um `else:` e, dentro dele, imprima 'Bloqueado'.",
        "opcoes": None, "gabarito": "Liberado\n", "xp_recompensa": 20
    },

    # --- Bolinha 5: Texto de Aprofundamento ---
    {
        "id_modulo": 5, "id_etapa": 5, "tipo": "TEORIA",
        "titulo": "A Magia do Espaço (Indentação)",
        "enunciado": "No Python, não usamos chaves `{}` para separar blocos de código. Usamos a **Indentação** (espaços ou 'Tab' no começo da linha).\n\nTudo que estiver 'empurrado' para a direita (com um Tab) debaixo de um `if`, pertence ao `if`.\nO que estiver colado na margem esquerda, sem espaços, está FORA do `if` e será executado pelo programa de qualquer jeito, independentemente da condição.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 6: 2 Objetivas ---
    {
        "id_modulo": 5, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "Lendo a Indentação",
        "enunciado": "Como o Python sabe quais comandos pertencem ao bloco do `else`?",
        "opcoes": [
            "Pela palavra 'fim' no final do código.",
            "Pelos comandos estarem recuados (indentados) com espaços para a direita, logo abaixo do else.",
            "Pelos parênteses ao redor dos comandos.",
            "Ele adivinha pelo sentido das palavras."
        ],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 5, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "O Comando Fora do Bloco",
        "enunciado": "Observe o código:\nif 5 > 10:\n    print('Gato')\nprint('Cachorro')\n\nO que o Python exibirá na tela?",
        "opcoes": ["Apenas Gato", "Apenas Cachorro", "Gato e Cachorro", "Não exibirá nada"],
        "gabarito": "B", "xp_recompensa": 10
    },

    # --- Bolinha 7: Texto Finalizador ---
    {
        "id_modulo": 5, "id_etapa": 7, "tipo": "TEORIA",
        "titulo": "Sinais de Comparação",
        "enunciado": "Para fazer perguntas mais complexas, usamos os Operadores Relacionais:\n\n`>` (Maior que)\n`<` (Menor que)\n`>=` (Maior ou igual)\n`<=` (Menor ou igual)\n`!=` (Diferente)\n\nSe você quiser checar se um número NÃO É igual a 10, você faz a seguinte pergunta: `if numero != 10:`.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 8: 2 Objetivas + 1 Escrever ---
    {
        "id_modulo": 5, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "Analisando a Desigualdade",
        "enunciado": "O que acontece ao rodarmos o código abaixo?\n\nmoedas = 10\nif moedas != 10:\n    print('A')\nelse:\n    print('B')",
        "opcoes": ["Mostra A", "Mostra B", "Erro de sintaxe", "Mostra 10"],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 5, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "Maior ou Igual",
        "enunciado": "Se a condição for `if pontos >= 50:`, o que acontece se a variável 'pontos' valer exatamente 50?",
        "opcoes": [
            "A condição será Verdadeira e o if será executado.",
            "A condição será Falsa, pois 50 não é maior que 50.",
            "Dá erro matemático.",
            "O programa pula direto para o else."
        ],
        "gabarito": "A", "xp_recompensa": 10
    },
    {
        "id_modulo": 5, "id_etapa": 8, "tipo": "PRATICA",
        "titulo": "Testando Diferenças",
        "enunciado": "Crie a variável `vida` com o valor 0. Faça um `if` para checar se a vida é DIFERENTE (`!=`) de 0. Se for diferente, imprima 'Vivo'. Crie um `else:` e imprima 'Game Over'.",
        "opcoes": None, "gabarito": "Game Over\n", "xp_recompensa": 25
    },

    # ======================================================================
    # ETAPA 9: TESTE FINAL DO MÓDULO 5 (O Troféu)
    # 7 Exercícios (2 Obj, 1 Prática, 3 Obj, 1 Prática)
    # ======================================================================

    # --- 2 Objetivas Iniciais (Intermediárias) ---
    {
        "id_modulo": 5, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: Recebendo Valores",
        "enunciado": "Qual a diferença vital entre o `=` (um igual) e o `==` (dois iguais) em Python?",
        "opcoes": [
            "Um igual `=` faz contas de matemática, e dois iguais `==` criam variáveis.",
            "Um igual `=` serve para ATRIBUIR (guardar) valor a uma variável. Dois iguais `==` servem para COMPARAR se duas coisas são iguais.",
            "Nenhuma, ambos fazem a mesma coisa.",
            "O `==` não existe no Python."
        ],
        "gabarito": "B", "xp_recompensa": 15
    },
    {
        "id_modulo": 5, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: A Regra do Else",
        "enunciado": "É obrigatório usar o `else` sempre que fizermos um `if`?",
        "opcoes": [
            "Sim, o Python dá erro se um 'if' não tiver seu respectivo 'else'.",
            "Sim, mas apenas quando trabalhamos com números.",
            "Não, o 'else' só funciona dentro de listas.",
            "Não. Você pode ter um 'if' sozinho. O 'else' é totalmente opcional e usado apenas quando você precisa de um 'Plano B'."
        ],
        "gabarito": "D", "xp_recompensa": 15
    },

    # --- 1 Prática Intermediária ---
    {
        "id_modulo": 5, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Prática: Multa de Velocidade",
        "enunciado": "Crie uma variável `velocidade` com o valor 95. Faça um `if` que verifique se a velocidade é estritamente MAIOR que 80. Se for, exiba a mensagem 'Multado!' usando o print.",
        "opcoes": None, "gabarito": "Multado!\n", "xp_recompensa": 30
    },

    # --- 3 Objetivas de Raciocínio (Difíceis) ---
    {
        "id_modulo": 5, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Caça ao Bug: Sintaxe Dupla",
        "enunciado": "Por que o código abaixo está errado?\n\nif idade >= 18\n    print('Pode dirigir')\nelse\n    print('Não pode')",
        "opcoes": [
            "Porque faltam aspas nos números.",
            "Porque faltam os dois-pontos (:) no final da linha do 'if' e também no final da linha do 'else'.",
            "Porque a palavra 'else' deveria estar na mesma linha do 'if'.",
            "Não tem nenhum erro, vai rodar perfeito."
        ],
        "gabarito": "B", "xp_recompensa": 20
    },
    {
        "id_modulo": 5, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Misturando Módulos",
        "enunciado": "Relembrando o Módulo 4: `len()` conta o tamanho de um texto. Se `nome = 'Ana'`, qual será o resultado do código abaixo?\n\nif len(nome) < 5:\n    print('Nome curto')\nelse:\n    print('Nome longo')",
        "opcoes": ["Nome longo", "Nome curto", "Ana", "Erro de tipo"],
        "gabarito": "B", "xp_recompensa": 20
    },
    {
        "id_modulo": 5, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "A Lógica Invertida",
        "enunciado": "O que será exibido na tela?\n\nligado = False\nif ligado == True:\n    print('Luz acesa')\nelse:\n    print('Luz apagada')",
        "opcoes": ["Luz acesa", "Luz apagada", "False", "True"],
        "gabarito": "B", "xp_recompensa": 20
    },

    # --- Prática Final ---
    {
        "id_modulo": 5, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Desafio Final: O Radar de Par ou Ímpar",
        "enunciado": "Juntando Matemática (Mod. 2) com Condições (Mod. 5)! \nCrie a variável `numero` valendo 7.\nCrie um `if` para checar se o número é PAR (lembre-se: um número é par se o resto da divisão dele por 2 for igual a zero, ou seja: `numero % 2 == 0`).\nSe for par, faça um print escrito 'PAR'.\nSenão (`else`), faça um print escrito 'IMPAR'.",
        "opcoes": None, "gabarito": "IMPAR\n", "xp_recompensa": 50
    },

    # ======================================================================
    # MÓDULO 6: Condições Aninhadas
    # ======================================================================

    # --- Bolinha 1: Texto Introdutório ---
    {
        "id_modulo": 6, "id_etapa": 1, "tipo": "TEORIA",
        "titulo": "O Caminho do Meio",
        "enunciado": "No Módulo 5, aprendemos o `if` (Sim) e o `else` (Não). Mas e se tivermos 3 ou mais opções?\n\nPara isso, o Python tem o `elif` (uma mistura de 'else' com 'if', que significa 'senão se').\n\nExemplo:\n`if cor == 'verde':`\n    `print('Siga')`\n`elif cor == 'amarelo':`\n    `print('Atenção')`\n`else:`\n    `print('Pare')`",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 2: 2 Objetivas ---
    {
        "id_modulo": 6, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "A Palavra Mágica",
        "enunciado": "Qual é a palavra-chave que usamos em Python para adicionar uma terceira (ou quarta, ou quinta...) opção de caminho no nosso código?",
        "opcoes": ["elseif", "else if", "elif", "senão se"],
        "gabarito": "C", "xp_recompensa": 10
    },
    {
        "id_modulo": 6, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "Anatomia do Comando",
        "enunciado": "Diferente do `else` (que fica sozinho na linha), o que o `elif` precisa OBRIGATORIAMENTE ter ao lado dele?",
        "opcoes": [
            "Um número.",
            "Uma condição a ser testada, exatamente como o 'if'. (Ex: elif idade > 10:)",
            "A palavra 'then'.",
            "Sempre a mesma condição que estava no 'if' anterior."
        ],
        "gabarito": "B", "xp_recompensa": 10
    },

    # --- Bolinha 3: Texto de Aprofundamento ---
    {
        "id_modulo": 6, "id_etapa": 3, "tipo": "TEORIA",
        "titulo": "As Regras do Jogo",
        "enunciado": "Existem três regras de ouro para as condições aninhadas:\n\n1. O bloco sempre deve começar com o `if`.\n2. Você pode usar QUANTOS `elif` quiser no meio do caminho (1, 5, 10... não há limites!).\n3. O `else` (se você for usá-lo) tem que ser sempre o último, para fechar a porta. Nunca coloque um `elif` depois de um `else`.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 4: 1 Escrever ---
    {
        "id_modulo": 6, "id_etapa": 4, "tipo": "PRATICA",
        "titulo": "O Caixa Eletrônico",
        "enunciado": "Crie a variável `opcao` valendo 2. Faça uma estrutura onde: \n- Se a opção for 1, imprima 'Saque'. \n- Senão se (`elif`) a opção for 2, imprima 'Extrato'. \n- Senão (`else`), imprima 'Sair'.",
        "opcoes": None, "gabarito": "Extrato\n", "xp_recompensa": 20
    },

    # --- Bolinha 5: Texto de Aprofundamento ---
    {
        "id_modulo": 6, "id_etapa": 5, "tipo": "TEORIA",
        "titulo": "A Corrida de Obstáculos",
        "enunciado": "Quando o Python encontra uma estrutura grande com `if`, vários `elif` e `else`, ele não executa tudo! Ele avalia de cima para baixo.\n\nAssim que ele encontra a PRIMEIRA condição que seja verdadeira, ele executa aquele bloco de comandos, ignora completamente todo o resto da estrutura e segue o baile! Apenas um caminho é escolhido.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 6: 2 Objetivas ---
    {
        "id_modulo": 6, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "Comportamento de Execução",
        "enunciado": "Com base no texto anterior, o que o Python faz depois de executar o bloco do primeiro `elif` verdadeiro que encontrou?",
        "opcoes": [
            "Ele testa os próximos 'elifs' só para ter certeza.",
            "Ele pula para o 'else' para finalizar.",
            "Ele ignora todo o resto da estrutura condicional e vai para a linha abaixo dela.",
            "Ele executa o programa desde o início."
        ],
        "gabarito": "C", "xp_recompensa": 10
    },
    {
        "id_modulo": 6, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "Quantas opções?",
        "enunciado": "Em um menu com 5 opções diferentes que o usuário pode escolher, como ficaria a estrutura ideal no código?",
        "opcoes": [
            "Um if, quatro elses.",
            "Cinco ifs separados.",
            "Um if, três elifs e um else final.",
            "Cinco elifs sem if."
        ],
        "gabarito": "C", "xp_recompensa": 10
    },

    # --- Bolinha 7: Texto Finalizador ---
    {
        "id_modulo": 6, "id_etapa": 7, "tipo": "TEORIA",
        "titulo": "O Final Opcional",
        "enunciado": "Muitos alunos acham que toda estrutura grande precisa terminar com `else`. Isso é um grande mito!\n\nVocê pode criar um programa que tenha apenas um `if` seguido de um ou vários `elif`. Se nenhuma das condições testadas for verdadeira, o Python simplesmente não faz nada e continua lendo o resto do programa normalmente.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 8: 2 Objetivas + 1 Escrever ---
    {
        "id_modulo": 6, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "Leitura de Código",
        "enunciado": "nome = 'Pedro'\nif nome == 'Ana':\n    print('Menina')\nelif nome == 'João':\n    print('Menino')\n\nO que aparecerá na tela?",
        "opcoes": ["Menina", "Menino", "Erro, falta o else", "Não aparecerá nada (a tela ficará em branco)"],
        "gabarito": "D", "xp_recompensa": 10
    },
    {
        "id_modulo": 6, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "Ordem de Estrutura",
        "enunciado": "Qual das opções abaixo apresenta uma estrutura condicional logicamente correta em Python?",
        "opcoes": [
            "if -> else -> elif",
            "elif -> if -> else",
            "if -> elif -> elif -> else",
            "else -> elif -> if"
        ],
        "gabarito": "C", "xp_recompensa": 10
    },
    {
        "id_modulo": 6, "id_etapa": 8, "tipo": "PRATICA",
        "titulo": "O Condicional Incompleto",
        "enunciado": "Crie a variável `idade` com o valor 15. Faça um `if` checando se a idade é maior ou igual a 18 (imprima 'Adulto'). Faça um `elif` checando se a idade é igual a 15 (imprima 'Adolescente'). Não coloque `else`!",
        "opcoes": None, "gabarito": "Adolescente\n", "xp_recompensa": 25
    },

    # ======================================================================
    # ETAPA 9: TESTE FINAL DO MÓDULO 6 (O Troféu)
    # 7 Exercícios (2 Obj, 1 Prática, 3 Obj, 1 Prática)
    # ======================================================================

    # --- 2 Objetivas Iniciais (Intermediárias) ---
    {
        "id_modulo": 6, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: if isolado vs elif",
        "enunciado": "Qual a diferença entre colocar dois `if` seguidos (um embaixo do outro) e usar a estrutura `if` seguida de `elif`?",
        "opcoes": [
            "Não tem diferença, é só questão de estética.",
            "O elif é mais lento que o if.",
            "Se você usa dois 'if', o Python testa as duas coisas e pode executar ambas. Se usa 'elif', ele liga os testes, escolhendo apenas um deles.",
            "O elif permite pular linhas de código."
        ],
        "gabarito": "C", "xp_recompensa": 15
    },
    {
        "id_modulo": 6, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: Os Dois Pontos",
        "enunciado": "Qual é a linha de código completamente correta para iniciar um bloco de elif?",
        "opcoes": [
            "elif (idade > 10)",
            "elif idade > 10:",
            "elif: idade > 10",
            "else if idade > 10:"
        ],
        "gabarito": "B", "xp_recompensa": 15
    },

    # --- 1 Prática Intermediária ---
    {
        "id_modulo": 6, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Prática: Menu de Jogos",
        "enunciado": "Vamos fazer um seletor! Crie uma variável `jogo` valendo 'Valorant'. Usando `if` e `elif`, verifique: se jogo for 'Minecraft', imprima 'Blocos'. Se for 'Valorant', imprima 'Tiro'.",
        "opcoes": None, "gabarito": "Tiro\n", "xp_recompensa": 30
    },

    # --- 3 Objetivas de Raciocínio (Difíceis) ---
    {
        "id_modulo": 6, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Caça ao Bug: Condições Aninhadas",
        "enunciado": "Por que o código abaixo vai dar erro de sintaxe e não vai rodar?\n\nif valor > 10:\n    print('Maior')\nelif:\n    print('Menor')",
        "opcoes": [
            "Porque faltou o else.",
            "Porque o 'elif' foi escrito sozinho, sem nenhuma condição para ser testada antes dos dois-pontos.",
            "Porque as palavras no print não têm aspas duplas.",
            "Porque a variável 'valor' não aceita números."
        ],
        "gabarito": "B", "xp_recompensa": 20
    },
    {
        "id_modulo": 6, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Sobreposição de Condições",
        "enunciado": "Observe com muita atenção a ordem lógica:\n\nidade = 20\nif idade >= 10:\n    print('A')\nelif idade >= 18:\n    print('B')\n\nO número 20 é maior que 10 e também é maior que 18. O que o Python fará?",
        "opcoes": [
            "Vai mostrar A e B.",
            "Vai mostrar B, pois 18 é mais próximo de 20.",
            "Vai mostrar A, pois ele executa sempre a PRIMEIRA condição verdadeira que encontra e ignora o resto, não chegando a ler o elif.",
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

    # --- Prática Final ---
    {
        "id_modulo": 6, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Desafio Final: O Boletim Escolar",
        "enunciado": "Clássico exercício do Professor Guanabara! Crie a variável `media` com o valor numérico 5.5.\nCrie a seguinte estrutura condicional completa:\n- Se a média for maior ou igual a 7.0, imprima 'Aprovado'.\n- Senão se (`elif`) a média for maior ou igual a 5.0, imprima 'Recuperação'.\n- Senão (`else`), imprima 'Reprovado'.",
        "opcoes": None, "gabarito": "Recuperação\n", "xp_recompensa": 50
    },

    # ======================================================================
    # MÓDULO 7: Estrutura de Repetição FOR
    # ======================================================================

    # --- Bolinha 1: Texto Introdutório ---
    {
        "id_modulo": 7, "id_etapa": 1, "tipo": "TEORIA",
        "titulo": "O Laço de Repetição",
        "enunciado": "Imagine que você precisa escrever 'Oi' na tela 3 vezes. Em vez de fazer três `print('Oi')`, o Python tem os 'Laços de Repetição'.\n\nO mais famoso é o `for` (para). Usamos ele junto com a função `range()` (intervalo) para dizer quantas vezes queremos repetir uma ação.\n\nExemplo:\n`for c in range(1, 4):`\n    `print('Oi')`\n\nO Python vai repetir o bloco indentado automaticamente!",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 2: 2 Objetivas ---
    {
        "id_modulo": 7, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "A Função do Laço",
        "enunciado": "Qual é a principal utilidade da estrutura `for` na programação?",
        "opcoes": [
            "Tomar decisões matemáticas complexas.",
            "Repetir um bloco de código várias vezes de forma automática, economizando linhas.",
            "Criar variáveis de texto.",
            "Perguntar a idade do usuário."
        ],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 7, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "O Parceiro do For",
        "enunciado": "Qual é o nome da função nativa do Python que quase sempre acompanha o `for` para gerar os números da contagem?",
        "opcoes": ["count()", "loop()", "range()", "repeat()"],
        "gabarito": "C", "xp_recompensa": 10
    },

    # --- Bolinha 3: Texto de Aprofundamento ---
    {
        "id_modulo": 7, "id_etapa": 3, "tipo": "TEORIA",
        "titulo": "O Segredo do Range",
        "enunciado": "A função `range(1, 4)` diz ao Python: 'Comece no 1 e vá até o 4'. Mas preste muita atenção a esta regra de ouro absoluta:\n\n**O último número NUNCA é incluído!**\n\nOu seja, `range(1, 4)` vai contar: 1, 2 e 3. Quando chega no 4, ele simplesmente para e sai do laço sem executar.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 4: 1 Escrever ---
    {
        "id_modulo": 7, "id_etapa": 4, "tipo": "PRATICA",
        "titulo": "Contando nos Dedos",
        "enunciado": "Crie um laço `for` usando uma variável `i` e a função `range()` configurada para começar no 1 e ir até o 3 (lembre-se da regra do último número para fazer isso dar certo!). Dentro do laço, dê um `print(i)` para exibir a contagem.",
        "opcoes": None, "gabarito": "1\n2\n3\n", "xp_recompensa": 20
    },

    # --- Bolinha 5: Texto de Aprofundamento ---
    {
        "id_modulo": 7, "id_etapa": 5, "tipo": "TEORIA",
        "titulo": "A Variável Fantasma",
        "enunciado": "No código `for c in range(1, 4):`, essa letra `c` é uma variável criada na hora. Ela muda de valor a cada 'volta' do laço.\n\nNa primeira volta, o `c` vale 1. Na segunda, ele se atualiza sozinho para 2. Na terceira volta, vira 3. Depois, o laço acaba. Por isso, ao imprimir essa variável, vemos os números subirem na tela!",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 6: 2 Objetivas ---
    {
        "id_modulo": 7, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "Quantas Voltas?",
        "enunciado": "Se um programador escrever `for c in range(1, 10):`, quantas vezes o laço vai se repetir no total?",
        "opcoes": ["10 vezes", "9 vezes", "8 vezes", "1 vez"],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 7, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "O Valor Final",
        "enunciado": "Considere o laço: `for x in range(1, 5):`. Qual será o valor da variável `x` na ÚLTIMA vez que o bloco de código for executado?",
        "opcoes": ["5", "1", "4", "0"],
        "gabarito": "C", "xp_recompensa": 10
    },

    # --- Bolinha 7: Texto Finalizador ---
    {
        "id_modulo": 7, "id_etapa": 7, "tipo": "TEORIA",
        "titulo": "Saltos e Marcha Ré",
        "enunciado": "O `range` pode receber um 3º número, que é o 'passo' (como ele conta os números).\n\n- Pular de 2 em 2: `range(0, 10, 2)` (Conta: 0, 2, 4, 6, 8).\n- Contagem Regressiva: `range(5, 0, -1)` (Conta: 5, 4, 3, 2, 1. Esse -1 no final manda o Python andar de costas!).",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 8: 2 Objetivas + 1 Escrever ---
    {
        "id_modulo": 7, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "Lendo a Marcha Ré",
        "enunciado": "O que será exibido se executarmos o código abaixo?\n\nfor n in range(3, 0, -1):\n    print(n)",
        "opcoes": ["0, 1, 2, 3", "3, 2, 1", "3, 2, 1, 0", "Dá erro"],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 7, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "O Salto Duplo",
        "enunciado": "Qual dos comandos abaixo fará o Python exibir os números 0, 2 e 4 (pulando de 2 em 2)?",
        "opcoes": [
            "for i in range(0, 5, 2):",
            "for i in range(0, 4, 2):",
            "for i in range(0, 5, 1):",
            "for i in range(2, 4, 0):"
        ],
        "gabarito": "A", "xp_recompensa": 10
    },
    {
        "id_modulo": 7, "id_etapa": 8, "tipo": "PRATICA",
        "titulo": "Criando Saltos",
        "enunciado": "Usando o laço `for` e o terceiro parâmetro do `range()` (o passo), exiba os números pares de 0 a 4 (ou seja, 0, 2 e 4, um em cada linha). Dica: lembre de até onde o range precisa ir para incluir o 4!",
        "opcoes": None, "gabarito": "0\n2\n4\n", "xp_recompensa": 25
    },

    # ======================================================================
    # ETAPA 9: TESTE FINAL DO MÓDULO 7 (O Troféu)
    # 7 Exercícios (2 Obj, 1 Prática, 3 Obj, 1 Prática)
    # ======================================================================

    # --- 2 Objetivas Iniciais (Intermediárias) ---
    {
        "id_modulo": 7, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: A Sintaxe Oculta",
        "enunciado": "Se você escrever apenas `range(3)` com apenas UM número dentro, o que o Python assume automaticamente?",
        "opcoes": [
            "Que é um erro de sintaxe.",
            "Ele assume que a contagem deve começar do zero. (Vai contar: 0, 1, 2).",
            "Ele assume que é o passo, e vai pular de 3 em 3.",
            "Ele conta infinitamente."
        ],
        "gabarito": "B", "xp_recompensa": 15
    },
    {
        "id_modulo": 7, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: O Fim da Linha",
        "enunciado": "Qual caractere é totalmente OBRIGATÓRIO no final da linha do `for` para que ele funcione, assim como no `if`?",
        "opcoes": ["O ponto final (.)", "O ponto e vírgula (;)", "Os dois-pontos (:)", "As chaves {}"],
        "gabarito": "C", "xp_recompensa": 15
    },

    # --- 1 Prática Intermediária ---
    {
        "id_modulo": 7, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Prática: O Início Zero",
        "enunciado": "Vamos testar o atalho! Crie um laço `for i in range(...)` passando apenas UM número dentro do range, de forma que o programa imprima na tela os números 0, 1 e 2.",
        "opcoes": None, "gabarito": "0\n1\n2\n", "xp_recompensa": 30
    },

    # --- 3 Objetivas de Raciocínio (Difíceis) ---
    {
        "id_modulo": 7, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "O Comando Fora do Laço",
        "enunciado": "Preste atenção à indentação:\n\nfor c in range(1, 3):\n    print('A')\nprint('B')\n\nO que o Python exibirá?",
        "opcoes": [
            "A, B, A, B",
            "A, A, B (O 'A' repete duas vezes no laço, e o 'B' roda só uma vez quando o laço acaba).",
            "B, B",
            "Erro de sintaxe"
        ],
        "gabarito": "B", "xp_recompensa": 20
    },
    {
        "id_modulo": 7, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Acumuladores",
        "enunciado": "Um padrão muito comum é somar os valores do laço em uma variável externa. Veja:\n\nsoma = 0\nfor i in range(1, 4):\n    soma = soma + i\n\nNo final do programa, qual será o valor guardado na variável 'soma'?",
        "opcoes": ["3", "4", "6", "0"],
        "gabarito": "C", "xp_recompensa": 20
    },
    {
        "id_modulo": 7, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Repetindo com Inputs",
        "enunciado": "O que acontece se colocarmos um `input()` DENTRO do bloco indentado de um `for` que repete 5 vezes?",
        "opcoes": [
            "Dá erro, pois inputs só funcionam fora de laços.",
            "O Python vai pausar o programa e perguntar 5 vezes seguidas para o usuário digitar algo.",
            "O Python pula o input e só faz os prints.",
            "O programa trava em um loop infinito."
        ],
        "gabarito": "B", "xp_recompensa": 20
    },

    # --- Prática Final ---
    {
        "id_modulo": 7, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Desafio Final: Ano Novo!",
        "enunciado": "Junte tudo o que aprendeu! \n1. Crie um laço `for` com uma contagem regressiva. O laço deve imprimir os números 3, 2 e 1 (lembre-se do -1 no passo do range).\n2. FORA DO LAÇO (sem espaços na esquerda), imprima a palavra 'FOGO!'.",
        "opcoes": None, "gabarito": "3\n2\n1\nFOGO!\n", "xp_recompensa": 50
    },

    # ======================================================================
    # MÓDULO 8: Estrutura de Repetição WHILE
    # ======================================================================

    # --- Bolinha 1: Texto Introdutório ---
    {
        "id_modulo": 8, "id_etapa": 1, "tipo": "TEORIA",
        "titulo": "O Laço Condicional",
        "enunciado": "No Módulo 7, usamos o `for` para repetir quando SABEMOS o limite (ex: contar de 1 a 10).\n\nMas e se não soubermos quando a repetição vai acabar? Usamos o `while` (Enquanto).\nEle repete o bloco de código DE NOVO E DE NOVO enquanto uma condição for verdadeira.\n\nExemplo:\n`c = 1`\n`while c < 4:`\n    `print(c)`\n    `c = c + 1`",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 2: 2 Objetivas ---
    {
        "id_modulo": 8, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "A Tradução",
        "enunciado": "O que a palavra `while` significa literalmente em português, e qual a sua lógica de funcionamento?",
        "opcoes": [
            "Significa 'Para'. Ele roda uma vez para cada item.",
            "Significa 'Se'. Ele faz um teste lógico apenas uma vez.",
            "Significa 'Enquanto'. Ele executa o bloco de código repetidamente ENQUANTO a condição testada for verdadeira.",
            "Significa 'Repita'. Ele repete infinitamente sem regras."
        ],
        "gabarito": "C", "xp_recompensa": 10
    },
    {
        "id_modulo": 8, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "A Variável Externa",
        "enunciado": "Ao contrário do `for`, que cria a variável de contagem sozinho (ex: `for c in range...`), o que precisamos fazer obrigatoriamente no `while`?",
        "opcoes": [
            "Não usamos variáveis com o while.",
            "Precisamos CRIAR a variável de controle antes dele começar.",
            "Temos que usar a palavra range() dentro dele.",
            "O usuário tem que digitar a variável toda vez."
        ],
        "gabarito": "B", "xp_recompensa": 10
    },

    # --- Bolinha 3: Texto de Aprofundamento ---
    {
        "id_modulo": 8, "id_etapa": 3, "tipo": "TEORIA",
        "titulo": "O Perigo do Loop Infinito",
        "enunciado": "Se você cria um `while` mas nunca altera a variável que ele está testando, o programa fica preso para sempre!\n\nSe você fizer:\n`c = 1`\n`while c < 4:`\n    `print(c)`\n\nComo o valor do `c` nunca muda, ele vai ser eternamente menor que 4. O computador vai imprimir o número 1 infinitamente até travar. Você SEMPRE precisa atualizar a variável dentro do laço (ex: `c = c + 1`).",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 4: 1 Escrever ---
    {
        "id_modulo": 8, "id_etapa": 4, "tipo": "PRATICA",
        "titulo": "O Seu Primeiro While",
        "enunciado": "Vamos testar sem travar! \n1. Crie uma variável `cont` com o valor 1.\n2. Crie um `while` que rode enquanto `cont` for menor ou igual a 3.\n3. Dentro do laço (indentado), imprima a palavra 'Loop'.\n4. Na linha seguinte (ainda dentro do laço), adicione 1 à variável `cont` (`cont = cont + 1`).",
        "opcoes": None, "gabarito": "Loop\nLoop\nLoop\n", "xp_recompensa": 20
    },

    # --- Bolinha 5: Texto de Aprofundamento ---
    {
        "id_modulo": 8, "id_etapa": 5, "tipo": "TEORIA",
        "titulo": "A Condição Falsa Inicial",
        "enunciado": "O `while` é um guarda muito rigoroso. Ele testa a condição ANTES de deixar o bloco rodar, a cada nova volta.\n\nMas o que acontece se a condição já for falsa logo na PRIMEIRA vez?\nExemplo:\n`x = 10`\n`while x < 5:`\n    `print('Rodando')`\n\nComo 10 não é menor que 5, o Python simplesmente ignora todo o bloco do `while` e o programa continua na linha abaixo dele, sem nunca imprimir 'Rodando'.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 6: 2 Objetivas ---
    {
        "id_modulo": 8, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "Identificando a Trava",
        "enunciado": "Observe o código:\nx = 0\nwhile x < 5:\n    print('Rodando')\n\nPor que este código é um loop infinito?",
        "opcoes": [
            "Porque faltaram os dois-pontos.",
            "Porque 0 sempre será menor que 5, e o código não atualiza o valor de 'x' em nenhum momento dentro do laço.",
            "Porque a palavra 'Rodando' é muito grande.",
            "Porque o 'x' começou com zero."
        ],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 8, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "O Salto do Guarda",
        "enunciado": "Se a variável inicial é `c = 50` e o laço é `while c < 10:`, quantas vezes o bloco indentado abaixo dele será executado?",
        "opcoes": ["10 vezes", "50 vezes", "1 vez", "Nenhuma vez, o bloco será ignorado pois a condição já é falsa no início."],
        "gabarito": "D", "xp_recompensa": 10
    },

    # --- Bolinha 7: Texto Finalizador ---
    {
        "id_modulo": 8, "id_etapa": 7, "tipo": "TEORIA",
        "titulo": "A Condição de Parada (Flag)",
        "enunciado": "O maior poder do `while` é continuar pedindo dados ao usuário até que ele digite uma 'senha' de saída.\n\nExemplo:\n`n = 1`\n`while n != 0:`\n    `n = int(input('Digite um valor (0 para parar): '))`\n\nNeste caso, o programa não tem um limite fixo (como 5 ou 10 vezes). Ele vai repetir 1000 vezes se o usuário quiser. Só vai parar quando o usuário digitar o número 0.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 8: 2 Objetivas + 1 Escrever ---
    {
        "id_modulo": 8, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "A Diferença de Ouro",
        "enunciado": "Considerando o que aprendemos sobre a 'Flag' de parada, qual é a diferença absoluta entre o `for` e o `while`?",
        "opcoes": [
            "O for é para matemática, o while é para textos.",
            "O for é usado quando SABEMOS o limite exato de repetições. O while é usado quando NÃO SABEMOS o limite, dependendo de uma condição para parar.",
            "Não existe diferença, os dois funcionam da mesma maneira.",
            "O while só roda uma vez no máximo."
        ],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 8, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "O Limite Misterioso",
        "enunciado": "Imagine um programa com a seguinte linha: `while texto != 'sair':`.\nQuando o laço vai parar de repetir?",
        "opcoes": [
            "Quando o programa acabar o tempo.",
            "Ele vai parar na primeira volta automaticamente.",
            "Ele é um loop infinito por natureza.",
            "Exclusivamente quando o usuário digitar a palavra 'sair'."
        ],
        "gabarito": "D", "xp_recompensa": 10
    },
    {
        "id_modulo": 8, "id_etapa": 8, "tipo": "PRATICA",
        "titulo": "Contando com While",
        "enunciado": "Para fixar o básico: crie uma variável `i` igual a 0. Usando o laço `while`, repita um bloco enquanto `i` for menor que 2. Dentro do bloco, imprima o valor de `i` e na linha seguinte some 1 a ele (`i = i + 1`).",
        "opcoes": None, "gabarito": "0\n1\n", "xp_recompensa": 25
    },

    # ======================================================================
    # ETAPA 9: TESTE FINAL DO MÓDULO 8 (O Troféu)
    # 7 Exercícios (2 Obj, 1 Prática, 3 Obj, 1 Prática)
    # ======================================================================

    # --- 2 Objetivas Iniciais (Intermediárias) ---
    {
        "id_modulo": 8, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: A Variável Externa",
        "enunciado": "O que precisamos fazer obrigatoriamente ANTES de iniciar um bloco `while`, que não precisávamos fazer no `for`?",
        "opcoes": [
            "Importar a biblioteca math.",
            "Criar a variável que será testada na condição.",
            "Colocar um comando if.",
            "Usar a função range()."
        ],
        "gabarito": "B", "xp_recompensa": 15
    },
    {
        "id_modulo": 8, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: Atualização",
        "enunciado": "Por que o comando `c = c + 1` (ou similar) é quase sempre obrigatório dentro de um laço `while` numérico?",
        "opcoes": [
            "Para deixar o código mais complexo.",
            "Para evitar um Loop Infinito, garantindo que a condição chegue a ser falsa em algum momento.",
            "Para o Python não dar erro de sintaxe.",
            "Para transformar o número em string."
        ],
        "gabarito": "B", "xp_recompensa": 15
    },

    # --- 1 Prática Intermediária ---
    {
        "id_modulo": 8, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Prática: Contagem do While",
        "enunciado": "Faça uma contagem de 1 a 3! Crie `x = 1`. Crie um `while` testando se `x <= 3`. Dentro dele, imprima a palavra 'Rodada', e na linha seguinte, atualize a variável para `x = x + 1`.",
        "opcoes": None, "gabarito": "Rodada\nRodada\nRodada\n", "xp_recompensa": 30
    },

    # --- 3 Objetivas de Raciocínio (Difíceis) ---
    {
        "id_modulo": 8, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Caça ao Bug: Loop Infinito",
        "enunciado": "Onde está o erro gravíssimo no código abaixo?\n\nvidas = 3\nwhile vidas > 0:\n    print('Ainda vivo!')",
        "opcoes": [
            "O while precisa de parênteses.",
            "Faltou o if antes do while.",
            "A variável 'vidas' não foi diminuída dentro do bloco, gerando um Loop Infinito que trava o computador.",
            "A variável deveria ser declarada como texto."
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
    {
        "id_modulo": 8, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "O Fim Invisível",
        "enunciado": "Se a condição do while é `while numero != 0:`, e o usuário digita '0' logo no primeiro input dentro do laço, o que acontece?",
        "opcoes": [
            "O programa roda mais uma vez para garantir.",
            "O programa apaga a tela.",
            "Quando o laço tenta voltar para o topo e testar a condição de novo, ele percebe que agora é falso e sai imediatamente da estrutura.",
            "O while dá erro e para o código."
        ],
        "gabarito": "C", "xp_recompensa": 20
    },

    # --- Prática Final ---
    {
        "id_modulo": 8, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Desafio Final: O Foguete Manual",
        "enunciado": "Vamos recriar a contagem regressiva (Módulo 7), mas agora usando apenas o `while`! \n1. Crie a variável `tempo` com o valor 3.\n2. Crie um `while` para rodar enquanto o tempo for estritamente MAIOR que 0.\n3. Dentro do laço: imprima o tempo, e depois diminua 1 do tempo (`tempo = tempo - 1`).\n4. Fora do laço (sem indentação), imprima 'FOGO!'.",
        "opcoes": None, "gabarito": "3\n2\n1\nFOGO!\n", "xp_recompensa": 50
    },

    # ======================================================================
    # MÓDULO 9: Interrompendo Repetições
    # ======================================================================

    # --- Bolinha 1: Texto Introdutório ---
    {
        "id_modulo": 9, "id_etapa": 1, "tipo": "TEORIA",
        "titulo": "O Laço Eterno",
        "enunciado": "No módulo passado, vimos que esquecer de atualizar a variável cria um 'Loop Infinito' acidental.\n\nMas e se quisermos criar um loop infinito PROPOSITAL? Usamos o comando `while True:` (com 'T' maiúsculo).\n\nComo 'True' significa 'Verdadeiro', a condição nunca será falsa, e o laço rodará para sempre. Mas como saímos dele? Veremos logo a seguir!",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 2: 2 Objetivas ---
    {
        "id_modulo": 9, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "A Condição Eterna",
        "enunciado": "Por que o comando `while True:` cria um laço infinito?",
        "opcoes": [
            "Porque ele testa se True é igual a False.",
            "Porque a condição de parada é literalmente a palavra 'Verdadeiro', ou seja, ela nunca vai se transformar em falsa sozinha.",
            "Porque o Python tem um bug no comando while.",
            "Porque faltou declarar uma variável numérica."
        ],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 9, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "Regra Maiúscula",
        "enunciado": "No Python, como as palavras lógicas de 'Verdadeiro' e 'Falso' devem ser escritas obrigatoriamente?",
        "opcoes": [
            "Tudo em minúsculo: true e false.",
            "Tudo em maiúsculo: TRUE e FALSE.",
            "Apenas a primeira letra deve ser maiúscula: True e False.",
            "Entre aspas."
        ],
        "gabarito": "C", "xp_recompensa": 10
    },

    # --- Bolinha 3: Texto de Aprofundamento ---
    {
        "id_modulo": 9, "id_etapa": 3, "tipo": "TEORIA",
        "titulo": "A Saída de Emergência",
        "enunciado": "Para escapar de um `while True:`, usamos o comando `break` (que significa quebrar/interromper).\n\nGeralmente, colocamos o `break` dentro de um `if`. Assim que o Python lê a palavra `break`, ele ejeta o programa imediatamente para FORA do laço.\n\nExemplo:\n`while True:`\n    `n = 10`\n    `if n == 10:`\n        `break`",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 4: 1 Escrever ---
    {
        "id_modulo": 9, "id_etapa": 4, "tipo": "PRATICA",
        "titulo": "Testando o Freio",
        "enunciado": "Vamos parar um loop infinito! \n1. Crie um `while True:`.\n2. Dentro dele, imprima 'Rodando'.\n3. Na linha de baixo (ainda no while), faça um `if 1 == 1:`.\n4. Dentro do if, coloque a palavra mágica `break`.\nAssim, ele vai rodar apenas uma vez e quebrar!",
        "opcoes": None, "gabarito": "Rodando\n", "xp_recompensa": 20
    },

    # --- Bolinha 5: Texto de Aprofundamento ---
    {
        "id_modulo": 9, "id_etapa": 5, "tipo": "TEORIA",
        "titulo": "O Abandono Súbito",
        "enunciado": "É muito importante entender o que o `break` faz com o resto do código.\n\nSe existir qualquer comando DEPOIS do `break` DENTRO do laço, esse comando será completamente IGNORADO. O `break` não avisa, ele simplesmente sai da repetição na mesma hora em que é ativado e continua o código principal lá embaixo.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 6: 2 Objetivas ---
    {
        "id_modulo": 9, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "A Interrupção Brusca",
        "enunciado": "O que acontece com os comandos que estão dentro do laço, mas que foram escritos nas linhas abaixo do `break` ativado?",
        "opcoes": [
            "Eles são executados pela última vez antes de sair.",
            "Eles dão erro de sintaxe.",
            "Eles são completamente ignorados, pois o break sai do laço na mesma hora.",
            "Eles são salvos na memória."
        ],
        "gabarito": "C", "xp_recompensa": 10
    },
    {
        "id_modulo": 9, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "Leitura de Break",
        "enunciado": "Analise o código:\n\nc = 1\nwhile True:\n    if c == 3:\n        break\n    c = c + 1\n\nQual será o valor final da variável 'c' guardado na memória quando o laço acabar?",
        "opcoes": ["1", "2", "3", "Infinito"],
        "gabarito": "C", "xp_recompensa": 10
    },

    # --- Bolinha 7: Texto Finalizador ---
    {
        "id_modulo": 9, "id_etapa": 7, "tipo": "TEORIA",
        "titulo": "O Poder das F-Strings",
        "enunciado": "Antes, para juntar texto com variáveis em um print, tínhamos que usar várias vírgulas ou sinais de +, o que deixava o código confuso.\n\nAgora vamos usar as **F-Strings**! Basta colocar um `f` antes das aspas, e você pode colocar qualquer variável dentro de chaves `{ }` direto no meio do texto.\n\nExemplo:\n`nome = 'Ana'`\n`print(f'O nome dela é {nome}!')`",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 8: 2 Objetivas + 1 Escrever ---
    {
        "id_modulo": 9, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "A Formatação Certa",
        "enunciado": "Temos a variável `moedas = 50`. Qual das opções abaixo usa a F-String da maneira perfeitamente correta para exibir a frase 'Tenho 50 moedas'?",
        "opcoes": [
            "print('Tenho {moedas} moedas'f)",
            "print(F'Tenho' {moedas} 'moedas')",
            "print(f'Tenho moedas {50}')",
            "print(f'Tenho {moedas} moedas')"
        ],
        "gabarito": "D", "xp_recompensa": 10
    },
    {
        "id_modulo": 9, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "Matemática na String",
        "enunciado": "A mágica das F-Strings é que elas conseguem resolver matemática lá dentro! O que aparece na tela se rodarmos o código abaixo?\n\nn = 10\nprint(f'O dobro é {n * 2}')",
        "opcoes": [
            "O dobro é n * 2",
            "O dobro é 20",
            "O dobro é {20}",
            "Erro, chaves só aceitam variáveis"
        ],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 9, "id_etapa": 8, "tipo": "PRATICA",
        "titulo": "Sua Primeira F-String",
        "enunciado": "Crie uma variável `linguagem` recebendo 'Python' e `versao` recebendo o número 3. Usando um único `print()` com a tecnologia de F-String (`f'...'`), exiba a frase exata: 'Aprendendo Python 3'.",
        "opcoes": None, "gabarito": "Aprendendo Python 3\n", "xp_recompensa": 25
    },

    # ======================================================================
    # ETAPA 9: TESTE FINAL DO MÓDULO 9 (O Troféu)
    # 7 Exercícios (2 Obj, 1 Prática, 3 Obj, 1 Prática)
    # ======================================================================

    # --- 2 Objetivas Iniciais (Intermediárias) ---
    {
        "id_modulo": 9, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: A Ferramenta",
        "enunciado": "O comando `break` serve exclusivamente para qual das finalidades abaixo?",
        "opcoes": [
            "Quebrar o computador (dar um erro proposital de sistema).",
            "Interromper e sair imediatamente de um laço de repetição (como for ou while).",
            "Pausar o programa por 5 segundos.",
            "Dividir uma variável matemática ao meio."
        ],
        "gabarito": "B", "xp_recompensa": 15
    },
    {
        "id_modulo": 9, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: As Chaves",
        "enunciado": "Nas F-Strings (ex: `f'Olá {nome}'`), para que servem as chaves `{}`?",
        "opcoes": [
            "Para enfeitar o texto exibido no terminal.",
            "Para criar um novo bloco de código, como no C++.",
            "Para avisar o Python que o que está lá dentro não é um texto comum, mas sim uma variável ou cálculo que deve ser resolvido e exibido.",
            "Para criar listas."
        ],
        "gabarito": "C", "xp_recompensa": 15
    },

    # --- 1 Prática Intermediária ---
    {
        "id_modulo": 9, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Prática: Interrupção e Print",
        "enunciado": "Crie um `while True:`. Dentro dele, faça um `print()` que escreva 'Entrou'. Logo abaixo (ainda no while), crie um `if True:` e coloque o `break` dentro dele. Ele vai imprimir apenas uma vez e sair.",
        "opcoes": None, "gabarito": "Entrou\n", "xp_recompensa": 30
    },

    # --- 3 Objetivas de Raciocínio (Difíceis) ---
    {
        "id_modulo": 9, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Caça ao Bug: Case Sensitive",
        "enunciado": "Por que o laço abaixo não vai rodar e acusará um erro fatal (NameError) na primeira linha?\n\nwhile true:\n    print('Correndo')\n    break",
        "opcoes": [
            "O break não pode ficar sozinho sem um if.",
            "A palavra 'true' está em minúsculo, mas o Python exige a primeira letra maiúscula ('True').",
            "Faltaram as chaves do while.",
            "A palavra 'Correndo' é grande demais para ser impressa."
        ],
        "gabarito": "B", "xp_recompensa": 20
    },
    {
        "id_modulo": 9, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Lógica do Break vs Flag",
        "enunciado": "Qual é a principal vantagem tática apontada pelo Professor Guanabara em usar `while True:` com `break` ao invés de usar uma condição comum lá em cima (ex: `while num != 999:`)?",
        "opcoes": [
            "O código roda muito mais rápido na memória RAM.",
            "Ocupa muito menos linhas de código na tela do VSCode.",
            "Evita que o programa execute comandos com o valor de parada. Ele permite sair IMEDIATAMENTE antes de realizar cálculos indesejados no fim do laço.",
            "Permite usar o input sem precisar usar variáveis."
        ],
        "gabarito": "C", "xp_recompensa": 20
    },
    {
        "id_modulo": 9, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Simulando o Fim",
        "enunciado": "Analise com cuidado:\nsoma = 0\nwhile True:\n    x = 5\n    if x == 5:\n        break\n    soma = soma + 1\n\nQual será o valor da variável 'soma' quando o laço acabar?",
        "opcoes": ["1", "5", "0", "Loop Infinito"],
        "gabarito": "C", "xp_recompensa": 20
    },

    # --- Prática Final ---
    {
        "id_modulo": 9, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Desafio Final: O Somatório de Fuga",
        "enunciado": "Juntando Acumulador + While True + Break + F-String!\n1. Crie as variáveis `soma = 0` e `c = 1`.\n2. Crie o laço `while True:`.\n3. Dentro dele, se `c == 4:`, dê o `break`.\n4. Na mesma indentação do `if` (fora dele, mas dentro do while), atualize a soma: `soma = soma + c`, e depois atualize o c: `c = c + 1`.\n5. TOTALMENTE FORA do laço, use uma F-String para exibir a frase exata: 'A soma final é 6' (usando a variável soma dentro das chaves).",
        "opcoes": None, "gabarito": "A soma final é 6\n", "xp_recompensa": 50
    },

    # ======================================================================
    # MÓDULO 10: Variáveis Compostas - Tuplas
    # ======================================================================

    # --- Bolinha 1: Texto Introdutório ---
    {
        "id_modulo": 10, "id_etapa": 1, "tipo": "TEORIA",
        "titulo": "As Variáveis Compostas",
        "enunciado": "Até agora, nossas variáveis eram como 'caixas' simples, que guardavam uma coisa só. Se você fizesse `lanche = 'Hambúrguer'` e depois `lanche = 'Suco'`, o Hambúrguer era apagado.\n\nAs Variáveis Compostas são caixas com divisórias! A mais simples delas é a **Tupla**.\nEla é criada usando parênteses `()`.\n\nExemplo:\n`lanche = ('Hambúrguer', 'Suco', 'Pizza')`\nO Python guarda tudo de uma vez, cada um na sua gaveta (0, 1 e 2).",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 2: 2 Objetivas ---
    {
        "id_modulo": 10, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "O Símbolo da Tupla",
        "enunciado": "Qual é a pontuação clássica e recomendada que usamos para abraçar os itens e criar uma Tupla no Python?",
        "opcoes": ["Chaves { }", "Colchetes [ ]", "Parênteses ( )", "Aspas ' '"],
        "gabarito": "C", "xp_recompensa": 10
    },
    {
        "id_modulo": 10, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "A Gaveta Inicial",
        "enunciado": "Assim como nos textos (strings), se você tiver a tupla `lanche = ('Suco', 'Pizza')`, qual é o número da gaveta (índice) que guarda a palavra 'Suco'?",
        "opcoes": ["Gaveta 1", "Gaveta 0", "Gaveta 2", "A gaveta 'Suco'"],
        "gabarito": "B", "xp_recompensa": 10
    },

    # --- Bolinha 3: Texto de Aprofundamento ---
    {
        "id_modulo": 10, "id_etapa": 3, "tipo": "TEORIA",
        "titulo": "A Regra de Ouro",
        "enunciado": "Lembre-se desta frase para o resto da sua vida como programador:\n\n**'As tuplas são IMUTÁVEIS.'**\n\nIsso significa que, depois que a tupla é criada, você NÃO PODE mudar, adicionar ou remover itens dela durante o funcionamento do programa.\nSe você tentar forçar a barra fazendo `lanche[0] = 'Água'`, o Python vai gritar e travar o programa com um erro na tela!",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 4: 1 Escrever ---
    {
        "id_modulo": 10, "id_etapa": 4, "tipo": "PRATICA",
        "titulo": "Sua Primeira Tupla",
        "enunciado": "Crie uma tupla chamada `jogos` contendo os textos 'Minecraft' e 'Valorant' (nesta exata ordem). Na linha de baixo, use o `print()` indicando o índice `[1]` para exibir apenas a palavra 'Valorant'.",
        "opcoes": None, "gabarito": "Valorant\n", "xp_recompensa": 20
    },

    # --- Bolinha 5: Texto de Aprofundamento ---
    {
        "id_modulo": 10, "id_etapa": 5, "tipo": "TEORIA",
        "titulo": "O Laço Desempacotador",
        "enunciado": "A verdadeira magia das variáveis compostas é usá-las junto com o laço `for`!\n\nVocê não precisa mais usar o comando `range()`. O Python é inteligente o suficiente para varrer a tupla sozinho, item por item.\n\nExemplo:\n`lanche = ('Suco', 'Pizza')`\n`for comida in lanche:`\n    `print(comida)`\n\nA variável `comida` vai receber automaticamente um item da tupla a cada volta do laço!",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 6: 2 Objetivas ---
    {
        "id_modulo": 10, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "Tentando Mudar o Passado",
        "enunciado": "Um aluno escreveu o seguinte código:\nt = ('A', 'B', 'C')\nt[1] = 'X'\nprint(t)\n\nO que vai acontecer ao rodar o programa?",
        "opcoes": [
            "A tela vai mostrar ('A', 'X', 'C').",
            "O programa vai ignorar a linha e mostrar ('A', 'B', 'C').",
            "A tupla vai virar apenas ('X').",
            "O programa vai travar com um erro (TypeError), porque as tuplas são imutáveis e não aceitam alterações."
        ],
        "gabarito": "D", "xp_recompensa": 10
    },
    {
        "id_modulo": 10, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "Lendo o Laço Mágico",
        "enunciado": "O que acontece ao executarmos o código abaixo?\ntupla = (10, 20)\nfor n in tupla:\n    print(n)",
        "opcoes": [
            "Ele imprime (10, 20) de uma vez só na mesma linha.",
            "Ele imprime o número 10 e depois o 20, um em cada linha.",
            "Ele imprime 0 e 1 (as posições numéricas).",
            "Dá erro por faltar a palavra 'range'."
        ],
        "gabarito": "B", "xp_recompensa": 10
    },

    # --- Bolinha 7: Texto Finalizador ---
    {
        "id_modulo": 10, "id_etapa": 7, "tipo": "TEORIA",
        "titulo": "Truques Secretos",
        "enunciado": "As tuplas aceitam dois truques fantásticos:\n\n1. **Fatiamento:** Assim como nas strings, você pode pegar pedaços da tupla. Se `t = (1, 2, 3)`, fazer `t[0:2]` pegará os itens 1 e 2.\n2. **Índice Reverso:** Se você usar números negativos, o Python conta de trás para frente! A gaveta `[-1]` SEMPRE pega o ÚLTIMO item da tupla, a `[-2]` o penúltimo, etc.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 8: 2 Objetivas + 1 Escrever ---
    {
        "id_modulo": 10, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "Fatiando a Tupla",
        "enunciado": "Se temos a tupla `lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')`, o que o comando `print(lanche[0:2])` exibirá?",
        "opcoes": [
            "Hambúrguer, Suco e Pizza.",
            "Hambúrguer e Suco (lembre-se, o fatiamento ignora o último número).",
            "Apenas o Suco.",
            "Dá erro pois tuplas não aceitam fatiamento."
        ],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 10, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "O Índice Reverso",
        "enunciado": "No Python, se você acessar a gaveta `[-1]` de uma tupla gigante com 50 itens, o que o Python retorna?",
        "opcoes": [
            "Dá um erro de índice fora do limite.",
            "Retorna o primeiro item.",
            "Retorna a tupla inteira invertida.",
            "Retorna exatamente o ÚLTIMO item da tupla."
        ],
        "gabarito": "D", "xp_recompensa": 10
    },
    {
        "id_modulo": 10, "id_etapa": 8, "tipo": "PRATICA",
        "titulo": "Pegando o Último",
        "enunciado": "Crie a tupla `t = ('A', 'B', 'C', 'D')`. Na linha de baixo, use o `print()` combinado com o índice negativo `[-1]` para imprimir na tela exclusivamente a letra 'D', independentemente do tamanho da tupla.",
        "opcoes": None, "gabarito": "D\n", "xp_recompensa": 25
    },

    # ======================================================================
    # ETAPA 9: TESTE FINAL DO MÓDULO 10 (O Troféu)
    # 7 Exercícios (2 Obj, 1 Prática, 3 Obj, 1 Prática)
    # ======================================================================

    # --- 2 Objetivas Iniciais (Intermediárias) ---
    {
        "id_modulo": 10, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: A Regra Absoluta",
        "enunciado": "Qual é a característica fundamental e inquebrável de uma Tupla em Python?",
        "opcoes": [
            "Elas só aceitam textos, nunca números.",
            "Elas não podem ser usadas dentro do comando print.",
            "Elas são IMUTÁVEIS, não podendo sofrer alterações durante a execução do programa.",
            "Elas têm limite máximo de 5 itens."
        ],
        "gabarito": "C", "xp_recompensa": 15
    },
    {
        "id_modulo": 10, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: Mistura de Tipos",
        "enunciado": "No Python, é possível ter uma mesma tupla misturando textos e números, como por exemplo `pessoa = ('Victor', 20)`?",
        "opcoes": [
            "Sim, as variáveis compostas no Python podem guardar tipos de dados completamente diferentes ao mesmo tempo.",
            "Não, uma tupla deve ser feita só de textos ou só de números.",
            "Apenas se colocarmos os números entre aspas.",
            "Sim, mas apenas na versão mais recente do Python."
        ],
        "gabarito": "A", "xp_recompensa": 15
    },

    # --- 1 Prática Intermediária ---
    {
        "id_modulo": 10, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Prática: Matemática com Tuplas",
        "enunciado": "Se você somar duas tuplas com o sinal `+`, o Python junta as duas em uma só! Crie a variável `a = (1, 2)` e a variável `b = (3, 4)`. Na linha de baixo, imprima o resultado direto da soma `a + b`.",
        "opcoes": None, "gabarito": "(1, 2, 3, 4)\n", "xp_recompensa": 30
    },

    # --- 3 Objetivas de Raciocínio (Difíceis) ---
    {
        "id_modulo": 10, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Caça ao Bug: Parênteses vs Colchetes",
        "enunciado": "Qual a diferença exata entre escrever `t = ('A', 'B')` e escrever `print(t[0])`?",
        "opcoes": [
            "É a mesma coisa.",
            "Colchetes servem para criar a tupla, parênteses para acessar.",
            "Parênteses () servem para CRIAR a tupla na memória. Colchetes [] servem para ACESSAR uma gaveta específica de uma variável que já existe.",
            "Colchetes indicam um erro no código, pois tuplas só usam parênteses."
        ],
        "gabarito": "C", "xp_recompensa": 20
    },
    {
        "id_modulo": 10, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Encontrando Itens na Tupla",
        "enunciado": "As tuplas possuem o método nativo `.index()`, que serve para descobrir em qual gaveta um determinado valor está escondido. Se `t = (5, 9, 2)`, qual será o resultado de `print(t.index(9))`?",
        "opcoes": ["9", "2", "1", "0"],
        "gabarito": "C", "xp_recompensa": 20
    },
    {
        "id_modulo": 10, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "O Comando Enumerate",
        "enunciado": "No Python, podemos usar a ferramenta `enumerate` no laço for para pegar a POSIÇÃO e o ITEM ao mesmo tempo: `for pos, item in enumerate(lanche):`\n\nSe `lanche = ('Pudim',)`, o que estará guardado dentro da variável `pos` logo na primeira (e única) volta?",
        "opcoes": ["Pudim", "0", "1", "lanche"],
        "gabarito": "B", "xp_recompensa": 20
    },

    # --- Prática Final ---
    {
        "id_modulo": 10, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Desafio Final: O Inventário Imutável",
        "enunciado": "Juntando tudo! \n1. Crie uma tupla chamada `numeros` contendo exatamente os valores inteiros 10, 20 e 30.\n2. Crie um laço `for` (sem usar a palavra range) para varrer a tupla `numeros` inteira.\n3. Dentro do laço, dê um `print()` para exibir cada um dos números. (Sairão os 3 números, um embaixo do outro).",
        "opcoes": None, "gabarito": "10\n20\n30\n", "xp_recompensa": 50
    },

    # ======================================================================
    # MÓDULO 11: Variáveis Compostas - Listas
    # ======================================================================

    # --- Bolinha 1: Texto Introdutório ---
    {
        "id_modulo": 11, "id_etapa": 1, "tipo": "TEORIA",
        "titulo": "A Evolução da Tupla",
        "enunciado": "As Tuplas (Módulo 10) são ótimas, mas têm um grande 'defeito': são imutáveis.\n\nPara resolver isso, usamos as **Listas**! Elas são totalmente mutáveis, permitindo alterar, adicionar e remover itens a qualquer momento.\n\nPara criar uma lista, em vez de parênteses, usamos COLCHETES `[ ]`.\n\nExemplo:\n`lanche = ['Hambúrguer', 'Suco']`\nAgora sim podemos fazer: `lanche[0] = 'Pudim'` (o Hambúrguer é apagado e substituído na hora!).",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 2: 2 Objetivas ---
    {
        "id_modulo": 11, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "O Símbolo da Lista",
        "enunciado": "Qual é a pontuação correta e obrigatória para se declarar uma Lista no Python?",
        "opcoes": ["Chaves { }", "Colchetes [ ]", "Parênteses ( )", "Barras / /"],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 11, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "Mudando o Passado",
        "enunciado": "Temos a lista: `notas = [5, 7, 4]`.\nO professor quer corrigir a primeira nota (o 5) para 8. Qual o comando exato para fazer essa substituição?",
        "opcoes": ["notas.append(8)", "notas[1] = 8", "notas[0] = 8", "notas.insert(0, 8)"],
        "gabarito": "C", "xp_recompensa": 10
    },

    # --- Bolinha 3: Texto de Aprofundamento ---
    {
        "id_modulo": 11, "id_etapa": 3, "tipo": "TEORIA",
        "titulo": "Aumentando a Fila",
        "enunciado": "Como adicionamos um item totalmente novo em uma lista que já existe?\n\n1. `.append('Picolé')`: É o mais usado! Ele adiciona o item sempre no FINAL da lista, como alguém entrando no fim da fila.\n2. `.insert(0, 'Bolo')`: Adiciona o item na posição específica que você escolher (nesse caso, na gaveta 0). Os outros itens não são apagados, eles apenas 'arredam' para a direita para dar espaço.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 4: 1 Escrever ---
    {
        "id_modulo": 11, "id_etapa": 4, "tipo": "PRATICA",
        "titulo": "A Lista de Compras",
        "enunciado": "Crie uma lista vazia chamada `compras` usando colchetes vazios `[]`. Na linha de baixo, use o método `.append()` para adicionar o texto 'Arroz' a ela. Depois, faça um `print()` da lista inteira.",
        "opcoes": None, "gabarito": "['Arroz']\n", "xp_recompensa": 20
    },

    # --- Bolinha 5: Texto de Aprofundamento ---
    {
        "id_modulo": 11, "id_etapa": 5, "tipo": "TEORIA",
        "titulo": "Apagando Itens",
        "enunciado": "Para remover itens de uma lista, temos três armas principais:\n\n1. `del lanche[3]`: Apaga apontando para o NÚMERO da gaveta.\n2. `lanche.pop(3)`: Também apaga pelo número da gaveta, mas se você deixar os parênteses vazios `pop()`, ele apaga automaticamente o ÚLTIMO item.\n3. `lanche.remove('Pizza')`: Apaga pelo NOME do item. (Atenção: Se houver duas Pizzas, ele apaga só a primeira que encontrar).",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 6: 2 Objetivas ---
    {
        "id_modulo": 11, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "O Estouro da Bolha",
        "enunciado": "Se a lista for `fila = ['Ana', 'Bia', 'Carlos']` e executarmos o comando `fila.pop()`, o que restará na lista?",
        "opcoes": ["['Ana', 'Bia']", "['Bia', 'Carlos']", "A lista ficará vazia", "Erro, o pop exige um número"],
        "gabarito": "A", "xp_recompensa": 10
    },
    {
        "id_modulo": 11, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "Remoção por Nome",
        "enunciado": "Qual dos comandos abaixo procura a palavra específica 'Espada' dentro da lista 'mochila' e a destrói?",
        "opcoes": ["mochila.delete('Espada')", "del mochila['Espada']", "mochila.remove('Espada')", "mochila.pop('Espada')"],
        "gabarito": "C", "xp_recompensa": 10
    },

    # --- Bolinha 7: Texto Finalizador ---
    {
        "id_modulo": 11, "id_etapa": 7, "tipo": "TEORIA",
        "titulo": "Organizando a Bagunça",
        "enunciado": "O Python tem um método incrível chamado `.sort()` para ordenar listas bagunçadas automaticamente!\n\nSe você tiver `valores = [8, 2, 5]` e usar `valores.sort()`, a lista se transformará em `[2, 5, 8]` (crescente).\n\nSe quiser na ordem inversa (do maior para o menor), basta usar `valores.sort(reverse=True)`.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 8: 2 Objetivas + 1 Escrever ---
    {
        "id_modulo": 11, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "Ordem Alfabética",
        "enunciado": "O método `.sort()` funciona apenas com números?",
        "opcoes": [
            "Sim, se usar com textos o Python dá erro.",
            "Não, ele também funciona com textos, organizando a lista em perfeita ordem alfabética.",
            "Funciona, mas ele apaga as letras maiúsculas.",
            "Ele funciona, mas embaralha as letras."
        ],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 11, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "O Reverso",
        "enunciado": "Qual é o comando exato que colocamos DENTRO dos parênteses do `.sort()` para avisar ao Python que queremos a ordem decrescente (do maior pro menor)?",
        "opcoes": ["reverse=True", "reverse=False", "invert=True", "decrescente"],
        "gabarito": "A", "xp_recompensa": 10
    },
    {
        "id_modulo": 11, "id_etapa": 8, "tipo": "PRATICA",
        "titulo": "Arrumando os Números",
        "enunciado": "Crie a lista `num = [3, 1, 2]`. Na linha de baixo, use o método `.sort()` nela. Na terceira linha, use o `print()` para exibir a lista e comprovar que o Python arrumou tudo para você.",
        "opcoes": None, "gabarito": "[1, 2, 3]\n", "xp_recompensa": 25
    },

    # ======================================================================
    # ETAPA 9: TESTE FINAL DO MÓDULO 11 (O Troféu)
    # 7 Exercícios (2 Obj, 1 Prática, 3 Obj, 1 Prática)
    # ======================================================================

    # --- 2 Objetivas Iniciais (Intermediárias) ---
    {
        "id_modulo": 11, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: A Grande Diferença",
        "enunciado": "Em uma frase, o que diferencia Listas de Tuplas?",
        "opcoes": [
            "Listas usam parênteses, Tuplas usam chaves.",
            "Listas aceitam números, Tuplas só aceitam textos.",
            "Tuplas são imutáveis (não mudam), enquanto Listas são totalmente mutáveis.",
            "Listas são muito mais rápidas na memória do computador que as Tuplas."
        ],
        "gabarito": "C", "xp_recompensa": 15
    },
    {
        "id_modulo": 11, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: Inserção Direta",
        "enunciado": "Qual a diferença entre `.append('A')` e `.insert(0, 'A')`?",
        "opcoes": [
            "Nenhuma, ambos fazem a mesma coisa.",
            "O append adiciona no final. O insert adiciona na posição escolhida (neste caso, na posição zero, empurrando o resto para a direita).",
            "O insert apaga o item que estava na posição zero para colocar o 'A' no lugar.",
            "O append só funciona com números."
        ],
        "gabarito": "B", "xp_recompensa": 15
    },

    # --- 1 Prática Intermediária ---
    {
        "id_modulo": 11, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Prática: Modificando Índices",
        "enunciado": "Crie a lista `cores = ['Azul', 'Verde']`. O designer mudou de ideia. Na linha de baixo, troque diretamente o 'Verde' (que está na gaveta 1) pela palavra 'Rosa' usando o sinal de igual (`=`). Depois, imprima a lista `cores`.",
        "opcoes": None, "gabarito": "['Azul', 'Rosa']\n", "xp_recompensa": 30
    },

    # --- 3 Objetivas de Raciocínio (Difíceis) ---
    {
        "id_modulo": 11, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Caça ao Bug: Erro de Remoção",
        "enunciado": "Um aluno tentou apagar um item, mas o Python travou dando um 'ValueError'. O que causou isso no código abaixo?\n\nlista = [10, 20, 30]\nlista.remove(40)",
        "opcoes": [
            "O método remove só funciona com textos.",
            "O método remove procura o item pelo VALOR exato. Como 40 não está na lista, o Python se perde e quebra o programa.",
            "Ele deveria ter usado aspas no 40.",
            "Faltou colocar em qual posição ele queria remover."
        ],
        "gabarito": "B", "xp_recompensa": 20
    },
    {
        "id_modulo": 11, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "A Ligação Perigosa (Avançado)",
        "enunciado": "Pegadinha clássica do Python! Se você tem `A = [1, 2]` e cria `B = A`, e na linha de baixo faz `B.append(3)`. Como ficará a lista A?",
        "opcoes": [
            "Ficará [1, 2]. O que acontece com B não afeta A.",
            "Ficará [1, 2, 3]. Quando você iguala listas com o sinal de =, o Python cria uma LIGAÇÃO (referência) entre elas. Alterar B altera A simultaneamente.",
            "Dará erro, pois B não é uma lista original.",
            "A lista A ficará vazia."
        ],
        "gabarito": "B", "xp_recompensa": 20
    },
    {
        "id_modulo": 11, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "A Cópia Verdadeira",
        "enunciado": "Sabendo do perigo da pergunta anterior, como fazemos o Python criar uma cópia INDEPENDENTE dos valores de `A` para dentro de `B` (sem criar ligações)?",
        "opcoes": [
            "B = A.copy()  (ou B = A[:])",
            "B = copy(A)",
            "B == A",
            "B = [A]"
        ],
        "gabarito": "A", "xp_recompensa": 20
    },

    # --- Prática Final ---
    {
        "id_modulo": 11, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Desafio Final: O Inventário RPG",
        "enunciado": "Sua mochila começou vazia. \n1. Crie a lista `mochila = []`.\n2. Use o `.append()` para adicionar 'Espada'.\n3. Use o `.append()` para adicionar 'Escudo'.\n4. O monstro quebrou sua espada! Use o `.remove('Espada')` para tirá-la da lista.\n5. Imprima a mochila para ver o que sobrou.",
        "opcoes": None, "gabarito": "['Escudo']\n", "xp_recompensa": 50
    },

    # ======================================================================
    # MÓDULO 12: Variáveis Compostas - Listas Parte 2
    # ======================================================================

    # --- Bolinha 1: Texto Introdutório ---
    {
        "id_modulo": 12, "id_etapa": 1, "tipo": "TEORIA",
        "titulo": "Listas dentro de Listas",
        "enunciado": "Sabemos que Listas podem guardar vários dados. Mas você sabia que uma lista pode guardar OUTRAS listas dentro dela?\n\nImagine que você tem a lista `dados = ['Ana', 25]`.\nAgora, você tem a lista da `galera = []`.\nPodemos colocar a Ana lá dentro: `galera.append(dados)`.\n\nAgora, a lista `galera` virou um 'fichário', onde cada gaveta contém uma sub-lista completa com o nome e a idade da pessoa!",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 2: 2 Objetivas ---
    {
        "id_modulo": 12, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "A Matriz",
        "enunciado": "Se criarmos uma lista contendo outras listas direto no código (sem usar o append), qual é a forma correta de escrevê-la?",
        "opcoes": [
            "galera = ['Ana', 25, 'João', 19]",
            "galera = [['Ana', 25], ['João', 19]]",
            "galera = (['Ana', 25], ['João', 19])",
            "galera = ['Ana'][25]"
        ],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 12, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "Entendendo o Fichário",
        "enunciado": "No exemplo `galera = [['Ana', 25], ['João', 19]]`, o que está guardado na gaveta principal zero (ou seja, `galera[0]`)?",
        "opcoes": [
            "Apenas o nome 'Ana'.",
            "Apenas o número 25.",
            "A lista inteira da Ana: ['Ana', 25].",
            "A letra 'A'."
        ],
        "gabarito": "C", "xp_recompensa": 10
    },

    # --- Bolinha 3: Texto de Aprofundamento ---
    {
        "id_modulo": 12, "id_etapa": 3, "tipo": "TEORIA",
        "titulo": "Gaveta dentro de Gaveta",
        "enunciado": "Se temos: `galera = [['Ana', 25], ['João', 19]]`.\n\nComo fazemos se quisermos pegar SÓ a idade do João (o número 19)?\nUsamos dois colchetes juntos!\n\nPrimeiro colocamos a gaveta principal (o João está na gaveta 1 da galera). Depois, colocamos a gaveta de dentro (a idade é o item 1 da sub-lista).\nO código fica: `print(galera[1][1])`.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 4: 1 Escrever ---
    {
        "id_modulo": 12, "id_etapa": 4, "tipo": "PRATICA",
        "titulo": "Acessando Matrizes",
        "enunciado": "Crie a variável `pessoas = [['Victor', 20], ['Gustavo', 45]]`. Na linha de baixo, use o `print()` e os colchetes duplos para exibir apenas o nome 'Gustavo'.",
        "opcoes": None, "gabarito": "Gustavo\n", "xp_recompensa": 20
    },

    # --- Bolinha 5: Texto de Aprofundamento ---
    {
        "id_modulo": 12, "id_etapa": 5, "tipo": "TEORIA",
        "titulo": "A Armadilha da Ligação",
        "enunciado": "Lembre-se do Módulo 11: o Python cria 'ligações' entre listas!\n\nSe você fizer `galera.append(dados)` e depois limpar a lista principal com `dados.clear()`, a lista 'galera' também perde tudo, ficando vazia.\n\nPara colocar uma sub-lista dentro da lista principal de forma segura, você DEVE adicionar uma CÓPIA usando o fatiamento total `[:]`.\nO jeito certo é: `galera.append(dados[:])`.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 6: 2 Objetivas ---
    {
        "id_modulo": 12, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "O Símbolo da Cópia",
        "enunciado": "Qual estrutura usamos dentro dos colchetes do append para garantir que estamos enviando uma cópia independente, e não criando uma ligação perigosa?",
        "opcoes": ["[:]", "[copy]", "[0]", "[-]"],
        "gabarito": "A", "xp_recompensa": 10
    },
    {
        "id_modulo": 12, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "As Consequências",
        "enunciado": "O que acontece se esquecermos do `[:]` ao dar um append de uma lista temporária para dentro da lista principal, e depois apagarmos a temporária?",
        "opcoes": [
            "A lista principal mantém os dados normais.",
            "Os dados dentro da lista principal também são apagados.",
            "O Python trava imediatamente com erro.",
            "A lista temporária não consegue ser apagada."
        ],
        "gabarito": "B", "xp_recompensa": 10
    },

    # --- Bolinha 7: Texto Finalizador ---
    {
        "id_modulo": 12, "id_etapa": 7, "tipo": "TEORIA",
        "titulo": "O Laço Desempacotador",
        "enunciado": "Podemos varrer listas compostas com o `for` de um jeito incrivelmente fácil!\n\n`galera = [['Ana', 25], ['João', 19]]`\n\n`for pessoa in galera:`\n    `print(f'{pessoa[0]} tem {pessoa[1]} anos')`\n\nA variável `pessoa` vai receber uma sub-lista inteira a cada volta (primeiro ['Ana', 25], depois ['João', 19]). Assim, podemos usar `pessoa[0]` para o nome e `pessoa[1]` para a idade.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 8: 2 Objetivas + 1 Escrever ---
    {
        "id_modulo": 12, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "A Variável do For",
        "enunciado": "No código `for p in galera:`, se `galera` é uma lista com 10 sub-listas dentro, o que a variável `p` representa a cada volta do laço?",
        "opcoes": [
            "O número da gaveta (0 a 9).",
            "A primeira letra de cada nome.",
            "Uma sub-lista completa por vez.",
            "A lista galera inteira todas as vezes."
        ],
        "gabarito": "C", "xp_recompensa": 10
    },
    {
        "id_modulo": 12, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "Filtrando os Dados",
        "enunciado": "Usando o mesmo laço `for pessoa in galera:`, qual comando você colocaria dentro do laço se quisesse imprimir APENAS os nomes (que estão no primeiro espaço da sub-lista)?",
        "opcoes": ["print(pessoa[0])", "print(galera[0])", "print(pessoa[1])", "print(pessoa)"],
        "gabarito": "A", "xp_recompensa": 10
    },
    {
        "id_modulo": 12, "id_etapa": 8, "tipo": "PRATICA",
        "titulo": "Listando as Idades",
        "enunciado": "Crie a variável `turma = [['Rui', 10], ['Lia', 11]]`.\nNa linha de baixo, crie um laço `for aluno in turma:`.\nDentro do laço, faça um print para exibir apenas a IDADE (índice 1) de cada aluno.",
        "opcoes": None, "gabarito": "10\n11\n", "xp_recompensa": 25
    },

    # ======================================================================
    # ETAPA 9: TESTE FINAL DO MÓDULO 12 (O Troféu)
    # 7 Exercícios (2 Obj, 1 Prática, 3 Obj, 1 Prática)
    # ======================================================================

    # --- 2 Objetivas Iniciais (Intermediárias) ---
    {
        "id_modulo": 12, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: A Estrutura",
        "enunciado": "O que realmente é uma 'Lista Composta' (ou Lista Aninhada) no Python?",
        "opcoes": [
            "Uma lista que contém números quebrados (floats).",
            "Uma lista que mistura textos e números soltos.",
            "Uma lista cujos itens principais são outras listas.",
            "Uma lista que não pode ser apagada."
        ],
        "gabarito": "C", "xp_recompensa": 15
    },
    {
        "id_modulo": 12, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: Os Dois Colchetes",
        "enunciado": "Na expressão `lista[2][0]`, o que o Python faz exatamente?",
        "opcoes": [
            "Pega a gaveta 2 e multiplica pela gaveta 0.",
            "Vai na gaveta principal de índice 2 e, dentro da sub-lista que está lá, pega o item de índice 0.",
            "Ele tenta pegar as gavetas 2 e 0 da lista principal ao mesmo tempo.",
            "Ele apaga esses itens."
        ],
        "gabarito": "B", "xp_recompensa": 15
    },

    # --- 1 Prática Intermediária ---
    {
        "id_modulo": 12, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Prática: Declaração Direta",
        "enunciado": "Mostre que sabe criar! Crie a variável `matriz` recebendo uma lista que contém outras duas listas. A primeira sub-lista terá os números 1 e 2. A segunda sub-lista terá os números 3 e 4. Na linha de baixo, imprima a variável inteira.",
        "opcoes": None, "gabarito": "[[1, 2], [3, 4]]\n", "xp_recompensa": 30
    },

    # --- 3 Objetivas de Raciocínio (Difíceis) ---
    {
        "id_modulo": 12, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Contando as Gavetas Principais",
        "enunciado": "A função `len()` conta o tamanho. Se temos `galera = [['Ana', 25], ['João', 19], ['Maria', 30]]`, qual o resultado de `print(len(galera))`?",
        "opcoes": ["6", "3", "2", "Erro"],
        "gabarito": "B", "xp_recompensa": 20
    },
    {
        "id_modulo": 12, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Caça ao Bug: Cópia Esquecida",
        "enunciado": "Olhe este código perigoso:\ndado = ['Pedro', 20]\ngrupo = []\ngrupo.append(dado)\ndado[0] = 'Bia'\ndado[1] = 18\ngrupo.append(dado)\n\nQual será o resultado de print(grupo)? (Lembre-se da ligação de listas!)",
        "opcoes": [
            "[['Pedro', 20], ['Bia', 18]]",
            "[['Bia', 18], ['Bia', 18]]",
            "[['Pedro', 20], ['Pedro', 20]]",
            "Dá erro"
        ],
        "gabarito": "B", "xp_recompensa": 20
    },
    {
        "id_modulo": 12, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "O Retorno da Formatação",
        "enunciado": "Usando as F-Strings que aprendemos:\n\nfor p in [['A', 10], ['B', 20]]:\n    print(f'{p[0]} vale {p[1]}')\n\nO que sai exatamente na primeira linha da tela?",
        "opcoes": ["A vale 10", "A vale B", "10 vale 20", "['A', 10]"],
        "gabarito": "A", "xp_recompensa": 20
    },

    # --- Prática Final ---
    {
        "id_modulo": 12, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Desafio Final: O Arquivo Secreto",
        "enunciado": "Crie uma lista chamada `turma` que contém duas outras listas: `['Victor', 'Aprovado']` e `['Vilão', 'Reprovado']`.\nNa linha de baixo, use o `print()` com os dois colchetes numéricos necessários para extrair e exibir apenas a palavra 'Reprovado' de dentro da matriz.",
        "opcoes": None, "gabarito": "Reprovado\n", "xp_recompensa": 50
    },

    # ======================================================================
    # MÓDULO 13: Variáveis Compostas - Dicionários
    # ======================================================================

    # --- Bolinha 1: Texto Introdutório ---
    {
        "id_modulo": 13, "id_etapa": 1, "tipo": "TEORIA",
        "titulo": "Dando Nomes às Gavetas",
        "enunciado": "Nas Listas e Tuplas, o Python numera as gavetas automaticamente (0, 1, 2...).\n\nNos **Dicionários**, VOCÊ escolhe o nome da gaveta! Eles são criados usando CHAVES `{ }`.\nCada item tem uma Chave (o nome da gaveta) e um Valor (o que está lá dentro).\n\nExemplo:\n`dados = {'nome': 'Pedro', 'idade': 25}`\n\nAgora, em vez de usar `dados[0]`, você usa `dados['nome']` para pegar o 'Pedro'. Muito mais legível!",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 2: 2 Objetivas ---
    {
        "id_modulo": 13, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "As Chaves do Reino",
        "enunciado": "Relembrando os símbolos das variáveis compostas: Tuplas usam ( ), Listas usam [ ]. Qual é o símbolo obrigatório que usamos para criar um Dicionário?",
        "opcoes": ["Chaves { }", "Colchetes [ ]", "Parênteses ( )", "Sinal de Maior/Menor < >"],
        "gabarito": "A", "xp_recompensa": 10
    },
    {
        "id_modulo": 13, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "Buscando o Tesouro",
        "enunciado": "Temos o seguinte dicionário: `filme = {'titulo': 'Star Wars', 'ano': 1977}`. \nQual comando usamos para imprimir apenas o número 1977 na tela?",
        "opcoes": ["print(filme[1])", "print(filme['ano'])", "print(filme.ano)", "print(filme[1977])"],
        "gabarito": "B", "xp_recompensa": 10
    },

    # --- Bolinha 3: Texto de Aprofundamento ---
    {
        "id_modulo": 13, "id_etapa": 3, "tipo": "TEORIA",
        "titulo": "Mutação sem Append",
        "enunciado": "Dicionários NÃO usam o `.append()` das listas! Se você quiser adicionar uma gaveta nova, basta dar um nome e um valor para ela que o Python cria na hora.\n\n`dados['sexo'] = 'M'` (Pronto, a chave 'sexo' foi criada e adicionada).\n\nPara remover uma gaveta inteira, usamos o clássico comando `del`.\n`del dados['idade']` (Apaga completamente a gaveta 'idade' e o seu valor).",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 4: 1 Escrever ---
    {
        "id_modulo": 13, "id_etapa": 4, "tipo": "PRATICA",
        "titulo": "Criando um Perfil",
        "enunciado": "Crie um dicionário chamado `aluno` que tenha duas chaves: `'nome'` com o valor `'Ana'` e `'nota'` com o valor `9`. Em seguida, use o `print()` para exibir apenas a nota da Ana, chamando a chave do dicionário.",
        "opcoes": None, "gabarito": "9\n", "xp_recompensa": 20
    },

    # --- Bolinha 5: Texto de Aprofundamento ---
    {
        "id_modulo": 13, "id_etapa": 5, "tipo": "TEORIA",
        "titulo": "As 3 Partes do Dicionário",
        "enunciado": "Os dicionários têm três métodos nativos extremamente úteis para separar as coisas:\n\n- `.values()`: Retorna SÓ os valores guardados (ex: 'Pedro', 25).\n- `.keys()`: Retorna SÓ os nomes das gavetas (ex: 'nome', 'idade').\n- `.items()`: Retorna TUDO agrupado (as chaves e os valores juntos).",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 6: 2 Objetivas ---
    {
        "id_modulo": 13, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "Pegando os Nomes",
        "enunciado": "Se rodarmos `print(dados.keys())` no dicionário `dados = {'nome': 'Victor', 'xp': 100}`, o que o Python retornará?",
        "opcoes": [
            "Apenas 'Victor' e 100.",
            "Apenas as palavras 'nome' e 'xp'.",
            "O dicionário completo.",
            "Dá erro de sintaxe."
        ],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 13, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "O Comando Completo",
        "enunciado": "Se o seu objetivo é pegar absolutamente todo o conteúdo do dicionário (tanto as gavetas quanto os dados), qual método você usa?",
        "opcoes": [".all()", ".keys()", ".values()", ".items()"],
        "gabarito": "D", "xp_recompensa": 10
    },

    # --- Bolinha 7: Texto Finalizador ---
    {
        "id_modulo": 13, "id_etapa": 7, "tipo": "TEORIA",
        "titulo": "Dicionários e o For",
        "enunciado": "Lembra que o `.items()` pega as chaves e os valores? Podemos usar isso no laço `for` de um jeito maravilhoso, usando DUAS variáveis ao mesmo tempo!\n\n`for k, v in dados.items():`\n    `print(f'O {k} é {v}')`\n\nNeste laço, a variável `k` (Key) guarda a Chave, e a variável `v` (Value) guarda o Valor a cada volta que o laço dá!",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 8: 2 Objetivas + 1 Escrever ---
    {
        "id_modulo": 13, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "A Ordem das Variáveis",
        "enunciado": "Na estrutura `for chave, valor in filme.items():`, o que acontece se o programador esquecer o `.items()` e tentar usar apenas `for chave, valor in filme:`?",
        "opcoes": [
            "O código funciona perfeitamente.",
            "O Python só exibe os valores numéricos.",
            "O Python trava com um erro (ValueError), porque sem o .items() ele não consegue dividir as chaves dos valores para as duas variáveis.",
            "Ele apaga o dicionário."
        ],
        "gabarito": "C", "xp_recompensa": 10
    },
    {
        "id_modulo": 13, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "O Laço Duplo",
        "enunciado": "Se rodarmos o código abaixo, quantas vezes o `print` será executado?\n\ncarro = {'marca': 'Fiat', 'cor': 'Vermelho', 'ano': 2022}\nfor k, v in carro.items():\n    print(k, v)",
        "opcoes": ["1 vez", "2 vezes", "3 vezes", "6 vezes"],
        "gabarito": "C", "xp_recompensa": 10
    },
    {
        "id_modulo": 13, "id_etapa": 8, "tipo": "PRATICA",
        "titulo": "Repetindo Valores",
        "enunciado": "Crie o dicionário `pc = {'CPU': 'AMD', 'RAM': '16GB'}`. Crie um laço `for` focado APENAS nos valores (use o método `.values()`). Dentro do laço, dê um print na variável que você criou para o for, de forma a exibir 'AMD' e '16GB' (um em cada linha).",
        "opcoes": None, "gabarito": "AMD\n16GB\n", "xp_recompensa": 25
    },

    # ======================================================================
    # ETAPA 9: TESTE FINAL DO MÓDULO 13 (O Troféu)
    # 7 Exercícios (2 Obj, 1 Prática, 3 Obj, 1 Prática)
    # ======================================================================

    # --- 2 Objetivas Iniciais (Intermediárias) ---
    {
        "id_modulo": 13, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: A Grande Diferença",
        "enunciado": "Qual a principal vantagem tática de usar um Dicionário no lugar de uma Lista?",
        "opcoes": [
            "Os dicionários ocupam muito menos espaço no HD.",
            "Os índices das Listas são apenas numéricos (0, 1, 2), enquanto nos Dicionários podemos criar índices personalizados com nomes literais (chaves).",
            "Dicionários não aceitam textos, tornando a matemática mais segura.",
            "As Listas precisam do comando print, os Dicionários não."
        ],
        "gabarito": "B", "xp_recompensa": 15
    },
    {
        "id_modulo": 13, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: Os Dois Elementos",
        "enunciado": "No dicionário `personagem = {'raca': 'Elfo', 'hp': 100}`, o texto 'raca' e o texto 'Elfo' são chamados, respectivamente, de:",
        "opcoes": [
            "Valor e Chave",
            "Índice e Variável",
            "Chave e Valor",
            "Item e Tupla"
        ],
        "gabarito": "C", "xp_recompensa": 15
    },

    # --- 1 Prática Intermediária ---
    {
        "id_modulo": 13, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Prática: Modificando Dados Existentes",
        "enunciado": "Você tem o dicionário: `jogador = {'nome': 'Victor', 'xp': 100}`. Na linha de baixo, troque o valor da chave `'xp'` para 500 (usando a atribuição direta `=` com os colchetes da chave). Na terceira linha, faça um `print()` exibindo apenas a chave `'xp'` para ver se atualizou.",
        "opcoes": None, "gabarito": "500\n", "xp_recompensa": 30
    },

    # --- 3 Objetivas de Raciocínio (Difíceis) ---
    {
        "id_modulo": 13, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "O Comando Inexistente",
        "enunciado": "Por que o código `jogador.append('Guerreiro')` daria erro se 'jogador' for um dicionário?",
        "opcoes": [
            "Porque faltaram as aspas duplas.",
            "Porque dicionários não possuem o método '.append()'. Para adicionar itens, basta criar a chave direta: jogador['classe'] = 'Guerreiro'.",
            "Porque 'Guerreiro' é um texto, e dicionários só aceitam números.",
            "Porque dicionários são imutáveis como as tuplas."
        ],
        "gabarito": "B", "xp_recompensa": 20
    },
    {
        "id_modulo": 13, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Deletando Gavetas",
        "enunciado": "Qual é o comando correto que apaga permanentemente a chave 'cor' (e o seu respectivo valor) de dentro do dicionário 'camisa'?",
        "opcoes": ["camisa.remove('cor')", "del camisa['cor']", "camisa.pop()", "camisa.delete('cor')"],
        "gabarito": "B", "xp_recompensa": 20
    },
    {
        "id_modulo": 13, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Caça ao Bug: Dicionário em Lista",
        "enunciado": "Podemos colocar Dicionários dentro de Listas! Exemplo: `brasil = [{'estado': 'RJ'}, {'estado': 'SP'}]`.\nQual comando abaixo usamos para imprimir a sigla 'SP'?",
        "opcoes": [
            "print(brasil[1]['estado'])",
            "print(brasil['estado'][1])",
            "print(brasil['SP'])",
            "print(brasil[2]['estado'])"
        ],
        "gabarito": "A", "xp_recompensa": 20
    },

    # --- Prática Final ---
    {
        "id_modulo": 13, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Desafio Final: O Pokedex",
        "enunciado": "Crie um dicionário chamado `pokemon` contendo duas chaves: `'nome'` recebendo `'Pikachu'`, e `'tipo'` recebendo `'Elétrico'`.\nNa linha seguinte, use um único `print()` misturado com uma **F-String** (Módulo 9) para exibir a frase exata: 'O Pikachu é do tipo Elétrico'.",
        "opcoes": None, "gabarito": "O Pikachu é do tipo Elétrico\n", "xp_recompensa": 50
    },

    # ======================================================================
    # MÓDULO 14: Funções Parte 1
    # ======================================================================

    # --- Bolinha 1: Texto Introdutório ---
    {
        "id_modulo": 14, "id_etapa": 1, "tipo": "TEORIA",
        "titulo": "A Arte de Não Repetir",
        "enunciado": "Sabe quando você precisa fazer a mesma coisa várias vezes no código? Em vez de copiar e colar, nós criamos uma 'Rotina' usando **Funções**.\n\nPara criar (definir) uma função no Python, usamos a palavra `def`.\n\nExemplo:\n`def mostra_linha():`\n    `print('-' * 20)`\n\nAgora, toda vez que você digitar `mostra_linha()` solto no seu código, o Python vai desenhar aquela linha de tracinhos sozinho!",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 2: 2 Objetivas ---
    {
        "id_modulo": 14, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "A Palavra Mágica",
        "enunciado": "Qual é a palavra-chave OBRIGATÓRIA que usamos para ensinar um comando novo para o Python, criando uma Função?",
        "opcoes": ["function", "create", "def", "fun"],
        "gabarito": "C", "xp_recompensa": 10
    },
    {
        "id_modulo": 14, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "A Filosofia das Funções",
        "enunciado": "Qual é o principal objetivo de se criar funções personalizadas em um programa grande?",
        "opcoes": [
            "Fazer o programa rodar sem usar a memória RAM.",
            "Automatizar Rotinas: evitar a repetição de código, tornando o programa menor, mais limpo e fácil de consertar.",
            "Permitir que o Python desenhe gráficos 3D.",
            "Ocultar o código do usuário final."
        ],
        "gabarito": "B", "xp_recompensa": 10
    },

    # --- Bolinha 3: Texto de Aprofundamento ---
    {
        "id_modulo": 14, "id_etapa": 3, "tipo": "TEORIA",
        "titulo": "Os Entregadores (Parâmetros)",
        "enunciado": "Uma função fica muito mais poderosa quando passamos informações para ela trabalharem. Chamamos isso de 'Parâmetros'.\n\nVeja:\n`def mensagem(texto):`\n    `print(texto)`\n\nQuando você chama a função no programa principal fazendo `mensagem('Sistema')`, a palavra 'Sistema' entra na variável 'texto', e a função a imprime na tela!",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 4: 1 Escrever ---
    {
        "id_modulo": 14, "id_etapa": 4, "tipo": "PRATICA",
        "titulo": "A Sua Primeira Função",
        "enunciado": "Vamos lá! \n1. Defina uma função chamada `dobro` que recebe um parâmetro chamado `n`.\n2. DENTRO da função (com a indentação), faça um `print(n * 2)`.\n3. FORA da função (sem espaço na esquerda), chame a função passando o número 5.",
        "opcoes": None, "gabarito": "10\n", "xp_recompensa": 20
    },

    # --- Bolinha 5: Texto de Aprofundamento ---
    {
        "id_modulo": 14, "id_etapa": 5, "tipo": "TEORIA",
        "titulo": "Mais de um Parâmetro",
        "enunciado": "Você pode pedir quantos parâmetros quiser, basta separá-á-los por vírgula!\n\n`def soma(a, b):`\n    `print(a + b)`\n\nSe você chamar `soma(4, 5)`, o Python entrega o 4 para o 'a' e o 5 para o 'b', e a função imprime 9.\nAtenção: a ordem que você envia os dados importa muito!",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 6: 2 Objetivas ---
    {
        "id_modulo": 14, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "Falta de Argumentos",
        "enunciado": "Temos a função `def soma(a, b):`. O que acontece se o programador chamar a função passando apenas um número, escrevendo `soma(5)`?",
        "opcoes": [
            "O Python assume que o 'b' vale zero e o resultado é 5.",
            "Dá um erro (TypeError), porque a função exige exatamente 2 parâmetros e você só enviou 1.",
            "O Python repete o número e o resultado é 10.",
            "O código roda normalmente e pergunta o segundo número."
        ],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 14, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "A Chamada Correta",
        "enunciado": "Você criou a função `def saudar(nome):`. Qual é a forma correta de 'chamar' essa função no código principal para que ela cumprimente a Ana?",
        "opcoes": [
            "saudar = 'Ana'",
            "def saudar('Ana')",
            "print(saudar) Ana",
            "saudar('Ana')"
        ],
        "gabarito": "D", "xp_recompensa": 10
    },

    # --- Bolinha 7: Texto Finalizador ---
    {
        "id_modulo": 14, "id_etapa": 7, "tipo": "TEORIA",
        "titulo": "O Empacotador Asterisco",
        "enunciado": "E se você quiser fazer uma função que recebe vários números, mas não sabe se o usuário vai passar 2, 5 ou 10 números de uma vez?\nUsamos o Empacotamento com o asterisco `*`!\n\n`def contador(*num):`\n    `print(num)`\n\nSe você chamar `contador(5, 7, 3)`, o Python pega todos esses números soltos e 'empacota' eles dentro de uma Tupla na variável 'num'!",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 8: 2 Objetivas + 1 Escrever ---
    {
        "id_modulo": 14, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "A Natureza do Pacote",
        "enunciado": "Quando usamos o empacotamento de parâmetros (exemplo: `def teste(*valores):`), qual é o formato/tipo de variável que o Python usa para guardar todos esses valores lá dentro?",
        "opcoes": ["Uma String", "Um Dicionário", "Uma Tupla", "Uma Lista"],
        "gabarito": "C", "xp_recompensa": 10
    },
    {
        "id_modulo": 14, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "O Comando Imprevisível",
        "enunciado": "Com a função `def valores(*v):`, o programador chamou primeiro `valores(1, 2)` e depois chamou `valores(9, 8, 7, 6)`. Isso vai dar erro?",
        "opcoes": [
            "Sim, a função precisa saber exatamente quantos números vai receber.",
            "Não! O asterisco permite enviar quantos argumentos você quiser. Ele cria uma tupla com 2 itens na primeira chamada, e outra com 4 itens na segunda.",
            "Vai dar erro apenas na segunda chamada, pois o limite é 3.",
            "O Python só aceita o primeiro envio."
        ],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 14, "id_etapa": 8, "tipo": "PRATICA",
        "titulo": "Praticando Parâmetros",
        "enunciado": "Crie a função `multiplicar` que pede dois parâmetros: `a` e `b`. Dentro dela, dê um `print(a * b)`. Fora da função, chame-a passando os números 4 e 5.",
        "opcoes": None, "gabarito": "20\n", "xp_recompensa": 25
    },

    # ======================================================================
    # ETAPA 9: TESTE FINAL DO MÓDULO 14 (O Troféu)
    # 7 Exercícios (2 Obj, 1 Prática, 3 Obj, 1 Prática)
    # ======================================================================

    # --- 2 Objetivas Iniciais (Intermediárias) ---
    {
        "id_modulo": 14, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: Os Dois Pontos",
        "enunciado": "Assim como o `if`, o `for` e o `while`, o comando `def` precisa de algo obrigatório no final da sua linha. O que é?",
        "opcoes": ["Ponto e vírgula (;)", "A palavra 'start'", "Os dois-pontos (:)", "Aspas simples"],
        "gabarito": "C", "xp_recompensa": 15
    },
    {
        "id_modulo": 14, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Caça ao Bug: Ordem dos Fatores",
        "enunciado": "O código abaixo vai dar erro de 'Nome não definido'. Por quê?\n\nsaudar('Victor')\ndef saudar(nome):\n    print(f'Olá, {nome}')",
        "opcoes": [
            "O nome da função não pode ser um verbo.",
            "O Python lê de cima para baixo. Você tentou CHAMAR a função na linha 1 antes dela ser CRIADA (o def só acontece na linha 2).",
            "A variável 'nome' deveria estar entre aspas.",
            "Faltou a indentação na linha 1."
        ],
        "gabarito": "B", "xp_recompensa": 15
    },

    # --- 1 Prática Intermediária ---
    {
        "id_modulo": 14, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Prática: Mensagem Formatada",
        "enunciado": "Defina uma função `exibe(nome, idade)`. Dentro dela, use um print com F-String para mostrar '{nome} tem {idade} anos'. Fora da função, chame-a passando 'Victor' e 20.",
        "opcoes": None, "gabarito": "Victor tem 20 anos\n", "xp_recompensa": 30
    },

    # --- 3 Objetivas de Raciocínio (Difíceis) ---
    {
        "id_modulo": 14, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Modificando Listas (Avançado)",
        "enunciado": "Se você passar uma LISTA inteira como parâmetro para uma função, e a função alterar os itens dessa lista lá dentro, o que acontece com a lista original fora da função?",
        "opcoes": [
            "Nada, pois a função cria uma cópia isolada da lista.",
            "A lista original TAMBÉM é alterada permanentemente! Listas são passadas por referência (ligação) para as funções.",
            "Dá um erro, pois funções não aceitam listas.",
            "A lista vira uma Tupla para se proteger."
        ],
        "gabarito": "B", "xp_recompensa": 20
    },
    {
        "id_modulo": 14, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Compreendendo o Empacotamento",
        "enunciado": "No código:\ndef valores(*nums):\n    print(len(nums))\n\nSe chamarmos `valores(10, 20, 30)`, qual será o resultado exato do print?",
        "opcoes": ["10", "60", "3", "0"],
        "gabarito": "C", "xp_recompensa": 20
    },
    {
        "id_modulo": 14, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Parâmetros Nomeados",
        "enunciado": "Você tem `def conta(a, b):`. O que o Python fará se você chamar a função escrevendo os nomes das variáveis fora de ordem: `conta(b=4, a=2)`?",
        "opcoes": [
            "Dá erro de sintaxe.",
            "Ele ignora as letras e passa o 4 pro 'a' e o 2 pro 'b'.",
            "Ele entende o recado! O 2 vai para o 'a' e o 4 vai para o 'b', pois você nomeou os parâmetros explicitamente.",
            "O programa ignora o comando."
        ],
        "gabarito": "C", "xp_recompensa": 20
    },

    # --- Prática Final ---
    {
        "id_modulo": 14, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Desafio Final: Calculadora de Terreno",
        "enunciado": "Crie uma função chamada `area` que receba os parâmetros `largura` e `comprimento`.\nDentro dela, calcule a multiplicação e faça um print com F-String no formato exato: `A área do terreno é X` (onde X é o resultado).\nFora da função, chame-a passando os números 5 e 10.",
        "opcoes": None, "gabarito": "A área do terreno é 50\n", "xp_recompensa": 50
    },

    # ======================================================================
    # MÓDULO 15: Funções Parte 2
    # ======================================================================

    # --- Bolinha 1: Texto Introdutório ---
    {
        "id_modulo": 15, "id_etapa": 1, "tipo": "TEORIA",
        "titulo": "O Manual e as Docstrings",
        "enunciado": "Quando esquecemos o que uma função faz, o Python tem um manual embutido! Basta usar o comando `help(print)` para ver a explicação oficial.\n\nMas e as funções que NÓS criamos? Podemos criar o nosso próprio manual para elas usando as chamadas **Docstrings** (Strings de Documentação).\nBasta abrir três aspas duplas `\"\"\"` logo abaixo da linha do `def` e escrever a sua explicação.\nAssim, se alguém usar o `help()` na sua função, verá o seu texto!",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 2: 2 Objetivas ---
    {
        "id_modulo": 15, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "Ajudante Embutido",
        "enunciado": "Qual é a função nativa do Python que funciona como um manual interativo, mostrando como usar outras funções, bibliotecas e comandos?",
        "opcoes": ["manual()", "help()", "doc()", "info()"],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 15, "id_etapa": 2, "tipo": "OBJETIVA",
        "titulo": "O Símbolo do Manual",
        "enunciado": "Onde e como escrevemos uma Docstring para que o Python a reconheça como o manual oficial daquela função?",
        "opcoes": [
            "No topo do arquivo, usando jogo da velha (#).",
            "Logo após o return, usando aspas simples.",
            "Logo abaixo da linha de declaração da função (def), usando três aspas duplas (\"\"\").",
            "Em qualquer lugar do código."
        ],
        "gabarito": "C", "xp_recompensa": 10
    },

    # --- Bolinha 3: Texto de Aprofundamento ---
    {
        "id_modulo": 15, "id_etapa": 3, "tipo": "TEORIA",
        "titulo": "Parâmetros Opcionais",
        "enunciado": "No módulo 14, vimos que se a função pedir 2 números e você passar só 1, dá erro.\n\nPara evitar que o programa quebre, podemos dar um valor 'padrão' para a variável logo na criação da função, tornando-a opcional!\nExemplo:\n`def somar(a, b=0):`\n\nSe você chamar `somar(5, 2)`, o 'b' valerá 2. Mas se você chamar só `somar(5)`, o Python não dá erro, ele faz o 'b' valer 0 automaticamente!",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 4: 1 Escrever ---
    {
        "id_modulo": 15, "id_etapa": 4, "tipo": "PRATICA",
        "titulo": "O Convidado Invisível",
        "enunciado": "Crie uma função `cumprimentar` que receba o parâmetro `nome='Visitante'` (isso o torna opcional). Dentro dela, faça um `print(nome)`. Fora da função, chame `cumprimentar()` com os parênteses VAZIOS, para provar que o programa não quebra e assume o valor padrão.",
        "opcoes": None, "gabarito": "Visitante\n", "xp_recompensa": 20
    },

    # --- Bolinha 5: Texto de Aprofundamento ---
    {
        "id_modulo": 15, "id_etapa": 5, "tipo": "TEORIA",
        "titulo": "Escopo de Variáveis",
        "enunciado": "As variáveis no Python têm um lugar onde nascem e morrem, chamado Escopo.\n\n**Escopo Local:** Variáveis criadas DENTRO de uma função só existem lá dentro. Assim que a função acaba, elas são destruídas.\n\n**Escopo Global:** Variáveis criadas no código principal (encostadas na margem esquerda) existem para todo mundo, inclusive para as funções lerem.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 6: 2 Objetivas ---
    {
        "id_modulo": 15, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "A Morte da Variável",
        "enunciado": "Se a variável 'x' foi criada dentro de uma função (Escopo Local), o que acontece se tentarmos dar um `print(x)` fora da função, no código principal?",
        "opcoes": [
            "Ela imprime o valor normal.",
            "Dá erro de variável não definida, pois o 'x' local foi destruído assim que a função acabou.",
            "Imprime zero.",
            "A função é executada novamente para achar o 'x'."
        ],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 15, "id_etapa": 6, "tipo": "OBJETIVA",
        "titulo": "O Poder Global",
        "enunciado": "O que caracteriza uma Variável Global?",
        "opcoes": [
            "Ela apaga as outras variáveis do código.",
            "Ela só funciona na internet.",
            "Ela é declarada no programa principal, e por isso pode ser lida e usada em qualquer parte do código, até mesmo dentro das funções.",
            "Ela é obrigada a ser um texto."
        ],
        "gabarito": "C", "xp_recompensa": 10
    },

    # --- Bolinha 7: Texto Finalizador ---
    {
        "id_modulo": 15, "id_etapa": 7, "tipo": "TEORIA",
        "titulo": "O Verdadeiro Poder: Return",
        "enunciado": "Até agora, nossas funções apenas usavam o `print()` para jogar resultados na tela.\nMas funções de verdade não imprimem coisas, elas DEVOLVEM o resultado para o programa principal usando a palavra `return`.\n\nExemplo:\n`def dobrar(n):`\n    `return n * 2`\n\nIsso permite guardar o resultado numa variável! Você faz `resultado = dobrar(5)` e o número 10 entra na sua variável.",
        "opcoes": None, "gabarito": "LEITURA", "xp_recompensa": 5
    },

    # --- Bolinha 8: 2 Objetivas + 1 Escrever ---
    {
        "id_modulo": 15, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "Print vs Return",
        "enunciado": "Qual a diferença fundamental entre uma função que finaliza com `print(soma)` e uma que finaliza com `return soma`?",
        "opcoes": [
            "Nenhuma, as duas palavras fazem exatamente a mesma coisa.",
            "O print apenas exibe na tela e o valor se perde. O return devolve o valor para quem chamou a função, permitindo guardar esse valor em uma variável ou usá-lo em outras contas.",
            "O return só funciona com textos, e o print com números.",
            "O return encerra o programa todo."
        ],
        "gabarito": "B", "xp_recompensa": 10
    },
    {
        "id_modulo": 15, "id_etapa": 8, "tipo": "OBJETIVA",
        "titulo": "Guardando o Retorno",
        "enunciado": "Se a função `def somar(a, b): return a + b` existe, qual é a linha correta para usar a função e GUARDAR o resultado em uma variável chamada 'total'?",
        "opcoes": [
            "total = print(somar(2, 3))",
            "somar(2, 3) = total",
            "total = somar(2, 3)",
            "return total = somar(2, 3)"
        ],
        "gabarito": "C", "xp_recompensa": 10
    },
    {
        "id_modulo": 15, "id_etapa": 8, "tipo": "PRATICA",
        "titulo": "Retornando um Cálculo",
        "enunciado": "Crie a função `metade` recebendo o parâmetro `n`. Em vez de dar print, faça a função RETORNAR a conta `n / 2`. No código principal (fora da função), faça um `print(metade(10))` para ver o retorno da função direto na tela.",
        "opcoes": None, "gabarito": "5.0\n", "xp_recompensa": 25
    },

    # ======================================================================
    # ETAPA 9: TESTE FINAL DO MÓDULO 15 (O Troféu)
    # 7 Exercícios (2 Obj, 1 Prática, 3 Obj, 1 Prática)
    # ======================================================================

    # --- 2 Objetivas Iniciais (Intermediárias) ---
    {
        "id_modulo": 15, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: A Regra do Return",
        "enunciado": "O que acontece IMEDIATAMENTE após o Python ler e executar a linha `return` dentro de uma função?",
        "opcoes": [
            "A função continua rodando os códigos abaixo dela normalmente até acabar.",
            "A função é pausada e pede um input ao usuário.",
            "A função se encerra NA MESMA HORA. O valor é devolvido e qualquer código que estiver abaixo do return (dentro da função) é completamente ignorado.",
            "Ele imprime o valor na tela do usuário."
        ],
        "gabarito": "C", "xp_recompensa": 15
    },
    {
        "id_modulo": 15, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Revisão: Variáveis Opcionais",
        "enunciado": "Se você cria: `def calcular(x, y=1, z=0):` e chama a função passando apenas `calcular(5)`, quais serão os valores guardados nas três variáveis locais?",
        "opcoes": [
            "Dá erro pois faltaram dois números na chamada.",
            "x=5, y=0, z=0",
            "x=5, y=1, z=0 (O 5 entra no 'x', os outros assumem seus valores padrões).",
            "x=1, y=1, z=0"
        ],
        "gabarito": "C", "xp_recompensa": 15
    },

    # --- 1 Prática Intermediária ---
    {
        "id_modulo": 15, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "Prática: O Guardião de Retorno",
        "enunciado": "Crie uma função `multiplicar` com parâmetros `a` e `b`. Faça ela retornar (`return`) a multiplicação deles. Fora da função, crie uma variável `resultado` que recebe a chamada de `multiplicar(4, 5)`. Na linha de baixo, dê print na variável `resultado`.",
        "opcoes": None, "gabarito": "20\n", "xp_recompensa": 30
    },

    # --- 3 Objetivas de Raciocínio (Difíceis) ---
    {
        "id_modulo": 15, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "Caça ao Bug: Escopo Traiçoeiro",
        "enunciado": "Observe o código atentamente:\n\ndef teste():\n    n = 5\n    print(n)\nn = 10\nteste()\nprint(n)\n\nQual será o resultado na tela? (Lembre-se: se você tem uma variável global 'n' e cria um 'n=5' dentro da função, o Python cria uma variável LOCAL nova sem alterar a global).",
        "opcoes": [
            "10 e 10",
            "5 e 5",
            "5 e 10 (O print local mostra a local 5. O print de baixo mostra a global 10).",
            "Dá erro de variável duplicada."
        ],
        "gabarito": "C", "xp_recompensa": 20
    },
    {
        "id_modulo": 15, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "O Comando Inatingível",
        "enunciado": "Leia o código da função:\n\ndef mensagem():\n    return 'Fim'\n    print('Será?')\n\nSe alguém chamar essa função, a palavra 'Será?' vai aparecer na tela?",
        "opcoes": [
            "Sim, pois o print está dentro da função.",
            "Vai dar erro de sintaxe.",
            "Não, pois como o print está ABAIXO do return, ele é um 'código morto'. A função é encerrada no momento em que o return é disparado.",
            "Aparece antes da palavra 'Fim'."
        ],
        "gabarito": "C", "xp_recompensa": 20
    },
    {
        "id_modulo": 15, "id_etapa": 9, "tipo": "OBJETIVA",
        "titulo": "O Retorno Invisível",
        "enunciado": "Se você criar uma função que tem apenas `print('Oi')` (ou seja, não possui a palavra `return`), e alguém tentar colocar o resultado dela em uma variável fazendo `a = minha_funcao()`, o que será guardado na variável 'a'?",
        "opcoes": [
            "O número 0.",
            "A palavra 'Oi'.",
            "O valor especial 'None' (Nulo/Vazio), porque a função não retornou nada oficialmente.",
            "Dá erro estrutural."
        ],
        "gabarito": "C", "xp_recompensa": 20
    },

    # --- Prática Final ---
    {
        "id_modulo": 15, "id_etapa": 9, "tipo": "PRATICA",
        "titulo": "O DESAFIO SUPREMO: Par ou Ímpar Elegante",
        "enunciado": "Sua última tarefa da trilha! Crie a função `analisar` que receba o parâmetro `n`.\nDentro dela, crie um `if` para ver se é PAR (resto da divisão por 2 igual a 0). Se for par, use `return 'PAR'`.\nSe não for, use `return 'IMPAR'`.\n\nFORA da função, crie uma variável `resultado` que recebe a chamada `analisar(8)`.\nPor fim, faça o `print(resultado)`.",
        "opcoes": None, "gabarito": "PAR\n", "xp_recompensa": 50
    }
]