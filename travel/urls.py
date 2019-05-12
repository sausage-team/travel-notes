"""
Travel Notes Router
"""
from django.urls import path
from travel import views

urlpatterns = [
    path('user/login', views.UserLogin.as_view()),
    path('user/logout', views.UserLogout.as_view()),
    path('user/register', views.UserRegister.as_view()),
    path('user/forget', views.UserForgetPwd.as_view()),
    path('user/<slug:uid>', views.UserView.as_view()),
    path('article/<int:pk>', views.ArticleView.as_view()),
    path('article', views.ArticlePost.as_view()),
    path('article/<int:offset>/<int:limit>', views.ArticleList.as_view()),
    path('ucenter/articles', views.UserCenter.as_view())
]
