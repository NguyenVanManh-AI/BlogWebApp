from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, ArticleViewSet, CommentsViewSet
from .views import UserPasswordUpdateAPIView, UserUpdateAPIView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'comments', CommentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/<int:pk>/update-info', UserUpdateAPIView.as_view(), name='user-info-update'),
    path('users/<int:pk>/changepassword', UserPasswordUpdateAPIView.as_view(), name='user-change-password'),
]