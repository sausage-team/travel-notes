from django.urls import path
from travel import views

urlpatterns = [
    path('list', views.TravelView.as_view()),
    path('user', views.UserView.as_view())
]
