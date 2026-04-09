from fastapi import FastAPI
from routes.todo import router as todo_router
from routes.auth import router as auth_router
from contextlib import asynccontextmanager
from database import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(todo_router)
app.include_router(auth_router)


