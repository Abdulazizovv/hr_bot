from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

licence_types = [
    "A ✅",
    "B ✅",
    "B, C ✅",
    "B, C, D ✅",
    "B, C, D, E ✅",
    "Yo'q ❌",
    "Boshqa ❓"
]

driver_licence_btn = InlineKeyboardMarkup(row_width=1)
for licence_id, licence_text in enumerate(licence_types):
    driver_licence_btn.insert(InlineKeyboardButton(text=licence_text, callback_data=f"licence:{licence_id}"))