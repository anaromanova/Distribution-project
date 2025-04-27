from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Message
from django.urls import reverse_lazy

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


