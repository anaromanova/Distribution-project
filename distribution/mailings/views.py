from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail  # Для отправки письма
from django.conf import settings

from .models import Distribution, MailingAttempt
from .forms import DistributionForm


class DistributionListView(ListView):
    model = Distribution
    template_name = 'mailings/distribution_list.html'
    context_object_name = 'distributions'

class DistributionCreateView(CreateView):
    model = Distribution
    form_class = DistributionForm
    template_name = 'mailings/distribution_form.html'
    success_url = reverse_lazy('mailings:distribution_list')

class DistributionUpdateView(UpdateView):
    model = Distribution
    form_class = DistributionForm
    template_name = 'mailings/distribution_form.html'
    success_url = reverse_lazy('mailings:distribution_list')

class DistributionDeleteView(DeleteView):
    model = Distribution
    template_name = 'mailings/distribution_confirm_delete.html'
    success_url = reverse_lazy('mailings:distribution_list')


def send_mailing(request, mailing_id):
    mailing = Distribution.objects.get(id=mailing_id)  # Получаем рассылку
    if mailing.status != 'Запущена':
        messages.error(request, 'Рассылка не запущена!')
        return redirect('mailing_list')

    message = mailing.message  # Сообщение для рассылки
    recipients = mailing.clients.all()  # Получаем всех клиентов для рассылки

    for recipient in recipients:
        try:
            # Попытка отправки письма
            send_mail(
                subject=message.subject,
                message=message.body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[recipient.email],
            )

            # Если письмо отправлено успешно, создаем запись с успешным статусом
            MailingAttempt.objects.create(
                mailing=mailing,
                client=recipient,
                status='успешно',
                server_response="Письмо успешно отправлено"
            )

        except Exception as e:
            # В случае ошибки отправки письма, создаем запись с ошибкой
            MailingAttempt.objects.create(
                mailing=mailing,
                client=recipient,
                status='не успешно',
                server_response=str(e)  # Ответ почтового сервера (ошибка)
            )

    # Обновляем статус рассылки
    mailing.status = 'Завершена'
    mailing.save()

    messages.success(request, 'Рассылка успешно отправлена!')
    return redirect('mailing_list')


def mailing_statistics(request, mailing_id):
    mailing = Distribution.objects.get(id=mailing_id)
    attempts = mailing.attempts.all()  # Все попытки этой рассылки

    successful_attempts = attempts.filter(status='успешно')
    failed_attempts = attempts.filter(status='не успешно')

    context = {
        'mailing': mailing,
        'total_attempts': attempts.count(),
        'successful_attempts': successful_attempts.count(),
        'failed_attempts': failed_attempts.count(),
        'successful_attempts_list': successful_attempts,
        'failed_attempts_list': failed_attempts
    }

    return render(request, 'mailings/mailing_statistics.html', context)


def home(request):
    total_mailings = Distribution.objects.count()  # Количество всех рассылок
    active_mailings = Distribution.objects.filter(status='Запущена').count()  # Количество активных рассылок
    unique_clients = Distribution.objects.values('clients').distinct().count()  # Количество уникальных получателей

    context = {
        'total_mailings': total_mailings,
        'active_mailings': active_mailings,
        'unique_clients': unique_clients,
    }

    return render(request, 'mailings/home.html', context)

def statistics(request):
    successful_attempts = MailingAttempt.objects.filter(status='Успешно').count()
    failed_attempts = MailingAttempt.objects.filter(status='Не успешно').count()
    total_messages_sent = MailingAttempt.objects.count()

    context = {
        'successful_attempts': successful_attempts,
        'failed_attempts': failed_attempts,
        'total_messages_sent': total_messages_sent,
    }

    return render(request, 'mailings/statistics.html', context)