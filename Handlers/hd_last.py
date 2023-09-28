from aiogram import Router
from aiogram.types import Message

# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер будет срабатывать на все сообщения, которые не отловят остальные хэндлеры ru
@router.message()
async def send_echo(message: Message, bot=None):
    if message.from_user.id == message.chat.id:
        await bot.send_message(chat_id=message.from_user.id,
                               text='Я пока не разговариваю, только каналы обслуживаю!))')
