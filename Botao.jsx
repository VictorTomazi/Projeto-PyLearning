import './Botao.css'; // Vamos criar esse arquivo de estilos no próximo passo

export default function Botao({ texto, onClick, variante = 'primario', desabilitado = false }) {
  // A 'variante' vai definir a cor do botão (primario, sucesso, erro, etc)
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
