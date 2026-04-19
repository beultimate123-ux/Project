import uvicorn
from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/balance")
async def balance():
    return {"content":"Ваш баланс 0 рублей"}

@app.get("/spin")
async def spin():
    result = None
    win_chance = random.randint(1, 3)
    if win_chance == 1 or win_chance == 2:
        roll_win = random.randint(1, 100)
        if 1 <= roll_win <= 49:
            result = "Вам выпало красное! Ваш выигрыш 25 монет!"
        elif 50 <= roll_win <= 98:
            result = "Вам выпало черное! Ваш выигрыш 50 монет!"
        elif 99 <= roll_win <= 100:
            result = "Вам выпало зеленое! Ваш выигрыш 500 монет!"
    elif win_chance == 3:
        roll_lose = random.randint(1, 100)
        if 1 <= roll_lose <= 49:
            result = "Вам выпало красное! Ваш проигрыш 10 монет!"
        elif 50 <= roll_lose <= 98:
            result = "Вам выпало черное! Ваш проигрыш 25 монет!"
        elif 99 <= roll_lose <= 100:
            result = "Вам выпало зеленое! Ваш проигрыш 250 монет!"
    return {"content":result}

@app.get("/slot")
async def slot():
    result = None
    spin_chance = random.randint(1, 27)
    if spin_chance == 1:
        result = "Вам выпала комбинация 777! Ваш выигрыш 1000 монет!"
    elif spin_chance == 2:
        result = "Вам выпала комбинация Лимоны! Ваш выигрыш 500 монет!"
    elif spin_chance == 3:
        result = "Вам выпала комбинация Bar! Ваш выигрыш 300 монет!"
    elif 4 <= spin_chance <= 27:
        result = "Вам не выпала ни одна комбинация! Ваш проигрыш 50 монет!"
    return {"content":result}

if __name__ == "__main__":
    uvicorn.run("core:app", host="127.0.0.1", port=8000, reload=True)