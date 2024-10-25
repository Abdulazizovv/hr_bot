from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from bot.data import config




PROXY_URL = 'http://proxy.server:3128/'

bot = Bot(token=config.BOT_TOKEN, proxy=PROXY_URL,parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# db = DataBase()


