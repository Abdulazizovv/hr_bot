from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


convince_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ha", callback_data="True"),
        ],
        [
            InlineKeyboardButton(text="Yo'q", callback_data="False")
        ]
    ]
)