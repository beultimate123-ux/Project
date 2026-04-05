from fastapi import FastAPI
import random
import aiogram
import sqlalchemy
import uvicorn

app = FastAPI()

@app.get("/")
def register():
    user_id = None
    telegram_id = None
    balance = 0

@app.get("/")
def choose():
    choosing = input('Выберите игру (0 - рулетка, 1 - слот машины)')
    if choosing == 0:
        spin()
    elif choosing == 1:
        slot()
    else:
        print('Команда не распознана')

@app.get("/")
def spin():

    bid_value = input('Размер вашей ставки')
    bid = input('Сделайте ставку (1 - красное, 2 - черное, 3 - четное, 4 - нечетное, 5 - зеленое')
    if bid == 1:
        pass

@app.get("/")
def slot():
    pass

@app.get("/")
def timer():
    pass

uvicorn.run(app, host="127.0.0.1", port=8000)