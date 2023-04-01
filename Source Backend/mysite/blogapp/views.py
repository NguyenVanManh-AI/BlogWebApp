from rest_framework import viewsets
from .models import User, Article, Comments, Avatar, CoverImage
from .serializers import UserSerializer, ArticleSerializer, CommentsSerializer, AvatarSerializer, CoverImageSerializer

# Viewsets for User model
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Viewsets for Article model
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# Viewsets for Comments model
class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

# Viewsets for Avatar model
class AvatarViewSet(viewsets.ModelViewSet):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer

# Viewsets for CoverImage model
class CoverImageViewSet(viewsets.ModelViewSet):
    queryset = CoverImage.objects.all()
    serializer_class = CoverImageSerializer