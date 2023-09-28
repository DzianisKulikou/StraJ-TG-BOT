from environs import Env  # Позволяет сохранять переменные в окружение
from aiogram import Bot, Dispatcher

from Handlers import hd_last
from config.config import load_config

env = Env()  # Создаем экземпляр класса Env
env.read_env()  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение

config = load_config('.env')
bot_token = env('bot_token')  # Сохраняем значение переменной окружения в переменную bot_token

# Создаем объекты бота и диспетчера
bot: Bot = Bot(config.tg_bot.token, parse_mode='HTML')
dp: Dispatcher = Dispatcher()

# Регистрируем роутеры в диспетчере
dp.include_router(hd_last.router)

# Запрос к серверу на получение абдейтов для бота
if __name__ == '__main__':
    # Запускаем поллинг
    dp.run_polling(bot)
