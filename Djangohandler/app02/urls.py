from django.urls import path, include
from app02 import views

urlpatterns = [
    path('index01/', views.index01, name='index01'),
    path('index02/', views.index02, name='index02'),
    path('index03/', views.index03, name='index03'),
    path('index04/', views.index04, name='index04'),
    path('index05/', views.index05, name='index05'),
    path('index06/', views.index06, name='index06'),
    path('index07/', views.index07, name='index07'),
    path('index08/', views.index08, name='index08'),
    path('index09/', views.index09, name='index09'),
    path('index10/', views.index10, name='index10'),
    path('index11/', views.index11, name='index11'),
    path('index12/', views.index12, name='index12'),
    path('index13/', views.index13, name='index13'),
    path('index15/', views.index15, name='index15'),
]
