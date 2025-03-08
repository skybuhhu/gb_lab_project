from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import ReplyKeyboardRemove
from aiogram import types

CANCEL_BUTTON = "Отмена"

from aiogram import types


def make_row_keyboard(items: list[str]) -> types.ReplyKeyboardMarkup:
    """
    Создает клавиатуру с кнопками, включая кнопку "Отмена".
    """
    # Создаем копию списка, чтобы не изменять исходный
    buttons = [types.KeyboardButton(text=item) for item in items]

    # Добавляем кнопку "Отмена" в конец
    buttons.append(types.KeyboardButton(text="Отмена"))

    # Группируем кнопки в строки (по одной кнопке в строке)
    keyboard = [[button] for button in buttons]

    # Возвращаем клавиатуру
    return types.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
