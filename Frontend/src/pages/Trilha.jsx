import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Cabecalho from '../components/Cabecalho';
import Rodape from '../components/Rodape';
import './Trilha.css';

export default function Trilha() {
  const [licoes, setLicoes] = useState([]);
  const [usuario, setUsuario] = useState(null);
  const [carregando, setCarregando] = useState(true);
  const [erro, setErro] = useState('');
  const navigate = useNavigate();

  const posicoesZigZag = [0, 45, 75, 45, 0, -45, -75, -45];

  useEffect(() => {
    const usuarioId = localStorage.getItem('usuario_id');
    if (!usuarioId) {
      navigate('/');
      return;
    }

    async function carregarTrilha() {
      try {
        const [respostaLicoes, respostaUsuario] = await Promise.all([
          fetch('https://pylearning-backend.onrender.com/api/licoes'),
          fetch(`https://pylearning-backend.onrender.com/api/usuarios/${usuarioId}`)
        ]);

        if (!respostaUsuario.ok) {
          localStorage.removeItem('usuario_id');
          navigate('/');
          return;
        }
        if (!respostaLicoes.ok) {
          throw new Error(`Erro ${respostaLicoes.status} ao buscar as lições`);
        }

        setLicoes(await respostaLicoes.json());
        setUsuario(await respostaUsuario.json());
      } catch (e) {
        console.error('Erro ao carregar a trilha:', e);
        setErro('Não foi possível carregar o mapa. O backend está rodando?');
      } finally {
        setCarregando(false);
      }
    }
    carregarTrilha();
  }, [navigate]);

  function fazerLogout() {

    // Abre a janelinha nativa do navegador perguntando se o usuário quer sair
    const querMesmoSair = window.confirm("Tem certeza que deseja sair da sua conta?");
    
    // Só executa o logout se ele clicar em "OK"
    if (querMesmoSair) {
      localStorage.removeItem('usuario_id');
      navigate('/');

  }
}

  // 1. Descobre quais módulos existem no banco (ex: [1, 2])
  const modulos = [...new Set(licoes.map(l => l.id_modulo))];

  return (
    <div className="pagina-trilha">
      <Cabecalho />

      <main className="tela-fundo-trilha">
        {carregando && <p className="aviso-trilha">Carregando mapa...</p>}
        {!carregando && erro && <p className="aviso-trilha">{erro}</p>}

        {!carregando && !erro && (
          <div className="conteudo-trilha" id="trilha">

            <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '30px' }}>
              <h3 style={{ margin: 0, color: '#333' }}>Olá, {usuario?.nome}!</h3>

              <div style={{ display: 'flex', gap: '15px' }}>
                {/* Badge de XP */}
                <div style={{ display: 'flex', alignItems: 'center', padding: '6px 16px', borderRadius: '50px', border: '2px solid #333', backgroundColor: 'white', fontWeight: 'bold', boxShadow: '0 2px 0 #333' }}>
                  <span style={{ color: '#2e7d32', marginRight: '8px', fontSize: '18px', fontWeight: '900' }}>XP</span>
                  <span style={{ color: '#333', fontSize: '16px' }}>{usuario?.xp}</span>
                </div>

                {/* Badge de Vidas */}
                <div style={{ display: 'flex', alignItems: 'center', padding: '6px 16px', borderRadius: '50px', border: '2px solid #333', backgroundColor: 'white', fontWeight: 'bold', boxShadow: '0 2px 0 #333' }}>
                  <span style={{ marginRight: '8px', fontSize: '18px' }}>💚</span>
                  <span style={{ color: '#333', fontSize: '16px' }}>{usuario?.vidas}</span>
                </div>
              </div>

              <button onClick={fazerLogout} className="botao-sair-pilula">
                    SAIR
              </button>
            </header>

            {/* 2. Desenha cada Módulo separado */}
            {modulos.map((numeroModulo) => {
              // Pega só as lições deste módulo específico
              const licoesDoModulo = licoes.filter(l => l.id_modulo === numeroModulo);
              // Descobre as etapas únicas dentro deste módulo
              const etapasDoModulo = [...new Set(licoesDoModulo.map(l => l.id_etapa))];

              return (
                <section key={`modulo-${numeroModulo}`} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', padding: '20px 0' }}>

                  <h2 style={{ marginBottom: '40px', color: '#333' }}>Módulo {numeroModulo}</h2>

                  {etapasDoModulo.map((numeroDaEtapa, index) => {
                    const deslocamentoEixoX = posicoesZigZag[index % posicoesZigZag.length];

                    // Verifica se é a última etapa da lista deste módulo
                    const ehTesteFinal = index === etapasDoModulo.length - 1;

                    return (
                      <div
                        key={`bolinha-${numeroModulo}-${numeroDaEtapa}`}
                        className="no-trilha"
                        style={{ transform: `translateX(${deslocamentoEixoX}px)` }}
                      >
                        <button
                          className="botao-circular"
                          // Cor escura se for o teste final
                          style={ehTesteFinal ? { backgroundColor: '#3B3B3B', boxShadow: '0 8px 0 #000000' } : {}}
                          // Envia o módulo e a etapa para a tela de exercício
                          onClick={() => navigate('/licao', { state: { etapa: numeroDaEtapa, modulo: numeroModulo } })}
                        >
                          {ehTesteFinal ? '🏆' : '⭐'}
                        </button>
                        <span className="titulo-licao">
                          {ehTesteFinal ? 'Teste Final' : `Etapa ${numeroDaEtapa}`}
                        </span>
                      </div>
                    );
                  })}
                </section>
              );
            })}

          </div>
        )}
      </main>

      <Rodape />
    </div>
  );
}