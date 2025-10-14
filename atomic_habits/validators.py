from django.core.exceptions import ValidationError


def validate_execution_time(execution_time):
    """Валидация, время выполнения должно быть не больше 120 секунд"""
    total_seconds = execution_time.hour * 3600 + execution_time.minute * 60 + execution_time.second
    if total_seconds > 120:
        raise ValidationError('Время выполнения не может превышать 120 секунд.')


def validate_frequency(frequency_days):
    """Валидация, нельзя выполнять привычку реже, чем 1 раз в 7 дней"""
    if frequency_days > 7:
        raise ValidationError('Привычка должна выполняться хотя бы раз в 7 дней.')


def validate_pleasant_habit(attrs):
    """Валидируем приятные привычки"""
    addition_habit = attrs.get('addition_habit')
    award = attrs.get('award')
    reward_action = attrs.get('reward_action')
    if addition_habit and not addition_habit.reward_action:
        raise ValidationError("В связанные привычки могут попадать только привычки с признаком приятной привычки.")
    if reward_action and (addition_habit or award):
        raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")


def validate_no_both_addition_and_award(attrs):
    """Валидируем отсутствие одновременного указания вознаграждения и связанной привычки"""
    addition_habit = attrs.get('addition_habit')
    award = attrs.get('award')
    if addition_habit and award:
        raise ValidationError(
            "Нельзя одновременно указывать и вознаграждение, и связанную привычку."
        )
