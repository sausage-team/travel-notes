from rest_framework import serializers
from travel.models import User, Article, ArticleImage
class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'uid', 'username', 'password', 'id_card', 'role', 'icon')

class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        allow_null=True,
        read_only=True,
        required=False
    )
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_time', 'updated_time', 'user', 'status')
    
    def to_representation(self, instance):
        representation = super(ArticleSerializer, self).to_representation(instance)
        representation['created_time'] = int(round(instance.created_time.timestamp() * 1000))
        representation['updated_time'] = int(round(instance.updated_time.timestamp() * 1000))
        return representation

class ArticleImageSerializer(serializers.ModelSerializer):
    img = serializers.CharField(required=False)
    class Meta:
        model = ArticleImage
        fields = ('id', 'article_id', 'img', 'img_type')


