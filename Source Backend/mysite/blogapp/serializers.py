from rest_framework import serializers
from .models import User, Article, Comments, Avatar, CoverImage

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'password', 'email', 'fullname', 'gender', 'date_of_birth']

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ['url', 'id', 'id_user', 'title', 'content', 'created_at', 'updated_at']

class CommentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comments
        fields = ['url', 'id', 'id_user', 'id_article', 'content', 'created_at', 'updated_at']

class AvatarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Avatar
        fields = ['url', 'id', 'id_user', 'path']

class CoverImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CoverImage
        fields = ['url', 'id', 'id_article', 'path']