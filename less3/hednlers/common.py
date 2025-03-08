import logging
from aiogram import Router, types ,F
from aiogram.types import Message
from aiogram.filters.command import Command
import asyncio
from less3.keyboards.button import kb1


from random import randint

from less3.randommodule.randomfox import fox







router = Router()

# Команда /start
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    logging.info(f"{message.from_user.id} использовал /start")
    await message.answer("Привет! Я эхо-бот на aiogram 3. Используй /help для списка команд.",reply_markup=kb1)

# Команда /help
@router.message(Command("help"))
async def cmd_help(message: types.Message):
    logging.info(f"{message.from_user.id} использовал /help")
    await message.answer("Доступные команды:\n/start - Начать работу с ботом\n/help - Показать список команд\n/about - О боте")

# Команда /about
@router.message(Command("about"))
async def cmd_about(message: types.Message):
    logging.info(f"{message.from_user.id} использовал /about")
    await message.answer("это эхо бот")




# Обработчик для команды /bear
@router.message(Command("bear"))
@router.message(Command("медведь"))
@router.message(F.text.func(lambda text: "покажи медведя" in text.lower()))
async def cmd_bear(message: types.Message):
    logging.info(f"{message.from_user.id} использовал /bear")
    await message.answer("вот медведь 🐻")
    #await message.answer_dice(emoji="🐻")

# Обработчик для команды /fox
@router.message(Command("fox"))
@router.message(Command("лиса"))
@router.message(F.text.func(lambda text: "покажи лису" in text.lower()))
async def cmd_fox(message: types.Message):
    logging.info(f"{message.from_user.id} использовал /fox")
    img_fox = fox()
    await message.answer("вот лиса ")
    await message.answer_photo(photo=img_fox)
    #await bot.send_photo(message.from_user.id,photo=img_fox)


#фильтер на текст randommodule
@router.message(F.text.lower() == 'num')
async def msg_random (message: types.Message):
    number = randint (1, 10)
    await message.answer(f'{number}')


#хендлер на сообщение
@router.message(F.text)

async def msg_echo (message: types.Message):
    msg_user = message.text.lower()
    name_user = message.chat.first_name
    if 'привет' in msg_user:
     await message.answer(f'Привет,{name_user} ,{msg_user}')
