# Service Marketplace API

FastAPI + PostgreSQL + Docker - Sistema de marketplace de serviços com autenticação JWT.

## Setup Rápido

### 1. Clone e configure

```bash
git clone https://github.com/seu-usuario/sso.git
cd sso
```

### 2. Variáveis de ambiente

```bash
cp .env.example .env
```

Edite `.env` com suas credenciais:
```
DATABASE_URL=postgresql://user:password@db:5432/marketplace
SECRET_KEY=sua-chave-secreta-muito-segura
```

### 3. Rodar com Docker

```bash
docker-compose up --build
```

A API estará em `http://localhost:8000`

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Rotas

- `POST /auth/register` - Cadastro de usuário
- `POST /auth/login` - Login (retorna JWT)
- `GET /users` - Listar usuários
- `GET /providers` - Listar fornecedores
- `GET /service_requests` - Pedidos de serviço
- `POST /service_requests` - Criar pedido
- `GET /reviews` - Avaliações

## Stack

- **Backend**: FastAPI + SQLAlchemy
- **Database**: PostgreSQL
- **Auth**: JWT (python-jose)
- **Password**: pbkdf2_sha256
- **ORM**: Alembic (migrations)

## Estrutura

```
app/
├── main.py           # Aplicação FastAPI
├── core/
│   ├── config.py     # Configurações
│   └── security.py   # JWT + Hash
├── models/           # SQLAlchemy models
├── schemas/          # Pydantic schemas
├── routes/           # Endpoints
├── services/         # Lógica de negócio
└── database/         # DB conexão
```

## Ambiente local (sem Docker)

```bash
# 1. Criar venv
python -m venv .venv
.venv\Scripts\activate  # Windows

# 2. Instalar deps
pip install -r requirements.txt

# 3. Variáveis
$env:DATABASE_URL="postgresql://user:password@localhost/marketplace"
$env:SECRET_KEY="sua-chave"

# 4. Rodar
uvicorn app.main:app --reload
```

---

**Pronto!** Faça push para seu GitHub agora. 🚀
