"""
main.py — Aplicação FastAPI da plataforma educativa de Python.

Como rodar (a partir da pasta do projeto):
    uvicorn main:app --reload
ou execute este arquivo direto no PyCharm (botão Run).

Documentação interativa (Swagger): http://127.0.0.1:8000/docs
"""
import os
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from sqlalchemy import func, update, desc  # Adicionado o 'desc' para o ranking
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Licao, Usuario
from sandbox import MAX_CODIGO_CHARS, StatusExecucao, executar_codigo


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Cria as tabelas na inicialização (suficiente para o trabalho acadêmico).
    Em um projeto maior, prefira migrações com Alembic."""
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Plataforma Educativa de Python",
    description="Backend de uma plataforma gamificada para ensino de Python.",
    version="0.1.0",
    lifespan=lifespan,
)

# CORS: permite que o frontend (em outra porta) chame esta API pelo navegador.
origens_permitidas = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://localhost:5173").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origem.strip() for origem in origens_permitidas],
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------------------------------
# Schemas (formato do JSON de entrada e saída)
# --------------------------------------------------------------------------
class ExecutarRequest(BaseModel):
    usuario_id: int = Field(gt=0, description="ID do aluno")
    licao_id: int = Field(gt=0, description="ID da lição sendo resolvida")
    # Agora o campo 'codigo' vai receber código Python OU a letra (A, B, C) das objetivas
    codigo: str = Field(min_length=1, max_length=MAX_CODIGO_CHARS, description="Resposta ou Código do aluno")


class ExecutarResponse(BaseModel):
    acertou: bool
    status: StatusExecucao
    saida: str
    mensagem: str
    xp_ganho: int
    xp_total: int
    vidas_restantes: int


# --------------------------------------------------------------------------
# Rotas Novas (Trilha e Ranking)
# --------------------------------------------------------------------------

@app.get("/api/licoes")
def listar_licoes(db: Session = Depends(get_db)):
    """Devolve todas as lições cadastradas, ordenadas por módulo."""
    return db.query(Licao).order_by(Licao.id_modulo, Licao.id).all()


@app.get("/api/ranking")
def obter_ranking(db: Session = Depends(get_db)):
    """Devolve o Top 10 usuários com mais XP."""
    return db.query(Usuario).order_by(desc(Usuario.xp)).limit(10).all()


# --------------------------------------------------------------------------
# Rota Principal de Correção e Execução
# --------------------------------------------------------------------------
@app.post("/api/executar", response_model=ExecutarResponse)
def executar(dados: ExecutarRequest, db: Session = Depends(get_db)) -> ExecutarResponse:
    
    usuario = db.get(Usuario, dados.usuario_id)
    if usuario is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Usuário não encontrado.")

    licao = db.get(Licao, dados.licao_id)
    if licao is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Lição não encontrada.")

    if usuario.vidas <= 0:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Você ficou sem vidas. Tente novamente mais tarde.")

    # 1. Roteamento Inteligente: Avalia o tipo da lição antes de corrigir
    if licao.tipo == "TEORIA":
        # Não roda nada, só dá o XP de leitura
        acertou = True
        status_exec = StatusExecucao.ACERTOU
        saida = "Leitura concluída"
        mensagem = "Teoria finalizada com sucesso!"
        
    elif licao.tipo == "OBJETIVA":
        # Compara a alternativa escolhida (dados.codigo) com o gabarito (A, B, C)
        if dados.codigo.strip().upper() == licao.gabarito_saida.strip().upper():
            acertou = True
            status_exec = StatusExecucao.ACERTOU
            saida = f"Alternativa enviada: {dados.codigo}"
            mensagem = "Alternativa correta!"
        else:
            acertou = False
            status_exec = StatusExecucao.ERROU
            saida = f"Alternativa enviada: {dados.codigo}"
            mensagem = "Alternativa incorreta."
            
    else:
        # PRATICA: Envia para o Sandbox (Código original da IA)
        resultado = executar_codigo(dados.codigo, licao.gabarito_saida)
        acertou = resultado.acertou
        status_exec = resultado.status
        saida = resultado.saida
        mensagem = resultado.mensagem

    # 2. UPDATEs Atômicos de XP e Vidas (Seu código excelente mantido)
    xp_ganho = 0
    if status_exec is StatusExecucao.ACERTOU:
        xp_ganho = licao.xp_recompensa
        db.execute(
            update(Usuario).where(Usuario.id == usuario.id).values(xp=Usuario.xp + xp_ganho)
        )
    elif status_exec in (StatusExecucao.ERROU, StatusExecucao.TIMEOUT):
        db.execute(
            update(Usuario)
            .where(Usuario.id == usuario.id)
            .values(vidas=func.greatest(Usuario.vidas - 1, 0))
        )

    db.commit()
    db.refresh(usuario)

    return ExecutarResponse(
        acertou=acertou,
        status=status_exec,
        saida=saida,
        mensagem=mensagem,
        xp_ganho=xp_ganho,
        xp_total=usuario.xp,
        vidas_restantes=usuario.vidas,
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    
