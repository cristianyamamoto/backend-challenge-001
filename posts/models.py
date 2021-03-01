from django.db import models
from helpers.models import TimestampModel
from topics.models import Topic
from django.conf import settings


class Post(TimestampModel):
    title = models.CharField(max_length=128, blank=False)
    content = models.TextField(blank=True)
    topic = models.ForeignKey(
        Topic, related_name='posts',
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='posts',
        on_delete=models.CASCADE)

    class Meta:
        ordering = ['-updated_at']

    # Shows up in the admin list
    def __str__(self):
        return self.title

