import { useNavigate } from 'react-router-dom';
import Botao from '../components/Botao';
import Pagina from '../components/Pagina';

// Aparece quando o endereço digitado não existe (rota "*" no App.jsx).
export default function NaoEncontrada() {
  const navigate = useNavigate();

  return (
    <Pagina largura={520}>
      <div className="painel-vidro">
        <h2>Ops! Página não encontrada 🧭</h2>
        <p style={{ margin: '12px 0 24px', color: '#333' }}>
          O endereço que você digitou não existe. Vamos voltar para a trilha?
        </p>
        <Botao texto="Ir para a trilha" variante="sucesso" onClick={() => navigate('/trilha')} />
      </div>
    </Pagina>
  );
}