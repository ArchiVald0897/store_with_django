from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')

    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Страна', **NULLABLE)
    verification_token = models.CharField(max_length=15, verbose_name='Токен', **NULLABLE)
    is_verificated = models.BooleanField(verbose_name='Верифицирован', default=False, **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
