import { useNavigate } from 'react-router-dom';
import { limparSessao } from '../api';
import './PainelUsuario.css';

// Faixa com o nome do aluno, o XP, as vidas e o botão de sair.
export default function PainelUsuario({ usuario }) {
  const navigate = useNavigate();

  function sair() {
    if (window.confirm('Tem certeza que deseja sair da sua conta?')) {
      limparSessao();
      navigate('/');
    }
  }

  return (
    <div className="painel-usuario">
      <h3 className="painel-usuario-nome">Olá, {usuario?.nome}!</h3>

      <div className="painel-usuario-selos">
        <div className="selo" aria-label={`${usuario?.xp} pontos de experiência`}>
          <span className="selo-xp">XP</span>
          <span className="selo-valor">{usuario?.xp}</span>
        </div>

        <div className="selo" aria-label={`${usuario?.vidas} vidas`}>
          <span className="selo-icone">💚</span>
          <span className="selo-valor">{usuario?.vidas}</span>
        </div>
      </div>

      <button type="button" onClick={sair} className="botao-sair-pilula">
        SAIR
      </button>
    </div>
  );
}