from celery import shared_task
from .models import Distribution

@shared_task
def send_scheduled_mailings():
    from django.utils import timezone
    now = timezone.now()
    mailings = Distribution.objects.filter(schedule__lte=now, status='planned')

    for mailing in mailings:
        # логика отправки
        # например, создаём и отправляем сообщение
        print(f"Отправка рассылки: {mailing}")
        mailing.status = 'sent'
        mailing.save()