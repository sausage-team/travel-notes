from django.db import models
from uuid import uuid4
from travel.bean.constant import Role, Icon

class User(models.Model):
    uid = models.CharField(max_length=40, default = str(uuid4()))
    username = models.CharField(max_length = 100, blank = False, default='')
    password = models.CharField(max_length = 100, blank = False)
    id_card = models.CharField(max_length = 18, blank = False)
    role = models.IntegerField(default=Role.NORMAL)
    icon = models.TextField(default=Icon.DEFAULT_ICON)
