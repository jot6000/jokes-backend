# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

jokedb = []

# post model
class Joke(BaseModel):
    id: int
    content: Text

@app.get("/")
def read_root():
  return {"home": "Home page"}

@app.get("/joke")
def get_jokes():
    return jokedb

@app.post("/joke")
def add_joke(joke: Joke):
    jokedb.append(joke.dict())
    return jokedb[-1]

@app.put("/joke/{post_id}")
def update_joke(joke_id: int, joke: Joke):
    jokedb[joke_id] = joke
    return {"message": "Joke has been updated succesfully"}

@app.delete("/joke/{post_id}")
def delete_joke(joke_id: int):
    jokedb.pop(joke_id-1)
    return {"message": "Joke has been deleted succesfully"}