"""
seed.py — Cria as tabelas no PostgreSQL e carrega os dados iniciais.

O que faz, nesta ordem:
    1. APAGA todas as tabelas do projeto (se existirem);
    2. CRIA as tabelas a partir do models.py;
    3. Insere: 1 trilha, os módulos e as lições de conteudo.py (com as
       alternativas das objetivas) e 1 aluno de teste.

ATENÇÃO: o passo 1 apaga TODOS os dados (alunos, XP, progresso...). Use apenas
em desenvolvimento. Rode sempre que mudar o models.py ou o conteudo.py.

Pré-requisito: o banco `plataforma_python` já precisa existir (crie vazio no
pgAdmin 4: botão direito em "Databases" > Create > Database).

Como rodar (na pasta do backend): python seed.py
No PyCharm: abra este arquivo e clique em Run.
"""

from sqlalchemy import text

from conteudo import MODULOS_E_LICOES
from database import Base, SessionLocal, engine
from models import Licao, Modulo, OpcaoLicao, Trilha, Usuario
from seguranca import hash_senha

# Nomes dos módulos
NOMES_MODULOS = {
    1: "Primeiros Comandos",
    2: "Operadores Aritméticos",
    3: "Utilizando Módulos",
    4: "Manipulando Textos",
    5: "Condições Básicas",
    6: "Condições Aninhadas",
    7: "Estrutura de Repetição FOR",
    8: "Estrutura de Repetição WHILE",
    9: "Interrompendo Repetições",
    10: "Variáveis Compostas - Tuplas",
    11: "Variáveis Compostas - Listas",
    12: "Variáveis Compostas - Listas Parte 2",
    13: "Variáveis Compostas - Dicionários",
    14: "Funções Parte 1",
    15: "Funções Parte 2",
}


def popular() -> None:
    # 1. Apaga as tabelas do projeto. `CASCADE` resolve as dependências entre elas
    #    e `IF EXISTS` evita erro quando ainda não existem. Os nomes vêm do
    #    próprio models.py (não são digitados pelo usuário).
    nomes_das_tabelas = ", ".join(Base.metadata.tables)
    with engine.begin() as conexao:
        conexao.execute(text(f"DROP TABLE IF EXISTS {nomes_das_tabelas} CASCADE"))

    # 2. Cria todas as tabelas do models.py
    Base.metadata.create_all(bind=engine)

    # 3. Dados iniciais
    with SessionLocal() as db:
        # Login de teste: aluno@teste.com / teste123 (a senha é salva como hash)
        db.add(Usuario(nome="Aluno Teste", email="aluno@teste.com", senha=hash_senha("teste123")))

        trilha = Trilha(nome="Python do Zero", descricao="Do primeiro print() aos primeiros programas.")
        db.add(trilha)
        db.flush()  # Envia ao banco para já termos o id da trilha

        # Um módulo para cada id_modulo que aparece no conteudo.py
        modulos: dict[int, Modulo] = {}
        for numero in sorted({item["id_modulo"] for item in MODULOS_E_LICOES}):
            modulos[numero] = Modulo(
                id_trilha=trilha.id,
                nome=NOMES_MODULOS.get(numero, f"Módulo {numero}"),
                ordem=numero,
            )
            db.add(modulos[numero])
        db.flush()  # Obtém os ids reais dos módulos

        for item in MODULOS_E_LICOES:
            licao = Licao(
                id_modulo=modulos[item["id_modulo"]].id,
                id_etapa=item["id_etapa"],
                titulo=item["titulo"],
                enunciado=item["enunciado"],
                tipo=item["tipo"],
                # No conteudo.py a chave se chama "gabarito"; no banco, "gabarito_saida".
                gabarito_saida=item["gabarito"],
                xp_recompensa=item["xp_recompensa"],
            )
            # Alternativas (só nas OBJETIVA): a 1ª vira A, a 2ª B, e assim por diante.
            for posicao, texto in enumerate(item["opcoes"] or []):
                licao.alternativas.append(OpcaoLicao(letra=chr(ord("A") + posicao), texto=texto))
            db.add(licao)

        db.commit()

    print(
        f"Banco pronto: {len(Base.metadata.tables)} tabelas criadas; "
        f"{len(modulos)} módulos e {len(MODULOS_E_LICOES)} lições carregados."
    )
    print("Login de teste: aluno@teste.com  /  senha: teste123")


if __name__ == "__main__":
    popular()