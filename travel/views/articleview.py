"""
Article Operation
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from travel.serializers import ArticleSerializer
from travel.models import Article

class ArticleView(APIView):
    def get_article(self, pk):
        """
        Find article by id
        """
        try:
            return Article.objects.get(id=pk)
        except Article.DoesNotExist:
            return None
    
    def get(self, request, pk):
        """
        Request article By id
        """
        article = self.get_article(pk)
        if (article is None):
            return Response({'status': -1})

        serializer = ArticleSerializer(data=article)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        """
        Delete article by id
        """
        article = self.get_article(pk)
        if (article is None):
            return Response({'status': -1})

        article.delete()
    
    def put(self, request, pk):
        """
        Update article by id
        """
        article = self.get_article(pk)
        if (article is None):
            return Response({'status': -1})
        
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':0})
        return Response({'status': -1})
    
class ArticlePost(ArticleView):
    def post(self, request):
        """
        Create article by id
        """
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':0})
        return Response({'status': -1})
    
    


    
