from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Student)
class StudentAdminModal(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "mobile", "email")
