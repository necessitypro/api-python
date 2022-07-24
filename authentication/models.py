"""default django packages"""
from django.contrib.auth.models import AbstractUser
from django.db import models

"""custom packages"""
from authentication.managers import CustomUserManager


class Account(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username",)

    objects = CustomUserManager()

    def __str__(self):
        return self.email
