from django.core.exceptions import ValidationError
from datetime import datetime, timedelta


# def validate_execution_time(execution_time):
#     if execution_time > timedelta(seconds=120):
#         raise ValidationError('Время выполнения не может превышать 120 секунд.')

def validate_execution_time(execution_time):
    """Валидация, время выполнения должно быть не больше 120 секунд"""
    total_seconds = execution_time.hour * 3600 + execution_time.minute * 60 + execution_time.second
    if total_seconds > 120:
        raise ValidationError('Время выполнения не может превышать 120 секунд.')


def validate_frequency(frequency_days):
    """Валидация, нельзя выполнять привычку реже, чем 1 раз в 7 дней"""
    if frequency_days > 7:
        raise ValidationError('Привычка должна выполняться хотя бы раз в 7 дней.')


# def validate_pleasant_habit(reward_action, addition_habit):
#     if addition_habit and not reward_action:
#         raise ValidationError("Связанная привычка может быть только у приятной привычки.")

# def validate_pleasant_habit(reward_action, addition_habit):
#     """В связанные привычки попадают только привычки с признаком приятной привычки"""
#     if reward_action is False and addition_habit:
#         raise ValidationError('Может быть выбрана только приятная привычка.')


# def validate_no_reward_or_related_for_pleasant(is_pleasant, reward, related_habit):
#     """У приятной привычки не может быть вознаграждения или связанной привычки."""
#     if is_pleasant and (reward or related_habit):
#         raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')
