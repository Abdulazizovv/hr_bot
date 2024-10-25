from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

skip_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Keyingi savol", callback_data="skip")
        ]
    ]
)