import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers import (
    bot_commands,
    bot_messages,
    bot_errors,
    bot_startup,
    callback_query)

# Загрузка переменных окружения из файла .env
load_dotenv()


async def main() -> None:
    bot = Bot(os.getenv('BOT_TOKEN'))
    dp = Dispatcher()
    dp.include_routers(
        bot_commands.router,
        bot_messages.router,
        callback_query.router,
        bot_startup.router,
        bot_errors.router
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
