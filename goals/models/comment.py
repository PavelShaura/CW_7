from django.db import models

from core.models import User
from .goal import Goal
from .dates_mixin import DatesModelMixin


class Comment(DatesModelMixin):
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    user = models.ForeignKey(User, verbose_name="Автор", on_delete=models.PROTECT)
    goal = models.ForeignKey(Goal, verbose_name="Цель", on_delete=models.CASCADE)
    text = models.CharField(verbose_name="Текст", max_length=1200)
