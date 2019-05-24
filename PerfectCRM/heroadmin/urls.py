from django.urls import path, re_path
from heroadmin import views
from django.conf.urls import include, url

urlpatterns = [
    path('login/', views.acc_login),
    path('logout/', views.acc_logout, name='logout'),
    path('', views.app_index, name='app_index'),
    re_path(r'^/(\w+)/(\w+)/', views.table_obj_list, name='table_obj_list'),
]
