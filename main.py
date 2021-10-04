# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime

app = FastAPI()

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