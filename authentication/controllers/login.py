from django.contrib.auth import authenticate
from authentication.models import Account

from api.utils.errors import get_error_response
from api.utils.validations import val_email, val_required


def LoginController(email, password):
    """login controller"""
    error = []
    user = None

    email = val_email(email)
    if email["error"] is not None:
        error.append(get_error_response("email", email["error"]))

    password = val_required(password)
    if password["error"] is not None:
        error.append(get_error_response("password", password["error"]))

    if len(error) == 0:
        account = Account.objects.filter(email=email["value"])
        if len(account) == 0:
            error.append(get_error_response("email", "EMAIL_INVALID"))

    if len(error) == 0:
        try:
            account = Account.objects.get(email=email["value"])
            auth = authenticate(email=account.email, password=password["value"])
            if auth is not None:
                if auth.is_active:
                    user = {
                        "first_name": auth.first_name,
                        "last_name": auth.last_name,
                        "email": auth.email,
                        "id": str(auth.id),
                    }
                else:
                    error.append(get_error_response("auth", "ACCOUNT_INACTIVE"))
            else:
                error.append(get_error_response("auth", "AUTH_INVALID_CREDENTIALS"))
        except Account.DoesNotExist:
            error.append(get_error_response("auth", "AUTH_INVALID_CREDENTIALS"))

    return error, user
