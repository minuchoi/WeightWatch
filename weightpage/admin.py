from django.contrib import admin

# Register your models here.
from .models import User, Weight, SideBar


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']


@admin.register(Weight)
class Weight(admin.ModelAdmin):
    list_display = ['user', 'weight', 'time']

@admin.register(SideBar)
class SideBar(admin.ModelAdmin):
    list_display = ['title', 'icon', 'url']



