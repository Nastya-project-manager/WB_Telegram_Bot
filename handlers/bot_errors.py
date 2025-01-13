from log_config import *
from aiogram import Router, Bot
from aiogram.types import ErrorEvent

router = Router()


@router.error()
async def error_handler(event: ErrorEvent, bot: Bot):
    await bot.send_message(chat_id='357295102', text=f'Критическая ошибка, вызванная {event.exception}')
    logging.critical("Критическая ошибка, вызванная %s", event.exception, exc_info=True)
