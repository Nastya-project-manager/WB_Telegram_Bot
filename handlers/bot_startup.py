from aiogram import Router
from log_config import *
import Parser


router = Router()


@router.startup()  # при запуске бота
async def startup():
    logging.info('Запуск бота v 0.0.1')
    logging.info('Скачивание актуальной версии меню')
    Parser.get_server_menu()
