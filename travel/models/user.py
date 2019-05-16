from django.db import models
from uuid import uuid4
from travel.bean.constant import Role, Icon

class User(models.Model):
    username = models.CharField(max_length = 100, blank = False)
    password = models.CharField(max_length = 100, blank = False)
    phone = models.CharField(max_length = 18, blank = True, default='')
    prefer = models.IntegerField(default=0)
    place = models.CharField(max_length=20, default='')
    role = models.IntegerField(default=Role.NORMAL)
    icon = models.TextField(default=Icon.DEFAULT_ICON)
