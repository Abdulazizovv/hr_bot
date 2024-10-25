from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterState(StatesGroup):
    full_name = State()
    phone_number = State()
    birth_year = State()
    position = State()
    region = State()
    nationality = State()
    education = State()
    experience = State()
    marriage = State()
    first_answer = State()
    salary = State()
    second_answer = State()
    convince = State()
    driver_license = State()
    has_car = State()
    third_answer = State()
    fourth_answer = State()
    fifth_answer = State()
    image = State()

