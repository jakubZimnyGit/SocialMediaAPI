import jwt
from . import schemas
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .config import Settings


oath2scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = Settings.SECRET_KEY
ALGORYTHM = Settings.ALGORYTHM
ACCESS_TOKEN_EXPIRE_MINUTES = Settings.ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORYTHM)
    
    return encoded_jwt

def verify_access_token(token: str, credentials_exception):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORYTHM])

        id = payload.get("user_id")

        if not id:
            raise credentials_exception

        token_data = schemas.TokenData(id=id)
    except InvalidTokenError:
        raise credentials_exception
    
    return token_data
def get_current_user(token: str = Depends(oath2scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return verify_access_token(token, credentials_exception) 