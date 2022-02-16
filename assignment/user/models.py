from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

# Create your models here.


class CustomUser(AbstractUser):

    username = models.CharField(max_length=50, default='Anonymous')

    email = models.EmailField(max_length=254, unique=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    class Meta:
        app_label = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
