<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include
from blogapp.views import UserRegisterView
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

=======
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
>>>>>>> c0eca83a2afc90e9ce247e3690163f5506aef4f3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),
<<<<<<< HEAD
    path('api/register/', UserRegisterView.as_view(), name='register'),
    path('api/login/', CustomTokenObtainPairView.as_view(), name='login'),
=======
>>>>>>> c0eca83a2afc90e9ce247e3690163f5506aef4f3
]
