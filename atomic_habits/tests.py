from rest_framework.test import APITestCase
from django.urls import reverse
from atomic_habits.models import Habits
from users.models import User
from rest_framework import status
from datetime import datetime


class HabitTestCase(APITestCase):
    def setUp(self):
        """Функция подготовки данных перед тестированием"""
        self.user = User.objects.create(email="admin@example.com")
        self.user.set_password("1234qwe")
        self.client.force_authenticate(user=self.user)
        self.habit = Habits.objects.create(
            owner=self.user,
            time="00:01:00",
            period=2,
            action="Отжимания!",
        )

    def test_wont_create(self):
        """Тестирование создания экземпляра привычки"""
        url = reverse("atomic_habits:habits-create")
        data = {
            "place": "test",
            "time": "00:01:00",
            "action": "test",
            "period": 1,
        }
        response = self.client.post(url, data)
        print(datetime.now())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habits.objects.all().count(), 2)

    def test_habit_list(self):
        """Тестирование запроса на вывод списка привычек"""
        url = reverse("atomic_habits:habits-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habits.objects.all().count(), 1)

    def test_wont_retrieve(self):
        """Тестирование запроса на вывод полей привычки по заданному pk"""
        url = reverse("atomic_habits:habits-get", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.habit.action)

    def test_wont_update(self):
        """Тестирование запроса на изменение полей привычки"""
        url = reverse("atomic_habits:habits-update", args=(self.habit.pk,))
        data_update = {
            "place": "тест",
            "action": "тест",
            "is_pleasant": False,
            "period": 1,
            "award": "тестовое вознаграждение",
            "time": "00:02:00",
        }
        response = self.client.patch(url, data=data_update)
        data = response.json()
        print(data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("time"), "00:02:00")

    def test_wont_delete(self):
        """Тестирование запроса на удаление привычки с заданным pk"""
        url = reverse("atomic_habits:habits-delete", kwargs={"pk": self.habit.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habits.objects.all().count(), 0)
