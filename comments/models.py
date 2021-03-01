from django.db import models
from helpers.models import TimestampModel
from posts.models import Post
from django.conf import settings


class Comment(TimestampModel):
    title = models.CharField(max_length=128, blank=False)
    content = models.TextField(blank=False)
    post = models.ForeignKey(
        Post, related_name='comments',
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='comments',
        on_delete=models.CASCADE)

    class Meta:
        ordering = ['-updated_at']

    # Shows up in the admin list
    def __str__(self):
        return self.title

