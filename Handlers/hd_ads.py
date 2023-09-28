from aiogram import Router

from aiogram.types import Message
from environs import Env
from aiogram.filters import Text

from config.config import load_config
from lexicon.l_ads import bar

# Инициализируем роутер уровня модуля
router: Router = Router()

# Получаем данные из .env
env = Env()  # Создаем экземпляр класса Env
env.read_env()  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
config = load_config('.env')
CHANNEL_ID_NA = config.tg_bot.channel_id_na
CHANNEL_ID_BL = config.tg_bot.channel_id_bl
CHANNEL_ID_BW = config.tg_bot.channel_id_bw
CHANNEL_ID = config.tg_bot.channel_id
ADMIN_ID = config.tg_bot.admin_id


# Правила нашего канала Барахолка Lodz
@router.message(Text(text='правила бар'))
async def process_dog_answer(message: Message, bot=None):
    if str(message.from_user.id) in ADMIN_ID:
        await bot.send_message(chat_id=CHANNEL_ID_BL,text=bar)
