import { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

import EditorDeCodigo from '../EditorDeCodigo';
import BarraDeProgresso from '../components/BarraDeProgresso';
import Botao from '../components/Botao';
import Pagina from '../components/Pagina';
import PainelUsuario from '../components/PainelUsuario';
import { chamarApi, enviarJson, obterUsuarioId } from '../api';
import './Exercicio.css';

const CODIGO_INICIAL = '# Escreva seu código aqui\n';

const letra = (indice) => String.fromCharCode(65 + indice); // 0 -> A, 1 -> B, ...

export default function Exercicio() {
  const usuarioId = obterUsuarioId();

  const [licoes, setLicoes] = useState([]);
  const [usuario, setUsuario] = useState(null);
  const [carregado, setCarregado] = useState(false);
  const [indice, setIndice] = useState(0);

  const [codigo, setCodigo] = useState(CODIGO_INICIAL); // Lições PRATICA
  const [escolha, setEscolha] = useState(null); // Lições OBJETIVA (letra escolhida)
  const [resultado, setResultado] = useState(null);
  const [enviando, setEnviando] = useState(false);
  const [erro, setErro] = useState('');

  const location = useLocation();
  const navigate = useNavigate();
  const etapaSelecionada = location.state?.etapa || 1;
  const moduloSelecionado = location.state?.modulo || 1;

  useEffect(() => {
    if (!usuarioId) {
      navigate('/');
      return;
    }

    async function carregar() {
      try {
        const [listaLicoes, dadosUsuario] = await Promise.all([
          chamarApi('/licoes'),
          chamarApi(`/usuarios/${usuarioId}`),
        ]);

        // Fica só com as lições da etapa e do módulo escolhidos na trilha
        const licoesDaEtapa = listaLicoes.filter(
          (l) => l.id_etapa === etapaSelecionada && l.id_modulo === moduloSelecionado
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
  }, [etapaSelecionada, moduloSelecionado, usuarioId, navigate]);

  function limparResposta() {
    setResultado(null);
    setEscolha(null);
    setCodigo(CODIGO_INICIAL);
    setErro('');
  }

  function proximaLicao() {
    setIndice((i) => i + 1);
    limparResposta();
  }

  // Devolve as vidas ao aluno e volta para a primeira pergunta da etapa
  async function recomecarLicao() {
    try {
      await chamarApi(`/usuarios/${usuarioId}/resetar-vidas`, { method: 'PUT' });
      setUsuario((atual) => ({ ...atual, vidas: 5 }));
      setIndice(0);
      limparResposta();
    } catch (e) {
      setErro(e.message);
    }
  }

  // Enquanto os dados não chegam, evita ler "licoes[indice]" de uma lista vazia
  if (!carregado || licoes.length === 0 || !usuario) {
    return (
      <Pagina largura={860}>
        <p className="aviso-pagina">
          {!carregado ? 'Carregando...' : erro || `Nenhuma lição encontrada para a Etapa ${etapaSelecionada}.`}
        </p>
      </Pagina>
    );
  }

  const concluido = indice >= licoes.length;

  async function enviar(resposta) {
    setEnviando(true);
    setErro('');
    try {
      const licaoAtual = licoes[indice];
      const dados = await enviarJson('/executar', {
        usuario_id: Number(usuarioId),
        licao_id: licaoAtual.id,
        codigo: resposta,
      });
      setResultado(dados);
      setUsuario((atual) => ({ ...atual, xp: dados.xp_total, vidas: dados.vidas_restantes }));
    } catch (e) {
      setErro(e.message);
    } finally {
      setEnviando(false);
    }
  }

  // --- Etapa concluída ---
  if (concluido) {
    return (
      <Pagina largura={860}>
        <div className="painel-vidro exercicio">
          <PainelUsuario usuario={usuario} />
          <section className="cartao-licao centralizado">
            <h2>🎉 Etapa {etapaSelecionada} concluída!</h2>
            <p>
              Ótimo trabalho! Seu total agora é de <b>{usuario.xp} XP</b>.
            </p>
            <Botao texto="Voltar para a trilha" variante="sucesso" onClick={() => navigate('/trilha')} />
          </section>
        </div>
      </Pagina>
    );
  }

  // --- Lição ativa ---
  const licao = licoes[indice];
  const acertou = resultado?.acertou === true;
  const semVidas = usuario.vidas <= 0; // "Game over"

  const rotuloBotao = { TEORIA: 'Entendi, avançar', OBJETIVA: 'Responder', PRATICA: 'Executar' }[licao.tipo];
  const botaoDesabilitado = enviando || (licao.tipo === 'OBJETIVA' && !escolha);

  function responder() {
    if (licao.tipo === 'TEORIA') return enviar('AVANCAR'); // A API só exige um texto não vazio
    if (licao.tipo === 'OBJETIVA') return enviar(escolha);
    return enviar(codigo);
  }

  const porcentagemProgresso = ((indice + (acertou ? 1 : 0)) / licoes.length) * 100;

  return (
    <Pagina largura={860}>
      <div className="painel-vidro exercicio">
        <PainelUsuario usuario={usuario} />

        <div className="barra-centralizada">
          <BarraDeProgresso porcentagem={porcentagemProgresso} />
        </div>

        <div className="area-exercicio-com-mascote">
          <img src="/mascote-sem-fundo.png" alt="Mascote PyLearning" className="mascote-exercicio" />

          {semVidas ? (
            <section className="cartao-licao centralizado">
              <h2>Você perdeu todas as vidas! 💔</h2>
              <p>Não desanime. A repetição é a chave para aprender Python.</p>
              <Botao texto="Recomeçar lição" variante="primario" onClick={recomecarLicao} />
              {erro && <div className="feedback erro">{erro}</div>}
            </section>
          ) : (
            <section className="cartao-licao" key={`licao-${indice}`}>
              <small className="etapa-rotulo">
                Módulo {licao.id_modulo} · Lição {indice + 1} de {licoes.length}
              </small>
              <h2>{licao.titulo}</h2>
              <p className="enunciado">{licao.enunciado}</p>

              {licao.tipo === 'OBJETIVA' && (
                <div className="opcoes">
                  {licao.opcoes?.map((texto, i) => (
                    <button
                      key={letra(i)}
                      type="button"
                      className={`opcao ${escolha === letra(i) ? 'selecionada' : ''}`}
                      onClick={() => setEscolha(letra(i))}
                      disabled={acertou || enviando}
                    >
                      <b className="opcao-letra">{letra(i)}</b>
                      <span>{texto}</span>
                    </button>
                  ))}
                </div>
              )}

              {licao.tipo === 'PRATICA' && <EditorDeCodigo value={codigo} onChange={setCodigo} />}

              {acertou ? (
                <Botao texto="Próxima →" variante="sucesso" onClick={proximaLicao} />
              ) : (
                <Botao
                  texto={enviando ? 'Enviando...' : rotuloBotao}
                  variante="primario"
                  onClick={responder}
                  desabilitado={botaoDesabilitado}
                />
              )}

              {resultado && (
                <div className={`feedback ${acertou ? 'ok' : 'erro'}`}>
                  {acertou ? '✅' : resultado.status === 'bloqueado' ? '⚠️' : '❌'} {resultado.mensagem}
                  {resultado.xp_ganho > 0 && ` +${resultado.xp_ganho} XP`}
                  {licao.tipo === 'PRATICA' && resultado.saida && (
                    <pre>
                      Saída do seu código:{'\n'}
                      {resultado.saida}
                    </pre>
                  )}
                </div>
              )}

              {erro && <div className="feedback erro">{erro}</div>}
            </section>
          )}
        </div>
      </div>
    </Pagina>
  );
}