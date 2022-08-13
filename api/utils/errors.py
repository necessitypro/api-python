err_codes = {
    "ACCOUNT_INACTIVE": "The account is not active",
    "AUTH_INVALID_CREDENTIALS": "The credentials are invalid",
    "EMAIL_REQUIRED": "The email is required.",
    "EMAIL_INVALID": "The email is invalid.",
    "FIELD_REQUIRED": "This field is required",
}


def get_error_message(code):
    """get error message"""
    return err_codes.get(code, "")


def get_error_response(field, code):
    """get error response"""
    return {"field": field, "code": code, "message": get_error_message(code)}
