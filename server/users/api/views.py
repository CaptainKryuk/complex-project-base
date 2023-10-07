from django.contrib.auth import authenticate, login
from rest_framework.response import Response

from common.api import DefaultApiView
from .serializers import UserCreateSerializer, UserLoginSerializer
from users.models import User


class RegistrationView(DefaultApiView):
    serializer = UserCreateSerializer

    def post(self, request):
        """
        проверка данных в сериалайзере
        создание пользователя
        """
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            User.objects.create_user(**serializer.data)
            return Response()
        return Response(serializer.errors)


class LoginView(DefaultApiView):
    serializer = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(request, **serializer.data)
            if user:
                login(request, user)
                return Response()
            return Response('Указан неверный логин или пароль')
        return Response(serializer.errors)