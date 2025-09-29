from django.urls import path

from atomic_habits.apps import AtomicHabitsConfig
from atomic_habits.views import (HabitsCreateAPIView, HabitsListAPIView,
                                   HabitsRetrieveAPIView, HabitsUpdateAPIView, HabitsDestroyAPIView)

app_name = AtomicHabitsConfig.name


urlpatterns = [
    path('habits/create/', HabitsCreateAPIView.as_view(), name='habits-create'),
    path('habits/', HabitsListAPIView.as_view(), name='habits-list'),
    path('habits/<int:pk>/', HabitsRetrieveAPIView.as_view(), name='habits-get'),
    path('habits/update/<int:pk>/', HabitsUpdateAPIView.as_view(), name='habits-update'),
    path('habits/delete/<int:pk>/', HabitsDestroyAPIView.as_view(), name='habits-delete')
]

