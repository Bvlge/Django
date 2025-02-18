# Meu Projeto Django

Este é um projeto Django configurado com Pipenv para gerenciamento de dependências e ambiente virtual.

## 🚀 Tecnologias Utilizadas

- Python 3
- Django
- Pipenv (gerenciamento de dependências)

## 📌 Requisitos

Antes de começar, certifique-se de ter instalado:

- [Python 3](https://www.python.org/downloads/)
- [Pipenv](https://pipenv.pypa.io/en/latest/)

## 📦 Instalação

Clone este repositório e acesse o diretório do projeto:

```sh
git clone https://github.com/seu-usuario/meu_projeto_django.git
cd meu_projeto_django
```

Crie o ambiente virtual e instale as dependências:

```sh
pipenv install
```

Ative o ambiente virtual:

```sh
pipenv shell
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

## 📂 Estrutura do Projeto

```sh
meu_projeto_django/
│── config/              # Configuração principal do projeto
│── manage.py            # Gerenciador do Django
│── Pipfile              # Gerenciamento de dependências com Pipenv
│── Pipfile.lock         # Versões exatas das dependências
│── README.md            # Documentação do projeto
```

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
