from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone
import os
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session
from fastapi import Depends
from database import get_session
from typing import Annotated

SessionDep = Annotated[Session, Depends(get_session)]

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)
SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM="HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def hashPassword(password: str):
    return pwd_context.hash(password)
def verifyPassword(inputPassword: str, storedPassword: str):
    return pwd_context.verify(inputPassword,storedPassword)
def create_access_token(user_id):
    data={
        "sub": str(user_id)
    }
    expire = datetime.now(timezone.utc) + timedelta(hours=1)
    data["exp"]=expire
    token = jwt.encode(data,SECRET_KEY,algorithm=ALGORITHM)
    return token

def get_current_user(session: SessionDep,token:str=Depends(oauth2_scheme)):
    return 2
