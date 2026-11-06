import Cabecalho from './Cabecalho';
import Rodape from './Rodape';
import './Pagina.css';

/**
 * Moldura padrão das telas internas (Trilha, Lição, Sobre nós...):
 * cabeçalho verde no topo, imagem de paisagem ao fundo e rodapé no fim.
 * O conteúdo (`children`) fica centralizado, com a largura máxima informada.
 * Dentro dele, use a classe "painel-vidro" para o cartão branco translúcido.
 */
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