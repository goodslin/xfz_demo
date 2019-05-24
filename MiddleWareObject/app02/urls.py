from django.urls import path
from app02 import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('transfer/', views.TransferView.as_view(), name='transfer'),
    path('logout/', views.logout, name='logout'),
]