from logging import getLogger
from django.http import HttpResponse, Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from travel.serializers import UserSerializer, ArticleSerializer
from travel.views import UserBase, ArticleBase
from travel.models import User, Article
from core.bean.wrapper import Wrapper, SUCCESS, FAIL
from travel.bean.constant import ArticleStatus, Role
from core.decorators.authorization import Authorization
logger = getLogger(__name__)

class UserCenterBase(UserBase, ArticleBase):
    def isAdmin(self, request):
        uid = request.session.get('uid', None)
        user = super().get_user(uid)
        if user.role == Role.ADMIN:
            return True
        return False

class UserCenterArticleList(UserCenterBase, APIView):
    @Authorization
    def get(self, request):
        uid = request.session.get('uid', None)
        arts = super().get_article_by_uid(uid)
        serializer = ArticleSerializer(arts, many=True)
        return Response(data=serializer.data)

class AdminCenterArticleList(UserCenterBase, APIView):
    @Authorization
    def get(self, request, offset, limit):
        if super().isAdmin(request):
            serializer = ArticleSerializer(super().articles(offset, limit), many=True)
            return Response(data=serializer.data)
        return Response(status=status.HTTP_403_FORBIDDEN)

class AdminCenterArticleCheck(UserCenterBase, APIView):
    @Authorization
    def put(self, request, pk):
        if super().isAdmin(request):
            article = super().get_article(pk)
            if article.status == ArticleStatus.WAIT:
                article.status = ArticleStatus.PASS
                article.save()
                return SUCCESS
            return FAIL
        return Response(status=status.HTTP_403_FORBIDDEN)

    