"""
Article Operation
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from travel.serializers import ArticleSerializer
from travel.models import Article
from travel.bean.wrapper import Wrapper, SUCCESS, FAIL

class ArticleView(APIView):
    """
    Basic Article View
    """
    def get_article(self, id):
        """
        Find article by id
        """
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return None
    
    def get(self, request, id):
        """
        Request article By id
        """
        article = self.get_article(id)
        if (article is None):
            return FAIL

        serializer = ArticleSerializer(data=article)
        return Response(Wrapper(data=serializer.data))
    
    def delete(self, request, id):
        """
        Delete article by id
        """
        article = self.get_article(id)
        if (article is None):
            return FAIL

        article.delete()
    
    def put(self, request, id):
        """
        Update article by id
        """
        article = self.get_article(id)
        if (article is None):
            return FAIL
        
        serializer = ArticleSerializer(article, data=request.data['data'])
        if serializer.is_valid():
            serializer.save()
            return SUCCESS
        return FAIL

class ArticlePost(ArticleView):
    def post(self, request):
        """
        Create article by id
        """
        serializer = ArticleSerializer(data=request.data['data'])
        if serializer.is_valid():
            serializer.save()
            return Response(Wrapper(data=serializer.data))
        return FAIL

class ArticleList(ArticleView):
    def get(self, request, offset, limit):
        """
        Request Article List
        """
        articles = Article.objects.all()[offset:offset+limit]
        serializer = ArticleSerializer(articles, many=True)
        return Response(Wrapper(data=serializer.data))

