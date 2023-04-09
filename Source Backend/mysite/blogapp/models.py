from django.db import models
## 
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator


class User(AbstractUser):
    first_name = None
    last_name = None
    last_login = None
    is_staff = None
    is_superuser = None
    username = None

    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, unique=True, blank=False)
  
    password = models.CharField(max_length=100, null=False,validators=[MinLengthValidator(6)])
    
    fullname = models.CharField(max_length=100, blank=False, null=False)
    gender = models.BooleanField(blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=True)
    avatar = models.ImageField(upload_to='static/avatars/', null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password','fullname','date_of_birth','gender',]

    def __str__(self):
        return str(self.id)

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    id_article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)



