from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    Этот обработчик получает сообщения с командой start.
    """
    await message.answer(f"Привет, {hbold(message.from_user.full_name)}!",parse_mode="HTML")
