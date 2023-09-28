from aiogram import Router

from aiogram.types import Message
from environs import Env
from aiogram.filters import Text

from config.config import load_config
from lexicon.l_ads import bar, BW, r_BW, r_OW

# Инициализируем роутер уровня модуля
router: Router = Router()

# Получаем данные из .env
env = Env()  # Создаем экземпляр класса Env
env.read_env()  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
config = load_config('.env')
CHANNEL_ID_NA = config.tg_bot.channel_id_na
CHANNEL_ID_BL = config.tg_bot.channel_id_bl
CHANNEL_ID_OW = config.tg_bot.channel_id_ow
CHANNEL_ID_BW = config.tg_bot.channel_id_bw
ADMIN_ID = config.tg_bot.admin_id


# Правила канала Барахолка Lodz
@router.message(Text(text='Правила Барахолка Lodz'))
async def button_1(message: Message, bot=None):
    if str(message.from_user.id) in ADMIN_ID:
        await bot.send_message(chat_id=CHANNEL_ID_BL, text=bar)


# Правила канала Барахолка Варшава
@router.message(Text(text='Правила Отдам Варшава'))
async def button_2(message: Message, bot=None):
    if str(message.from_user.id) in ADMIN_ID:
        await bot.send_message(chat_id=CHANNEL_ID_OW, text=BW)


@router.message(Text(text='Рекламa каналов на Бьюти Варшава'))
async def button_101(message: Message, bot=None):
    if str(message.from_user.id) in ADMIN_ID:
        await bot.send_message(chat_id=CHANNEL_ID_BW, text=r_BW)


@router.message(Text(text='Рекламa каналов на Отдам Варшава'))
async def button_101(message: Message, bot=None):
    if str(message.from_user.id) in ADMIN_ID:
        await bot.send_message(chat_id=CHANNEL_ID_OW, text=r_OW)
