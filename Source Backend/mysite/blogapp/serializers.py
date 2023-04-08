
from rest_framework import serializers, fields
from .models import User, Article, Comments, Avatar, CoverImage

class ArticleSerializer(serializers.ModelSerializer ):
    class Meta:
        model = Article
        fields = ['id', 'id_user', 'title', 'content', 'created_at', 'updated_at']

class CommentsSerializer(serializers.ModelSerializer ):
    class Meta:
        model = Comments
        fields = ['id', 'id_user', 'id_article', 'content', 'created_at', 'updated_at']

class AvatarSerializer(serializers.ModelSerializer ):
    #id_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)
    class Meta:
        model = Avatar
        fields = ['id', 'id_user', 'path']

class CoverImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoverImage
        fields = ['id', 'id_article', 'path']

class SearchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'fullname']

class SearchArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'fullname', 'gender' , 'date_of_birth']
        extra_kwargs = {'password': {'write_only': True}}

    

class UserUpdateSerializer(serializers.ModelSerializer):
    avatar = AvatarSerializer(required=False, allow_null=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'fullname', 'gender', 'date_of_birth', 'avatar']
        extra_kwargs = {'password': {'write_only': True}}
        
     

class UserPasswordUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('password',)

    # def validate_password(self, value):
    #     if len(value) <= 6:
    #         raise serializers.ValidationError('Password must be at least 6 characters long')
    #     return value
