
# To-do List

Aplicação para criar e gerenciar tarefas simples.


## Funcionalidades

### Done
- Criar tarefa
- Visualizar lista de tarefas
- Visualizar detalhes de tarefas
- Editar tarefa
- Deletar tarefa
- Pesquisar tarefa
- Cadastrar usuário
- Login
- Logout
- Visualizar perfil
- Editar perfil
- Excluir perfil

Backlog
- Alterar Senha


## Aprendizados Aplicados

- Configuração de variáveis de ambiente do Flask
- Uso do Jinja na criação das páginas
- Uso do Bootstrap para estilizar as páginas
- Configuração do banco de dados SQLite
- Filtrar itens de uma lista com JavaScript
- Uso do ORM Flask-SQLAlchemy para criar modelos, se conectar ao banco de dado e manipular os objetos
- Uso da biblioteca Flask-Login para fazer login, logout e verificar se o usuário está logado
- Uso ba biblioteca flask_migrate para criação e versionamento do banco de dados


## Rodando Localmente

Clone o projeto

```bash
  git clone https://github.com/kayanerocha/todo-list.git
```

Entre no diretório do projeto

```bash
  cd todo-list
```

Crie o ambiente virtual

```bash
  python -m venv .venv
```

Ative o ambiente virtual

```bash
  .venv\Scripts\activate
```

Instale as bibliotecas

```bash
  pip install -m requirements.txt
```

Configure as variávies de ambiente

```bash
  set FLASK_APP=app
  set FLASK_ENV=development
```

Renomei o arquivo .env.exemple para .env e adicione valores as variáveis de ambiente

```bash
  SECRET_KEY=
  MYSQL_HOST=
  MYSQL_USER=
  MYSQL_PASSWORD=
  MYSQL_PORT=
```

Inicie o banco de dados (Importante ter um banco de dados MySQL local chamado task)

```bash
  flask db init
```

Execute as migrations

```
flask db migrate
flask db upgrade
```

Rode a aplicação

```bash
  python app.py
```


## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

`SECRET_KEY`
`MYSQL_HOST`
`MYSQL_USER`
`MYSQL_PASSWORD`
`MYSQL_PORT`


## Stack Utilizada

**Front-end:** HTML, CSS, JavaScript, Bootstrap e Jinja

**Back-end:** Python, Flask e SQLite

