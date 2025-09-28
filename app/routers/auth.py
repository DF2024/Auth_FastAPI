import uvicorn
from sqlmodel import select, update
from fastapi import APIRouter, FastAPI, HTTPException, status, Query
from models import UserBase, UserCreate, User
from db import SessionDep

router = APIRouter()


@router.get("/user")
async def user():
    return {"messege" : "Prueba"}