from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


marriage_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Turmush qurgan", callback_data="True"),
        ],
        [
            InlineKeyboardButton(text="Turmush qurmagan", callback_data="False")
        ]
    ]
)