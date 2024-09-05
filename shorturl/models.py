from django.db import models
from datetime import timedelta
from django.utils.timezone import now

from sqids import Sqids


def expiration(days: int) -> timedelta:
    return now() + timedelta(days=days)


class URLMapping(models.Model):
    original_url = models.CharField(max_length=2048, blank=False)
    short_url = models.CharField(max_length=20, unique=True)
    expiration_date = models.DateTimeField()

    @property
    def get_unique_string(self):
        if self.pk is None and URLMapping.objects.last():
            new_pk = URLMapping.objects.last().id + 1
        elif self.pk is None:
            new_pk = 1
        sqids = Sqids(min_length=8)
        unique_string = sqids.encode([new_pk])
        return unique_string

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.get_unique_string
            self.expiration_date = expiration(days=30)
        super(URLMapping, self).save(*args, **kwargs)
