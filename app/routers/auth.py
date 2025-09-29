import uvicorn
from sqlmodel import select, update
from fastapi import APIRouter, FastAPI, HTTPException, status, Query
from models import UserBase, UserCreate, User
from db import SessionDep

router = APIRouter()



@router.post("/user", response_model = User, tags = ["Users"])
async def userCreate(user_data : UserCreate, session : SessionDep):
    user = User.model_validate(user_data.model_dump())
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@router.get("/user", response_model = list[User], tags = ["Users"])
async def userList(session : SessionDep):
    statament = select(User)
    result = session.exec(statament)
    user = result.all()
    return user