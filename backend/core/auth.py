import bcrypt
from datetime import datetime, timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from starlette import status
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from dao.user_dao import UserDAO, bcrypt_context

router = APIRouter(prefix='/auth', tags=['auth'])

SECRET_KEY = "qaxcvghu76543qasxcvbnkiytfdyu9876rdcvbht6ygvbhytr456uhvc" 
ALGORITHM = "HS256"
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

class Token(BaseModel):
    access_token: str
    token_type: str

async def authenticate_user(username: str, password: str):
    user = await UserDAO.get_user_for_auth(username)
    if not user:
        return False
    
    try:
        # Ensure 'password' is the plain text from the user
        # Ensure 'user['password']' is the $2b$... string from the DB
        if bcrypt.checkpw(password.encode('utf-8'), user['hashed_password'].encode('utf-8')):
            return user
        return False
    except ValueError as e:
        print(f"Bcrypt error: {e}")
        return False
        
    return user

def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail='Incorrect username or password'
        )
    
    token = create_access_token(user['username'], user['id'], timedelta(minutes=20))
    return {'access_token': token, 'token_type': 'bearer'}

# This is the dependency you use in OTHER files to protect routes
async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid Token')
        return {'username': username, 'id': user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid Token')