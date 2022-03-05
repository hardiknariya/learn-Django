from django.contrib import admin
from account.models import *
from django.contrib.auth.models import Group


# Register your models here.
admin.site.unregister(Group)


@admin.register(CustomUser)
class CustomUserAdminModal(admin.ModelAdmin):
    model = CustomUser
    list_display = ("id", "first_name", "last_name", "email")
