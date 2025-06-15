from django.urls import path
from . import views
from django.conf.urls.static import static

from config import settings

app_name = 'clients'

urlpatterns = [
    path('', views.ClientListView.as_view(), name='client_list'),
    path('client/<int:pk>/', views.ClientDetailView.as_view(), name='client_detail'),
    path('client/new/', views.ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>/edit/', views.ClientUpdateView.as_view(), name='client_edit'),
    path('client/<int:pk>/delete/', views.ClientDeleteView.as_view(), name='client_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
