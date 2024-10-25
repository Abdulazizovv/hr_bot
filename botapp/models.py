from django.db import models


# botga start bosgan userlarni saqlash uchun model
class BotUser(models.Model):
    user_id = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        ordering = ['-created_at']


# foydalanuvchilar yuborgan arizalar uchun model
class UserRequest(models.Model):
    user = models.ForeignKey(BotUser, on_delete=models.CASCADE) # user
    full_name = models.CharField(max_length=255) # ismi va familiyasi
    phone_number = models.CharField(max_length=255) #
    birth_year = models.CharField(max_length=6) # tug'ilgan yili
    position = models.CharField(max_length=255) # lavozim
    region = models.CharField(max_length=255) # viloyat
    nationality = models.CharField(max_length=255) # millati
    education = models.CharField(max_length=100) # ta'lim
    experience = models.CharField(max_length=255) # ish tajribasi
    marriage = models.BooleanField(default=False) # oilaviy ahvoli
    first_answer = models.TextField(blank=True, null=True) # qaysi korxonalarda ishlaganligi
    salary = models.CharField(max_length=255) # kutayotgan maosh
    second_answer = models.TextField(blank=True, null=True) # qancha muddat ishlay olishi
    convince = models.BooleanField(default=False) # sudlanganlik
    driver_license = models.CharField(max_length=100) # haydovchilik guvohnomasi
    has_car = models.BooleanField(default=False) # mashina borligi
    third_answer = models.CharField(max_length=25) # word dasturida ishlay olish darajasi
    fourth_answer = models.CharField(max_length=25) # excel dasturida ishlay olish darajasi
    fifth_answer = models.TextField() # boshqa dasturlarda ishlay olish darajasi
    image = models.CharField(max_length=255) # foydalanuvchi rasmi(telegram file id)

    created_at = models.DateTimeField(auto_now_add=True) # qachon yaratilganligi
    updated_at = models.DateTimeField(auto_now=True) # qachon yangilanganligi

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        ordering = ['-created_at']