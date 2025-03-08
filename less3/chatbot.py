import logging
from aiogram import Bot, Dispatcher, types ,F
from aiogram.types import Message
from aiogram.filters.command import Command
import asyncio
from hednlers import carrier_choise, common


import config










async def main():
    logging.basicConfig(
        level=logging.INFO,  # Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    TOKEN = config.token  # Замени на свой токен

    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(carrier_choise.router)
    dp.include_router(common.router)

    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
