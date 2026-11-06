import { useNavigate } from 'react-router-dom';
import Botao from '../components/Botao';
import Pagina from '../components/Pagina';
import './Sobre.css';

// ATENÇÃO: os textos abaixo são um modelo. Troque pelo texto de apresentação
// do projeto/equipe antes de entregar o trabalho.
const DIFERENCIAIS = [
  { icone: '📖', titulo: 'Teoria curta', texto: 'Conceitos explicados em poucas linhas, sem enrolação.' },
  { icone: '💻', titulo: 'Prática de verdade', texto: 'Você escreve código Python e vê o resultado na hora.' },
  { icone: '⭐', titulo: 'Jogo de aprender', texto: 'Ganhe XP, mantenha suas vidas e avance pela trilha.' },
];

export default function Sobre() {
  const navigate = useNavigate();

  return (
    <Pagina largura={760}>
      <div className="painel-vidro sobre">
        <h2>Sobre nós</h2>

        <p>
          O PyLearning é uma plataforma gamificada de ensino de Python, no estilo dos aplicativos de idiomas, criada
          como projeto da disciplina de Análise e Projeto de Sistemas do curso de Ciência da Computação do CEUNSP.
        </p>
        <p>
          Nossa ideia é que aprender a programar seja leve: lições curtas, desafios práticos e uma trilha que mostra
          o quanto você já evoluiu.
        </p>

        <div className="sobre-cartoes">
          {DIFERENCIAIS.map((item) => (
            <div key={item.titulo} className="sobre-cartao">
              <span className="sobre-icone" aria-hidden="true">
                {item.icone}
              </span>
              <h3>{item.titulo}</h3>
              <p>{item.texto}</p>
            </div>
          ))}
        </div>

        <div className="sobre-acao">
          <Botao texto="Ir para a trilha" variante="sucesso" onClick={() => navigate('/trilha')} />
        </div>
      </div>
    </Pagina>
  );
}