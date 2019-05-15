from django.db import models
from django.utils import timezone
from travel.bean.constant import ArticleStatus
from . import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    author = models.CharField(max_length=10,default='')
    cover = models.CharField(max_length=100,default='')
    preview = models.TextField(default='')
    content = models.TextField(default='')
    created_time = models.DateTimeField(default = timezone.now)
    updated_time = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, related_name="articles", on_delete=models.SET_NULL, null=True)
    status = models.IntegerField(default=ArticleStatus.WAIT)
    thumb = models.IntegerField(default=0)
    frequency = models.IntegerField(default=0)
    category = models.IntegerField(default=0)

class ArticleImage(models.Model):
    img = models.TextField()
    img_type = models.CharField(max_length=10)
    article_id = models.IntegerField(default=-1)
    created_time = models.DateTimeField(default = timezone.now)
    updated_time = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ('created_time',)