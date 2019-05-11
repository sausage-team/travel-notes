"""
Travel Notes Router
"""
from django.urls import path
from travel import views

urlpatterns = [
    path('travel', views.TravelView.as_view()),
    path('user', views.UserView.as_view()),
    path('article/<int:pk>', views.ArticleView.as_view()),
    path('article', views.ArticlePost.as_view()),
]
