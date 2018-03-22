from django.db import models
from django.conf import settings

from app.utils.models import TimeStampModel


class Post(TimeStampModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='posts',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(blank=True)

