from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, ArticleViewSet, CommentsViewSet, AvatarViewSet, CoverImageViewSet, UserUpdateAPIView, UserPasswordUpdateAPIView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'comments', CommentsViewSet)
router.register(r'avatars', AvatarViewSet)
router.register(r'coverimages', CoverImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/<pk>/update-info', UserUpdateAPIView.as_view()),
    path('users/<int:pk>/changepassword', UserPasswordUpdateAPIView.as_view(), name='user-change-password'),
]