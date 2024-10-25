from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


degrees = ["O'rta", "O'rta maxsus", "Oliy | Bakalavr", "Oliy | Magistratura"]

education_kb = InlineKeyboardMarkup(row_width=2)
for degree_id, degree_text in enumerate(degrees):
    education_kb.insert(InlineKeyboardButton(text=degree_text, callback_data=f"degree:{degree_id}"))