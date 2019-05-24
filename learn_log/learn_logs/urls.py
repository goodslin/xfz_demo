"""定义learn_logs的URL模式"""
from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    #主页
    path('',views.index,name='index'),

    #显示所有的主题
    path('topics/',views.topics,name='topics'),

    #特定主题的详细页面
    path('topics/<topic_id>',views.topic,name='topic'),

    #用户添加新主题的网页
    path('new_topic/',views.topic,name='new_topic'),
]