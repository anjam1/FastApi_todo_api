from fastapi import APIRouter, status, HTTPException, Depends
from database import get_db
from schemas import ToDO, UpdateTodo, UpdateTodoStatus
from sqlalchemy.orm import Session
import models
import oauth2
router = APIRouter(
    prefix="/todos",
    tags=['To Dos']
)

@router.get("/")
def get_todos(db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    # Only return todos belonging to the logged-in user
    todos = db.query(models.Todos).filter(models.Todos.owner_id == current_user.id).all()
    return todos


@router.get("/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    todo = db.query(models.Todos).filter(
        models.Todos.id == todo_id,
        models.Todos.owner_id == current_user.id
    ).first()
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                           detail=f"Todo with id: {todo_id} not found")
    return todo

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_todo(todo: ToDO, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    # Add owner_id from the logged-in user
    todo_data = todo.dict()
    todo_data['owner_id'] = current_user.id
    new_todo = models.Todos(**todo_data)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    todo = db.query(models.Todos).filter(
        models.Todos.id == todo_id,
        models.Todos.owner_id == current_user.id
    ).first()
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                           detail=f"Todo with id: {todo_id} not found")
    db.delete(todo)
    db.commit()
    return

@router.put("/{todo_id}")
def update_todo(todo_id: int, updated_todo: UpdateTodo, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    todo_query = db.query(models.Todos).filter(
        models.Todos.id == todo_id,
        models.Todos.owner_id == current_user.id
    )
    todo = todo_query.first()

    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                           detail=f"Todo with id {todo_id} not found")

    todo_query.update(updated_todo.dict(), synchronize_session=False)
    db.commit()
    db.refresh(todo)
    return todo

@router.patch("/{todo_id}/status")
def update_todo_status(todo_id: int, status_update: UpdateTodoStatus, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    todo_query = db.query(models.Todos).filter(
        models.Todos.id == todo_id,
        models.Todos.owner_id == current_user.id
    )
    todo = todo_query.first()

    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                           detail=f"Todo with id {todo_id} not found")

    todo_query.update(status_update.dict(), synchronize_session=False)
    db.commit()
    db.refresh(todo)
    return todo