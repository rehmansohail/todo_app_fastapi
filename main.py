from fastapi import FastAPI
from routes.todo import router as todo_router
from routes.auth import router as auth_router
from contextlib import asynccontextmanager
from database import create_db_and_tables
from limiter import limiter

from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.state.limiter = limiter

app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

app.include_router(todo_router)
app.include_router(auth_router)


