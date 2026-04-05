import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import core

API_TOKEN = '8502481185:AAGHsrxFMqPkhTsfwS6Wmy3rLzhztYpPmIo'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Приветствую в нашем казино боте!")

@dp.message(Command("balance"))
async def cmd_balance(message: types.Message):
    await message.answer(core.balance())

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())