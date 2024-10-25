from aiogram import types
from bot.loader import dp



@dp.message_handler(commands=['info'])
@dp.message_handler(text="📑 Korxona haqida to'liq ma'lumot")
async def bot_info(message: types.Message):
    await message.answer("""
Korxona nomi: FURQAT PRINT SERVIS xususiy korxonasi

Korxona manzili: Farg’ona viloyati Furqat tumani Tadbirkorlar uyi binosida

Faoliyat turi: onlayn va offlayn dukonlar faoliyati, muhr va shtamplar tayyorlash, biznes rejalar tayyorlash, auksion savdolarida qatnashish, aholi va tadbirkorlarga yana boshqa konsalting xizmatlari ko’rsatish.

Korxonada ishlash rejimi:  Onlayn yoki offlaynda

Korxona yoshi: 10 yoshda

Qo’shimcha imkoniyatlar: Xodimlarni o’qitish va shaxsiy rivojlanishiga ko’maklashadi. Xodimlarining kelgusidagi orzu niyatlarini amalga oshirishiga ko’maklashadi.

Korxona lokatsiyasi: https://maps.google.com/maps?q=40.484424,70.790241&ll=40.484424,70.790241&z=16
""")