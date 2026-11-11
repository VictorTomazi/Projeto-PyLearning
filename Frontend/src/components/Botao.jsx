import './Botao.css';

export default function Botao({ texto, onClick, variante = 'primario', desabilitado = false }) {
  // A 'variante' vai definir a cor do botão
  const classeBotao = `botao-base botao-${variante}`;

  return (
    <button 
      className={classeBotao} 
      onClick={onClick} 
      disabled={desabilitado}
    >
      {texto}
    </button>
  );
}