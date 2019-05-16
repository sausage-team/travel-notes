from django.db import models
from django.utils import timezone

# Create your models here.

class ThumbUpArticle(models.Model):
    article_id = models.IntegerField()
    user_id = models.IntegerField()