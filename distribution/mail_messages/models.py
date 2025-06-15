from django.db import models
from django.utils import timezone
from distribution.accounts.models import User

class Message(models.Model):
    subject = models.CharField(max_length=255)  # Тема письма
    body = models.TextField()  # Тело письма
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ["subject"]

    def __str__(self):
        return self.subject
