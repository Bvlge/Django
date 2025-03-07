# Django REST Module

Este módulo é parte integrante de uma plataforma de controle financeiro baseada em microserviços, implementado com Django e Django REST Framework. Ele fornece endpoints para gerenciamento de usuários, autenticação via JWT, e integração com um microserviço Go para o cálculo de estatísticas financeiras e despesas mensais por categoria.

---

## Índice

- [Objetivo](#objetivo)
- [Principais Funcionalidades](#principais-funcionalidades)
- [Arquitetura e Tecnologias](#arquitetura-e-tecnologias)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Pré-requisitos](#pré-requisitos)
- [Instalação e Configuração](#instalação-e-configuração)
- [Como Executar](#como-executar)
- [Endpoints Disponíveis](#endpoints-dispon%C3%ADveis)
- [Fluxo de Dados e Integração](#fluxo-de-dados-e-integra%C3%A7%C3%A3o)
- [Contribuição](#contribui%C3%A7%C3%A3o)
- [Licença](#licen%C3%A7a)

---

## Objetivo

O módulo Django REST tem como finalidade:
- **Gerenciamento de Usuários e Autenticação:** Permitir o registro, login e consulta do perfil dos usuários utilizando JWT.
- **Integração com Microserviço Go:** Consumir endpoints do microserviço Go para obter estatísticas financeiras e análises de despesas.
- **Gerenciamento de Transações:** Registrar e consultar transações financeiras com detalhamento por categoria, data e tipo (receita ou despesa).

---

## Principais Funcionalidades

1. **Autenticação e Gestão de Usuários**
   - Registro de novos usuários com validação de e-mail e senha.
   - Login e geração de tokens JWT utilizando o pacote `rest_framework_simplejwt`.
   - Consulta do perfil do usuário autenticado e, opcionalmente, consulta de detalhes de usuários específicos.

2. **Gerenciamento de Transações**
   - Criação, leitura, atualização e exclusão (CRUD) de transações financeiras.
   - Associação de cada transação ao usuário autenticado, garantindo o isolamento dos dados.

3. **Integração com Microserviço de Estatísticas (Go)**
   - Endpoints para obter estatísticas financeiras e despesas mensais por categoria.
   - Encaminhamento do token JWT do Django para o microserviço Go, permitindo a continuidade da autenticação e autorização entre os módulos.
   - Tratamento de parâmetros de data para filtragem dos dados financeiros.

---

## Arquitetura e Tecnologias

| **Componente**                | **Tecnologia/Framework**                                           | **Descrição**                                                         |
| ----------------------------- | ------------------------------------------------------------------ | --------------------------------------------------------------------- |
| **Framework Web**             | [Django](https://www.djangoproject.com/)                           | Plataforma para desenvolvimento web com arquitetura MVC.            |
| **API REST**                  | [Django REST Framework](https://www.django-rest-framework.org/)      | Criação de APIs RESTful para comunicação com clientes e serviços.     |
| **Autenticação**              | [JWT](https://github.com/davesque/django-rest-framework-simplejwt)   | Implementação de autenticação baseada em token.                       |
| **Documentação de API**       | [drf_yasg](https://github.com/axnsan12/drf-yasg) e [drf_spectacular](https://drf-spectacular.readthedocs.io/) | Geração de documentação Swagger e Redoc.                              |
| **Integração Externa**        | [Requests](https://docs.python-requests.org/)                        | Comunicação com o microserviço Go para obtenção de estatísticas.        |
| **Banco de Dados**            | PostgreSQL                                                         | Armazenamento dos dados de usuários e transações.                     |
| **CORS**                      | [django-cors-headers](https://github.com/adamchainz/django-cors-headers) | Permite o consumo das APIs por clientes em diferentes domínios.       |

---

## Estrutura do Projeto

```plaintext
config/
├── config/                     # Configurações do projeto Django
│   ├── settings.py             # Configuração geral, JWT, conexão com o microserviço Go, etc.
│   ├── urls.py                 # Definição de rotas principais e documentação da API
│   └── wsgi.py
├── transactions/               # App responsável pelas transações financeiras
│   ├── models.py               # Modelo da transação com categoria, tipo, data e valor
│   ├── serializers.py          # Serializadores para transformar dados de transação
│   ├── views.py                # Endpoints para CRUD e integração com o microserviço Go
│   └── services/
│       └── statistics_services.py  # Serviços para comunicação com o microserviço Go
├── users/                      # App responsável pela gestão de usuários
│   ├── models.py               # Modelo customizado de usuário (CustomUser)
│   ├── serializers.py          # Serializadores para registro e perfil do usuário
│   ├── views.py                # Endpoints para registro, login e consulta de usuário
│   └── urls.py                # Rotas específicas do app de usuários
└── manage.py                   # Script para gerenciamento do projeto Django
```

---

## Pré-requisitos

- **Python 3.8+**  
- **Django 5.1+**  
- **Banco de dados PostgreSQL**  
- Variáveis de ambiente necessárias (ex.: `JWT_SECRET`, `GO_STATISTICS_URL`, `DATABASES`)

---

## Instalação e Configuração

1. **Clone o Repositório**

   ```bash
   git clone https://seurepositorio.com/django-rest-module.git
   cd django-rest-module
   ```

2. **Crie um Ambiente Virtual e Ative-o**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   # ou
   venv\Scripts\activate  # Windows
   ```

3. **Instale as Dependências**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configuração do Ambiente**

   Configure as variáveis de ambiente necessárias (você pode criar um arquivo `.env` ou configurar diretamente no ambiente):

   ```dotenv
   SECRET_KEY=your_secret_key
   JWT_SECRET=your_jwt_secret
   GO_STATISTICS_URL=http://localhost:8080/statistics
   DATABASE_URL=postgres://postgres:123@localhost:5432/bvlgedb
   ```

5. **Realize as Migrações**

   ```bash
   python manage.py migrate
   ```

6. **Crie um Superusuário (Opcional)**

   ```bash
   python manage.py createsuperuser
   ```

---

## Como Executar

1. **Inicie o Servidor de Desenvolvimento**

   ```bash
   python manage.py runserver
   ```

2. **Acesse a Documentação da API**

   - **Swagger:** `http://localhost:8000/api/swagger/`
   - **Redoc:** `http://localhost:8000/api/redoc/`

---

## Endpoints Disponíveis

### Endpoints do Usuário

- **Registro de Usuário**
  - **URL:** `/api/users/register/`
  - **Método:** POST
  - **Descrição:** Registra um novo usuário.

- **Obter Token JWT (Login)**
  - **URL:** `/api/users/token/`
  - **Método:** POST
  - **Descrição:** Autentica o usuário e retorna os tokens de acesso e refresh.

- **Atualizar Token**
  - **URL:** `/api/users/token/refresh/`
  - **Método:** POST
  - **Descrição:** Atualiza o token de acesso.

- **Perfil do Usuário**
  - **URL:** `/api/users/user/`
  - **Método:** GET
  - **Descrição:** Retorna os dados do usuário autenticado.

### Endpoints de Transações e Estatísticas

- **CRUD de Transações**
  - **URL:** `/api/transactions/transactions/`
  - **Métodos:** GET, POST, PUT, PATCH, DELETE
  - **Descrição:** Gerencia as transações financeiras do usuário.

- **Estatísticas Financeiras**
  - **URL:** `/api/transactions/statistics/`
  - **Método:** GET
  - **Parâmetros (Query):** `start_date` (padrão: `1970-01-01`), `end_date`
  - **Descrição:** Consulta o microserviço Go para retornar estatísticas financeiras.

- **Despesas Mensais por Categoria**
  - **URL:** `/api/transactions/statistics/category-expenses/`
  - **Método:** GET
  - **Parâmetros (Query):** `start_date` (padrão: `2023-01-01`), `end_date` (padrão: data atual)
  - **Descrição:** Consulta o microserviço Go para retornar a média mensal e total das despesas agrupadas por categoria.

---

## Fluxo de Dados e Integração

1. **Autenticação e Gerenciamento de Usuários**
   - O usuário realiza o registro e login, recebendo um token JWT.
   - O token é utilizado para acessar endpoints protegidos e identificar o usuário.

2. **Gerenciamento de Transações**
   - Usuários autenticados criam e consultam transações financeiras.
   - Cada transação é associada ao usuário autenticado, garantindo privacidade dos dados.

3. **Integração com o Microserviço Go**
   - Endpoints de estatísticas repassam o token JWT e parâmetros de data para o microserviço Go.
   - O microserviço Go processa os dados e retorna estatísticas financeiras e análises de despesas mensais por categoria, que são então repassadas ao cliente.
---

## Contribuição

Contribuições são sempre bem-vindas! Para contribuir:

1. Faça um fork do repositório.
2. Crie uma branch com a sua feature:  
   ```bash
   git checkout -b minha-feature
   ```
3. Realize suas alterações e faça commits com mensagens claras.
4. Envie suas alterações:  
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request para revisão.

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Este README oferece uma visão abrangente do módulo Django REST para controle financeiro, detalhando sua configuração, execução e integração com o microserviço Go. Caso tenha dúvidas ou sugestões, sinta-se à vontade para abrir uma issue ou entrar em contato.
