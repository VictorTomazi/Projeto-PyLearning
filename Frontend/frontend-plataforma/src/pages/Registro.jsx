import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import './Login.css'; // Login e Registro compartilham o mesmo visual

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
      const resposta = await fetch('https://pylearning-backend.onrender.com/api/registro', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nome, email, senha })
      });

      const dados = await resposta.json();

      if (resposta.ok) {
        alert('Conta criada com sucesso! Por favor, faça login para acessar a plataforma.');

        // Joga de volta para a tela inicial (Login)
        navigate('/');
      } else {
        // `detail` é um texto nos erros esperados (ex.: email já cadastrado)
        alert(typeof dados.detail === 'string' ? dados.detail : 'Erro ao criar conta. Confira os dados informados.');
      }

    } catch {
      alert('Não foi possível conectar ao servidor. O backend está ligado?');
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

        <button type="submit" className="botao-entrar-arredondado">Registrar</button>

      </form>

      <footer className="rodape-login">
        Copyright@ 2026 Python | Todos os Direitos Reservados
      </footer>
    </div>
  );
}