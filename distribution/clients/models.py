from django.db import models

from distribution.accounts.models import User

class Client(models.Model):
    email = models.EmailField(unique=True)  # Уникальный email
    full_name = models.CharField(max_length=255)  # Ф. И. О.
    comment = models.TextField(blank=True, null=True)  # Комментарий (необязательное поле)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clients')

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ["email", "full_name", "comment"]


    def __str__(self):
        return self.full_name

