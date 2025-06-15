from django.urls import path
from . import views
from django.conf.urls.static import static

from config import settings

app_name = 'mailings'

urlpatterns = [
    path('distributions', views.DistributionListView.as_view(), name='distribution_list'),
    path('create/', views.DistributionCreateView.as_view(), name='distribution_create'),
    path('update/<int:pk>/', views.DistributionUpdateView.as_view(), name='distribution_update'),
    path('delete/<int:pk>/', views.DistributionDeleteView.as_view(), name='distribution_delete'),
    path('<int:mailing_id>/send/', views.send_mailing, name='send_mailing'),
    path('<int:mailing_id>/statistics/', views.mailing_statistics, name='mailing_statistics'),
    path('', views.home, name='home'),  # Главная страница
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
