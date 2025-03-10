import logging
from aiogram import Bot, Dispatcher, types ,F
from aiogram.types import Message
from aiogram.filters.command import Command
import asyncio
from button import kb1

from random import randint

import config
from randomfox import fox


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
    await message.answer("Привет! Я эхо-бот на aiogram 3. Используй /help для списка команд.",reply_markup=kb1)

# Команда /help
@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    logging.info(f"{message.from_user.id} использовал /help")
    await message.answer("Доступные команды:\n/start - Начать работу с ботом\n/help - Показать список команд\n/about - О боте")

# Команда /about
@dp.message(Command("about"))
async def cmd_about(message: types.Message):
    logging.info(f"{message.from_user.id} использовал /about")
    await message.answer("это эхо бот")




# Обработчик для команды /bear
@dp.message(Command("bear"))
@dp.message(Command("медведь"))
@dp.message(F.text.func(lambda text: "покажи медведя" in text.lower()))
async def cmd_bear(message: types.Message):
    logging.info(f"{message.from_user.id} использовал /bear")
    await message.answer("вот медведь 🐻")
    #await message.answer_dice(emoji="🐻")

# Обработчик для команды /fox
@dp.message(Command("fox"))
@dp.message(Command("лиса"))
@dp.message(F.text.func(lambda text: "покажи лису" in text.lower()))
async def cmd_fox(message: types.Message):
    logging.info(f"{message.from_user.id} использовал /fox")
    img_fox = fox()
    await message.answer("вот лиса ")
    #await message.answer_photo(photo=img_fox)
    await bot.send_photo(message.from_user.id,photo=img_fox)


#фильтер на текст randommodule
@dp.message(F.text.lower() == 'num')
async def msg_random (message: types.Message):
    number = randint (1, 10)
    await message.answer(f'{number}')


#хендлер на сообщение
@dp.message(F.text)

async def msg_echo (message: types.Message):
    msg_user = message.text.lower()
    name_user = message.chat.first_name
    if 'привет' in msg_user:
     await message.answer(f'Привет,{name_user} ,{msg_user}')

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
