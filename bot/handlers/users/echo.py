from aiogram import types

from bot.loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer("Iltimos, pastdagi tugmalardan birini bosing")
