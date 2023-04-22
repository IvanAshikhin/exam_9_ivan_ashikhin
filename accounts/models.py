from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class Account(AbstractUser):
    username = models.CharField(
        max_length=50,
        verbose_name='Username',
        null=False,
        unique=True
    )
    favorite_posts = models.ManyToManyField(
        to='photo.Photo',
        verbose_name='Favorite posts',
        related_name='favorite'
    )


USERNAME_FIELD = "username"
REQUIRED_FIELDS = []

object = UserManager()


class Meta:
    verbose_name = 'Профиль'
    verbose_name_plural = 'Профили'
