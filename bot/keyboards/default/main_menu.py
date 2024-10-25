from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✍️ Ro'yxatdan o'tish"),
            KeyboardButton(text="📑 Korxona haqida to'liq ma'lumot"),
        ],
    ],
    resize_keyboard=True
)