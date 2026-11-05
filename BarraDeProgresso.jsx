import './BarraDeProgresso.css';

export default function BarraDeProgresso({ porcentagem }) {
  return (
    <div className="barra-fundo">
      <div 
        className="barra-preenchimento" 
        style={{ width: `${porcentagem}%` }}
      >
        {/* Essa div interna é opcional, mas dá aquele reflexo/brilho 3D no topo da barra */}
        <div className="barra-brilho"></div>
      </div>
    </div>
  );
}
