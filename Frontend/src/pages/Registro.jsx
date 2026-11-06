import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { enviarJson } from '../api';
import './Login.css'; // Login e Registro compartilham o mesmo visual

export default function Registro() {
  const [nome, setNome] = useState('');
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');
  const [erro, setErro] = useState('');
  const [enviando, setEnviando] = useState(false);
  const navigate = useNavigate();

  async function handleRegistro(e) {
    e.preventDefault();
    setErro('');

    if (!nome.trim() || !email || !senha) {
      setErro('Por favor, preencha todos os campos.');
      return;
    }

    const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!regexEmail.test(email)) {
      setErro('Por favor, digite um endereço de email válido.');
      return; // Trava a execução aqui, não deixa ir pro servidor
    }

    setEnviando(true);
    try {
      await enviarJson('/registro', { nome, email, senha });

      // Volta para o login já mostrando a mensagem de sucesso
      navigate('/', { state: { aviso: 'Conta criada com sucesso! Faça login para acessar a plataforma.' } });
    } catch (e) {
      setErro(e.message); // Ex.: "Este email já está cadastrado."
    } finally {
      setEnviando(false);
    }
  }

  return (
    <div className="tela-fundo">
      {/* Mesmas classes do Login: 'tela-autenticacao' aplica o sombreado nas letras */}
      <form className="formulario-transparente tela-autenticacao" onSubmit={handleRegistro}>

        <h2 className="titulo-verde">Criar Conta</h2>

        <p className="texto-registro">
          Já tem uma conta? <Link to="/" className="link-verde">Faça login aqui.</Link>
        </p>
        <hr className="linha-verde" />

        {erro && <div className="aviso-formulario erro" role="alert">{erro}</div>}

        <div className="grupo-campo">
          <label htmlFor="registro-nome">Como quer ser chamado?</label>
          <div className="campo-gamificado">
            <div className="campo-icone">👤</div>
            <input
              id="registro-nome"
              type="text"
              placeholder="Digite seu nome"
              maxLength={150}
              value={nome}
              onChange={(e) => setNome(e.target.value)}
            />
          </div>
        </div>

        <div className="grupo-campo">
          <label htmlFor="registro-email">Email</label>
          <div className="campo-gamificado">
            <div className="campo-icone">✉️</div>
            <input
              id="registro-email"
              type="email"
              placeholder="Digite seu email"
              maxLength={100}
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
        </div>

        <div className="grupo-campo">
          <label htmlFor="registro-senha">Senha</label>
          <div className="campo-gamificado">
            <div className="campo-icone">🔒</div>
            <input
              id="registro-senha"
              type="password"
              placeholder="Crie uma senha"
              maxLength={128}
              value={senha}
              onChange={(e) => setSenha(e.target.value)}
            />
          </div>
        </div>

        <button type="submit" className="botao-entrar-arredondado" disabled={enviando}>
          {enviando ? 'Criando conta...' : 'Registrar'}
        </button>

      </form>

      <footer className="rodape-login">
        Copyright@ 2026 Python | Todos os Direitos Reservados
      </footer>
    </div>
  );
}