import uvicorn

from fastapi import FastAPI, Request
from sqlmodel import select
from routers import auth 
from db import SessionDep, lifespan

app = FastAPI(
    lifespan=lifespan
    )

app.include_router(auth.router)