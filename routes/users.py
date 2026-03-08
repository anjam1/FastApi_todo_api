from fastapi import APIRouter, Depends, status, HTTPException
from database import get_db
from schemas import CreateUser, UserOut
from sqlalchemy.orm import Session
import models
from utils import hash

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserOut)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    # check if the user name is occupied or not
    name_lower = user.name.lower()
    existing_user = db.query(models.User).filter(
          models.User.name == name_lower
      ).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
          )
    hash_password = hash(user.password)
    user.password = hash_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user




