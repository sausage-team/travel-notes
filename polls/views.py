from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views import View
from django.db.models import QuerySet
from .models import BaseModel, Question, Choice

# Create your views here.

#funciton-level view
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#class-level view
class JsonView(View):
    def dispatch(self,request, *args, **kwargs):
        res = super().dispatch(request,*args,**kwargs)
        if isinstance(res,QuerySet):
            res = [obj.to_json() for obj in res]
        elif isinstance(res, BaseModel):
            res = res.to_json()
        else:
            return JsonResponse(res, safe = False)
        
        return HttpResponse(res, content_type="application/json")

class TestView(JsonView):
    def get(self, request):
        question = Question.objects.get(pk=1)
        return question


