# Meu Projeto Django

Este é um projeto Django configurado com Pipenv para gerenciamento de dependências e ambiente virtual.

## 🚀 Tecnologias Utilizadas

- Python 3
- Django

## 📌 Requisitos

Antes de começar, certifique-se de ter instalado:

- [Python 3](https://www.python.org/downloads/)

## 📦 Instalação

Clone este repositório e acesse o diretório do projeto:

```sh
git clone https://github.com/seu-usuario/meu_projeto_django.git
cd meu_projeto_django
```

Crie o ambiente virtual e instale as dependências:

```sh
python -m venv
```

```sh
pip install -r requirements.txt
```

## ⚙️ Configuração do Projeto

Crie as migrações do banco de dados e aplique-as:

```sh
python manage.py migrate
```

Crie um superusuário para acessar o painel de administração:

```sh
python manage.py createsuperuser
```

## 🏃 Executando o Servidor

Para iniciar o servidor de desenvolvimento, execute:

```sh
python manage.py runserver
```

Acesse o projeto no navegador: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


## 🔧 Comandos Úteis

- Criar uma nova aplicação Django:

  ```sh
  python manage.py startapp nome_do_app
  ```

- Rodar as migrações:

  ```sh
  python manage.py makemigrations
  python manage.py migrate
  ```

- Criar um superusuário:

  ```sh
  python manage.py createsuperuser
  ```

## 📜 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usá-lo e modificá-lo! 🚀
