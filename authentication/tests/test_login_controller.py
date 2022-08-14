import pytest
from authentication.models import Account
from authentication.controllers.login import LoginController


@pytest.mark.django_db
def test_login_with_empty_email_and_password():
    """test login with empty email and password"""
    error, user = LoginController(email="", password="")

    assert user is None
    assert error[0]["field"] == "email"
    assert error[0]["code"] == "EMAIL_REQUIRED"

    assert error[1]["field"] == "password"
    assert error[1]["code"] == "FIELD_REQUIRED"


@pytest.mark.django_db
def test_login_with_invalid_email_and_password():
    """test login with invalid email and password"""
    error, user = LoginController(email="invalid_email", password="")

    assert user is None
    assert error[0]["field"] == "email"
    assert error[0]["code"] == "EMAIL_INVALID"


@pytest.mark.django_db
def test_login_with_email_and_password():
    """test login with valid email and password"""
    error, user = LoginController(email="info@necessity.pro", password="password")

    assert user is None
    assert error[0]["field"] == "email"
    assert error[0]["code"] == "EMAIL_INVALID"


@pytest.mark.django_db
def test_login_with_valid_email_and_invalid_password():
    """test login with valid email and invalid password"""
    Account.objects.create_user(email="info@necessity.pro", password="password")

    error, user = LoginController(
        email="info@necessity.pro", password="invalid_password"
    )

    assert user is None
    assert error[0]["field"] == "auth"
    assert error[0]["code"] == "AUTH_INVALID_CREDENTIALS"


@pytest.mark.django_db
def test_login_with_valid_email_and_valid_password():
    """test login with valid email and valid password"""
    account = Account.objects.create_user(
        email="info@necessity.pro", password="password"
    )

    error, user = LoginController(email="info@necessity.pro", password="password")

    assert user is not None
    assert len(error) == 0
    assert user["email"] == account.email
    assert user["id"] == str(account.id)
    assert user["first_name"] == account.first_name
    assert user["last_name"] == account.last_name
