from pydantic import BaseModel, EmailStr, field_validator
from sqlmodel import SQLModel, Field, Relationship, Session
from datetime import datetime, timedelta
from typing import Optional
from enum import Enum

## username
## email
## hashed_password


class User(SQLModel, table = True):
    id : int | None = Field(default = None, primary_key = True)
    username : str = Field(default = None)
    email : EmailStr = Field(default = None)
    hashed_password : str
    created_at : datetime = Field(default_factory=datetime.utcnow)

class UserCreate(SQLModel):
    username : str
    email : EmailStr
    password : str

class UserLogin(SQLModel):
    username : str
    password : str

class UserResponse(SQLModel):
    id: int
    username: str
    email: EmailStr

class Config:
    orm_mode = True