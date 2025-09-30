from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from atomic_habits.models import Habits
from atomic_habits.validators import validate_execution_time, validate_frequency, validate_pleasant_habit


class HabitsSerializer(serializers.ModelSerializer):
    time = serializers.TimeField(validators=[validate_execution_time])
    period = serializers.IntegerField(validators=[validate_frequency])

    class Meta:
        model = Habits
        fields = '__all__'

    def validate(self, attrs):
        addition_habit = attrs.get('addition_habit')
        validate_pleasant_habit(addition_habit)
        return attrs
