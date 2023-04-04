from django.db import models

## 
from django.contrib.auth.models import AbstractUser

# Create your models here.

##
class User(AbstractUser):
    # Delete not use field
    first_name = None
    last_name = None
    username = None
    last_login = None
    is_staff = None
    is_superuser = None
    id = models.AutoField(primary_key=True)
    # username = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=100)
    
    fullname = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth = models.CharField(max_length=30, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    id_article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

class Avatar(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='avatar')
    path = models.ImageField(upload_to='static/avatars/')

    def __str__(self):
        return f'Avatar of {self.user.username}'
    
class CoverImage(models.Model):
    id = models.AutoField(primary_key=True)
    id_article = models.OneToOneField(Article, on_delete=models.CASCADE, related_name='cover_image')
    path = models.ImageField(upload_to='static/cover_images/')

    def __str__(self):
        return f'Cover image of {self.article.title}'
    
# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=30, unique=True)
#     password = models.CharField(max_length=128)
#     email = models.EmailField(unique=True)
#     fullname = models.CharField(max_length=100)
#     gender = models.CharField(max_length=10)
#     date_of_birth = models.DateField()

#     def __str__(self):
#         return self.email
