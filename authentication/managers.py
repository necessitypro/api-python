from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """custom user manager for the CustomUser model"""

    def create_user(self, email, password=None, **extra_fields):
        """create and save a new user"""
        if not email:
            raise ValueError("The provided email address is invalid")
        email = self.normalize_email(email)

        account = self.filter(email=email)
        if account.exists():
            raise ValueError("The provided email address already exist")

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """create and save a new superuser"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(email, password, **extra_fields)
