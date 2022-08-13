from rest_framework.response import Response
from django.utils import timezone


def ErrorResponse(error, status_code=400, response=None):
    """Return a JSON response with a success=False and the error message."""
    response = {
        "success": False,
        "timestamp": timezone.now(),
        "error": error,
        "data": None,
    }
    return Response(response, status=status_code)


def SuccessResponse(data, status_code=200, response=None):
    """Return a JSON response with a success=True"""
    response = {
        "success": True,
        "timestamp": timezone.now(),
        "data": data,
        "error": None,
    }
    return Response(response, status=status_code)
