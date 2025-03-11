from pydantic import BaseModel, EmailStr, Field
from typing_extensions import Annotated
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    owner_id: int
    owner: UserOut

    class config:
        from_attributes = True 

class PostCreate(PostBase):
    pass


class PostOut(BaseModel):
    Post: PostBase
    votes: int

    class config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int]


class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(le=1)]