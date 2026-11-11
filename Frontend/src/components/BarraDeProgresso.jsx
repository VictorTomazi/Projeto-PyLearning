import './BarraDeProgresso.css';

export default function BarraDeProgresso({ porcentagem }) {
  return (
    <div className="barra-fundo">
      <div 
        className="barra-preenchimento" 
        style={{ width: `${porcentagem}%` }}
      >
        <div className="barra-brilho"></div>
      </div>
    </div>
  );
}