import { useLocation, useNavigate } from 'react-router-dom';
import './Cabecalho.css';

export default function Cabecalho() {
  const navigate = useNavigate();
  const { pathname } = useLocation();
  const naHome = pathname === '/home';
  const naTrilha = pathname === '/trilha';

  function rolarPara(id) {
    const secao = id ? document.getElementById(id) : null;
    if (secao) {
      secao.scrollIntoView({ behavior: 'smooth', block: 'start' });
    } else {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }

  const itens = [
    { rotulo: 'HOME', aoClicar: () => (naHome ? rolarPara(null) : navigate('/home')), ativo: naHome },
    {
      rotulo: 'TRILHA',
      aoClicar: () => (naTrilha ? rolarPara('trilha') : navigate('/trilha')),
      ativo: naTrilha || pathname === '/licao',
    },
    { rotulo: 'PERFIL', aoClicar: () => navigate('/perfil'), ativo: pathname === '/perfil' },
    { rotulo: 'SUPORTE', aoClicar: () => rolarPara('suporte') },
  ];

  return (
    <header className="cabecalho">
      <div className="cabecalho-container">
        <div 
          className="cabecalho-logo" 
          onClick={() => (naHome ? rolarPara(null) : navigate('/home'))}
          aria-label="Ir para a página inicial"
        >
          <img src="/mascote-sem-fundo.png" alt="Mascote PyLearning" className="logo-imagem" />
          <span className="logo-texto">PyLearning</span>
        </div>

        <nav className="cabecalho-menu" aria-label="Menu principal">
          {itens.map((item) => (
            <button
              key={item.rotulo}
              type="button"
              className={`cabecalho-botao${item.ativo ? ' ativo' : ''}`}
              onClick={item.aoClicar}
              aria-current={item.ativo ? 'page' : undefined}
            >
              {item.rotulo}
            </button>
          ))}
        </nav>
      </div>
    </header>
  );
}