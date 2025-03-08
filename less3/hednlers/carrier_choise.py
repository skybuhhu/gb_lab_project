import logging

from aiogram import Router, types ,F
from aiogram.types import Message
from aiogram.filters.command import Command
import asyncio
from less3.keyboards.prof_button import make_row_keyboard
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup




router = Router()


available_jobs = [
    "програмист",
    "дизайнер",
    "маркетолог",
    "бухгалтер",
    "менеджер",

]

available_grades = [
    "jun",
    "midle",
    "senior",
]

class ChoiseProfile (StatesGroup):
    job = State()
    grade = State()



# Команда /prof
@router.message(Command("prof"))
async def cmd_prof(message: types.Message, state:FSMContext):
    logging.info(f"{message.from_user.id} использовал /prof")
    await message.answer(
        text="Выбери профессию",
        reply_markup=make_row_keyboard(available_jobs))
    await state.set_state(ChoiseProfile.job)

#фильтр тчобы профессия была выбрана из job
@router.message(ChoiseProfile.job, F.text.in_(available_jobs))
async def prof_choisen(message: types.Message, state:FSMContext):
    await state.update_data(profession=message.text)
    await message.answer(
        text="Выбери уровень",
        reply_markup=make_row_keyboard(available_grades))
    await state.set_state(ChoiseProfile.grade)

@router.message(ChoiseProfile.job)
async def prof_choisen1(message: types.Message, state:FSMContext):
    await message.answer(
        text="Выбери профессию",
        reply_markup=make_row_keyboard(available_jobs))
    await state.set_state(ChoiseProfile.job)

@router.message(ChoiseProfile.grade, F.text.in_(available_grades))
async def prof_choisen2(message: types.Message, state:FSMContext):
    await state.update_data(grade=message.text)
    user_date = await state.get_data()
    await message.answer(
         f"Ваша профессия: {user_date['profession']}\n"
        f"Ваш уровень: {user_date['grade']}",
        reply_markup=types.ReplyKeyboardRemove())
    await state.clear()


@router.message(ChoiseProfile.grade)
async def prof_choisen3(message: types.Message, state:FSMContext):
    await message.answer(
        text="Выбери уровень",
        reply_markup=make_row_keyboard(available_grades))
    await state.set_state(ChoiseProfile.grade)

