import asyncio
import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

from bot_config import bot, dp, database
from handlers.start import start_router
# from handlers.picture import picture_router
from handlers.other_messages import other_msg_router
from handlers.opros_dialog import opros_router


async def on_startup(bot: Bot):
    print("Бот запустился")
    database.create_tables()


async def main():
    dp.include_router(start_router)
    # dp.include_router(picture_router)
    dp.include_router(opros_router)

    dp.include_router(user_router)

    dp.include_router(states_router)

    dp.include_router(dishes_router)

    dp.register_message_handler(review_start, Command('оставить_отзыв'))
    # в самом конце общий обработчик
    dp.include_router(other_msg_router)

    dp.startup.register(on_startup)
    # запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
