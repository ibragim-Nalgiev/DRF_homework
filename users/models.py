from django.contrib.auth.models import AbstractUser
from .manager import Manager

from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
        username = None
        email = models.EmailField(unique=True, verbose_name='почта')
        first_name = models.CharField(max_length=150, verbose_name='имя', **NULLABLE)
        last_name = models.CharField(max_length=150, verbose_name='фамилия', **NULLABLE)
        avatar = models.ImageField(upload_to='media/users/', verbose_name='аватар', **NULLABLE)
        phone = models.IntegerField(default=None, verbose_name='телефон', **NULLABLE)
        city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
        is_active = models.BooleanField(default=True, verbose_name='Статус активации')

        objects = Manager()

        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = []

        def __str__(self):
            return f'{self.first_name}, {self.last_name}'

        class Meta:
            verbose_name = 'пользователь'
            verbose_name_plural = 'пользователи'

