import pytest
from authentication.models import Account

"""test user model"""


@pytest.mark.django_db
def test_create_new_user():
    """test creating a new user"""
    account = Account.objects.create_user(
        email="info@necessity.pro", password="password"
    )
    assert str(account) == "info@necessity.pro"
    assert account.email == "info@necessity.pro"
    assert account.is_active is True


@pytest.mark.django_db
def test_create_new_user_invalid_email():
    """test creating a new user with invalid email address"""
    with pytest.raises(ValueError):
        Account.objects.create_user(email="necessity.pro", password="password")
        raise ValueError("The provided email address is invalid")


@pytest.mark.django_db
def test_create_superuser():
    """test creating a superuser"""
    account = Account.objects.create_superuser(
        email="info@necessity.pro", password="password"
    )
    assert str(account) == "info@necessity.pro"
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
        raise ValueError("The provided email address already exist")
