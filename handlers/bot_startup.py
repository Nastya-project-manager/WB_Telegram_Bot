from aiogram import Router
from log_config import *


router = Router()


@router.startup()  # при запуске бота
async def startup():
    logging.info('Запуск бота v 0.0.1')
