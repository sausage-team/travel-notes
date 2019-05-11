from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField(default='')
    created_time = models.DateTimeField(default = timezone.now)
    updated_time = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ('created_time',)