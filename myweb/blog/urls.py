from django.contrib import admin
from blog import views
from django.urls import path


urlpatterns = [
    path('article/<int:year>/<int:month>', views.article_year),
    path('register/', views.register, name="reg"),

]
