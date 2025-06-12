from django.db import models
from distribution.mail_messages.models import Message  # Импортируем сообщение
from distribution.clients.models import Client  # Импортируем клиента
from django.utils import timezone
from distribution.accounts.models import User

class Distribution(models.Model):
    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('completed', 'Завершена'),
    ]

    subject = models.CharField(max_length=255)  # Тема рассылки
    start_time = models.DateTimeField()  # Дата и время первой отправки
    end_time = models.DateTimeField()    # Дата и время окончания отправки
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='created')  # Статус рассылки
    message = models.ForeignKey(Message, on_delete=models.CASCADE)  # Сообщение для отправки
    recipients = models.ManyToManyField(Client, related_name='distributions')  # Получатели рассылки
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='distributions')

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ['-start_time']

    def __str__(self):
        return f"Рассылка {self.subject} (статус: {self.status})"


class MailingAttempt(models.Model):
    STATUS_CHOICES = [
        ('Успешно', 'Успешно'),
        ('Не успешно', 'Не успешно'),
    ]

    mailing = models.ForeignKey('Distribution', on_delete=models.CASCADE,
                                related_name='attempts')  # Внешний ключ на рассылку
    attempt_time = models.DateTimeField(default=timezone.now)  # Дата и время попытки
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)  # Статус
    server_response = models.TextField(null=True, blank=True)  # Ответ почтового сервера
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mailings')

    def __str__(self):
        return f"Попытка {self.status} для рассылки {self.mailing.id} на {self.attempt_time}"

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылок'
        ordering = ['-attempt_time']