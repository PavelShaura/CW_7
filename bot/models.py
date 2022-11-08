from django.db import models

from core.models import User


class TgUser(models.Model):

    chat_id = models.BigIntegerField(verbose_name=' TG Chat ID', unique=True)
    username = models.CharField(max_length=255, verbose_name='TG username', unique=True, blank=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    verification_code = models.CharField(max_length=100, unique=True, blank=True, default=None)

    class Meta:
        verbose_name = "Телеграм Пользователь"
        verbose_name_plural = "Телеграмм Пользователи"
