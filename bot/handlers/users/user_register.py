from aiogram import types
from bot.loader import dp
from asgiref.sync import sync_to_async
from bot.states.register_state import RegisterState
from bot.keyboards.inline import positions_kb, pos
from bot.keyboards.inline import regions_btn, regions
from bot.keyboards.inline import nationality_btn, nations
from bot.keyboards.inline import education_kb, degrees, marriage_btn, convince_btn, skip_btn, submit_btn
from bot.keyboards.inline import driver_licence_btn, licence_types, has_car_btn, third_answer_btn
from bot.keyboards.default import cancel_kb, main_menu_kb
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands=['register'])
@dp.message_handler(text="✍️ Ro'yxatdan o'tish")
async def register_user(message: types.Message):
    await message.answer("<i><b>Ro'yxatdan o'tish boshlandi!</b></i>\n\nIsm familyangizni kiriting:", parse_mode="HTML", reply_markup=cancel_kb)
    await RegisterState.full_name.set()


@dp.message_handler(state=RegisterState.full_name)
async def get_full_name(message: types.Message, state):
    full_name = message.text
    await state.update_data(full_name=full_name)
    await message.answer("Telefon raqamingizni kiriting:\nmasalan: +998901234567")
    await RegisterState.phone_number.set()


@dp.message_handler(state=RegisterState.phone_number)
async def get_phone_number(message: types.Message, state):
    phone_number = message.text
    await state.update_data(phone_number=phone_number)
    await message.answer("Tug'ilgan yilingizni kiriting:\nmasalan: 1999")
    await RegisterState.birth_year.set()


@dp.message_handler(state=RegisterState.birth_year)
async def get_birth_year(message: types.Message, state):
    birth_year = message.text
    await state.update_data(birth_year=birth_year)
    await message.answer("Iltimos, soha yo'nalishlaridan birini tanglang👇:", reply_markup=positions_kb)
    await RegisterState.position.set()


@dp.callback_query_handler(state=RegisterState.position)
async def get_position(call: types.CallbackQuery, state: FSMContext):
    position = call.data
    await state.update_data(position=pos[int(position[9:])])
    await call.message.edit_text("Hududni tanlang:", reply_markup=regions_btn)
    await RegisterState.region.set()


@dp.callback_query_handler(state=RegisterState.region)
async def get_region(call: types.CallbackQuery, state: FSMContext):
    region = call.data
    await state.update_data(region=regions[int(region[7:])])
    await call.message.edit_text("Millatingiz:", reply_markup=nationality_btn)
    await RegisterState.nationality.set()


@dp.callback_query_handler(state=RegisterState.nationality)
async def get_nationality(call: types.CallbackQuery, state: FSMContext):
    nation = call.data
    await state.update_data(nationality=nations[int(nation[7:])])
    await call.message.edit_text("Ma'lumotingiz:", reply_markup=education_kb)
    await RegisterState.education.set()


@dp.callback_query_handler(state=RegisterState.education)
async def get_education(call: types.CallbackQuery, state: FSMContext):
    degree = call.data
    await state.update_data(education=degrees[int(degree[7:])])
    await call.message.edit_text("Oilaviy holatingiz:", reply_markup=marriage_btn)
    await RegisterState.marriage.set()


@dp.callback_query_handler(state=RegisterState.marriage)
async def get_marriage(call: types.CallbackQuery, state: FSMContext):
    marriage = "Turmush qurgan" if call.data else "Turmush qurmagan"
    await state.update_data(marriage=marriage)
    await call.message.edit_text("<b>Ish tajribangizni kiriting.</b>\n<i>Qaysi korxona yoki tashkilotlarda qanday lavozimlarda ishlagansiz?</i>")
    await RegisterState.experience.set()


@dp.message_handler(state=RegisterState.experience)
async def get_experience(message: types.Message, state: FSMContext):
    experience = message.text
    await state.update_data(experience=experience)
    await message.answer("Bizda qancha oylik maoshga ishlamoqchisiz:")
    await RegisterState.salary.set()


@dp.message_handler(state=RegisterState.salary)
async def get_salary(message: types.Message, state: FSMContext):
    salary = message.text
    await state.update_data(salary=salary)
    await message.answer("Bizning korxonada qancha muddat ishlamoqchisiz?")
    await RegisterState.first_answer.set()


@dp.message_handler(state=RegisterState.first_answer)
async def get_first_answer(message: types.Message, state: FSMContext):
    first_answer = message.text
    await state.update_data(first_answer=first_answer)
    await message.answer("Sudlanganmisiz?", reply_markup=convince_btn)
    await RegisterState.convince.set()


@dp.callback_query_handler(state=RegisterState.convince)
async def get_convince(call: types.CallbackQuery, state: FSMContext):
    convince = "Sudlangan" if call.data == "True" else "Sudlanmagan"
    await state.update_data(convince=convince)
    await call.message.edit_text("Haydovchilik guvohnomangiz bormi?:", reply_markup=driver_licence_btn)
    await RegisterState.driver_license.set()


@dp.callback_query_handler(state=RegisterState.driver_license)
async def get_driver_license(call: types.CallbackQuery, state: FSMContext):
    data = call.data
    driver_license = licence_types[int(data[8:])]
    await state.update_data(driver_license=driver_license)
    await call.message.edit_text("Shaxsiy avtomobilingiz bormi?", reply_markup=has_car_btn)
    await RegisterState.has_car.set()


@dp.callback_query_handler(state=RegisterState.has_car)
async def get_has_car(call: types.CallbackQuery, state: FSMContext):
    has_car = "Bor" if call.data else "Yo'q"
    await state.update_data(has_car=has_car)
    await call.message.edit_text("Word dasturini bilish darajangiz:", reply_markup=third_answer_btn)
    await RegisterState.third_answer.set()


@dp.callback_query_handler(state=RegisterState.third_answer)
async def get_third_answer(call: types.CallbackQuery, state: FSMContext):
    third_answer = str(call.data) + " %"
    await state.update_data(third_answer=third_answer)
    await call.message.edit_text("Excel dasturini bilish darajangiz:", reply_markup=third_answer_btn)
    await RegisterState.fourth_answer.set()


@dp.callback_query_handler(state=RegisterState.fourth_answer)
async def get_fourth_answer(call: types.CallbackQuery, state: FSMContext):
    fourth_answer = str(call.data) + " %"
    await state.update_data(fourth_answer=fourth_answer)
    await call.message.edit_text("Boshqa qanday dasturlar bilan ishlay olasiz?\n<i>Nomi va necha foiz(%)</i>", reply_markup=skip_btn)
    await RegisterState.fifth_answer.set()


@dp.callback_query_handler(text="skip", state=RegisterState.fifth_answer)
async def skip_fifth_answer(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(fifth_answer="Yo'q")
    await call.message.edit_text("Iltimos, o'zingizni suratingizni yuboring:")
    await RegisterState.image.set()


@dp.message_handler(state=RegisterState.fifth_answer)
async def get_fifth_answer(message: types.Message, state: FSMContext):
    fifth_answer = message.text
    await state.update_data(fifth_answer=fifth_answer)
    await message.answer("Iltimos, o'zingizni suratingizni yuboring:")
    await RegisterState.image.set()


@dp.message_handler(content_types=types.ContentType.PHOTO, state=RegisterState.image)
async def get_image(message: types.Message, state: FSMContext):
    image = message.photo[-1].file_id
    await state.update_data(image=image)
    data = await state.get_data()
    if data.get("image"):
        await message.answer_photo(data.get("image"), 
                         f"<b>Ro'yxatdan o'tish deyarli yakunlandi. Malumotlaringizni tekshiring va tasdinglang!</b>\n\n"
                         f"<b>Ism familya:</b> {data.get('full_name')}\n"
                         f"<b>Telefon raqam:</b> {data.get('phone_number')}\n"
                         f"<b>Tug'ilgan yil:</b> {data.get('birth_year')}\n"
                         f"<b>Yo'nalish:</b> {data.get('position')}\n"
                         f"<b>Hudud:</b> {data.get('region')}\n"
                         f"<b>Millat:</b> {data.get('nationality')}\n"
                         f"<b>Ma'lumot:</b> {data.get('education')}\n"
                         f"<b>Oilaviy holat:</b> {data.get('marriage')}\n"
                         f"<b>Ish tajribasi:</b> {data.get('experience')}\n"
                         f"<b>Oylik maosh:</b> {data.get('salary')}\n"
                         f"<b>Muddat:</b> {data.get('first_answer')}\n"
                         f"<b>Sudlanganmi:</b> {data.get('convince')}\n"
                         f"<b>Haydovchilik guvohnomasi:</b> {data.get('driver_license')}\n"
                         f"<b>Shaxsiy avtomobil:</b> {data.get('has_car')}\n"
                         f"<b>Word dasturi bilish darajasi:</b> {data.get('third_answer')}\n"
                         f"<b>Excel dasturi bilish darajasi:</b> {data.get('fourth_answer')}\n"
                         f"<b>Boshqa dasturlar bilish darajasi:</b> {data.get('fifth_answer')}\n", reply_markup=submit_btn)
    else:
        await message.answer(f"<b>Ro'yxatdan o'tish muvaffaqiyatli yakunlandi!</b>\n\n"
                            f"<b>Ism familya:</b> {data.get('full_name')}\n"
                            f"<b>Telefon raqam:</b> {data.get('phone_number')}\n"
                            f"<b>Tug'ilgan yil:</b> {data.get('birth_year')}\n"
                            f"<b>Yo'nalish:</b> {data.get('position')}\n"
                            f"<b>Hudud:</b> {data.get('region')}\n"
                            f"<b>Millat:</b> {data.get('nationality')}\n"
                            f"<b>Ma'lumot:</b> {data.get('education')}\n"
                            f"<b>Oilaviy holat:</b> {data.get('marriage')}\n"
                            f"<b>Ish tajribasi:</b> {data.get('experience')}\n"
                            f"<b>Oylik maosh:</b> {data.get('salary')}\n"
                            f"<b>Muddat:</b> {data.get('first_answer')}\n"
                            f"<b>Sudlanganmi:</b> {data.get('convince')}\n"
                            f"<b>Haydovchilik guvohnomasi:</b> {data.get('driver_license')}\n"
                            f"<b>Shaxsiy avtomobil:</b> {data.get('has_car')}\n"
                            f"<b>Word dasturi bilish darajasi:</b> {data.get('third_answer')}\n"
                            f"<b>Excel dasturi bilish darajasi:</b> {data.get('fourth_answer')}\n"
                            f"<b>Boshqa dasturlar bilish darajasi:</b> {data.get('fifth_answer')}\n"
                            f"<b>Rasm:</b> {data.get('image')}\n",
                            reply_markup=submit_btn
        )



@dp.callback_query_handler(text="cancel", state="*")
async def cancel(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("Ro'yxatdan o'tish bekor qilindi!\nSiz bosh sahifadasiz", reply_markup=main_menu_kb)
    await state.finish()

@dp.callback_query_handler(text="submit", state="*")
async def submit(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    await call.message.answer("⏳")
    data = await state.get_data()
    from bot.utils import generate_pdf
    from bot.utils.db_api import add_user_request
    file_name = f"{call.message.from_user.id}_data.pdf"
    image_stream = await dp.bot.download_file_by_id(data.get("image"))
    caption_text = f"👤Ism sharif: {data.get('full_name')}" \
                   f"\n📞Telefon raqam: {data.get('phone_number')}" \
                   f"\n#️⃣Soha: {data.get('position')}" \
                   f"\n📍Hudud: {data.get('region')}"
    pdf = await generate_pdf.create_pdf_with_tables(filename=file_name, data=data, image_stream=image_stream)
    pdf_file_id, image_file_id = await generate_pdf.upload_to_channel(pdf, data.get("image"), caption_text)
    await call.message.answer_document(document=pdf_file_id, caption=caption_text)
    await sync_to_async(add_user_request)(
        user_id=call.from_user.id,
        full_name=data.get("full_name"),
        phone_number=data.get("phone_number"),
        birth_year=data.get("birth_year"),
        position=data.get("position"),
        region=data.get("region"),
        nationality=data.get("nationality"),
        education=data.get("education"),
        experience=data.get("experience"),
        marriage=True if data.get("marriage")=="Turmush qurgan" else False,
        first_answer=data.get("first_answer"),
        salary=data.get("salary"),
        second_answer=data.get("second_answer"),
        convince=True if data.get("convince")== "Sudlangan" else False,
        driver_license=data.get("driver_license"),
        has_car=True if data.get("has_car") == "Bor" else False,
        third_answer=data.get("third_answer"),
        fourth_answer=data.get("fourth_answer"),
        fifth_answer=data.get("fifth_answer"),
        image=image_file_id
    )

    await state.finish()
    