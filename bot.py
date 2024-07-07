import os
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

from handlers import start_handler, registration_handler, menu_handler

load_dotenv()


async def main():
    bot = Bot(token=os.environ.get("TOKEN"))
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_routers(
        start_handler.router,
        registration_handler.router,
        menu_handler.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
