import { useState } from 'react';
import { useLocation, useNavigate, Link } from 'react-router-dom';
import { enviarJson, salvarSessao } from '../api';
import './Login.css';

export default function Login() {
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');
  const [erro, setErro] = useState('');
  const [enviando, setEnviando] = useState(false);
  const navigate = useNavigate();
  const location = useLocation();

  // Mensagem enviada pela tela de registro (ex.: "Conta criada com sucesso!")
  const aviso = location.state?.aviso;

  async function handleLogin(e) {
    e.preventDefault(); // Impede a página de recarregar
    setErro('');

    if (!email || !senha) {
      setErro('Por favor, preencha o email e a senha.');
      return;
    }

    setEnviando(true);
    try {
      const dados = await enviarJson('/login', { email, senha });

      // Sucesso! Salva o ID e o e-mail (mostrado no Perfil) e joga o aluno para o mapa de lições
      salvarSessao({ id: dados.id, email: dados.email });
      navigate('/trilha');
    } catch (e) {
      // Erro 401 (senha errada ou email não existe) ou falha de conexão
      setErro(e.message);
    } finally {
      setEnviando(false);
    }
  }

  return (
    <div className="tela-fundo">
      {/* A classe 'tela-autenticacao' aplica o sombreado nas letras */}
      <form className="formulario-transparente tela-autenticacao" onSubmit={handleLogin}>

        <h2 className="titulo-verde">Login</h2>

        <p className="texto-registro">
          Ainda não tem uma conta? <Link to="/registro" className="link-verde">Registre-se aqui.</Link>
        </p>
        <hr className="linha-verde" />

        {aviso && <div className="aviso-formulario sucesso" role="status">{aviso}</div>}
        {erro && <div className="aviso-formulario erro" role="alert">{erro}</div>}

        <div className="grupo-campo">
          <label htmlFor="login-email">Email</label>
          <div className="campo-gamificado">
            <div className="campo-icone">✉️</div>
            <input
              id="login-email"
              type="email"
              placeholder="Digite seu email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
        </div>

        <div className="grupo-campo">
          <label htmlFor="login-senha">Senha</label>
          <div className="campo-gamificado">
            <div className="campo-icone">🔒</div>
            <input
              id="login-senha"
              type="password"
              placeholder="Digite sua senha"
              value={senha}
              onChange={(e) => setSenha(e.target.value)}
            />
          </div>
        </div>

        <button type="submit" className="botao-entrar-arredondado" disabled={enviando}>
          {enviando ? 'Entrando...' : 'Entrar'}
        </button>

      </form>

      <footer className="rodape-login">
        Copyright@ 2026 Python | Todos os Direitos Reservados
      </footer>
    </div>
  );
}