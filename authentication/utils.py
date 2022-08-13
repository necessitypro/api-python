from django.utils import timezone
from datetime import timedelta
import jwt


def CreateRefreshToken(data):
    """create refresh token"""
    return jwt.encode(
        {
            "exp": timezone.now() + timedelta(days=7),
            "data": data,
            "iss": "necessity.pro",
            "iat": timezone.now(),
        },
        key="secret",
        algorithm="HS256",
    )


def CreateRefreshTokenCookie(response, data):
    """create refresh token cookie"""
    response.set_cookie(
        "refresh_token",
        CreateRefreshToken(data),
        max_age=7 * 24 * 60 * 60,
        httponly=True,
        samesite="Strict",
    )

    return response


def CreateAccessToken(data):
    """create access token"""
    return jwt.encode(
        {
            "exp": timezone.now() + timedelta(days=1),
            "data": data,
            "iss": "necessity.pro",
            "iat": timezone.now(),
        },
        key="secret",
        algorithm="HS256",
    )


def CreateAccessTokenCookie(response, data):
    """create access token cookie"""
    response.set_cookie(
        "access_token",
        CreateAccessToken(data),
        max_age=24 * 60 * 60,
        httponly=True,
        samesite="Strict",
    )

    return response


def DecodeToken(token):
    """decode token"""
    return jwt.decode(token, "secret", algorithms=["HS256"])
