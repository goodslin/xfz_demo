from django.urls import path, include
from app03 import views


urlpatterns = [
    path('', views.large_csv_view, name='large_csv_view'),
    path('test/', views.AddBook.as_view(), name='test'),
    path('add_article/', views.add_article, name='add_article'),
    path('article_list/', views.ArticleListView.as_view(), name='article_list'),
    # path('page/', views.page_views, name='page_views'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('login/', views.login, name='login'),
    path('error/', views.error_view, name='error'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('register/', views.RegisterView.as_view()),
    path('add_book/', views.add_book),
    path('index1/', views.IndexViews.as_view()),
]