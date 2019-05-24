from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.index),
    path('', views.index, name='index'),
    path('<int:news_id>/', views.news_detail, name='news_detail'),
]
