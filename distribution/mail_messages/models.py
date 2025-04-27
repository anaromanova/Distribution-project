from django.db import models


class Message(models.Model):
    subject = models.CharField(max_length=255)  # Тема письма
    body = models.TextField()  # Тело письма

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ["subject"]

    def __str__(self):
        return self.subject
