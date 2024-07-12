# from typing import Optional, List
from fastapi import FastAPI  #Response, status, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

#from fastapi.params import Body
#from pydantic import BaseModel
#from random import randrange
# from sqlalchemy.orm import Session
from . import models    #schemas, utils
from .database import engine   # get_db
from .routers import post, user, auth, vote
from .config import settings

#setting for password hashing - hashing algorythm bcrypt

# models.Base.metadata.create_all(bind=engine) no longer needed since alembic does all

app = FastAPI()

# origins = ["https://www.google.com"] # domains that can talk to our API

origins = ["*"]

app.add_middleware(
    CORSMiddleware, # middleware is a function that runs before every request
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},  {
#     "title": "favorite foods", "content": "I like pizza", "id": 2
# }]


# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p


# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p["id"] == id:
#             return i

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def read_root():
    return {"Hello": "Olga"}
