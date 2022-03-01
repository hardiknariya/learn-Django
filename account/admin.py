from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import *


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdminModal(admin.ModelAdmin):
    model = CustomUser
    list_display = ("id", "first_name", "last_name", "email")
