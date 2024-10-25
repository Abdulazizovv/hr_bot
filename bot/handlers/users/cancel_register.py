from aiogram import types
from bot.loader import dp
from bot.keyboards.default import main_menu_kb
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="Bekor qilish❌", state="*")
async def cancel_register(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Ro'yxatdan o'tish bekor qilindi!\nSiz bosh sahifadasiz!", reply_markup=main_menu_kb)