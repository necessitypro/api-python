"""default django packages"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4

"""custom packages"""
from authentication.managers import CustomUserManager


class Account(AbstractUser):
    username = None
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)
    email_verified_on = models.DateTimeField(null=True, editable=False)
    token = models.UUIDField(default=uuid4, editable=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return self.email
