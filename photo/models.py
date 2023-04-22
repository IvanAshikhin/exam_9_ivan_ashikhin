from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Photo(models.Model):
    image = models.ImageField(null=False, blank=True, upload_to='images')
    signature = models.TextField(null=False, blank=True, max_length=1000, verbose_name='Подпись')
    date = models.DateTimeField(verbose_name='Дата создания', default=timezone.now)
    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), null=False, blank=False,
                               on_delete=models.CASCADE)
