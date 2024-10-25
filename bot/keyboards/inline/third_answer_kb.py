from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


third_answer_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=" 0 %", callback_data="0"),
        ],
        [
            InlineKeyboardButton(text=" 25 %", callback_data="25"),
        ],
        [
            InlineKeyboardButton(text=" 50 %", callback_data="50"),
        ],
        [
            InlineKeyboardButton(text=" 75 %", callback_data="75"),
        ],
        [
            InlineKeyboardButton(text=" 100 %", callback_data="100"),
        ]
    ]
)