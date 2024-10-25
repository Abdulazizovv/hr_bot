from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from bot.loader import dp
from bot.keyboards.default.main_menu import main_menu_kb
from bot.utils.db_api.db import add_user
from asgiref.sync import sync_to_async


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # salomlashish xabari
    await message.answer(f"""
    АССАЛОМУ АЛЕЙКУМ!!!    
СИЗНИ ҚАДРЛАЙДИГАН ЖАМОАДА ИШЛАШНИ ХОҲЛАЙСИЗМИ?   
            
Унда сиз учун АЖОЙИБ ИМКОНИЯТ!   
            
            
☝️ Сиздан ДИПЛОМ талаб қилинмайди!   
            
✳️ ИШ НИМАДАН ИБОРАТ:   
▪️Мижозлар билан киришимли булиш;   
▪️Хушмуомалалик билан компания маҳсулотлари ҳақида маълумот бериш ва сотиш;   
▪️Мижозлар маълумотларини базага киритиш;   
▪️ Сотув режаларини амалга ошириш.  
            
            
            
✅ БИЗ, АЙНАН СИЗНИ ТАНЛАЙМИЗ, АГАР СИЗ:    
• 20-30 ёшдаги йигит-қиз бўлсангиз;   
• Хушмуомилали;   
• Жамоада ишлаш маҳорати;   
• Маълумотларга эътиборли;    
• Масьулиятли;   
• Стресс холатларига чидамли;   
• Музокара маҳоратига эга; 
            
            
            
😍 Сизни қандай ИМКОНИЯТЛАР кутмоқда БИЛАСИЗМИ?   
• Бир мақсад асосида йиғилган ЖАМОА аъзоси бўлиш;   
• Ойлик маошдан ташқари  БОНУСЛАРГА эга бўлиш имконияти;   
• Замонавий шинам офисда ишлаш;   
• Ўз вақтида ойлик маош + Сотувлардан бонуслар олиш    
• Расман ишга кабул қилиш;   
• БЕПУЛ ўқиш ва Тажриба олиш имконияти;   
• Шахсий ривожланиш ва Карера қилиш;   
• Иш вакти: 9:00 - 18:00 гача. дам олиш вақтлари хафтада бир кун.
            
            
            
👧🏻 Агар сизга ахоли ва тадбиркорлар билан ишлаш қизиқ булса, СИЗ БИЗНИ САФИМИЗДАСИЗ!

ИЛТИМОС ҚИЛАМИЗ ҚУЙИДАГИ САВОЛЛАРГА АНИҚ МАЪЛУМОТ БЕРИНГ!
""", reply_markup=main_menu_kb)
    # foydalanuvchi haqida ma'lumotlar
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    await sync_to_async(add_user)(user_id, first_name, last_name, username)


