from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.app_index),
    path('login/', views.acc_login),
    re_path(r'^(\w+)/(\w+)/', views.table_obj_list, name='table_obj_list'),
    path('test/', views.test),
]