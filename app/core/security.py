import os, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jwt import InvalidTokenError, ExpiredSignatureError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

pwd = CryptContext(schemes=["argon2"], deprecated="auto")

JWT_SECRET = os.getenv("JWT_SECRET", "change-me")
JWT_ALG = os.getenv("JWT_ALG", "HS256")
JWT_EXPIRE_MIN = 60 * 24

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def hash_password(p: str) -> str:
    return pwd.hash(p)

def verify_password(p: str, hp: str) -> bool:
    return pwd.verify(p, hp)

def create_token(user_id: int) -> str:
    payload = {"sub": str(user_id),
               "exp": datetime.now(timezone.utc) + timedelta(minutes=JWT_EXPIRE_MIN)}
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALG)

def decode_token(t: str) -> int:
    try:
        data = jwt.decode(t, JWT_SECRET, algorithms=[JWT_ALG])
        return int(data["sub"])
    except ExpiredSignatureError:
        raise InvalidTokenError("Token has expired")
    except InvalidTokenError:
        raise InvalidTokenError("Invalid token")

def get_current_user_id(token: str = Depends(oauth2_scheme)) -> int:
    try:
        return decode_token(token)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )
