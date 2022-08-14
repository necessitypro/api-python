from rest_framework.views import APIView
from authentication.controllers.login import LoginController
from authentication.utils import CreateRefreshTokenCookie, CreateAccessTokenCookie
from api.utils.response import ErrorResponse, SuccessResponse
from api.utils.errors import get_error_response


class LoginView(APIView):
    """login api view"""

    def post(self, request):
        """login post email and password"""
        data = request.data
        error = []

        if not data.get("email"):
            error.append(get_error_response("email", "FIELD_REQUIRED"))

        if not data.get("password"):
            error.append(get_error_response("password", "FIELD_REQUIRED"))

        if len(error) == 0:
            error, user = LoginController(data["email"], data["password"])
            if len(error) > 0:
                return ErrorResponse(error)

            response = SuccessResponse(user)
            response = CreateAccessTokenCookie(response, user)
            response = CreateRefreshTokenCookie(response, user)
            return response

        return ErrorResponse(error)
