"""
seed.py — Recria o banco do zero e o popula com dados de teste.

Cria:
    - 1 aluno de teste (id 1)
    - todas as lições de conteudo.py (ids 1, 2, 3... na mesma ordem da lista)

ATENÇÃO: este script APAGA as tabelas `usuarios` e `licoes` (incluindo XP e
vidas) e as recria. Use somente em desenvolvimento.

Por que apagar? O `create_all` do SQLAlchemy só cria tabelas que ainda não
existem; ele NÃO adiciona colunas novas (id_modulo, tipo, opcoes) a uma tabela
antiga. Sem recriar, qualquer consulta a `licoes` falha com erro 500.

Como rodar (a partir da pasta do backend):
    python seed.py
No PyCharm, basta abrir o arquivo e clicar em Run.
"""
from conteudo import MODULOS_E_LICOES
from database import Base, SessionLocal, engine
from models import Licao, Usuario
from sqlalchemy import text


def popular() -> None:
    # 1. Limpeza bruta: apaga as tabelas atuais e qualquer tabela fantasma que dependa delas
    with engine.connect() as conn:
        conn.execute(text("DROP TABLE IF EXISTS usuarios, licoes, opcoes_licao, progresso_usuario, tentativas CASCADE;"))
        conn.commit()

    # 2. Recria a estrutura limpa usando o models.py atual
    Base.metadata.create_all(bind=engine)

    # 3. Insere os dados de teste
    with SessionLocal() as db:
        db.add(Usuario(nome="Aluno Teste", email="aluno@teste.com", senha="hash-de-teste"))
        db.add(Usuario(nome="Victor Tomazi", email="tomazivictor@gmail.com", senha="1234"))

        for item in MODULOS_E_LICOES:
            db.add(
                Licao(
                    id_modulo=item["id_modulo"],
                    titulo=item["titulo"],
                    enunciado=item["enunciado"],
                    tipo=item["tipo"],
                    opcoes=item["opcoes"],
                    gabarito_saida=item["gabarito"],
                    xp_recompensa=item["xp_recompensa"],
                )
            )

        db.commit()

    print(f"Banco recriado com sucesso.")


if __name__ == "__main__":
    popular()
