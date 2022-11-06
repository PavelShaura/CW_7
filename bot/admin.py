from django.contrib import admin

from bot.models import TgUser


class BotAdmin(admin.ModelAdmin):
    list_display = ("tg_user_id", "tg_chat_id", "user")
    search_fields = ("tg_user_id", "tg_chat_id", "user")

admin.site.register(TgUser,BotAdmin)
