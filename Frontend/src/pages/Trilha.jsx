import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Pagina from '../components/Pagina';
import PainelUsuario from '../components/PainelUsuario';
import { chamarApi, limparSessao, obterUsuarioId } from '../api';
import './Trilha.css';

const POSICOES_ZIGZAG = [0, 45, 75, 45, 0, -45, -75, -45];

// Mapeamento com os títulos oficiais da nossa trilha
const NOMES_MODULOS = {
  1: "Primeiros Comandos",
  2: "Operadores Aritméticos",
  3: "Utilizando Módulos",
  4: "Manipulando Textos",
  5: "Condições Básicas",
  6: "Condições Aninhadas",
  7: "Estrutura de Repetição FOR",
  8: "Estrutura de Repetição WHILE",
  9: "Interrompendo Repetições",
  10: "Variáveis Compostas - Tuplas",
  11: "Variáveis Compostas - Listas",
  12: "Variáveis Compostas - Listas Parte 2",
  13: "Variáveis Compostas - Dicionários",
  14: "Funções Parte 1",
  15: "Funções Parte 2"
};

export default function Trilha() {
  const [licoes, setLicoes] = useState([]);
  const [usuario, setUsuario] = useState(null);
  const [concluidas, setConcluidas] = useState([]); // ids das lições que o aluno já concluiu
  const [carregando, setCarregando] = useState(true);
  const [erro, setErro] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const usuarioId = obterUsuarioId();
    if (!usuarioId) {
      navigate('/');
      return;
    }

    async function carregarTrilha() {
      try {
        const [listaLicoes, dadosUsuario] = await Promise.all([
          chamarApi('/licoes'),
          chamarApi(`/usuarios/${usuarioId}`),
        ]);
        setLicoes(listaLicoes);
        setUsuario(dadosUsuario);

        // O progresso é um extra: se a rota falhar, o mapa funciona sem as marcações de "concluída".
        chamarApi(`/usuarios/${usuarioId}/progresso`).then(setConcluidas).catch(() => {});
      } catch (e) {
        if (e.status === 404) {
          // A conta não existe mais (ex.: banco recriado): volta para o login
          limparSessao();
          navigate('/');
          return;
        }
        setErro(e.message);
      } finally {
        setCarregando(false);
      }
    }
    carregarTrilha();
  }, [navigate]);

  // Descobre quais módulos existem no banco (ex: [1, 2])
  const modulos = [...new Set(licoes.map((l) => l.id_modulo))];

  return (
    <Pagina largura={640}>
      {carregando && <p className="aviso-pagina">Carregando mapa...</p>}
      {!carregando && erro && <p className="aviso-pagina">{erro}</p>}

      {!carregando && !erro && (
        <div className="painel-vidro" id="trilha">
          <PainelUsuario usuario={usuario} />

          {/* Desenha cada módulo separado */}
          {modulos.map((numeroModulo) => {
            const licoesDoModulo = licoes.filter((l) => l.id_modulo === numeroModulo);
            // Etapas únicas dentro deste módulo (cada uma é uma "bolinha" do mapa)
            const etapasDoModulo = [...new Set(licoesDoModulo.map((l) => l.id_etapa))];

            return (
              <section key={`modulo-${numeroModulo}`} className="modulo-trilha">
                {/* Aqui está a mágica: puxando o nome do dicionário pelo número do módulo! */}
                <h2 className="titulo-modulo">
                  Módulo {numeroModulo}: {NOMES_MODULOS[numeroModulo] || "Título"}
                </h2>

                {etapasDoModulo.map((numeroDaEtapa, index) => {
                  const deslocamentoEixoX = POSICOES_ZIGZAG[index % POSICOES_ZIGZAG.length];

                  // A última etapa do módulo é o teste final
                  const ehTesteFinal = index === etapasDoModulo.length - 1;

                  // Etapa concluída = todas as lições dela estão no progresso do aluno
                  const idsDaEtapa = licoesDoModulo.filter((l) => l.id_etapa === numeroDaEtapa).map((l) => l.id);
                  const concluida = idsDaEtapa.length > 0 && idsDaEtapa.every((id) => concluidas.includes(id));

                  const classes = ['botao-circular', ehTesteFinal && 'final', concluida && 'concluida']
                    .filter(Boolean)
                    .join(' ');
                  const nomeDaEtapa = ehTesteFinal ? 'Teste Final' : `Etapa ${numeroDaEtapa}`;

                  return (
                    <div
                      key={`bolinha-${numeroModulo}-${numeroDaEtapa}`}
                      className="no-trilha"
                      style={{ transform: `translateX(${deslocamentoEixoX}px)` }}
                    >
                      <button
                        type="button"
                        className={classes}
                        aria-label={concluida ? `${nomeDaEtapa} (concluída)` : nomeDaEtapa}
                        // Envia o módulo e a etapa para a tela de lição
                        onClick={() => navigate('/licao', { state: { etapa: numeroDaEtapa, modulo: numeroModulo } })}
                      >
                        {ehTesteFinal ? '🏆' : concluida ? '✔' : '⭐'}
                      </button>
                      <span className="titulo-licao">{nomeDaEtapa}</span>
                    </div>
                  );
                })}
              </section>
            );
          })}
        </div>
      )}
    </Pagina>
  );
}