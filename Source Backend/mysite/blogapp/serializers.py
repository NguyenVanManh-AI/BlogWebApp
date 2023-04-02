from rest_framework import serializers
from .models import User, Article, Comments, Avatar, CoverImage

<<<<<<< HEAD
##
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'email', 'username', 'password', 'fullname', 'gender' , 'date_of_birth')
        extra_kwargs = {'password': {'write_only': True}}

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'id', 'username', 'password', 'email', 'fullname', 'gender', 'date_of_birth']
=======
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'password', 'email', 'fullname', 'gender', 'date_of_birth']
>>>>>>> c0eca83a2afc90e9ce247e3690163f5506aef4f3

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
<<<<<<< HEAD
        fields = ['url', 'id', 'id_article', 'path']
=======
        fields = ['url', 'id', 'id_article', 'path']
>>>>>>> c0eca83a2afc90e9ce247e3690163f5506aef4f3
