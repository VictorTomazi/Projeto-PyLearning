MODULOS_E_LICOES = [
    # 1. Apenas explicação (Sem questões)
    {
        "id_modulo": 1,
        "titulo": "Aula 1 - Primeiros comandos em Python",
        "enunciado": "Antes de começarmos a fazer grandes linhas de códigos, é necessário entender conceitos básicos...\n\nQuando precisamos mandar uma mensagem, usamos o 'print'. Ele precisa de parênteses e aspas.",
        "tipo": "TEORIA",  # O frontend vai ler isso e esconder o editor de código e as alternativas
        "opcoes": None,
        "gabarito": "AVANCAR",  # Apenas um controle interno para liberar o botão de próximo
        "xp_recompensa": 5  # XP bônus só por ler a teoria
    },

    # 2. Fixação rápida (Múltipla Escolha)
    {
        "id_modulo": 1,
        "titulo": "Aula 1 - Fixação 1",
        "enunciado": "Como você escreveria a seguinte mensagem: Olá, Mundo!",
        "tipo": "OBJETIVA",
        "opcoes": [
            "print 'Olá, Mundo!'",
            "print(Olá, Mundo!)",
            "print('Olá, Mundo!')",
            "'Olá, Mundo!'"
        ],
        "gabarito": "C",
        "xp_recompensa": 10
    },

    # 3. Mão na massa (Sandbox)
    {
        "id_modulo": 1,
        "titulo": "Aula 1 - Prática",
        "enunciado": "Agora é sua vez! Digite o código para imprimir exatamente a mensagem: Sou o mais novo estudante de Python!",
        "tipo": "PRATICA",
        "opcoes": None,
        "gabarito": "Sou o mais novo estudante de Python!",
        "xp_recompensa": 15
    }
]
