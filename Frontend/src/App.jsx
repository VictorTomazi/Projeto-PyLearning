import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './pages/Login';
import Registro from './pages/Registro';
import Trilha from './pages/Trilha';
import Exercicio from './pages/Exercicio';
import Sobre from './pages/Sobre';
import NaoEncontrada from './pages/NaoEncontrada';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* A página inicial (/) é o Login */}
        <Route path="/" element={<Login />} />

        {/* Rota para criar a conta */}
        <Route path="/registro" element={<Registro />} />

        {/* O mapa de lições */}
        <Route path="/trilha" element={<Trilha />} />

        {/* A tela da lição (teoria, objetiva ou editor de código) */}
        <Route path="/licao" element={<Exercicio />} />

        {/* Página "Sobre nós" (botão do cabeçalho) */}
        <Route path="/sobre" element={<Sobre />} />

        {/* Qualquer outro endereço */}
        <Route path="*" element={<NaoEncontrada />} />
      </Routes>
    </BrowserRouter>
  );
}