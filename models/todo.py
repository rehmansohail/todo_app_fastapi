from sqlmodel import SQLModel,Field
from pydantic import Field as PydanticField

class TodoCreate(SQLModel):
    title: str = PydanticField(min_length=1)
    description: str | None = None
    completed: bool=False

class Todo(TodoCreate, table=True):
    id: int | None = Field(default=None, primary_key=True)
    
class TodoPublic(TodoCreate):
    id:int

class TodoUpdate(SQLModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None

