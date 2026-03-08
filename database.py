from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from urllib.parse import quote
from dotenv import load_dotenv
import os
load_dotenv()


password = os.getenv("DATABASE_PASSWORD", " ")
encoded_password = quote(password, safe='')
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:Postgress password1212@@localhost/postgres"  # local fallback
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()