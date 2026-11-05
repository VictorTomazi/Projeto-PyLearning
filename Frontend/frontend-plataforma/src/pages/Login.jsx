import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import './Login.css'; 

export default function Login() {
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');
  const navigate = useNavigate();

  async function handleLogin(e) {
    e.preventDefault(); // Impede a página de recarregar
    
    // Se o usuário tentar logar com os campos vazios
    if (!email || !senha) {
      alert("Por favor, preencha o email e a senha.");
      return;
    }

    try {
      const resposta = await fetch('http://127.0.0.1:8000/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        // Enviando os dados exatamente como o banco vai pedir
        body: JSON.stringify({ email: email, senha: senha }) 
      });

      const dados = await resposta.json();

      if (resposta.ok) {
        // Sucesso! Salva o ID e joga o aluno para o mapa de lições
        localStorage.setItem('usuario_id', dados.id);
        navigate('/trilha');
      } else {
        // Erro 401 (Senha errada ou email não existe)
        alert(dados.detail || 'Email ou senha incorretos.'); 
      }
    } catch (erro) {
      alert('Não foi possível conectar ao servidor. O backend está ligado?');
    }
  }

  return (
    <div className="tela-fundo">
      {/* 1. Adicionamos a classe 'tela-autenticacao' no formulário para aplicar o sombreado nas letras */}
      <form className="formulario-transparente tela-autenticacao" onSubmit={handleLogin}>
        
        <h2 className="titulo-verde">Login</h2>
        
        <p className="texto-registro">
          Ainda não tem uma conta? <Link to="/registro" className="link-verde">Registre-se aqui.</Link>
        </p>
        <hr className="linha-verde" />

        <div className="grupo-campo">
          <label>Email</label>
          {/* 2. Nova estrutura do input gamificado para o Email */}
          <div className="campo-gamificado">
            <div className="campo-icone">✉️</div>
            <input 
              type="email" 
              placeholder="Digite seu email"
              value={email} 
              onChange={(e) => setEmail(e.target.value)} 
            />
          </div>
        </div>

        <div className="grupo-campo">
          <label>Senha</label>
          {/* 2. Nova estrutura do input gamificado para a Senha */}
          <div className="campo-gamificado">
            <div className="campo-icone">🔒</div>
            <input 
              type="password" 
              placeholder="Digite sua senha"
              value={senha} 
              onChange={(e) => setSenha(e.target.value)} 
            />
          </div>
        </div>

        <button type="submit" className="botao-entrar-arredondado">Entrar</button>

      </form>

      <footer className="rodape-login">
        Copyright@ 2026 Python | Todos os Direitos Reservados
      </footer>
    </div>
  );
}