from django.core.exceptions import ValidationError
from datetime import datetime, timedelta


def validate_execution_time(execution_time):
    """Валидация, время выполнения должно быть не больше 120 секунд"""
    total_seconds = execution_time.hour * 3600 + execution_time.minute * 60 + execution_time.second
    if total_seconds > 120:
        raise ValidationError('Время выполнения не может превышать 120 секунд.')


def validate_frequency(frequency_days):
    """Валидация, нельзя выполнять привычку реже, чем 1 раз в 7 дней"""
    if frequency_days > 7:
        raise ValidationError('Привычка должна выполняться хотя бы раз в 7 дней.')


def validate_pleasant_habit(addition_habit):
    if addition_habit and not addition_habit.reward_action:
        raise ValidationError("В связанные привычки могут попадать только привычки с признаком приятной привычки.")
