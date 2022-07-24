import pytest
from authentication.models import Account

"""test user model"""


@pytest.mark.django_db
def test_create_new_user():
    """test creating a new user"""
    account = Account.objects.create_user(
        email="info@necessity.pro", password="password"
    )
    assert account.email == "info@necessity.pro"
    assert account.is_active is True


@pytest.mark.django_db
def test_create_superuser():
    """test creating a superuser"""
    account = Account.objects.create_superuser(
        email="info@necessity.pro", password="password"
    )
    assert account.email == "info@necessity.pro"
    assert account.is_superuser is True
    assert account.is_staff is True
    assert account.is_active is True


@pytest.mark.django_db
def test_create_duplicate_user():
    """test creating a duplicate user"""
    Account.objects.create_user(email="info@necessity.pro", password="password")
    with pytest.raises(ValueError):
        Account.objects.create_user(email="info@necessity.pro", password="password")
        raise ValueError("User with this email already exists")
