from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str            # Токен для доступа к телеграм-боту
    channel_id_bw: str    # id канала бьюти Варшава
    channel_id_na: str    # id канала наша
    channel_id_bl: str    # id канала барахолка Lodz
    channel_id_ow: str    # id канала Отдам Варшава
    my_id: str            # id мой
    ira_id: str           # id Иры
    admin_id: list        # id Мой и Иры


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('bot_token'),
                               channel_id_bw=env('CHANNEL_ID_BW'),
                               channel_id_na=env('CHANNEL_ID_NA'),
                               channel_id_bl=env('CHANNEL_ID_BL'),
                               channel_id_ow=env('CHANNEL_ID_OW'),
                               my_id=env('MY_ID'),
                               ira_id=env('IRA_ID'),
                               admin_id=env('ADMIN_ID')))
