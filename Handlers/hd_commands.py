from datetime import datetime

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message, bot=None):
    if message.from_user.id == message.chat.id:
        await bot.send_message(chat_id=message.from_user.id,
                               text='Я пока не разговариваю, только каналы обслуживаю!))')
        print(datetime.now(), message.from_user.id, message.from_user.full_name,
              message.from_user.username)  # id chat, id user, name user
