import { useLocation, useNavigate } from 'react-router-dom';
import './Cabecalho.css';

export default function Cabecalho() {
  const navigate = useNavigate();
  const { pathname } = useLocation();
  const naTrilha = pathname === '/trilha';

  // Rola suavemente até o elemento com o id informado; sem id, volta ao topo da página.
  function rolarPara(id) {
    const secao = id ? document.getElementById(id) : null;
    if (secao) {
      secao.scrollIntoView({ behavior: 'smooth', block: 'start' });
    } else {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }

  // Para mudar o que cada botão faz, edite apenas esta lista.
  const itens = [
    { rotulo: 'HOME', aoClicar: () => (naTrilha ? rolarPara(null) : navigate('/trilha')) },
    {
      rotulo: 'TRILHA',
      aoClicar: () => (naTrilha ? rolarPara('trilha') : navigate('/trilha')),
      ativo: naTrilha || pathname === '/licao',
    },
    { rotulo: 'SOBRE NÓS', aoClicar: () => navigate('/sobre'), ativo: pathname === '/sobre' },
    { rotulo: 'SUPORTE', aoClicar: () => rolarPara('suporte') }, // Desce até o rodapé (id="suporte")
  ];

  return (
    <header className="cabecalho">
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
    </header>
  );
}