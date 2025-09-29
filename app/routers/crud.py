import uvicorn
from routers import auth
from sqlmodel import select, update
from fastapi import APIRouter, FastAPI, HTTPException, status, Query
from models import User, UserCreate, UserLogin, UserResponse, Token
from db import SessionDep
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


router = APIRouter()

oauth_scheme = OAuth2PasswordBearer(tokenUrl = "login")

## ENDPOINTS

## CREAR UN USUARIO Y HASHEO DE CONTRASEÑA 
@router.post("/register", response_model = UserResponse)
async def register(
    user_data : UserCreate, 
    session : SessionDep
    ):
    statament = select(User).where(User.username == user_data.username)
    existing_user = session.exec(statament).first()
    if existing_user:
        raise HTTPException(status_code = 400, detail = "El usuario ya existe")

    ## AQUÍ SE HASHEA LA CONTRASEÑA
    hashed_pw = auth.hash_password(user_data.password)

    new_user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_pw
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user

## LOGIN

@router.post("/login", response_model=Token)
async def login(
    user_data: UserLogin,
    session: SessionDep
):
    statement = select(User).where(User.username == user_data.username)
    db_user = session.exec(statement).first()

    if not db_user or not auth.verify_password(user_data.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    token = auth.create_access_tokken({"sub": db_user.username})


    return {"access_token": token, "token_type": "bearer"}