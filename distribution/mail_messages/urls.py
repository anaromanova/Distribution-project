from django.urls import path
from . import views

app_name = 'mail_messages'

urlpatterns = [
    path('', views.MessageListView.as_view(), name='message_list'),  # Список сообщений
    path('messages/create/', views.MessageCreateView.as_view(), name='message_create'),  # Создание сообщения
    path('messages/update/<int:pk>/', views.MessageUpdateView.as_view(), name='message_update'),  # Редактирование сообщения
    path('messages/delete/<int:pk>/', views.MessageDeleteView.as_view(), name='message_delete'),  # Удаление сообщения
]