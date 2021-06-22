from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
        Bu sınıfımız default olarak bir kullanıcıda olması gereken özellikleri belirtiyor..
        Çok açıklayıcı bir açıklama oldu bu.
    """

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True, null=False)
    name = models.CharField(max_length=255)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
