import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import requests

API_TOKEN = '8502481185:AAGHsrxFMqPkhTsfwS6Wmy3rLzhztYpPmIo'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Приветствую в нашем казино боте!")

@dp.message(Command("balance"))
async def cmd_balance(message: types.Message):
    r = requests.get('http://127.0.0.1:8000')
    if r.status_code == 200:
        a = r.json()
        await message.answer(str(a["content"]))

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())