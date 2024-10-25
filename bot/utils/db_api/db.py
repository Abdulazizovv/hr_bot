from botapp.models import BotUser, UserRequest
import logging


# foydalanuvchini ma'lumotlar bazasida mavjudligini tekshirish
def check_user_exists(user_id: int):
    if BotUser.objects.filter(user_id=user_id).exists():
        return True
    return False

# agar foydalanuvchi mavjud bo'lmasa uning ma'lumotlarini bazaga qo'shish
def add_user(user_id: int, first_name: str, last_name: None|str, username: str):
    if not check_user_exists(user_id):
        try:
            BotUser.objects.create(
                user_id=user_id,
                first_name=first_name,
                last_name=last_name,
                username=username
            )
            return True
        except Exception as err:
            logging.error('Error while adding user: ', err)
            return False
    return False


# foydalanuvchi arizasini bazaga qo'shish
def add_user_request(user_id: int,
                     full_name: str,
                     phone_number: str,
                     birth_year: str,
                     position: str,
                     region: str,
                     nationality: str,
                     education: str,
                     experience: str,
                     marriage: bool,
                     first_answer: None|str,
                     salary: str,
                     second_answer: None|str,
                     convince: bool,
                     driver_license: str,
                     has_car: bool,
                     third_answer: str,
                     fourth_answer: str,
                     fifth_answer: str,
                     image: str):
    if user_id:
        try:
            user = BotUser.objects.get(user_id=user_id)
            UserRequest.objects.create(
                user=user,
                full_name=full_name,
                phone_number=phone_number,
                birth_year=birth_year,
                position=position,
                region=region,
                nationality=nationality,
                education=education,
                experience=experience,
                marriage=marriage,
                first_answer=first_answer,
                salary=salary,
                second_answer=second_answer,
                convince=convince,
                driver_license=driver_license,
                has_car=has_car,
                third_answer=third_answer,
                fourth_answer=fourth_answer,
                fifth_answer=fifth_answer,
                image=image
            )
            return True
        except Exception as err:
            logging.error(f'Error while adding user request: {err}')
            return False
    return False

# foydalanuvchi arizalarini olish
def get_user_requests(user_id: int):
    if user_id:
        try:
            user = BotUser.objects.get(user_id=user_id)
            return UserRequest.objects.filter(user=user)
        except Exception as err:
            logging.error(f'Error while getting user requests: {err}')
            return []
    return []


def add_user_request(user_id: int,
                     full_name: str,
                     phone_number: str,
                     birth_year: str,
                     position: str,
                     region: str,
                     nationality: str,
                     education: str,
                     experience: str,
                     marriage: bool,
                     first_answer: None|str,
                     salary: str,
                     second_answer: None|str,
                     convince: bool,
                     driver_license: str,
                     has_car: bool,
                     third_answer: str,
                     fourth_answer: str,
                     fifth_answer: str,
                     image: str
                     ):
    if user_id:
        try:
            user = BotUser.objects.get(user_id=user_id)
            UserRequest.objects.create(
                user=user,
                full_name=full_name,
                phone_number=phone_number,
                birth_year=birth_year,
                position=position,
                region=region,
                nationality=nationality,
                education=education,
                experience=experience,
                marriage=marriage,
                first_answer=first_answer,
                salary=salary,
                second_answer=second_answer,
                convince=convince,
                driver_license=driver_license,
                has_car=has_car,
                third_answer=third_answer,
                fourth_answer=fourth_answer,
                fifth_answer=fifth_answer,
                image=image
            )
            return True
        except Exception as err:
            logging.error(f'Error while adding user request: {err}')
            return False
    return False