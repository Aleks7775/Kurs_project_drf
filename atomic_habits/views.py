from django.shortcuts import render
from rest_framework import viewsets, generics

from atomic_habits.models import Habits
from users.models import User
from atomic_habits.paginators import CustomPagination
from atomic_habits.serializers import HabitsSerializer
from users.permissions import IsOwner


class HabitsCreateAPIView(generics.CreateAPIView):
    """Класс контроллера для создания привычки"""

    serializer_class = HabitsSerializer
    # permission_classes =

    def perform_create(self, serializer):
        """Присваивания привычки к пользователю"""
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()



class HabitsListAPIView(generics.ListAPIView):
    """Класс контроллера для вывода списка привычек"""

    serializer_class = HabitsSerializer
    pagination_class = CustomPagination
    # queryset = Habits.objects.all()

    def get_queryset(self):
        """Пользователь видет свои и публичные привычки"""
        user = self.request.user
        user_habits = Habits.objects.filter(owner=user)
        public_habits = Habits.objects.filter(is_published=True)

        return user_habits | public_habits



class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    """Класс контроллера для вывода экземпляра привычки"""

    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsOwner,)


class HabitsUpdateAPIView(generics.UpdateAPIView):
    """Класс контроллера для изменения экземпляра привычки"""

    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsOwner,)


class HabitsDestroyAPIView(generics.DestroyAPIView):
    """Класс контроллера для удаления экземпляра привычки"""

    queryset = Habits.objects.all()
    permission_classes = (IsOwner,)
