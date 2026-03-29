from fastapi import FastAPI
import aiogram
import sqlalchemy
import uvicorn

app = FastAPI()

@app.get("/")
def register():
    pass

@app.get("/")
def choose():
    pass

@app.get("/")
def spin():
    pass

@app.get("/")
def slot():
    pass

@app.get("/")
def add():
    pass

@app.get("/")
def timer():
    pass

uvicorn.run(app, host="127.0.0.1", port=8000)