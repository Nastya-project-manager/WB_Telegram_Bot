from log_config import *
from aiogram import Router
from aiogram.types import ErrorEvent

router = Router()


@router.error()
async def error_handler(event: ErrorEvent):
    logging.critical("Критическая ошибка, вызванная %s", event.exception, exc_info=True)
