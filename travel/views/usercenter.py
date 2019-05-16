from logging import getLogger
from django.http import HttpResponse, Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from core.bean.wrapper import Wrapper, SUCCESS, FAIL
from travel.serializers import UserSerializer, ArticleSerializer, PreviewArticleSerializer, CollectedArticleSerializer
from travel.views import UserBase, ArticleBase
from travel.models import User, Article, CollectedArticle
from travel.bean.constant import ArticleStatus, Role
from travel.bean.articlewrapper import ArticleWrapper

from core.decorators.authorization import Authorization
logger = getLogger(__name__)

class UserCenterBase(UserBase, ArticleBase):
    def isAdmin(self, request):
        uid = request.session.get('uid', None)
        user = super().get_user(uid)
        if user.role == Role.ADMIN:
            return True
        return False

class UserCenterUserModify(UserCenterBase, APIView):

    @Authorization
    def put(self, request):
        uid = request.session.get('uid', None)
        user = self.get_user(uid)
        if (user is None):
            return FAIL

        ret = UserSerializer(user).data
        ret.update(request.data['data'])
        user = User(**ret)
        user.save()
        return SUCCESS

class UserCenterArticleList(UserCenterBase, APIView):
    @Authorization
    def get(self, request):
        uid = request.session.get('uid', None)
        arts = super().get_article_by_uid(uid)
        serializer = ArticleSerializer(arts, many=True)
        return Response(ArticleWrapper(
            data = {'articles': serializer.data}
        ))

class UserCenterCollectList(UserCenterBase, APIView):
    @Authorization
    def get(self, request):
        uid = request.session.get('uid', None)
        articles = CollectedArticle.objects.filter(user = uid)
        serializer = CollectedArticleSerializer(articles, many=True)
        collects = serializer.data
        
        return Response(ArticleWrapper(data = {
            'articles': [collect['article'] for collect in collects]
        }))

class AdminCenterArticleList(UserCenterBase, APIView):
    @Authorization
    def get(self, request, offset, limit):
        if super().isAdmin(request):
            serializer = ArticleSerializer(super().articles(offset, limit), many=True)
            return Response(ArticleWrapper(data={
                'articles': serializer.data
            }))
        return Response(status=status.HTTP_403_FORBIDDEN)

class AdminCenterArticleCheck(UserCenterBase, APIView):
    @Authorization
    def put(self, request, pk, status):
        if super().isAdmin(request):
            article = super().get_article(pk)
            if article.status == ArticleStatus.WAIT:
                article.status = status
                article.save()
                return SUCCESS
            return FAIL
        return Response(status=status.HTTP_403_FORBIDDEN)

    