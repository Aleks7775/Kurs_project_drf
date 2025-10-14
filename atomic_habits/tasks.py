from datetime import datetime, timedelta

from celery import shared_task

from atomic_habits.models import Habits
from atomic_habits.services import send_telegram_message


@shared_task
def task():
    """Периодическая задача отправки уведомлений в телеграмм за 5 минут до начала выполнения привычки"""
    wonts = Habits.objects.all()
    for wont in wonts:
        if wont.user.chat_id and wont.time <= datetime.now().time() - timedelta(
            minutes=5
        ):
            text = f"мне нужно {wont.action} в {wont.time} в {wont.place}"
            send_telegram_message(text, wont.user.tg_chat_id)
