from typing import Optional
from fastapi import FastAPI, Body
from pydantic import BaseModel


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your posts data"}

@app.post("/createposts")
def create_post(post: Post):
    print(post)
    print(post.dict())    
    return {"data": post} 








