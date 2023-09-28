from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from lexicon.l_button import l_button

# Создаем объекты кнопок 'на команду start для админов'
# Кнопка "Правила Барахолка Lodz"
_button_1: KeyboardButton = KeyboardButton(text=l_button['button_1'])
# Кнопка "Правила Барахолка Варшава"
_button_2: KeyboardButton = KeyboardButton(text=l_button['button_2'])

# Создаем объект клавиатуры, добавляя в него кнопки 'на команду start для админов'
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[_button_1], [_button_2]], resize_keyboard=True)
