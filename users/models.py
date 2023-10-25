from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')

    phone_number = models.CharField(max_length=40, verbose_name='Номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    country = models.CharField(max_length=40, verbose_name='Страна', **NULLABLE)

    verification_token = models.CharField(max_length=15, verbose_name='Код верификации', **NULLABLE)
    is_verified = models.BooleanField(default=False, verbose_name='Статус верификации')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
