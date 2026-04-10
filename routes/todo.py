from fastapi import APIRouter,HTTPException,Query,Depends
from typing import Annotated
from sqlmodel import Session, select
from models.todo import *
from database import get_session
from security import *
from models.user import *

router = APIRouter(tags=["todos"])
SessionDep = Annotated[Session, Depends(get_session)]



@router.post("/todos", response_model=TodoPublic)
def create_todo(todo: TodoCreate, session: SessionDep,current_user: User = Depends(get_current_user)):
    db_todo = Todo(
    **todo.model_dump(),
    user_id=current_user
)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo


@router.get("/todos", response_model=list[TodoPublic])
def read_todos(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
    current_user: User = Depends(get_current_user)
):
    todos = session.exec(select(Todo).where(Todo.user_id==current_user).offset(offset).limit(limit)).all()
    return todos

@router.get("/todos/{todo_id}", response_model=TodoPublic)
def read_todo(todo_id: int, session: SessionDep,current_user: User = Depends(get_current_user)):
    todo = session.exec(select(Todo).where(todo_id==Todo.id, Todo.user_id==current_user)).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, session: SessionDep,current_user: User = Depends(get_current_user)):
    todo = session.exec(select(Todo).where(todo_id==Todo.id, Todo.user_id==current_user)).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    session.delete(todo)
    session.commit()
    return {"message": "Deleted Successfully"}


@router.patch("/todos/{todo_id}", response_model=TodoPublic)
def update_todo(todo_id: int, todo: TodoUpdate, session: SessionDep,current_user: User= Depends(get_current_user)):
    todo_db = session.exec(select(Todo).where(todo_id==Todo.id, Todo.user_id==current_user)).first()
    if not todo_db:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo_data = todo.model_dump(exclude_unset=True)
    todo_db.sqlmodel_update(todo_data)
    session.add(todo_db)
    session.commit()
    session.refresh(todo_db)
    return todo_db
