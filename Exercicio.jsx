import { useEffect, useState } from 'react';
// 1. Mudamos o caminho para achar a pasta components
import EditorDeCodigo from '../EditorDeCodigo'; 
// 2. Mudamos o caminho para achar o App.css na pasta raiz (se você não usar App.css, pode apagar essa linha)
import '../App.css'; 
import BarraDeProgresso from '../components/BarraDeProgresso';

const API_URL = 'http://127.0.0.1:8000/api';
// Se tiver alguém logado, pega o ID. Se for null, usa o ID 1 (Aluno Teste) por segurança.
const USUARIO_ID = localStorage.getItem('usuario_id') || 1;
const CODIGO_INICIAL = '# Escreva seu código aqui\n';

const letra = (indice) => String.fromCharCode(65 + indice); 

async function chamarApi(caminho, opcoes) {
  let resposta;
  try {
    resposta = await fetch(`${API_URL}${caminho}`, opcoes);
  } catch {
    throw new Error('Não foi possível conectar ao servidor. O backend está rodando em http://127.0.0.1:8000?');
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

// 3. O nome da função principal muda de App para Exercicio

export default function Exercicio() {
  const [licoes, setLicoes] = useState([]);
  const [usuario, setUsuario] = useState(null);
  const [carregado, setCarregado] = useState(false);
  const [indice, setIndice] = useState(0);

  const [codigo, setCodigo] = useState(CODIGO_INICIAL); // Lições PRATICA
  const [escolha, setEscolha] = useState(null);         // Lições OBJETIVA (letra)
  const [resultado, setResultado] = useState(null);
  const [enviando, setEnviando] = useState(false);
  const [erro, setErro] = useState('');
  const [ranking, setRanking] = useState([]);

  const licao = licoes[indice];
  const concluido = licoes.length > 0 && indice >= licoes.length;

  // Ao abrir a página: busca as lições e os dados do aluno.
  useEffect(() => {
    async function carregar() {
      try {
        const [listaLicoes, dadosUsuario] = await Promise.all([
          chamarApi('/licoes'),
          chamarApi(`/usuarios/${USUARIO_ID}`),
        ]);
        setLicoes(listaLicoes);
        setUsuario(dadosUsuario);
      } catch (e) {
        setErro(e.message);
      } finally {
        setCarregado(true);
      }
    }
    carregar();
  }, []);

  // Ao terminar todas as lições: busca o ranking.
  useEffect(() => {
    if (!concluido) return;
    chamarApi('/ranking').then(setRanking).catch((e) => setErro(e.message));
  }, [concluido]);

  async function enviar(resposta) {
    setEnviando(true);
    setErro('');
    try {
      const dados = await chamarApi('/executar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ usuario_id: USUARIO_ID, licao_id: licao.id, codigo: resposta }),
      });
      setResultado(dados);
      setUsuario((atual) => ({ ...atual, xp: dados.xp_total, vidas: dados.vidas_restantes }));
    } catch (e) {
      setErro(e.message);
    } finally {
      setEnviando(false);
    }
  }

  function proximaLicao() {
    setIndice((i) => i + 1);
    setResultado(null);
    setEscolha(null);
    setCodigo(CODIGO_INICIAL);
    setErro('');
  }

  // Telas de carregamento / erro / banco vazio
  if (!carregado || licoes.length === 0 || !usuario) {
    return (
      <main className="app">
        <p>{!carregado ? 'Carregando...' : erro || 'Nenhuma lição cadastrada. Rode "python seed.py" no backend.'}</p>
      </main>
    );
  }

  const topo = (
    <header className="topo">
      <span>Olá, {usuario.nome}!</span>
      <span className="status">
        <span>⭐ {usuario.xp} XP</span>
        <span>❤️ {usuario.vidas}</span>
      </span>
    </header>
  );

  // Tela final
  if (concluido) {
    return (
      <main className="app">
        {topo}
        <section className="cartao">
          <h2>🎉 Você concluiu todas as lições!</h2>
          <p>Seu total: {usuario.xp} XP.</p>
          <h3>Ranking</h3>
          <ol className="ranking">
            {ranking.map((item) => (
              <li key={item.nome}>
                {item.nome} — {item.xp} XP
              </li>
            ))}
          </ol>
          {erro && <div className="feedback erro">{erro}</div>}
        </section>
      </main>
    );
  }

  // Tela de uma lição
  const acertou = resultado?.acertou === true;
  const semVidas = usuario.vidas <= 0;

  const rotuloBotao = { TEORIA: 'Entendi, avançar', OBJETIVA: 'Responder', PRATICA: 'Executar' }[licao.tipo];
  const botaoDesabilitado = enviando || semVidas || (licao.tipo === 'OBJETIVA' && !escolha);

  function responder() {
  if (licao.tipo === 'TEORIA') return enviar('AVANCAR');
  if (licao.tipo === 'OBJETIVA') return enviar(escolha);
  return enviar(codigo);
}

const porcentagemProgresso = ((indice + (acertou ? 1 : 0)) / licoes.length) * 100

  
  return (
    <main className="app">
      {topo}
        <div style={{ maxWidth: '600px', margin: '0 auto', width: '100%' }}>
        <BarraDeProgresso porcentagem={porcentagemProgresso} />
      </div>
      <section className="cartao">
        <small className="etapa">
          Módulo {licao.id_modulo} · Lição {indice + 1} de {licoes.length}
        </small>
        <h2>{licao.titulo}</h2>
        <p className="enunciado">{licao.enunciado}</p>

        {licao.tipo === 'OBJETIVA' && (
          <div className="opcoes">
            {licao.opcoes.map((texto, i) => (
              <button
                key={letra(i)}
                className={`opcao ${escolha === letra(i) ? 'selecionada' : ''}`}
                onClick={() => setEscolha(letra(i))}
                disabled={acertou || enviando || semVidas}
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
            {enviando ? 'Enviando...' : rotuloBotao}
          </button>
        )}

        {resultado && (
          <div className={`feedback ${acertou ? 'ok' : 'erro'}`}>
            {acertou ? '✅' : resultado.status === 'bloqueado' ? '⚠️' : '❌'} {resultado.mensagem}
            {resultado.xp_ganho > 0 && ` +${resultado.xp_ganho} XP`}
            {licao.tipo === 'PRATICA' && resultado.saida && <pre>Saída do seu código:{'\n'}{resultado.saida}</pre>}
          </div>
        )}

        {semVidas && <div className="feedback erro">💔 Você ficou sem vidas. Volte mais tarde!</div>}
        {erro && <div className="feedback erro">{erro}</div>}
      </section>
    </main>
  );
}
