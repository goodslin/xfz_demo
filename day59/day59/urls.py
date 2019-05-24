"""day59 URL Configuration

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
from django.urls import path
from app01 import views
from app02 import views as v2
from app03 import views as v3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.users),
    path('add_user/', views.add_user),
    path('edit_user-<int:nid>/', views.edit_user),
    path('test/', v2.test),
    # path('love/', v2.love),
    path('ajax/', v2.ajax),
    path('xuliehua/', v3.xuliehua),
    path('get_data/', v3.get_data),
]
