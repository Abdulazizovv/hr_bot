from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


cancel_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bekor qilish❌")
        ]
    ],
    resize_keyboard=True
)