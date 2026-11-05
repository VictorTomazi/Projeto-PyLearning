"""
seguranca.py — Hash e verificação de senhas (Argon2).

O banco guarda apenas o HASH na coluna `senha_hash`; a senha original nunca é
salva. O Argon2 gera um "sal" aleatório a cada hash, então duas senhas iguais
produzem hashes diferentes — por isso a conferência usa `verificar_senha` e
não uma comparação direta (`==`).

Instalação:  pip install argon2-cffi
"""
from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerificationError

_hasher = PasswordHasher()


def hash_senha(senha: str) -> str:
    """Gera o hash que deve ser salvo em Usuario.senha."""
    return _hasher.hash(senha)


def verificar_senha(senha: str, senha_hash: str) -> bool:
    """True se a senha digitada corresponde ao hash salvo; False caso contrário."""
    try:
        return _hasher.verify(senha_hash, senha)
    except (VerificationError, InvalidHashError):
        # Senha errada ou valor salvo que não é um hash válido
        return False