from fastapi import FastAPI, Depends

from rp_poetry import crud, schemas

app = FastAPI()

@app.get("/todos", response_model=List[schemas.Todo])
def get_todos(db: Session = Depends(get_db)):
    return crud.get_todos(db)

@app.post("/todos", response_model=schemas.Todo)
def create_todo(title: str, db: Session = Depends(get_db)):
    return crud.create_todo(db, title)

# Similar endpoints for get_todo_by_id, update_todo, and delete_todo using appropriate HTTP methods and response models
