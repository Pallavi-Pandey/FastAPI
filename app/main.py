from typing import Optional
from fastapi import FastAPI, Body, Response, status, HTTPException, Depends
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas, utils
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import post, user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()



while True:
    try:
        conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres", 
                            password="password", cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesfull !!! ")
        break
    except Exception as error:
        print("Connection to database failed")
        print("Error: ", error)
        time.sleep(2)

my_posts = [{"title": "Post 1", "content": "This is my first post", "id": 1}, 
            {"title": "Post 2", "content": "This is my second post", "id": 2}, 
            {"title": "Post 3", "content": "This is my third post", "id": 3}]

def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post

def find_post_index(id):
    for index, post in enumerate(my_posts):
        if post["id"] == id:
            return index
    return None

app.include_router(post.router)
app.include_router(user.router)
# app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello World"}


