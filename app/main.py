from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings


# models.Base.metadata.create_all(bind=en  gine)

app = FastAPI()


app.include_router(post.router)
app.include_router(user.router)
app.include_router(vote.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Hello World"} 


