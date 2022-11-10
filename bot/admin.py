from django.contrib import admin

from bot.models import TgUser
from goals.admin import BaseAdmin


class TelegramUserAdmin(BaseAdmin):
    list_display = ('chat_id', 'username', 'user')
    readonly_fields = ('chat_id', 'verification_code')


admin.site.register(TgUser, TelegramUserAdmin)
