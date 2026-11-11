import { useNavigate } from 'react-router-dom';
import Botao from '../components/Botao';
import Pagina from '../components/Pagina';
import './Home.css';

// Revisar essa parte
const DIFERENCIAIS = [
  { icone: '📖', titulo: 'Teoria curta', texto: 'Conceitos explicados em poucas linhas, sem enrolação.' },
  { icone: '💻', titulo: 'Prática de verdade', texto: 'Você escreve código Python e vê o resultado na hora.' },
  { icone: '⭐', titulo: 'Jogo de aprender', texto: 'Ganhe XP, mantenha suas vidas e avance pela trilha.' },
];

export default function Home() {
  const navigate = useNavigate();

  return (
    <Pagina largura={860}>
      <section className="painel-vidro home-destaque">
        <img src="/mascote-sem-fundo.png" alt="Mascote PyLearning" className="home-mascote" />

        <div className="home-destaque-texto">
          <h1 className="home-titulo">Aprenda Python jogando</h1>
          <p className="home-subtitulo">
            Lições curtas, exercícios de código e uma trilha para você evoluir no seu ritmo.
          </p>
          <div className="home-acao">
            <Botao texto="Ir para a trilha" variante="sucesso" onClick={() => navigate('/trilha')} />
          </div>
        </div>
      </section>

      <section className="painel-vidro home-sobre" id="sobre">
        <h2>Sobre nós</h2>

        <p>
          O PyLearning é uma plataforma gamificada de ensino de Python, no estilo dos aplicativos de idiomas, criada
          como projeto da disciplina de Análise e Projeto de Sistemas do curso de Ciência da Computação do CEUNSP.
        </p>
        <p>
          Nossa ideia é que aprender a programar seja leve: lições curtas, desafios práticos e uma trilha que mostra
          o quanto você já evoluiu.
        </p>

        <div className="home-cartoes">
          {DIFERENCIAIS.map((item) => (
            <div key={item.titulo} className="home-cartao">
              <span className="home-icone" aria-hidden="true">
                {item.icone}
              </span>
              <h3>{item.titulo}</h3>
              <p>{item.texto}</p>
            </div>
          ))}
        </div>
      </section>
    </Pagina>
  );
}