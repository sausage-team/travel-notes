from django.db import models
class User(models.Model):
    username = models.CharField(max_length = 100, blank = False, default='')
    password = models.CharField(max_length = 100, blank = False)
    idCard = models.CharField(max_length = 11, blank = False)