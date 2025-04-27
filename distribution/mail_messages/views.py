from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Message
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.cache import cache_page

# Представление для просмотра списка сообщений
class MessageListView(ListView):
    model = Message
    template_name = 'message_list.html'
    context_object_name = 'messages'

# Представление для создания нового сообщения
class MessageCreateView(CreateView):
    model = Message
    template_name = 'message_form.html'
    fields = ['subject', 'body']
    success_url = reverse_lazy('mail_messages:message_list')  # Перенаправление после создания

# Представление для редактирования сообщения
class MessageUpdateView(UpdateView):
    model = Message
    template_name = 'message_form.html'
    fields = ['subject', 'body']
    success_url = reverse_lazy('mail_messages:message_list')

# Представление для удаления сообщения
class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'message_confirm_delete.html'
    success_url = reverse_lazy('mail_messages:message_list')


@login_required
def manage_own_mailings(request):
    if request.user.groups.filter(name='User').exists():
        mailings = Message.objects.filter(owner=request.user)
    else:
        mailings = Message.objects.all()
    return render(request, 'mailings/manage_mailings.html', {'mailings': mailings})


@cache_page(60 * 15)  # Кеширование страницы на 15 минут
def mailing_list_view(request):
    mailings = Message.objects.all()
    return render(request, 'mailings/message_list.html', {'mailings': mailings})
