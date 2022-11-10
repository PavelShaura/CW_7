from django.db import models

from core.models import User


class TgUser(models.Model):

    chat_id = models.BigIntegerField(verbose_name='TG chat ID', unique=True)
    username = models.CharField(verbose_name='TG user ', max_length=255, null=True, blank=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    verification_code = models.CharField(max_length=100, null=True, blank=True, default=None)

    class Meta:
        verbose_name = 'Телеграм Пользователь'
        verbose_name_plural = 'Телеграм Пользователи'
