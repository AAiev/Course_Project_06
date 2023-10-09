from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=30, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)
    verification_key = models.CharField(max_length=10, verbose_name='ключ верификации', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='активация пользователя')



    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
