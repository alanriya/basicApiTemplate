from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

# schema defines the structure of a request and a response.
# this ensures that when a user wants to create a post, the request will only go through when it has a certain data in the request. 

# Pydantic Model for the User
class UserCreate(BaseModel):
    email:EmailStr
    password:str

class UserOut(BaseModel):
    email:EmailStr
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Pydantic Model for Post
class PostBase(BaseModel):
    title: str
    content: str
    published: bool=True

class PostCreate(PostBase):
    pass

class Post(PostBase): # inheritance, title, content and published are included.
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config: 
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int
    
    class Config: 
        orm_mode = True

# Pydantic Model for the Token
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
    
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
