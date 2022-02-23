from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from pydantic import BaseSettings
from fastapi.middleware.cors import CORSMiddleware

# use pydantic for validation.
# class Settings(BaseSettings):
#     database_password: str = "localhost"
#     database_username: str = "alan"
#     secret_key: str = "secretKey"

# command that tells sqlalchemy to create the table.
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins=origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message":"Hello"}


