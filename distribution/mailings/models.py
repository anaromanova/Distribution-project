from django.db import models
from mail_messages.models import Message  # Импортируем сообщение
from clients.models import Client  # Импортируем клиента
from django.utils import timezone

class Distribution(models.Model):
    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('completed', 'Завершена'),
    ]

    start_time = models.DateTimeField()  # Дата и время первой отправки
    end_time = models.DateTimeField()    # Дата и время окончания отправки
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='created')  # Статус рассылки
    message = models.ForeignKey(Message, on_delete=models.CASCADE)  # Сообщение для отправки
    recipients = models.ManyToManyField(Client, related_name='distributions')  # Получатели рассылки

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ['-start_time']

    def __str__(self):
        return f"Рассылка {self.pk} - {self.get_status_display()}"


class MailingAttempt(models.Model):
    mailing = models.ForeignKey('Mailing', on_delete=models.CASCADE, related_name='attempts')
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)  # Каждый клиент
    attempt_time = models.DateTimeField(default=timezone.now)  # Время попытки отправки
    status = models.CharField(max_length=50, choices=[('успешно', 'успешно'), ('не успешно', 'не успешно')])  # Статус
    server_response = models.TextField(null=True, blank=True)  # Ответ почтового сервера, если есть ошибка

    def __str__(self):
        return f"Попытка {self.status} для {self.client.email} на {self.attempt_time}"

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылок'
        ordering = ['-attempt_time']