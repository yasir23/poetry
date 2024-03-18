from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str

class Todo(TodoBase):
    id: int
    completed: bool = False
    class Config:
        orm_mode = True
