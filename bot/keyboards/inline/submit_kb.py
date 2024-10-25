from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


submit_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bekor qilish ❌", callback_data="cancel"),
            InlineKeyboardButton(text="Tasdiqlash ✅", callback_data="submit")
        ]
    ]
)