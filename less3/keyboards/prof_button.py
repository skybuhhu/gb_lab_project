from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import ReplyKeyboardRemove
from aiogram import types

CANCEL_BUTTON = "Отмена"

from aiogram import types


def make_row_keyboard(items: list[str]) -> types.ReplyKeyboardMarkup:
    """
    Создает клавиатуру с кнопками, группируя их по 3 в строку.
    Кнопка "Отмена" всегда на отдельной строке.
    """
    # Создаем копию списка, чтобы не изменять исходный
    buttons = [types.KeyboardButton(text=item) for item in items]

    # Группируем кнопки по 3 в строку
    keyboard = [buttons[i:i + 3] for i in range(0, len(buttons), 3)]

    # Добавляем кнопку "Отмена" на отдельной строке
    keyboard.append([types.KeyboardButton(text="Отмена")])

    # Возвращаем клавиатуру
    return types.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
