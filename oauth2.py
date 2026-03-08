from datetime import datetime, timedelta, timezone
import jwt
import schemas
from jose import JWTError,jwt
# from jwt.exceptions import PyJWTError
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
import database
import models
from dotenv import load_dotenv
import os

load_dotenv()

oauth_schem = OAuth2PasswordBearer(tokenUrl="login")

secret_key: str = os.getenv("JWT_SECRET_KEY")
algorithm: str = "HS256"
access_token_expire_minutes: int = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=access_token_expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])  # ✅ Fixed
        user_id = payload.get("user_id")
        if user_id is None:
            raise credentials_exception

        # Convert user_id to string for TokenData
        token_data = schemas.TokenData(id=str(user_id))
    except JWTError:
        raise credentials_exception
    return token_data


# def get_current_user(token: str = Depends(oauth_schem)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"}  # ✅ Fixed typo
#     )
#     return verify_access_token(token, credentials_exception)

#  upto above the get_current_user function is doing nothing but just returning verify_access_token function
#  we can make it more useable if we make it return the current user. we do it as under:


def get_current_user(token: str = Depends(oauth_schem), db: Session = Depends(database.get_db) ):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}  # ✅ Fixed typo
    )
    token_data = verify_access_token(token, credentials_exception)

    # Convert string id to integer for database query
    try:
        user_id = int(token_data.id)
    except (ValueError, TypeError):
        raise credentials_exception

    user = db.query(models.User).filter(models.User.id == user_id).first()

    # If user doesn't exist (was deleted), raise exception
    if user is None:
        raise credentials_exception

    return user
