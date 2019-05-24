"""Djangohandler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app01 import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('add_book/', views.add_book, name='add_book'),
    path('book_detail/', views.book_detail, name='book_detail'),
    path('del_book_detail/', views.del_book_detail, name='del_book_detail'),
    path('add_more_book/', views.add_more_book, name='add_more_book'),
    path('author_get_book/', views.author_get_book, name='author_get_book'),
    path('book_get_author/', views.book_get_author, name='book_get_author'),
    path('author_add_authorinfo/', views.author_add_authorinfo, name='author_add_authorinfo'),
    path('another_add/', views.another_add, name='another_add'),
    path('add_tag/', views.add_tag, name='add_tag'),
    path('choose_tag/', views.choose_tag, name='choose_tag'),
    path('app02/', include("app02.urls")),
    path('app03/', include("app03.urls")),
    path('app05/', include("app05.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
