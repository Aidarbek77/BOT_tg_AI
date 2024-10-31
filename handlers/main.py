from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# ... другие импорты

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

# Регистрация обработчиков
dp.register_message_handler(review_start, Command('оставить_отзыв'))
# ... другие обработчики

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)n())