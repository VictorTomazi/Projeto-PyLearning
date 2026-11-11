import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './pages/Login';
import Registro from './pages/Registro';
import Home from './pages/Home';
import Trilha from './pages/Trilha';
import Exercicio from './pages/Exercicio';
import Perfil from './pages/Perfil';
import NaoEncontrada from './pages/NaoEncontrada';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* A página inicial é o Login */}
        <Route path="/" element={<Login />} />

        {/* Rota para criar a conta */}
        <Route path="/registro" element={<Registro />} />

        {/* Home: boas-vindas e "Sobre nós" */}
        <Route path="/home" element={<Home />} />

        {/* O mapa de lições */}
        <Route path="/trilha" element={<Trilha />} />

        {/* A tela da lição */}
        <Route path="/licao" element={<Exercicio />} />

        {/* Perfil: alterar nome e senha */}
        <Route path="/perfil" element={<Perfil />} />

        {/* Qualquer outro endereço */}
        <Route path="*" element={<NaoEncontrada />} />
      </Routes>
    </BrowserRouter>
  );
}