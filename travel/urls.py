"""
Travel Notes Router
"""
from django.urls import path
from travel import views

urlpatterns = [
    path('captcha', views.CaptchView.as_view()),
    path('user/login', views.UserLogin.as_view()),
    path('user/logout', views.UserLogout.as_view()),
    path('user/register', views.UserRegister.as_view()),
    path('user/forget', views.UserForgetPwd.as_view()),
    path('user/<int:uid>', views.UserView.as_view()),
    path('article', views.ArticlePost.as_view()),
    path('article/cover', views.ArticleImagePost.as_view()),
    path('article/cover/<int:pk>', views.ArticleImageGet.as_view()),
    path('article/collect/<int:pk>', views.ArticleCollect.as_view()),
    path('article/thumb/<int:pk>', views.ArticleThumbUp.as_view()),
    path('article/<int:pk>', views.ArticleView.as_view()),
    path('article/<int:offset>/<int:limit>', views.ArticleList.as_view()),
    path('ucenter/articles/collections', views.UserCenterCollectList.as_view()),
    path('ucenter/articles', views.UserCenterArticleList.as_view()),
    path('admin/articles/<int:offset>/<int:limit>', views.AdminCenterArticleList.as_view()),
    path('admin/article/<int:pk>/<int:status>', views.AdminCenterArticleCheck.as_view()),
]