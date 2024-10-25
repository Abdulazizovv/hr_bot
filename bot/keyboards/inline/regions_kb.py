from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


regions = ["Toshkent shahri", "Toshkent viloyati", "Andijon", "Buxoro", "Jizzax", "Qashqadaryo", "Navoiy", "Namangan", "Samarqand", "Surxondaryo", "Sirdaryo", "Farg'ona", "Xorazm", "Qoraqalpog'iston Respublikasi"]


regions_btn = InlineKeyboardMarkup(row_width=2)
for region_id, region_text in enumerate(regions):
    regions_btn.insert(InlineKeyboardButton(text=region_text, callback_data=f"region:{region_id}"))
