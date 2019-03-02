from django.db import models
from django.utils import timezone
from datetime import datetime, date
import time
import json

# Create your models here.
class BaseModel(models.Model):
    class Meta:
        abstract = True

    def getRefFields(self):
        pass

    def ignoreFields(self):
        pass

    def isAttrInstance(self, attr, cls):
        return isinstance(getattr(self,attr), cls)

    def to_dict(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)

        res_dict = {}

        for attr in fields:
            if self.isAttrInstance(attr, datetime) or \
                    self.isAttrInstance(attr, date):
                res_dict[attr] = time.mktime(getattr(self, attr).timetuple())
            elif self.isAttrInstance(attr, BaseModel):
                res_dict[attr] = getattr(self,attr).to_dict()
            elif self.isAttrInstance(attr,(int,bool,float,str,list,dict,set,tuple)):
                res_dict[attr] = getattr(self, attr)

        if 'basemodel_ptr' in res_dict:
            res_dict.pop('basemodel_ptr')
        
        ignores = self.ignoreFields()
        if ignores is not None:
            for ig in ignores:
                res_dict.pop(ig)

        return res_dict
    
    def to_json(self):
        return json.dumps(self.to_dict(), ensure_ascii=False).encode("utf-8").decode()

class Question(BaseModel):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date_published")

    def __str__(self):
        return self.question_text

class Choice(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
