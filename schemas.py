from typing import List
from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str
    name: str = ''
    role: int = 0

class UserInDB(UserCreate):
    id: int

class UserCreateResponse(BaseModel):
    success: bool
    message: str
    user: UserInDB | None

class UserListResponse(BaseModel):
    count: int = 0
    users: List[UserInDB] | None
