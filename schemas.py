from pydantic import BaseModel, Field
from datetime import date
from pydantic import EmailStr
from typing import Optional

class ToDO(BaseModel):

    title: str = Field(min_length=7, max_length=50)
    description: str = Field(min_length=30, max_length=100)
    target_date: date
    is_complete: bool = False
    # Note: owner_id will be set from the logged-in user, not from request

class UpdateTodo(BaseModel):
    title: str = Field(min_length=7, max_length=50)
    description: str = Field(min_length=30, max_length=100)
    is_complete: bool = False

class CreateUser(BaseModel):
    name: str = Field(min_length=10, max_length=20)
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr

class TokenData(BaseModel):
    id: str  # Will store user_id from JWT as string
    
class UpdateTodoStatus(BaseModel):
    is_complete: bool 
