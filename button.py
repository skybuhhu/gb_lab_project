from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Создаем кнопки
button1 = KeyboardButton(text='/start')
button2 = KeyboardButton(text='/help')
button3 = KeyboardButton(text='/about')
button4 = KeyboardButton(text='Покажи медведя')
button5 = KeyboardButton(text='Покажи лису')

# Создаем клавиатуру
kb1 = ReplyKeyboardMarkup(
    keyboard=[[button1, button2, button3], [button4, button5]],  # Две строки кнопок
    resize_keyboard=True  # Клавиатура подстраивается под размер экрана
)


