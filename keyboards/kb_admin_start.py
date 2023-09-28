from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from lexicon.l_button import l_button, l_button_r

# Создаем объекты кнопок 'на команду start для админов'
# Кнопка "Правила Барахолка Lodz"
_button_1: KeyboardButton = KeyboardButton(text=l_button['button_1'])
# Кнопка "Правила Барахолка Варшава"
_button_2: KeyboardButton = KeyboardButton(text=l_button['button_2'])

# Кнопка 'Рекламa каналов на Бьюти Варшава'
_button_101: KeyboardButton = KeyboardButton(text=l_button_r['button_101'])
# Кнопка 'Рекламa каналов на Отдам Варшава'
_button_102: KeyboardButton = KeyboardButton(text=l_button_r['button_102'])

# Создаем объект клавиатуры, добавляя в него кнопки 'на команду start для админов'
kb_admin_ob: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[_button_1], [_button_2], [_button_101],
                                                                 [_button_102]],
                                                       resize_keyboard=True)
