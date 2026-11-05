import { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom'; 

import EditorDeCodigo from '../EditorDeCodigo'; 
import '../App.css'; 
import BarraDeProgresso from '../components/BarraDeProgresso';
import './Exercicio.css';

const API_URL = 'https://pylearning-backend.onrender.com/api';
const CODIGO_INICIAL = '# Escreva seu código aqui\n';

const letra = (indice) => String.fromCharCode(65 + indice); 

async function chamarApi(caminho, opcoes) {
  let resposta;
  try {
    resposta = await fetch(`${API_URL}${caminho}`, opcoes);
  } catch {
    throw new Error('Não foi possível conectar ao servidor. O backend está a correr em http://127.0.0.1:8000?');
  }

  const dados = await resposta.json().catch(() => null);
  if (!resposta.ok) {
    throw new Error(
      typeof dados?.detail === 'string'
        ? dados.detail
        : `Erro ${resposta.status} no servidor (veja o terminal do backend).`
    );
  }
  return dados;
}

export default function Exercicio() {
  const usuarioId = localStorage.getItem('usuario_id') || 1;

  const [licoes, setLicoes] = useState([]);
  const [usuario, setUsuario] = useState(null);
  const [carregado, setCarregado] = useState(false);
  const [indice, setIndice] = useState(0);

  const [codigo, setCodigo] = useState(CODIGO_INICIAL); 
  const [escolha, setEscolha] = useState(null);         
  const [resultado, setResultado] = useState(null);
  const [enviando, setEnviando] = useState(false);
  const [erro, setErro] = useState('');
  
  const location = useLocation();
  const navigate = useNavigate();
  const etapaSelecionada = location.state?.etapa || 1; 
  const moduloSelecionado = location.state?.modulo || 1;

  useEffect(() => {
    async function carregar() {
      try {
        const [listaLicoes, dadosUsuario] = await Promise.all([
          chamarApi('/licoes'),
          chamarApi(`/usuarios/${usuarioId}`),
        ]);
        
        const licoesDaEtapa = listaLicoes.filter(
          l => l.id_etapa === etapaSelecionada && l.id_modulo === moduloSelecionado
        );
        setLicoes(licoesDaEtapa);
        setUsuario(dadosUsuario);
      } catch (e) {
        setErro(e.message);
      } finally {
        setCarregado(true);
      }
    }
    carregar();
  }, [etapaSelecionada, moduloSelecionado, usuarioId]);

  function fazerLogout() {
    localStorage.removeItem('usuario_id');
    navigate('/');
  }

  function proximaLicao() {
    setIndice((i) => i + 1);
    setResultado(null);
    setEscolha(null);
    setCodigo(CODIGO_INICIAL);
    setErro('');
  }

  // --- FUNÇÃO ADICIONADA: RECOMEÇAR LIÇÃO ---
  async function recomecarLicao() {
    try {
      // 1. Chama a nova rota do Render para devolver 5 vidas no banco
      await chamarApi(`/usuarios/${usuarioId}/resetar-vidas`, { method: 'PUT' });

      // 2. Atualiza os dados na tela para o aluno voltar a jogar imediatamente
      setUsuario((atual) => ({ ...atual, vidas: 5 }));
      setIndice(0); // Volta para a primeira pergunta da etapa
      setResultado(null);
      setEscolha(null);
      setCodigo(CODIGO_INICIAL);
      setErro('');
    } catch (error) {
      alert("Erro ao recomeçar a lição. Tente novamente.");
    }
  }

  if (!carregado || licoes.length === 0 || !usuario) {
    return (
      <main className="app">
        <p>{!carregado ? 'A carregar...' : erro || `Nenhuma lição encontrada para a Etapa ${etapaSelecionada}.`}</p>
      </main>
    );
  }

  const concluido = indice >= licoes.length;

  async function enviar(resposta) {
    setEnviando(true);
    setErro('');
    try {
      const licaoAtual = licoes[indice]; 
      const dados = await chamarApi('/executar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ usuario_id: usuarioId, licao_id: licaoAtual.id, codigo: resposta }),
      });
      setResultado(dados);
      setUsuario((atual) => ({ ...atual, xp: dados.xp_total, vidas: dados.vidas_restantes }));
    } catch (e) {
      setErro(e.message);
    } finally {
      setEnviando(false);
    }
  }

  const topo = (
    <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '30px' }}>
      <h3 style={{ margin: 0, color: '#333' }}>Olá, {usuario.nome}!</h3>
      
      <div style={{ display: 'flex', gap: '15px' }}>
        <div style={{ display: 'flex', alignItems: 'center', padding: '6px 16px', borderRadius: '50px', border: '2px solid #333', backgroundColor: 'white', fontWeight: 'bold', boxShadow: '0 2px 0 #333' }}>
          <span style={{ color: '#2e7d32', marginRight: '8px', fontSize: '18px', fontWeight: '900' }}>XP</span> 
          <span style={{ color: '#333', fontSize: '16px' }}>{usuario.xp}</span>
        </div>
        
        <div style={{ display: 'flex', alignItems: 'center', padding: '6px 16px', borderRadius: '50px', border: '2px solid #333', backgroundColor: 'white', fontWeight: 'bold', boxShadow: '0 2px 0 #333' }}>
          <span style={{ marginRight: '8px', fontSize: '18px' }}>💚</span> 
          <span style={{ color: '#333', fontSize: '16px' }}>{usuario.vidas}</span>
        </div>
      </div>

      <button onClick={fazerLogout} className="botao-sair-pilula">
        SAIR
      </button>
    </header>
  );

  if (concluido) {
    return (
      <main className="app">
        {topo}
        <section className="cartao" style={{ textAlign: 'center' }}>
          <h2>🎉 Etapa {etapaSelecionada} concluída!</h2>
          <p>Ótimo trabalho! O seu total agora é de <b>{usuario.xp} XP</b>.</p>
          <button 
            className="botao" 
            onClick={() => navigate('/trilha')}
            style={{ marginTop: '20px' }}
          >
            Voltar para a trilha
          </button>
        </section>
      </main>
    );
  }

  const licao = licoes[indice]; 
  const acertou = resultado?.acertou === true;
  
  // Variável mágica que usamos para verificar o "Game Over"
  const semVidas = usuario.vidas <= 0;

  const rotuloBotao = { TEORIA: 'Entendi, avançar', OBJETIVA: 'Responder', PRATICA: 'Executar' }[licao.tipo];
  const botaoDesabilitado = enviando || semVidas || (licao.tipo === 'OBJETIVA' && !escolha);

  function responder() {
    if (licao.tipo === 'TEORIA') return enviar('AVANCAR');
    if (licao.tipo === 'OBJETIVA') return enviar(escolha);
    return enviar(codigo);
  }

  const porcentagemProgresso = ((indice + (acertou ? 1 : 0)) / licoes.length) * 100;

  return (
    <main className="app">
      {topo}
      <div style={{ maxWidth: '600px', margin: '0 auto 20px', width: '100%' }}>
        <BarraDeProgresso porcentagem={porcentagemProgresso} />
      </div>

      <div className="area-exercicio-com-mascote">
        
        <img 
          src="/mascote.png" 
          alt="Mascote PyLearning" 
          className="mascote-exercicio" 
        />

        {/* --- A MÁGICA ACONTECE AQUI (A antiga "Parte C") --- */}
        {semVidas ? (
          
          <section className="cartao" style={{ textAlign: 'center' }}>
            <h2>Você perdeu todas as vidas! 💔</h2>
            <p>Não desanime. A repetição é a chave para aprender Python.</p>
            <button 
              onClick={recomecarLicao} 
              className="botao-entrar-arredondado" 
              style={{ marginTop: '20px' }}
            >
              Recomeçar Lição
            </button>
          </section>

        ) : (
          
          <section className="cartao" key={`licao-${indice}`}>
            <small className="etapa">
              Módulo {licao.id_modulo} · Lição {indice + 1} de {licoes.length}
            </small>
            <h2>{licao.titulo}</h2>
            <p className="enunciado">{licao.enunciado}</p>

            {licao.tipo === 'OBJETIVA' && (
              <div className="opcoes">
                {licao.opcoes?.map((texto, i) => (
                  <button
                    key={letra(i)}
                    className={`opcao ${escolha === letra(i) ? 'selecionada' : ''}`}
                    onClick={() => setEscolha(letra(i))}
                    disabled={acertou || enviando}
                  >
                    <b>{letra(i)}</b> {texto}
                  </button>
                ))}
              </div>
            )}

            {licao.tipo === 'PRATICA' && <EditorDeCodigo value={codigo} onChange={setCodigo} />}

            {acertou ? (
              <button className="botao" onClick={proximaLicao}>
                Próxima →
              </button>
            ) : (
              <button className="botao" onClick={responder} disabled={botaoDesabilitado}>
                {enviando ? 'A enviar...' : rotuloBotao}
              </button>
            )}

            {resultado && (
              <div className={`feedback ${acertou ? 'ok' : 'erro'}`}>
                {acertou ? '✅' : resultado.status === 'bloqueado' ? '⚠️' : '❌'} {resultado.mensagem}
                {resultado.xp_ganho > 0 && ` +${resultado.xp_ganho} XP`}
                {licao.tipo === 'PRATICA' && resultado.saida && <pre>Saída do seu código:{'\n'}{resultado.saida}</pre>}
              </div>
            )}
          </section>
        )}
        
      </div>
    </main>
  );
}