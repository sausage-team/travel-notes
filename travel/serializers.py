from rest_framework import serializers
from travel.models import User, Article

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'uid', 'username', 'password', 'id_card')

class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        allow_null=True,
        read_only=True,
        required=False
    )
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_time', 'updated_time', 'user')
