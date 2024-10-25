from django.contrib import admin
from .models import BotUser, UserRequest


class BotUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'first_name', 'last_name', 'username')
    search_fields = ('user_id', 'first_name', 'last_name', 'username')
    list_filter = ('first_name', 'last_name', 'username')
    empty_value_display = '-empty-'
    list_per_page = 10


class UserRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'birth_year', 'position', 'region', 'nationality', 'education', 'experience', 'marriage', 'first_answer', 'salary', 'second_answer', 'convince', 'driver_license', 'has_car', 'third_answer', 'fourth_answer', 'fifth_answer')
    search_fields = ('full_name', 'phone_number', 'birth_year', 'position', 'region', 'nationality', 'education', 'experience', 'marriage', 'first_answer', 'salary', 'second_answer', 'convince', 'driver_license', 'has_car', 'third_answer', 'fourth_answer', 'fifth_answer')
    list_filter = ('full_name', 'phone_number', 'birth_year', 'position', 'region', 'nationality', 'education', 'experience', 'marriage', 'first_answer', 'salary', 'second_answer', 'convince', 'driver_license', 'has_car', 'third_answer', 'fourth_answer', 'fifth_answer')
    empty_value_display = '-empty-'
    list_per_page = 10


admin.site.register(BotUser, BotUserAdmin)
admin.site.register(UserRequest, UserRequestAdmin)