# Todo App — FastAPI Backend

A REST API backend for a multi-user todo application. Users can register, log in, and manage their own tasks independently. Built with FastAPI and deployed on Render with a cloud PostgreSQL database.

**Live API:** [Click Here](https://todo-app-fastapi-uddf.onrender.com/docs)

> To try the API, first create an account using `/signup`. Then click the **Authorize** button on the top right of the Swagger UI, and paste your username (email), password there and leave the rest of the fields empty. All todo endpoints will then work for your account.

---

## Tech Stack

- **Fastapi** — web framework
- **SQLModel** — ORM (built on SQLAlchemy + Pydantic)
- **PostgreSQL** — database (hosted on Neon)
- **JWT** — authentication via python-jose
- **Slow API** — for rate limiting
- **Pytest** — for writing test cases
- **Docker** — containerization
- **Render** — deployment

---



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



## Environment Variables

| Variable | Description |
|---|---|
| `DATABASE_URL` | PostgreSQL connection string |
| `SECRET_KEY` | Secret key used to sign JWT tokens (Use any string here) |