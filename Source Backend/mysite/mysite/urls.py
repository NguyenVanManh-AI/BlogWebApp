from django.contrib import admin
from django.urls import path, include
from blogapp.views import UserRegisterView, SearchView
from rest_framework_simplejwt import views as jwt_views

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['fullname'] = user.fullname
        token['gender'] = user.gender
        token['date_of_birth'] = user.date_of_birth
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Add extra responses here
        data['username'] = self.user.username
        data['email'] = self.user.email
        data['fullname'] = self.user.fullname
        data['gender'] = self.user.gender
        data['date_of_birth'] = self.user.date_of_birth
        return data


from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),
    path('api/register/', UserRegisterView.as_view(), name='register'),
    path('api/login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('search/', SearchView.as_view(), name='search'),
]
