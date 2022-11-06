from django.db import models
from django.utils import timezone


class DatesModelMixin(models.Model):
    class Meta:
        # mark class as abstract, table in the db won't be created
        abstract = True

    created = models.DateTimeField(verbose_name="Дата создания")
    updated = models.DateTimeField(verbose_name="Дата последнего обновления")

    def save(self, *args, **kwargs):
        # when object is created it has no id
        if not self.id:
            self.created = timezone.now()
        # each time when save is called set new date
        self.updated = timezone.now()
        return super().save(*args, **kwargs)