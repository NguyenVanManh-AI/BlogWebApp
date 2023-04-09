from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, ArticleViewSet, CommentsViewSet
from .views import UserPasswordUpdateAPIView, UserUpdateAPIView, comments_for_article, ArticleListView, UserArticleListView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'comments', CommentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('users/<int:pk>/articles', UserArticleListView.as_view(), name='user-all-article'),
    path('articles', ArticleListView.as_view(), name='all-article'),
    path('users/<int:pk>/update-info', UserUpdateAPIView.as_view(), name='user-info-update'),
    path('users/<int:pk>/changepassword', UserPasswordUpdateAPIView.as_view(), name='user-change-password'),
    path('articles/<int:article_id>/comments/', comments_for_article, name='comments_for_article'),
]