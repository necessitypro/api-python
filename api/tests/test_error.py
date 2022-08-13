from api.utils.errors import get_error_message, get_error_response


def test_get_error_message_with_no_code():
    """test get_error_response with no code"""
    assert get_error_message("") == ""


def test_get_error_message():
    """test get_error_message"""
    assert get_error_message("ACCOUNT_INACTIVE") == "The account is not active"
    assert get_error_message("ACCOUNT_INACTIVE") == "The account is not active"


def test_get_error_response_with_no_field_and_code():
    """test get_error_response with no field and code"""
    assert get_error_response("account", "") == {
        "field": "account",
        "code": "",
        "message": "",
    }


def test_get_error_response():
    """test get_error_response"""
    assert get_error_response("account", "ACCOUNT_INACTIVE") == {
        "field": "account",
        "code": "ACCOUNT_INACTIVE",
        "message": "The account is not active",
    }
