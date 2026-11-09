// Tudo o que as páginas precisam para falar com o backend fica aqui.
// Assim o endereço da API é trocado em UM lugar só.

// Para testar com o backend rodando no seu computador, crie o arquivo `.env.local`
// na raiz do frontend (ao lado do package.json) com a linha:
//     VITE_API_URL=http://127.0.0.1:8000/api
// e reinicie o `npm run dev`. Sem esse arquivo, usa o backend publicado no Render.
export const API_URL = import.meta.env.VITE_API_URL || 'https://pylearning-backend.onrender.com/api';

/**
 * Chama a API e devolve o JSON. Qualquer falha vira um Error com mensagem pronta
 * para mostrar ao aluno; `erro.status` guarda o código HTTP (ex.: 404, 401).
 */
export async function chamarApi(caminho, opcoes) {
  let resposta;
  try {
    resposta = await fetch(`${API_URL}${caminho}`, opcoes);
  } catch {
    throw new Error(
      'Não foi possível conectar ao servidor. Se ele estiver iniciando, aguarde cerca de 1 minuto e tente novamente.'
    );
  }

  const dados = await resposta.json().catch(() => null);
  if (!resposta.ok) {
    const erro = new Error(
      typeof dados?.detail === 'string'
        ? dados.detail
        : `Erro ${resposta.status} no servidor. Tente novamente em instantes.`
    );
    erro.status = resposta.status;
    throw erro;
  }
  return dados;
}

/** Atalho para enviar um objeto como JSON (POST por padrão). */
export function enviarJson(caminho, corpo, metodo = 'POST') {
  return chamarApi(caminho, {
    method: metodo,
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(corpo),
  });
}

// --- Sessão do aluno (guardada no navegador) ---
const CHAVE_USUARIO = 'usuario_id';
const CHAVE_EMAIL = 'usuario_email';

export const obterUsuarioId = () => localStorage.getItem(CHAVE_USUARIO);
export const obterEmail = () => localStorage.getItem(CHAVE_EMAIL);

/** Chamada no login: guarda o id e o e-mail devolvidos pela API. */
export function salvarSessao({ id, email }) {
  localStorage.setItem(CHAVE_USUARIO, id);
  if (email) localStorage.setItem(CHAVE_EMAIL, email);
}

export function limparSessao() {
  localStorage.removeItem(CHAVE_USUARIO);
  localStorage.removeItem(CHAVE_EMAIL);
}