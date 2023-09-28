from datetime import datetime

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from environs import Env

from config.config import load_config
from keyboards.kb_admin_start import kb_admin_ob

# Инициализируем роутер уровня модуля
router: Router = Router()

# Получаем данные из .env
env = Env()  # Создаем экземпляр класса Env
env.read_env()  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
config = load_config('.env')
ADMIN_ID = config.tg_bot.admin_id


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message, bot=None):
    if message.from_user.id == message.chat.id:
        if str(message.from_user.id) in ADMIN_ID:
            await message.answer(text='На какой канал нужно опубликовать правила?', reply_markup=kb_admin_ob)
        else:
            await bot.send_message(chat_id=message.from_user.id,
                                   text='Я пока не разговариваю, только каналы обслуживаю!))')
            print(datetime.now(), message.from_user.id, message.from_user.full_name,
                  message.from_user.username)  # id chat, id user, name user
