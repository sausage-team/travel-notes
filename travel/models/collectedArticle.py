from django.db import models
from django.utils import timezone
from .article import Article

# Create your models here.

class CollectedArticle(models.Model):
    article = models.OneToOneField(Article, on_delete=models.DO_NOTHING)
    user = models.IntegerField()