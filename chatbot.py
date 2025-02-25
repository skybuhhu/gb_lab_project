import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters.command import Command
import asyncio

import config


logging.basicConfig(
    level=logging.INFO,  # Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s"
)

TOKEN = config.token  # Замени на свой токен

bot = Bot(token=TOKEN)
dp = Dispatcher()


# Команда /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    logging.info(f"{message.from_user.id} использовал /start")
    await message.answer("Привет! Я эхо-бот на aiogram 3. Используй /help для списка команд.")

# Команда /help
@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    logging.info(f"{message.from_user.id} использовал /help")
    await message.answer("Доступные команды:\n/start - Начать работу с ботом\n/help - Показать список команд\n/about - О боте")

# Команда /about
@dp.message(Command("about"))
async def cmd_about(message: types.Message):
    logging.info(f"{message.from_user.id} использовал /about")
    await message.answer("Этот бот создан на aiogram 3. Он повторяет ваши сообщения и выполняет команды.")


@dp.message()
async def echo_handler(message: Message):
    await message.answer(message.text)  # Отправляет обратно то же сообщение

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
