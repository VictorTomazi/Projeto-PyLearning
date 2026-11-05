import { Link } from 'react-router-dom';

export default function Trilha() {
  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Mapa de Lições 🗺️</h1>
      <p>Aqui ficarão os botões e os fundos que a sua equipe está fazendo no Figma.</p>
      
      {/* Esse Link funciona como uma tag <a>, mas sem recarregar a página */}
      <Link to="/licao" style={{ 
        display: 'inline-block', 
        padding: '10px 20px', 
        background: '#4CAF50', 
        color: 'white', 
        textDecoration: 'none', 
        borderRadius: '5px' 
      }}>
        Ir para o Exercício 1
      </Link>
    </div>
  );
}
