import uvicorn
from sqlmodel import select, update
from fastapi import APIRouter, FastAPI, HTTPException, status, Query
from models import User, UserCreate, UserLogin, UserResponse
from db import SessionDep
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


router = APIRouter()

oauth_scheme = OAuth2PasswordBearer(tokenUrl = "login")

## ENDPOINTS

@router.post("/register", response_model = UserResponse)
async def register(user_data : UserCreate, session : SessionDep):
    statament = select(User).where(User.username == user.username)
    existing_user = session.exec(statament).first()
    if existing_user:
        raise HTTPException(status_code = 400, detail = "El usuario ya existe")

    ## AQUÍ SE HASHEA LA CONTRASEÑA
    hashed_pw = auth.hash_password(user.password)
    new_user = User(username= user.username, email = user.email, hashed_password = hashed_pw)
    
    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user


