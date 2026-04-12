from fastapi import APIRouter,HTTPException,Query,Depends,Request
from typing import Annotated
from sqlmodel import Session, select
from models.todo import *
from database import get_session
from security import *
from models.user import *
from limiter import limiter

router = APIRouter(tags=["todos"])
SessionDep = Annotated[Session, Depends(get_session)]

rate_limit="20/minute"

@router.post("/todos", response_model=TodoPublic)
@limiter.limit(rate_limit)
def create_todo(request: Request, todo: TodoCreate, session: SessionDep,current_user: User = Depends(get_current_user)):
    db_todo = Todo(
    **todo.model_dump(),
    user_id=current_user
)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo


@router.get("/todos", response_model=list[TodoPublic])
@limiter.limit(rate_limit)
def read_todos(
    request: Request,
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
    current_user: User = Depends(get_current_user)
):
    todos = session.exec(select(Todo).where(Todo.user_id==current_user).offset(offset).limit(limit)).all()
    return todos

@router.get("/todos/{todo_id}", response_model=TodoPublic)
@limiter.limit(rate_limit)
def read_todo(request: Request, todo_id: int, session: SessionDep,current_user: User = Depends(get_current_user)):
    todo = session.exec(select(Todo).where(todo_id==Todo.id, Todo.user_id==current_user)).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.delete("/todos/{todo_id}")
@limiter.limit(rate_limit)
def delete_todo(request: Request, todo_id: int, session: SessionDep,current_user: User = Depends(get_current_user)):
    todo = session.exec(select(Todo).where(todo_id==Todo.id, Todo.user_id==current_user)).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    session.delete(todo)
    session.commit()
    return {"message": "Deleted Successfully"}


@router.patch("/todos/{todo_id}", response_model=TodoPublic)
@limiter.limit(rate_limit)
def update_todo(request: Request, todo_id: int, todo: TodoUpdate, session: SessionDep,current_user: User= Depends(get_current_user)):
    todo_db = session.exec(select(Todo).where(todo_id==Todo.id, Todo.user_id==current_user)).first()
    if not todo_db:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo_data = todo.model_dump(exclude_unset=True)
    todo_db.sqlmodel_update(todo_data)
    session.add(todo_db)
    session.commit()
    session.refresh(todo_db)
    return todo_db
