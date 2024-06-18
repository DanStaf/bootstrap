from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='почта', unique=True)
    avatar = models.ImageField(null=True, blank=True, verbose_name='Аватар')
    phone = models.CharField(null=True, blank=True, max_length=150, verbose_name='Телефон')
    country = models.CharField(null=True, blank=True, max_length=150, verbose_name='Страна')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
