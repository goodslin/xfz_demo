from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from . import models


def index(request):
    # user = User.objects.create_user(username='admin', email='test@admin.com', password='admin123')
    # user = User.objects.create_superuser(username='goodslin', email='goodslin@qq.com', password='123456')
    # user = User.objects.get(username='admin')
    # user.set_password('123456')
    # user.save()
    username = 'goodslin'
    password = 'jacklin012'
    user = authenticate(request, username=username, password=password)
    if user:
        print('登陆成功')
    else:
        print('用户名或密码错误')
    return HttpResponse("success")


"""
def proxy_view(request):
    blacklist = models.Person.get_blacklist()
    for person in blacklist:
        print(person.username)
    return HttpResponse('proxy')
"""


def my_authenicate(telephone, password):
    user = User.objects.filter(extension__telephone=telephone).first()
    if user:
        is_correct = user.check_password(password)
        if is_correct:
            return user
        else:
            return None
    else:
        return None


def one_view(request):
    # user = User.objects.create_user(username='bbb', email='bbb@qq.com', password='222222')
    # user.extension.telephone = '13111234321'
    # user.save()
    telephone = request.GET.get('telephone')
    password = request.GET.get('password')
    user = my_authenicate(telephone=telephone, password=password)
    if user:
        print('验证成功')
    else:
        print('验证失败')
    return HttpResponse('User模型建立成功')


def inherit_view(request):
    user = User.objects.create_user()