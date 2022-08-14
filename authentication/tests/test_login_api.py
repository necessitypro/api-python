import pytest
from api.utils.clients import Client
from authentication.models import Account


def test_login_with_empty_email_and_password():
    """test login with empty no email and password fields"""

    client = Client()
    response = client.post("/auth/login/", {})

    assert response.status_code == 400
    assert len(response.data["error"]) == 2
    assert response.data["error"][0]["field"] == "email"
    assert response.data["error"][0]["code"] == "FIELD_REQUIRED"
    assert response.data["error"][1]["field"] == "password"
    assert response.data["error"][1]["code"] == "FIELD_REQUIRED"
    assert response.data["data"] is None


def test_login_with_invalid_email():
    """test login with empty email and password"""

    client = Client()
    response = client.post("/auth/login/", {"email": "", "password": ""})

    assert response.status_code == 400
    assert len(response.data["error"]) == 2
    assert response.data["error"][0]["field"] == "email"
    assert response.data["error"][0]["code"] == "FIELD_REQUIRED"
    assert response.data["error"][1]["field"] == "password"
    assert response.data["error"][1]["code"] == "FIELD_REQUIRED"
    assert response.data["data"] is None


def test_login_with_invalid_email_and_password():
    """test login with invalid email and password"""

    client = Client()
    response = client.post(
        "/auth/login/", {"email": "invalid_email", "password": "invalid_password"}
    )

    assert response.status_code == 400
    assert len(response.data["error"]) == 1
    assert response.data["error"][0]["field"] == "email"
    assert response.data["error"][0]["code"] == "EMAIL_INVALID"
    assert response.data["data"] is None


@pytest.mark.django_db
def test_login_with_email_and_password():
    """test login with valid email and password"""

    client = Client()
    response = client.post(
        "/auth/login/", {"email": "info@necessity.pro", "password": "password"}
    )

    assert response.status_code == 400
    assert len(response.data["error"]) == 1
    assert response.data["error"][0]["field"] == "email"
    assert response.data["error"][0]["code"] == "EMAIL_INVALID"
    assert response.data["data"] is None


@pytest.mark.django_db
def test_login_with_valid_email_and_invalid_password():
    """test login with valid email and invalid password"""

    Account.objects.create_user(email="info@necessity.pro", password="password")

    client = Client()
    response = client.post(
        "/auth/login/", {"email": "info@necessity.pro", "password": "invalid_password"}
    )

    assert response.status_code == 400
    assert len(response.data["error"]) == 1
    assert response.data["error"][0]["field"] == "auth"
    assert response.data["error"][0]["code"] == "AUTH_INVALID_CREDENTIALS"
    assert response.data["data"] is None


@pytest.mark.django_db
def test_login_with_valid_email_and_valid_password():
    """test login with valid email and valid password"""

    Account.objects.create_user(email="info@necessity.pro", password="password")
    account = Account.objects.get(email="info@necessity.pro")

    client = Client()
    response = client.post(
        "/auth/login/", {"email": "info@necessity.pro", "password": "password"}
    )

    assert response.status_code == 200
    assert response.data["error"] is None
    assert response.cookies.get("access_token") is not None
    assert response.cookies.get("refresh_token") is not None
    assert response.data["data"]["id"] == str(account.id)
    assert response.data["data"]["email"] == account.email
    assert response.data["data"]["first_name"] == account.first_name
    assert response.data["data"]["last_name"] == account.last_name
