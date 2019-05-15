"""
Article Operation
"""
from base64 import b64decode
from logging import getLogger
from django.http import HttpResponse, Http404
from django.db import transaction
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from core.bean.wrapper import Wrapper, SUCCESS, FAIL
from core.decorators.authorization import Authorization
from travel.serializers import ArticleSerializer, ArticleImageSerializer, PreviewArticleSerializer
from travel.models import User, Article, ArticleImage, CollectedArticle
from travel.bean.constant import ArticleStatus, SortType
from travel.bean.articlewrapper import ArticleWrapper
from .imagetransfer import ImageTransfer
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
    def articles(self, offset=0, limit=10, status = 1):
        try:
            if status:
                return Article.objects.filter(status=status)[offset:offset+limit]
            return Article.objects.all()[offset:offset+limit]
        except Article.DoesNotExist:
            return []
    
    def get_article_cover(self, pk):
        try:
            return ArticleImage.objects.get(id = pk)
        except ArticleImage.DoesNotExist:
            return None


class ArticleView(ArticleBase, APIView):
    """
    Basic Article View
    """
    def get(self, request, pk):
        """
        Request article By id
        """
        try:
            article = self.get_article(pk)
            if (article is None
                or article.status == ArticleStatus.WAIT):
                return FAIL
            with transaction.atomic():
                article.frequency = article.frequency + 1
                article.save()
            serializer = ArticleSerializer(article)
            return Response(ArticleWrapper(data=serializer.data))
        except Exception as e:
            logger.error(e)
            return FAIL
    
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
            return Response(ArticleWrapper(data=serializer.data))
        return FAIL

class ArticleThumbUp(ArticleView):
    @Authorization
    def put(self, request, pk):
        """
        Thumb Up Article
        """
        try:
            with transaction.atomic():
                article = self.get_article(pk)
                if article is None:
                    return FAIL
                article.thumb = article.thumb + 1
                article.save()
                return SUCCESS
        except Exception as e:
            logger.error(e)
            return FAIL

class ArticleCollect(ArticleView):
    @Authorization
    def put(self, request, pk):
        """
        Collect Article
        """
        article = self.get_article(pk)
        if article is None:
            return FAIL
        uid = request.session.get('uid', None)
        CollectedArticle.objects.create(user=uid, article = article)
        return SUCCESS

    @Authorization
    def delete(self, request, pk):
        """
        Delete Collected Artcile
        """
        article = self.get_article(pk)
        if article is None:
            return FAIL
        uid = request.session.get('uid', None)
        ret = CollectedArticle.objects.filter(user=uid, article=article)
        if ret:
            ret.delete()
            return SUCCESS
        return FAIL

class ArticleList(ArticleView):
    def get(self, request, offset, limit):
        """
        Request Article List
        """
        params = {
            'status': ArticleStatus.PASS,
        }
        uid = request.session.get('uid', None)
        if uid:
            user = User.objects.get(id = uid)
            if user.prefer:
                params['category'] = user.prefer
        data = Article.objects.filter(**params).order_by('-updated_time')
        count = data.count()

        if count < limit:
            data = Article.objects.filter(status = ArticleStatus.PASS).order_by('-updated_time')

        articles = data[offset:offset+limit]
        serializer = PreviewArticleSerializer(articles, many=True)
        return Response(ArticleWrapper(data={
            'articles':serializer.data,
            'count': count
        }))
    
    def post(self, request, offset, limit):
        """
        Request Article List by
        """
        data = request.data['data']
        search = data['search']
        filter_type = data['filter_type']
        sort_type = data['sort_type']

        params = {}
        if search:
            params['title__icontains'] = search
        if filter_type:
            params['category'] = filter_type

        data = Article.objects.filter(
            status = ArticleStatus.PASS, 
            **params
        )
        if sort_type == SortType.THUMB:
            data = data.order_by('-thumb')
        elif sort_type == SortType.FREQ:
            data = data.order_by('-frequency')

        articles = data[offset:offset+limit]
        serializer = PreviewArticleSerializer(articles, many=True)
        return Response(ArticleWrapper(data={
            'articles':serializer.data,
            'count': data.count()
        }))

class ArticleImageGet(ArticleView):
    def get(self, request, pk):
        cover = self.get_article_cover(pk)
        serializer = ArticleImageSerializer(cover)
        data = serializer.data
        img = b64decode(data['img'])
        return HttpResponse(img, content_type=f"image/{data['img_type']}")

class ArticleImagePost(ImageTransfer, ArticleView):
    @Authorization
    def post(self, request):
        img = request.FILES.get('upload', None)
        if img is None:
            return FAIL
        b64_img = self.img2base64(img)
        img_type = img.name.split('.')[-1]
        cover = ArticleImage.objects.create(
            img=b64_img,
            img_type=img_type
        )
        return Response(
            {
                'fileName':'Sausage',
                'uploaded':1,
                'id': cover.id,
                'url': f'/api/article/cover/{cover.id}'
            }
        )