from sqlalchemy.orm import Session

from app import models

def get_todos(db: Session):
    return db.query(models.Todo).all()

def create_todo(db: Session, title: str):
    new_todo = models.Todo(title=title)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

# Similar functions for get_todo_by_id, update_todo, and delete_todo
