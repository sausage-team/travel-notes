"""
Article Operation
"""
from logging import getLogger
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from travel.serializers import ArticleSerializer
from travel.models import Article
from travel.bean.wrapper import Wrapper, SUCCESS, FAIL
from core.decorators.authorization import Authorization
from travel.bean.constant import ArticleStatus
logger = getLogger(__name__)

class ArticleBase(object):
    def get_article(self, pk):
        """
        Find article by id
        """
        try:
            return Article.objects.get(id=pk)
        except Article.DoesNotExist:
            return None
    def get_article_by_uid(self, uid):
        """
        Find articles by uid
        """
        try:
            return Article.objects.filter(user_id=uid)
        except Article.DoesNotExist:
            return []
    def articles(self):
        # TODO
        # Paginator
        try:
            return Article.objects.all()
        except Article.DoesNotExist:
            return []

class ArticleView(ArticleBase, APIView):
    """
    Basic Article View
    """
    def get(self, request, pk):
        """
        Request article By id
        """
        article = self.get_article(pk)
        if (article is None
            || article.status == ArticleStatus.WAIT):
            return FAIL

        serializer = ArticleSerializer(data=article)
        return Response(Wrapper(data=serializer.data))
    
    @Authorization
    def delete(self, request, pk):
        """
        Delete article by id
        """
        article = self.get_article(pk)
        if (article is None):
            return FAIL
        uid = request.session.get('uid', None)
        if uid == article.user_id:
            article.delete()
            return SUCCESS
        return FAIL
    
    @Authorization
    def put(self, request, pk):
        """
        Update article by id
        """
        article = self.get_article(pk)
        if (article is None):
            return FAIL
        uid = request.session.get('uid', None)
        if uid != article.user_id:
            return FAIL

        serializer = ArticleSerializer(article, data=request.data['data'])
        if serializer.is_valid():
            serializer.save()
            return SUCCESS
        return FAIL

class ArticlePost(ArticleView):
    @Authorization
    def post(self, request):
        """
        Create article by id
        """
        uid = request.session.get('uid', None)

        if uid is None:
            return Response(status=status.HTTP_403_FORBIDDEN)

        article = request.data['data']
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid():
            article = serializer.save()
            article.user_id = uid
            article.save()
            return Response(Wrapper(data=serializer.data))
        return FAIL

class ArticleList(ArticleView):
    def get(self, request, offset, limit):
        """
        Request Article List
        """
        articles = Article.objects.filter(status = ArticleStatus.PASS)[offset:offset+limit]
        serializer = ArticleSerializer(articles, many=True)
        return Response(Wrapper(data=serializer.data))

