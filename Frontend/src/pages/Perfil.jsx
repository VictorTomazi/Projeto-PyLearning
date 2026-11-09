import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Botao from '../components/Botao';
import Pagina from '../components/Pagina';
import { chamarApi, enviarJson, limparSessao, obterEmail, obterUsuarioId } from '../api';
import './Login.css'; // Reaproveita os campos "gamificados" e os avisos de erro/sucesso
import './Perfil.css';

export default function Perfil() {
  const navigate = useNavigate();
  const usuarioId = obterUsuarioId();
  const email = obterEmail(); // Guardado no login; é só exibido, nunca enviado para alteração

  const [nomeAtual, setNomeAtual] = useState(''); // Nome como está salvo no servidor
  const [nome, setNome] = useState(''); // Nome digitado no campo
  const [novaSenha, setNovaSenha] = useState('');
  const [confirmarSenha, setConfirmarSenha] = useState('');
  const [senhaAtual, setSenhaAtual] = useState('');

  const [carregando, setCarregando] = useState(true);
  const [enviando, setEnviando] = useState(false);
  const [erro, setErro] = useState('');
  const [sucesso, setSucesso] = useState('');

  useEffect(() => {
    if (!usuarioId) {
      navigate('/');
      return;
    }

    async function carregar() {
      try {
        const dados = await chamarApi(`/usuarios/${usuarioId}`);
        setNomeAtual(dados.nome);
        setNome(dados.nome);
      } catch (e) {
        if (e.status === 404) {
          // A conta não existe mais: volta para o login
          limparSessao();
          navigate('/');
          return;
        }
        setErro(e.message);
      } finally {
        setCarregando(false);
      }
    }
    carregar();
  }, [usuarioId, navigate]);

  async function salvar(e) {
    e.preventDefault();
    setErro('');
    setSucesso('');

    const nomeLimpo = nome.trim();
    const mudouNome = nomeLimpo !== nomeAtual;
    const mudouSenha = novaSenha !== '';

    if (!nomeLimpo) {
      setErro('O nome não pode ficar vazio.');
      return;
    }
    if (!mudouNome && !mudouSenha) {
      setErro('Você ainda não alterou nada.');
      return;
    }
    if (mudouSenha && novaSenha !== confirmarSenha) {
      setErro('A confirmação da nova senha não confere.');
      return;
    }
    if (!senhaAtual) {
      setErro('Digite sua senha atual para salvar as alterações.');
      return;
    }

    setEnviando(true);
    try {
      // Só envia o que mudou
      const corpo = { senha_atual: senhaAtual };
      if (mudouNome) corpo.nome = nomeLimpo;
      if (mudouSenha) corpo.nova_senha = novaSenha;

      const atualizado = await enviarJson(`/usuarios/${usuarioId}/perfil`, corpo, 'PUT');

      setNomeAtual(atualizado.nome);
      setNome(atualizado.nome);
      setNovaSenha('');
      setConfirmarSenha('');
      setSenhaAtual('');
      setSucesso('Perfil atualizado com sucesso!');
    } catch (e) {
      setErro(e.message); // Ex.: "Senha atual incorreta."
    } finally {
      setEnviando(false);
    }
  }

  return (
    <Pagina largura={560}>
      {carregando ? (
        <p className="aviso-pagina">Carregando perfil...</p>
      ) : (
        <form className="painel-vidro perfil" onSubmit={salvar}>
          <h2>Meu perfil</h2>

          {sucesso && <div className="aviso-formulario sucesso" role="status">{sucesso}</div>}
          {erro && <div className="aviso-formulario erro" role="alert">{erro}</div>}

          {/* 1. Nome de exibição */}
          <div className="grupo-campo">
            <label htmlFor="perfil-nome">Nome de exibição</label>
            <div className="campo-gamificado">
              <div className="campo-icone">👤</div>
              <input
                id="perfil-nome"
                type="text"
                maxLength={150}
                value={nome}
                onChange={(e) => setNome(e.target.value)}
              />
            </div>
          </div>

          {/* 2. E-mail (somente leitura) */}
          <div className="grupo-campo">
            <label htmlFor="perfil-email">Email</label>
            <div className="campo-gamificado somente-leitura">
              <div className="campo-icone">✉️</div>
              <input
                id="perfil-email"
                type="email"
                value={email || 'Indisponível (saia e entre novamente)'}
                readOnly
                disabled
              />
            </div>
            <small className="dica-campo">O email não pode ser alterado.</small>
          </div>

          {/* 3. Senha */}
          <div className="grupo-campo">
            <label htmlFor="perfil-nova-senha">Nova senha</label>
            <div className="campo-gamificado">
              <div className="campo-icone">🔒</div>
              <input
                id="perfil-nova-senha"
                type="password"
                placeholder="Deixe em branco para manter a atual"
                maxLength={128}
                autoComplete="new-password"
                value={novaSenha}
                onChange={(e) => setNovaSenha(e.target.value)}
              />
            </div>
          </div>

          <div className="grupo-campo">
            <label htmlFor="perfil-confirmar-senha">Confirmar nova senha</label>
            <div className="campo-gamificado">
              <div className="campo-icone">🔒</div>
              <input
                id="perfil-confirmar-senha"
                type="password"
                placeholder="Repita a nova senha"
                maxLength={128}
                autoComplete="new-password"
                value={confirmarSenha}
                onChange={(e) => setConfirmarSenha(e.target.value)}
              />
            </div>
          </div>

          <hr className="perfil-separador" />

          {/* Confirmação: vale para qualquer alteração (nome ou senha) */}
          <div className="grupo-campo">
            <label htmlFor="perfil-senha-atual">Senha atual</label>
            <div className="campo-gamificado">
              <div className="campo-icone">🔑</div>
              <input
                id="perfil-senha-atual"
                type="password"
                placeholder="Necessária para salvar as alterações"
                maxLength={128}
                autoComplete="current-password"
                value={senhaAtual}
                onChange={(e) => setSenhaAtual(e.target.value)}
              />
            </div>
          </div>

          <Botao texto={enviando ? 'Salvando...' : 'Salvar alterações'} variante="sucesso" desabilitado={enviando} />
        </form>
      )}
    </Pagina>
  );
}