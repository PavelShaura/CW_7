from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from typing import List

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    readonly_fields = ('last_login', 'date_joined')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info',
        {'fields': ('first_name', 'last_name', 'email')},
         ),
        ('Permission',
         {'fields': ('last_login', 'date_joined')}),
        ('Important dates',
        {'fields': ('is_active', 'is_superuser')})
    )
