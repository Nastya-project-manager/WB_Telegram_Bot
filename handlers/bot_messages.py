from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def echo_handler(message: Message) -> None:
    """
    Хендлер на любое сообщение в не машины состояний
    Эхо хендлер
    """
    try:
        # Отправляем копию сообщения пользователя
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # Но не все типы поддерживаются для копирования, поэтому необходимо с этим справиться.
        await message.answer("Понял, спасибо!")
