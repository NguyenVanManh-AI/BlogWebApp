from rest_framework import serializers, fields
from .models import User, Article, Comments, Avatar, CoverImage



##
class UserSerializer(serializers.ModelSerializer):
    # date_of_birth = fields.DateField(input_formats=['%Y-%m-%dT%'])

    class Meta:
        model = User
        fields = ('url', 'id', 'email', 'username', 'password', 'fullname', 'gender' , 'date_of_birth')
        extra_kwargs = {'password': {'write_only': True}}

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'id', 'username', 'password', 'email', 'fullname', 'gender', 'date_of_birth']

class ArticleSerializer(serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Article
        fields = ['url', 'id', 'id_user', 'title', 'content', 'created_at', 'updated_at']

class CommentsSerializer(serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Comments
        fields = ['url', 'id', 'id_user', 'id_article', 'content', 'created_at', 'updated_at']

class AvatarSerializer(serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Avatar
        fields = ['url', 'id', 'id_user', 'path']

class CoverImageSerializer(serializers.ModelSerializer ):
    class Meta:
        model = CoverImage
        fields = ['url', 'id', 'id_article', 'path']


class SearchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'fullname']

class SearchArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title']
