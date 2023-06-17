from aiogram import Bot, Dispatcher
from config import TOKEN, IP, PGUSER, PGPASSWORD, DATABASE
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

from db_api.db_database import Database

logging.basicConfig(level=logging.INFO)

db = Database(DATABASE, PGUSER, PGPASSWORD, IP, '5432')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

