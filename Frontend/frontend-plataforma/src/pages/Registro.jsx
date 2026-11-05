import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import './Login.css'; // Reaproveitamos todo o visual da tela de Login!

export default function Registro() {
  const [nome, setNome] = useState('');
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');
  const navigate = useNavigate();

  async function handleRegistro(e) {
    e.preventDefault();

    if (!nome || !email || !senha) {
      alert("Por favor, preencha todos os campos.");
      return;
    }

    const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    
    if (!regexEmail.test(email)) {
      alert("Por favor, digite um endereço de email válido.");
      return; // Trava a execução aqui, não deixa ir pro servidor
    }

    try {
      const resposta = await fetch('http://127.0.0.1:8000/api/registro', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nome, email, senha })
      });

      const dados = await resposta.json();

      if (resposta.ok) {
        // Mostra uma mensagem amigável (pode trocar por um toast/notificação depois se quiser)
        alert('Conta criada com sucesso! Por favor, faça login para acessar a plataforma.');
        
        // Joga de volta para a tela inicial (Login)
        navigate('/'); 
      } else {
        alert(dados.detail || 'Erro ao criar conta.');
      }
      
    } catch {
      alert('Não foi possível conectar ao servidor.');
    }
  }

  return (
    <div className="tela-fundo">
      <form className="formulario-transparente" onSubmit={handleRegistro}>
        
        <h2 className="titulo-verde">Criar Conta</h2>
        
        <p className="texto-registro">
          Já tem uma conta? <Link to="/" className="link-verde">Faça login aqui.</Link>
        </p>
        <hr className="linha-verde" />

        <div className="grupo-campo">
          <label>Como quer ser chamado?</label>
          <div className="input-com-icone">
            <span className="icone-fundo-verde">👤</span>
            <input 
              type="text" 
              value={nome} 
              onChange={(e) => setNome(e.target.value)} 
            />
          </div>
        </div>

        <div className="grupo-campo">
          <label>Email</label>
          <div className="input-com-icone">
            <span className="icone-fundo-verde">✉️</span>
            <input 
              type="email" 
              value={email} 
              onChange={(e) => setEmail(e.target.value)} 
            />
          </div>
        </div>

        <div className="grupo-campo">
          <label>Senha</label>
          <div className="input-com-icone">
            <span className="icone-fundo-verde">🔒</span>
            <input 
              type="password" 
              value={senha} 
              onChange={(e) => setSenha(e.target.value)} 
            />
          </div>
        </div>

        <button type="submit" className="botao-entrar-arredondado" style={{ marginTop: '20px' }}>
          Registrar
        </button>

      </form>

      <footer className="rodape-login">
        Copyright@ 2026 Python | Todos os Direitos Reservados
      </footer>
    </div>
  );
}