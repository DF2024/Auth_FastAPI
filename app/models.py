from pydantic import BaseModel, EmailStr, field_validator
from sqlmodel import SQLModel, Field, Relationship, Session
from typing import Optional
from enum import Enum

## username
## email
## hashed_password


class UserBase(SQLModel):
    username : str = Field(default = None)
    email : EmailStr = Field(default = None)
    hashed_password : str = Field(default = None)

class UserCreate(UserBase):
    pass

class User(UserBase, table = True):
    id : int | None = Field(default = None, primary_key = True)
