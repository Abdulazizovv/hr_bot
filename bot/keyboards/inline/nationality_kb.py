from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

nations = ["O'zbek", "Rus", "Qozoq", "Qirg'iz", "Turkman", "Tojik", "Boshqa"]

nationality_btn = InlineKeyboardMarkup(row_width=2)
for nation_id, nation_text in enumerate(nations):
    nationality_btn.insert(InlineKeyboardButton(text=nation_text, callback_data=f"nation:{nation_id}"))
    