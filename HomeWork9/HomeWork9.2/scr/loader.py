from aiogram import Bot, Dispatcher
from config import TOKEN
from data_base import DataBase

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
data_menger = DataBase()