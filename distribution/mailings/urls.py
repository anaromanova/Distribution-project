from django.urls import path
from . import views

app_name = 'mailings'

urlpatterns = [
    path('', views.DistributionListView.as_view(), name='distribution_list'),
    path('create/', views.DistributionCreateView.as_view(), name='distribution_create'),
    path('update/<int:pk>/', views.DistributionUpdateView.as_view(), name='distribution_update'),
    path('delete/<int:pk>/', views.DistributionDeleteView.as_view(), name='distribution_delete'),
    path('<int:mailing_id>/send/', views.send_mailing, name='send_mailing'),
]
