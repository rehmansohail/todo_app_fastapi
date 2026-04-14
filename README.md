# Todo App — FastAPI Backend

A REST API backend for a multi-user todo application. Users can register, log in, and manage their own tasks independently. Built with FastAPI and deployed on Render with a cloud PostgreSQL database.

**Live API:** [Click Here](https://todo-app-fastapi-uddf.onrender.com/docs)

> To try the API, first create an account using `/signup`. Then click the **Authorize** button on the top right of the Swagger UI, and paste your username (email), password there and leave the rest of the fields empty. All todo endpoints will then work for your account.

---

## Features

- **JWT Authentication** — secure login/signup using `python-jose`, each user's todos are completely isolated from others
- **Full CRUD for Todos** — create, read, update and delete tasks via `SQLModel` and `PostgreSQL`
- **Rate Limiting** — all endpoints are limited to 20 requests/minute using `slowapi` to prevent spam
- **Tests** — auth and todo flows covered using `pytest` and FastAPI's `TestClient` with a separate SQLite test database
- **Dockerised** — includes a `Dockerfile` for easy local setup and deployment
- **Cloud Deployed** — hosted on Render with a Neon PostgreSQL database

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Database ORM | SQLModel + SQLAlchemy |
| Database | PostgreSQL (Neon) |
| Authentication | JWT via python-jose, passwords hashed with passlib bcrypt |
| Rate Limiting | SlowAPI |
| Testing | Pytest + FastAPI TestClient |
| Server | Uvicorn |
| Deployment | Render (Docker) |

---

## Project Structure

```
todo_app_fastapi/
├── models/
│   ├── todo.py        # Todo schemas and table definition
│   └── user.py        # User schemas and table definition
├── routes/
│   ├── todo.py        # CRUD endpoints for todos
│   └── auth.py        # Signup and login endpoints
├── tests/
│   ├── conftest.py    # Test fixtures, test database setup
│   ├── test_auth.py   # Auth flow tests
│   └── test_todo.py   # Todo CRUD tests
├── main.py            # App entry point, middleware setup
├── database.py        # Database connection and session
├── security.py        # JWT logic, password hashing, current user dependency
├── limiter.py         # Rate limiter setup
└── Dockerfile
```

## Running Locally

### With Docker (recommended)

Make sure Docker is installed, then:

```bash
git clone https://github.com/rehmansohail/todo_app_fastapi
cd todo_app_fastapi
```

Create a `.env` file in the project root:

DATABASE_URL=your_postgresql_url  
SECRET_KEY=your_secret_key

Then build and run:

```bash
docker build -t todo-app .
docker run -p 8000:8000 --env-file .env todo-app
```

Visit [http://localhost:8000/docs](http://localhost:8000/docs)

---

### Without Docker

```bash
git clone https://github.com/rehmansohail/todo_app_fastapi
cd todo_app_fastapi
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file:

DATABASE_URL=your_postgresql_url  
SECRET_KEY=your_secret_key

Then run:

```bash
uvicorn main:app --reload
```

Visit [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Running Tests

```bash
pytest tests/
```

Tests use a separate SQLite database and do not touch your production database.

---

## What's Next

This is a backend-only project right now, but there's a lot of room to grow:

- **Frontend** — a proper UI so users don't have to interact through Swagger
- **Task filtering** — sort and filter todos by completion status
- **Timestamps** — track when a task was created and when it was completed
- **AI integration** — let users ask for help on a specific task without leaving the app

A simple todo list can be made remarkably powerful with the right features. If any of these interest you, fork the repo, build it out, and open a pull request — if the feature is solid I'll merge it in.

---

## Environment Variables

| Variable | Description |
|---|---|
| `DATABASE_URL` | PostgreSQL connection string |
| `SECRET_KEY` | Secret key used to sign JWT tokens (Use any string here) |