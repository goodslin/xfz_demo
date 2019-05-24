from django.urls import path, include
from .views import user
from django.conf import urls

urlpatterns = [
    path('index.html', user.index),
    path('base-info.html', user.base_info),
    path('tag.html', user.tag),
    path('category.html', user.category),
    path('article-<int:article_type_id>-<int:category_id>.html', user.article, name='article'),
    path('add-article-<int:nid>.html', user.add_article),
    path('edit-article-<int:nid>.html', user.edit_article),
    path('upload-avatar.html', user.upload_avatar),
]
