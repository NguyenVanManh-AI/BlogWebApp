from rest_framework import viewsets
from .models import User, Article, Comments
from .serializers import UserPasswordUpdateSerializer, UserSerializer, ArticleSerializer
from .serializers import CommentsSerializer, SearchUserSerializer, CommentWithUserInfoSerializer,SearchArticleSerializer, UserUpdateSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView, status
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password

from rest_framework import generics, permissions

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
                'error_message': 'error',
                'errors_code': 400,
            }, status=status.HTTP_400_BAD_REQUEST)

from django.db.models import Q
from django.http import JsonResponse
class SearchView(generics.ListAPIView):
    serializer_class = None

    def post(self, request):
        search_query = request.data.get('text_search', '')
        query = Q(fullname__icontains=search_query)
        queryset = User.objects.filter(query)[:10]

        data = []
        for user in queryset:
            user_serializer = UserSerializer(user)
            data.append({'user': user_serializer.data})

        if queryset.count() < 10:
            remaining = 10 - queryset.count()
            articles = Article.objects.filter(title__icontains=search_query)[:remaining]

            for article in articles:
                article_serializer = ArticleSerializer(article)
                data.append({'aritcle': article_serializer.data})

        return JsonResponse({'results': data})
    
import os
from django.conf import settings
class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        if 'avatar' in request.data:
            # Xóa ảnh cũ
            if instance.avatar:
                path = instance.avatar.path
                if os.path.isfile(os.path.join(settings.MEDIA_ROOT, path)):
                    os.remove(os.path.join(settings.MEDIA_ROOT, path))
                    
            # Lưu ảnh mới
            instance.avatar = request.data['avatar']


        serializer.save()
        return Response(serializer.data)

    
class UserPasswordUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserPasswordUpdateSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        oldpassword = request.data.get('oldpassword')
        newpassword = make_password(request.data.get('password'))
        if check_password(oldpassword, instance.password):
            instance.password = newpassword
            instance.save(update_fields=['password'])
            serializer = self.get_serializer(instance)
            return Response({'message': 'Password Changed'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Incorrect Old Password'}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET'])
def comments_for_article(request, article_id):
    comments = Comments.objects.filter(id_article=article_id).order_by('-id')
    serializer = CommentWithUserInfoSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def comments(request):
    if request.method == 'GET':
        comments = Comments.objects.all().order_by('-id')
        serializer = CommentWithUserInfoSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentWithUserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PATCH', 'DELETE'])
def comments_by_id(request, id_comment):
    try:
        comment = Comments.objects.get(id=id_comment)
    except Comments.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentWithUserInfoSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = CommentWithUserInfoSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        comment.delete()
        return Response({'message': 'Comment deleted.'}, status=status.HTTP_204_NO_CONTENT)

from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 10

class CustomPagination2(PageNumberPagination):
    page_size = 6

class ArticleListView(APIView):
    def get(self, request):
        paginator = CustomPagination()
        articles = Article.objects.all().order_by('-id')
        paginated_articles = paginator.paginate_queryset(articles, request)
        article_serializer = ArticleSerializer(paginated_articles, many=True)

        data = []
        for article_data in article_serializer.data:
            user = User.objects.get(id=article_data['id_user'])
            user_serializer = UserSerializer(user)
            comments = Comments.objects.filter(id_article=article_data['id']).order_by('-id')
            comment_serializer = CommentWithUserInfoSerializer(comments, many=True)
            data.append({'article': article_data, 'user': user_serializer.data, 'comment': comment_serializer.data})

        return paginator.get_paginated_response(data)
    
class SingleArticleListView(APIView):
    def get(self, request, id_article):
        paginator = CustomPagination()
        articles = Article.objects.filter(id=id_article).order_by('-id')
        paginated_articles = paginator.paginate_queryset(articles, request)
        article_serializer = ArticleSerializer(paginated_articles, many=True)

        data = []
        for article_data in article_serializer.data:
            user = User.objects.get(id=article_data['id_user'])
            user_serializer = UserSerializer(user)
            comments = Comments.objects.filter(id_article=article_data['id']).order_by('-id')
            comment_serializer = CommentWithUserInfoSerializer(comments, many=True)
            data.append({'article': article_data, 'user': user_serializer.data, 'comment': comment_serializer.data})

        return paginator.get_paginated_response(data)
   
    
class UserArticleListView(APIView):
    def get(self, request, user_id):
        paginator = CustomPagination2()
        articles = Article.objects.filter(id_user=user_id).order_by('-id')
        paginated_articles = paginator.paginate_queryset(articles, request)
        article_serializer = ArticleSerializer(paginated_articles, many=True)

        data = []
        for article_data in article_serializer.data:
            user = User.objects.get(id=article_data['id_user'])
            user_serializer = UserSerializer(user)
            comments = Comments.objects.filter(id_article=article_data['id']).order_by('-id')
            comment_serializer = CommentWithUserInfoSerializer(comments, many=True)
            data.append({'article': article_data, 'user': user_serializer.data, 'comment': comment_serializer.data})

        return paginator.get_paginated_response(data)
