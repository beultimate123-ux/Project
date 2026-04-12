import uvicorn
from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
async def balance():
    return {"content":"Ваш баланс 0 рублей"}

@app.get("/spin")
async def spin():
    roll = random.randint(1, 100)


if __name__ == "__main__":
    uvicorn.run("core:app", host="127.0.0.1", port=8000, reload=True)