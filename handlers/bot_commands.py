from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from keyboard import categories_key

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    Этот обработчик получает сообщения с командой start.
    """
    await message.delete()
    await message.answer(f"Привет, {hbold(message.from_user.full_name)}!\n"
                         f"Это бот который поможет найти самые лучше предложение в категории на WB",
                         parse_mode="HTML",
                         reply_markup=categories_key.categories())
