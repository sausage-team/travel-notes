from logging import getLogger
from django.http import HttpResponse, Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from travel.serializers import UserSerializer, ArticleSerializer
from travel.views import UserBase, ArticleBase
from travel.models import User, Article
from travel.bean.wrapper import Wrapper, SUCCESS, FAIL
logger = getLogger(__name__)

class UserCenterBase(UserBase, ArticleBase):
   pass

class UserCenter(UserCenterBase, APIView):
    def get(self, request):
        uid = request.session.get('uid', None)
        if uid is None:
            return Response(status=status.HTTP_403_FORBIDDEN)

        arts = super().get_article_by_uid(uid)
        serializer = ArticleSerializer(arts, many=True)
        return Response(data=serializer.data)
    