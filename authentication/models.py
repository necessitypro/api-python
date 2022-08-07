"""default django packages"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4

"""custom packages"""
from authentication.managers import CustomUserManager
from geography.models import Country


class Account(AbstractUser):
    """custom user model"""

    username = None
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(unique=True, help_text="The email of the user")
    email_verified = models.BooleanField(
        default=False, help_text="Is the email verified?"
    )
    email_verified_on = models.DateTimeField(
        null=True,
        editable=False,
        help_text="The date and time when the email was verified",
    )
    token = models.UUIDField(
        default=uuid4, editable=False, help_text="The token of the user"
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.RESTRICT,
        null=True,
        help_text="The country of the user",
    )
    phone = models.BigIntegerField(null=True, help_text="The phone of the user")
    phone_verified = models.BooleanField(
        default=False, help_text="Is the phone verified?"
    )
    phone_verified_on = models.DateTimeField(
        null=True,
        editable=False,
        help_text="The date and time when the phone was verified",
    )
    phone_one_time_code = models.IntegerField(
        null=True, editable=False, help_text="The one time code of the phone"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return self.email
