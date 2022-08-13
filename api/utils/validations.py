import re
from django.core.validators import validate_email


def val_email(email, required=True):
    """validate email"""

    error = None
    email = email.strip().lower()

    if required and not email:
        error = "EMAIL_REQUIRED"

    if not error and not re.fullmatch(
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", email
    ):
        error = "EMAIL_INVALID"

    return {"error": error, "value": email}


def val_required(value, required=True):
    """validate required"""

    error = None

    if required and not value:
        error = "FIELD_REQUIRED"

    return {"error": error, "value": value}
