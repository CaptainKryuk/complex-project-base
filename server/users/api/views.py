from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from common.api import DefaultApiView
from .serializers import UserCreateSerializer, UserLoginSerializer
from users.models import User
from common.views import SessionCsrfExemptAuthentication


class RegistrationView(APIView):
    serializer = UserCreateSerializer
    authentication_classes = (SessionCsrfExemptAuthentication,)

    def post(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(**serializer.data)
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)  # type: ignore
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserInfoView(DefaultApiView):
    def get(self, request):
        if request.user and request.user.is_authenticated:
            return Response()
        return Response(status=status.HTTP_403_FORBIDDEN)