from enum import Enum

from typing import List, Optional

from pydantic import BaseModel

class Role(str, Enum):
    admin = 'admin'
    user = 'user'

class UserBase(BaseModel):
    username: str
    email: str = None
    full_name: Optional[str] = None
    role : Role = Role.user


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    disabled: bool

    class Config:
        orm_mode = True
