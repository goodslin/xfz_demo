from django.urls import path
from .views import account, home
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register.html', account.register),
    path('check_code.html', account.check_code),
    path('index.html', home.index),
    path('login.html', account.login),
    path('logout.html', account.logout),
    path('all/<int:article_type_id>.html', home.index, name='index'),
    path('<str:site>.html', home.home),
    path('<str:site>/<int:nid>.html', home.detail),
    path('', home.index),
]
