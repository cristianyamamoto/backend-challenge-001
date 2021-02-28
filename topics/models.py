from django.db import models
from helpers.models import TimestampModel
from django.conf import settings


class Topic(TimestampModel):
    title = models.CharField(max_length=128, blank=False)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256, blank=True)
    url_name = models.SlugField(max_length=64, unique=True, db_index=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    class Meta:
        ordering = ['updated_at']

    # Shows up in the admin list
    def __str__(self):
        return self.title

