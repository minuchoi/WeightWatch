from django.contrib import admin

# Register your models here.
from .models import UserDetail


@admin.register(UserDetail)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ['username', 'password']