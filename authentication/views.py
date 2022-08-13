import jwt
from rest_framework.views import APIView
from authentication.controllers.login import LoginController

from api.utils.response import ErrorResponse, SuccessResponse

from authentication.utils import CreateRefreshTokenCookie, CreateAccessTokenCookie


class LoginView(APIView):
    """login api view"""

    def post(self, request):
        """login post email and password"""
        data = request.data
        error, user = LoginController(data["email"], data["password"])

        if error is not None:
            return ErrorResponse(error)
        else:
            if user is not None:
                response = SuccessResponse(user)
                response = CreateAccessTokenCookie(response, user)
                response = CreateRefreshTokenCookie(response, user)
                return response
