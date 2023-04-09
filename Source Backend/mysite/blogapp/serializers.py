
from rest_framework import serializers
from .models import User, Article, Comments



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'fullname', 'gender' , 'date_of_birth', 'avatar']
        extra_kwargs = {'password': {'write_only': True}}




class ArticleSerializer(serializers.ModelSerializer ):
    class Meta:
        model = Article
        fields = ['id', 'id_user', 'title', 'content', 'created_at', 'updated_at']




class CommentsSerializer(serializers.ModelSerializer ):
    class Meta:
        model = Comments
        fields = ['id', 'id_user', 'id_article', 'content', 'created_at', 'updated_at']




class SearchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'fullname']

class SearchArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title']



    
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'fullname', 'gender', 'date_of_birth', 'avatar']
        
     

class UserPasswordUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    oldpassword = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('password', 'oldpassword')

class CommentWithUserInfoSerializer(serializers.ModelSerializer):
    fullname = serializers.CharField(source='id_user.fullname', read_only=True)
    avatar = serializers.ImageField(source='id_user.avatar', read_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'id_user', 'id_article', 'content', 'created_at', 'updated_at', 'fullname', 'avatar']