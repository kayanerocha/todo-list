
# To-do List

Aplicação para criar e gerenciar tarefas simples.


## Funcionalidades

### Done
- Criar tarefa
- Visualizar lista de tarefas
- Visualizar detalhes de tarefas
- Editar tarefa
- Deletar tarefa

### Backlog
- Pesquisar tarefa
- Cadastrar usuário
- Visualizar perfil
- Editar perfil
- Excluir perfil
- Login
- Logout



## Aprendizados

- Configuração de variáveis de ambiente do Flask
- Uso do Jinja na criação das páginas
- Uso do Bootstrap para estilizar as páginas
- Configuração do banco de dados SQLite



## Rodando Localmente

Clone o projeto

```bash
  git clone https://link-para-o-projeto
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

Renomei o arquivo .env.exemple para .env e adicione uma SECRET_KEY

```bash
  SECRET_KEY=
```

Inicie o banco de dados

```bash
  python init_db.py
```

Rode a aplicação

```bash
  python app.py
```


## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

`SECRET_KEY`


## Stack Utilizada

**Front-end:** HTML, CSS, Bootstrap e Jinja

**Back-end:** Python, Flask e SQLite

