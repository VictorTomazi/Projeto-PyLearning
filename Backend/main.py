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
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import desc, func, select, update
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, selectinload

from database import Base, engine, get_db
from models import Licao, Modulo, ProgressoUsuario, Tentativa, Usuario
from sandbox import MAX_CODIGO_CHARS, StatusExecucao, executar_codigo
from seguranca import hash_senha, verificar_senha


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Cria as tabelas que ainda não existirem ao iniciar o servidor.
    Atenção: `create_all` não altera tabelas já existentes; se mudar os models,
    rode `python seed.py` para recriar o banco. Em um projeto maior, use Alembic."""
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Plataforma Educativa de Python",
    description="Backend de uma plataforma gamificada para ensino de Python.",
    version="0.3.0",
    lifespan=lifespan,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # O asterisco permite qualquer site (ótimo para testes e TCC)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# CORS: permite que o frontend (em outra porta) chame esta API pelo navegador.
# Em desenvolvimento liberamos qualquer porta de localhost/127.0.0.1 (o Vite muda
# de porta quando a 5173 está ocupada). Em produção, defina CORS_ORIGINS
# (separadas por vírgula) com o domínio real do frontend.
origens_permitidas = [o.strip() for o in os.getenv("CORS_ORIGINS", "").split(",") if o.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origens_permitidas,
    allow_origin_regex=r"https?://(localhost|127\.0\.0\.1)(:\d+)?",
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------------------------------
# Schemas (formato do JSON de entrada e saída)
# --------------------------------------------------------------------------
class ExecutarRequest(BaseModel):
    usuario_id: int = Field(gt=0, description="ID do aluno")
    licao_id: int = Field(gt=0, description="ID da lição sendo resolvida")
    # Recebe código Python (PRATICA), a letra da alternativa (OBJETIVA: A, B, C...)
    # ou qualquer texto não vazio (TEORIA, que ignora o conteúdo).
    codigo: str = Field(min_length=1, max_length=MAX_CODIGO_CHARS, description="Resposta ou código do aluno")


class ExecutarResponse(BaseModel):
    acertou: bool
    status: StatusExecucao
    saida: str
    mensagem: str
    xp_ganho: int
    xp_total: int
    vidas_restantes: int


# Os schemas "públicos" abaixo definem exatamente quais campos saem pela API.
# Isso evita vazar o gabarito das lições e o e-mail/hash de senha dos alunos.
class LicaoPublica(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    id_modulo: int
    id_etapa: int
    titulo: str
    enunciado: str
    tipo: str
    opcoes: list[str] | None = None
    xp_recompensa: int


class UsuarioPublico(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nome: str
    xp: int
    vidas: int


class RankingItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    nome: str
    xp: int


# --------------------------------------------------------------------------
# Rotas de consulta (trilha, aluno, progresso e ranking)
# --------------------------------------------------------------------------
@app.get("/api/licoes", response_model=list[LicaoPublica])
def listar_licoes(db: Session = Depends(get_db)):
    """Devolve todas as lições (sem o gabarito), na ordem da trilha: módulo, etapa e lição."""
    consulta = (
        select(Licao)
        .join(Licao.modulo)
        .options(selectinload(Licao.alternativas))  # Carrega as alternativas de uma vez
        .order_by(Modulo.id_trilha, Modulo.ordem, Licao.id_etapa, Licao.id)
    )
    return db.scalars(consulta).all()


@app.get("/api/usuarios/{usuario_id}", response_model=UsuarioPublico)
def obter_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """Devolve nome, XP e vidas do aluno (usado para preencher o topo da tela)."""
    usuario = db.get(Usuario, usuario_id)
    if usuario is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Usuário não encontrado.")
    return usuario


@app.get("/api/usuarios/{usuario_id}/progresso", response_model=list[int])
def obter_progresso(usuario_id: int, db: Session = Depends(get_db)):
    """Devolve os ids das lições que o aluno já concluiu (tabela progresso_usuario)."""
    if db.get(Usuario, usuario_id) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Usuário não encontrado.")
    consulta = select(ProgressoUsuario.id_licao).where(ProgressoUsuario.id_usuario == usuario_id)
    return db.scalars(consulta).all()


@app.get("/api/ranking", response_model=list[RankingItem])
def obter_ranking(db: Session = Depends(get_db)):
    """Devolve o Top 10 de alunos com mais XP (apenas nome e XP)."""
    return db.scalars(select(Usuario).order_by(desc(Usuario.xp)).limit(10)).all()


# --------------------------------------------------------------------------
# Rota principal de correção e execução
# --------------------------------------------------------------------------
# Usa `def` (e não `async def`) de propósito: o sandbox bloqueia por até 3s e,
# com `def`, o FastAPI executa a função em uma thread separada.
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

    # 1. Roteamento: avalia o tipo da lição antes de corrigir
    if licao.tipo == "TEORIA":
        # Não roda nada, só concede o XP de leitura
        acertou = True
        status_exec = StatusExecucao.ACERTOU
        saida = "Leitura concluída"
        mensagem = "Teoria finalizada com sucesso!"

    elif licao.tipo == "OBJETIVA":
        # Compara a alternativa escolhida (dados.codigo) com o gabarito (A, B, C...)
        saida = f"Alternativa enviada: {dados.codigo}"
        if dados.codigo.strip().upper() == licao.gabarito_saida.strip().upper():
            acertou = True
            status_exec = StatusExecucao.ACERTOU
            mensagem = "Alternativa correta!"
        else:
            acertou = False
            status_exec = StatusExecucao.ERROU
            mensagem = "Alternativa incorreta."

    else:
        # PRATICA: envia para o sandbox
        resultado = executar_codigo(dados.codigo, licao.gabarito_saida)
        acertou = resultado.acertou
        status_exec = resultado.status
        saida = resultado.saida
        mensagem = resultado.mensagem

    # 2. Histórico: guarda a tentativa na tabela `tentativas` (teoria é só leitura, não conta)
    if licao.tipo != "TEORIA":
        db.add(
            Tentativa(
                id_usuario=usuario.id,
                id_licao=licao.id,
                codigo_enviado=dados.codigo,
                resultado="SUCESSO" if acertou else "ERRO",
                saida_obtida=saida or mensagem,
            )
        )

    # 3. Progresso, XP e vidas
    xp_ganho = 0
    if status_exec is StatusExecucao.ACERTOU:
        # INSERT ... ON CONFLICT DO NOTHING: só a PRIMEIRA conclusão cria a linha em
        # `progresso_usuario` (rowcount == 1). Assim o XP de uma lição é pago uma única vez,
        # mesmo que o aluno refaça a lição ou envie duas requisições ao mesmo tempo.
        inserido = db.execute(
            pg_insert(ProgressoUsuario.__table__)
            .values(id_usuario=usuario.id, id_licao=licao.id, status="CONCLUIDO")
            .on_conflict_do_nothing(index_elements=["id_usuario", "id_licao"])
        )
        if inserido.rowcount == 1:
            xp_ganho = licao.xp_recompensa
            # UPDATE atômico feito pelo próprio banco (`xp = xp + N`)
            db.execute(
                update(Usuario).where(Usuario.id == usuario.id).values({Usuario.xp: Usuario.xp + xp_ganho})
            )
        else:
            mensagem += " (Você já tinha concluído esta lição, então não ganha XP de novo.)"

    elif status_exec in (StatusExecucao.ERROU, StatusExecucao.TIMEOUT):
        db.execute(
            update(Usuario)
            .where(Usuario.id == usuario.id)
            .values({Usuario.vidas: func.greatest(Usuario.vidas - 1, 0)})
        )

    db.commit()  # Tentativa, progresso e XP/vidas são gravados juntos, na mesma transação
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


# --------------------------------------------------------------------------
# Autenticação: registro e login
# --------------------------------------------------------------------------
# Modelos que o React vai enviar
class DadosRegistro(BaseModel):
    nome: str = Field(min_length=1, max_length=150)
    email: str = Field(min_length=1, max_length=100)
    senha: str = Field(min_length=1, max_length=128)


class DadosLogin(BaseModel):
    email: str = Field(min_length=1, max_length=100)
    senha: str = Field(min_length=1, max_length=128)


@app.post("/api/registro")
def registrar_usuario(dados: DadosRegistro, db: Session = Depends(get_db)):
    # E-mail sempre em minúsculas e sem espaços, para "Ana@x.com" e "ana@x.com" não virarem contas diferentes
    email = dados.email.strip().lower()
    if "@" not in email:
        raise HTTPException(status_code=400, detail="E-mail inválido.")

    # Verifica se alguém já usou esse email
    if db.scalar(select(Usuario).where(Usuario.email == email)) is not None:
        raise HTTPException(status_code=400, detail="Este email já está cadastrado.")

    # Cria o usuário novinho (a senha é salva como HASH, nunca em texto puro)
    novo_usuario = Usuario(
        nome=dados.nome.strip(),
        email=email,
        senha=hash_senha(dados.senha),
        xp=0,
        vidas=5,
    )
    db.add(novo_usuario)
    try:
        db.commit()
    except IntegrityError:
        # Dois cadastros com o mesmo e-mail chegaram ao mesmo tempo; o banco barrou o segundo
        db.rollback()
        raise HTTPException(status_code=400, detail="Este email já está cadastrado.")
    db.refresh(novo_usuario)

    # Devolve o ID para o React
    return {"id": novo_usuario.id, "nome": novo_usuario.nome}


@app.post("/api/login")
def fazer_login(dados: DadosLogin, db: Session = Depends(get_db)):
    # Tenta achar o usuário pelo email
    usuario = db.scalar(select(Usuario).where(Usuario.email == dados.email.strip().lower()))

    # Se o usuário não existir OU a senha não bater, bloqueia o acesso
    if usuario is None or not verificar_senha(dados.senha, usuario.senha):
        raise HTTPException(status_code=401, detail="Email ou senha incorretos.")

    # Se deu tudo certo, devolve o ID para o React salvar no localStorage
    return {"id": usuario.id, "email": usuario.email}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)