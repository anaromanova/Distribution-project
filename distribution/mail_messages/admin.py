from django.contrib import admin
from .models import Message

# Пример для добавления действий в админку
class MailingAdmin(admin.ModelAdmin):
    list_display = ['subject', 'status', 'created_at']
    actions = ['disable_mailing']

    def disable_mailing(self, request, queryset):
        queryset.update(status='Завершена')

admin.site.register(Message, MailingAdmin)
