from django.urls import path
from crm01 import views

urlpatterns = [
    path('', views.dashboard, name='sales_dashboard'),
]