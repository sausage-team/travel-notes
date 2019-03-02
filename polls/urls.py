from django.urls import path

from . import views

urlpatterns = [
    path("json_clz_test/",views.TestView.as_view(), name="json_clz_test"),
    path("",views.index, name='index'),
]
