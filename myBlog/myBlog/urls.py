"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import django_summernote
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from blog import views as blog_view
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', blog_view.index_unlog, name='index_unlog'),
    path('login', blog_view.login, name='login'),
    path('login_1', blog_view.login_1, name='login_1'),
    path('log', blog_view.login_success, name='login_success'),
    path('register', blog_view.register, name='register'),
    path('forget', blog_view.forget_password, name='forget'),
    path('reset', blog_view.reset, name='reset'),
    path('get_validCode', blog_view.get_valid_code_img, name='get_validCode'),

    path('summernote/', include('django_summernote.urls')),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    path('static/<path:path>', serve, {'document_root': settings.STATIC_ROOT}),
]
