import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './pages/Login';
import Registro from './pages/Registro';
import Trilha from './pages/Trilha';
import Exercicio from './pages/Exercicio';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Agora a página inicial (/) é o Login */}
        <Route path="/" element={<Login />} />
        
        {/* Rota para criar a conta */}
        <Route path="/registro" element={<Registro />} />
        
        {/* O mapa de lições foi movido para /trilha */}
        <Route path="/trilha" element={<Trilha />} />
        
        {/* A tela do seu editor de código */}
        <Route path="/licao" element={<Exercicio />} />
      </Routes>
    </BrowserRouter>
  );
}