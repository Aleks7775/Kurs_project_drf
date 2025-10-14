from rest_framework.generics import (CreateAPIView, ListAPIView, UpdateAPIView,
                                     DestroyAPIView)
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """Класс контролера создания пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """Сохраняем нового пользователя при регистрации, активируем и кэшируем пароль"""
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(ListAPIView):
    """Класс контролера для вывода списка пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(UpdateAPIView):
    """Класс контролера изменения пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(DestroyAPIView):
    """Класс контролера для удаления пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
