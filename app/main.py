
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import  engine

from .routers import post,user,auth, vote
from pydantic_settings import BaseSettings
from .config import settings

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()    

options = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=options,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Welcome to my API"}





