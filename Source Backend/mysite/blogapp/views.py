from rest_framework import viewsets
from .models import User, Article, Comments, Avatar, CoverImage
from .serializers import UserSerializer, ArticleSerializer, CommentsSerializer, AvatarSerializer, CoverImageSerializer

<<<<<<< HEAD
##
from rest_framework.views import APIView, status
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password

=======
>>>>>>> c0eca83a2afc90e9ce247e3690163f5506aef4f3
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
<<<<<<< HEAD
    serializer_class = CoverImageSerializer


class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            user = serializer.save()
            
            return JsonResponse({
                'message': 'Register successful!'
            }, status=status.HTTP_201_CREATED)

        else:
            return JsonResponse({
                'error_message': 'Error!',
                'errors_code': 400,
            }, status=status.HTTP_400_BAD_REQUEST)
=======
    serializer_class = CoverImageSerializer
>>>>>>> c0eca83a2afc90e9ce247e3690163f5506aef4f3
