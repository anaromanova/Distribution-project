from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from mail_messages.models import Distribution
from django.conf import settings

class Command(BaseCommand):
    help = 'Отправка рассылки вручную'

    def add_arguments(self, parser):
        parser.add_argument('mailing_id', type=int)

    def handle(self, *args, **options):
        mailing_id = options['mailing_id']
        mailing = Distribution.objects.get(id=mailing_id)  # Получаем рассылку

        if mailing.status != 'Запущена':
            self.stdout.write(self.style.ERROR('Рассылка не запущена!'))
            return

        message = mailing.message  # Сообщение для рассылки
        recipients = mailing.clients.all()  # Получаем всех клиентов

        # Отправляем письма
        for recipient in recipients:
            send_mail(
                subject=message.subject,
                message=message.body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[recipient.email],
            )

        # Обновляем статус рассылки
        mailing.status = 'Завершена'
        mailing.save()

        self.stdout.write(self.style.SUCCESS('Рассылка успешно отправлена!'))