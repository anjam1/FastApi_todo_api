from sqlalchemy import String, Boolean, Integer, Date, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from database import Base

class Todos(Base):
    __tablename__ = "To Dos"

    id = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = mapped_column(String, nullable=False)
    description = mapped_column(String, nullable=False)
    target_date = mapped_column(Date, nullable=False)
    is_complete = mapped_column(Boolean, default=False)
    owner_id = mapped_column(Integer, ForeignKey("users.id"), nullable=False)

    # Relationship to User
    owner = relationship("User", back_populates="todos")

    

class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = mapped_column(String, nullable=False)
    email = mapped_column(String, unique=True)
    password = mapped_column(String)

    # Relationship to Todos
    todos = relationship("Todos", back_populates="owner")
    


