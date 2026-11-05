import './Rodape.css';

// O id="suporte" é o destino do botão SUPORTE do cabeçalho.
export default function Rodape() {
  return (
    <footer className="rodape" id="suporte">
      <p className="rodape-titulo">PyLearning - Plataforma de Ensino de Python.</p>
      <p className="rodape-contato">
        Suporte via WhatsApp:{' '}
        <a href="https://wa.me/5511930324611" target="_blank" rel="noreferrer">
          +55 (11) 93032-4611
        </a>{' '}
        | E-mail: <a href="mailto:victor.tomazi@cs.ceunsp.edu.br">victor.tomazi@cs.ceunsp.edu.br</a>
      </p>
    </footer>
  );
}