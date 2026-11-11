import Cabecalho from './Cabecalho';
import Rodape from './Rodape';
import './Pagina.css';

export default function Pagina({ children, largura = 640 }) {
  return (
    <div className="pagina">
      <Cabecalho />

      <main className="pagina-fundo">
        <div className="pagina-conteudo" style={{ maxWidth: largura }}>
          {children}
        </div>
      </main>

      <Rodape />
    </div>
  );
}