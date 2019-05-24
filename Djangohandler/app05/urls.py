from django.urls import path
from app05 import views

urlpatterns = [
    path('', views.session_view),
]
