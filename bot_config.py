from aiogram import Bot, Dispatcher
from dotenv import dotenv_values

from database.database import Database


token = dotenv_values('.env')['BOT_TOKEN']
if not token:
    token = "7270594509:AAG8ovcPAwujaBMdIKoAqwr5tIg98LELOdw"
bot = Bot(token=token)
dp = Dispatcher()
database = Database("db.sqlite")