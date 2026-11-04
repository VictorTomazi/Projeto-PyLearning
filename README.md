# Projeto-PyLearning
Arquivos para o Projeto PyLearning


1. Preparando o Terreno no PyCharm/VsCode

Abra o editor de código e crie um Novo Projeto (ele já vai criar aquele ambiente virtual venv automático para você).

Dentro da pasta do projeto, crie 5 arquivos vazios com os nomes exatos: database.py, models.py, sandbox.py, main.py e requirements.txt.

Copie os códigos que estão nesse repositório e cole dentro de seus respectivos arquivos.

Cole também aquela pequena lista dos "requirements" dentro do requirements.txt.

2. Instalando o Motor (Dependências)

Abra a aba Terminal no editor de código.

Digite o comando: pip install -r requirements.txt e dê Enter. Ele vai baixar o FastAPI, o SQLAlchemy e o conector do Postgres para o projeto.

3. Ligando o Banco de Dados
Como estamos usando PostgreSQL real, você precisa dele rodando no seu PC:

Baixe a versão mais atual do PostgreSQL no site oficial.

Abra o pgAdmin (o gerenciador do PostgreSQL).

Clique com o botão direito em "Databases" -> Create -> Database...

(Caso tenha problema nessa parte, siga esse manual:

Olhe para o painel da esquerda do pgAdmin (na aba chamada Browser / Navegador).

Clique no ícone de seta ao lado da opção Servers para expandir.

Se ele pedir uma senha master logo de cara, digite a senha que você definiu ao abrir o pgAdmin pela primeira vez (ou crie uma, se ele solicitar).

Em seguida, clique na seta ao lado do servidor principal (geralmente se chama PostgreSQL 16, PostgreSQL 15 ou PostgreSQL 17, dependendo da versão que você instalou).

Nota: Aqui o pgAdmin vai pedir a senha do usuário postgres que você criou durante a instalação do PostgreSQL. Digite a senha para conectar.

Agora que o servidor expandiu, a pasta Databases (ou Bancos de dados) vai aparecer logo abaixo dele!

Clique com o botão direito em cima de Databases > selecione Create > Database... (ou Criar > Banco de Dados...).

)

Nomeie exatamente como plataforma_python e salve.

Dica: Vá no código do database.py e confira se a linha de conexão (postgresql://...) está com o seu usuário e senha corretos do seu banco local (geralmente é postgres e a senha que você criou quando instalou).

4. Rodando a API

No editor de código, abra o arquivo main.py e clique no botão verde de Play (ou digite python main.py no terminal).

O servidor vai ligar! Ele criará automaticamente as tabelas no seu banco de dados vazio.

5. Testando como um Usuário
O FastAPI cria uma tela visual para você testar a API sem precisar programar uma linha de HTML.

Abra o seu navegador e acesse: [http://127.0.0.1:8000/docs]

Você verá a interface do Swagger. Vai ter uma caixinha lá com a sua rota /api/executar.

Rode o seguinte comando INSERT no pgAdmin para criar um aluno falso e uma lição de teste:

[
INSERT INTO usuarios (nome, email, senha) VALUES ('Aluno Teste', 'aluno@teste.com', 'hash-qualquer');

INSERT INTO licoes (titulo, enunciado, gabarito_saida) VALUES ('Olá, mundo', 'Imprima: Olá, mundo!', 'Olá, mundo!');
]

Depois, volte no navegador, clique em "Try it out", e clique em Execute!
