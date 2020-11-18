from django.contrib import admin

# Register your models here.
from .models import User, Weight


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']


@admin.register(Weight)
class Weight(admin.ModelAdmin):
    list_display = ['user', 'weight', 'time']




