from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


pos = ["Sotuv bo'limi", "Kompyuter mutaxassisi"]

positions_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=pos_text, callback_data=f"position:{pos_id}") for pos_id, pos_text in enumerate(pos)]
    ]
)