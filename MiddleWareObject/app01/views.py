from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import View
from .models import User
from django.contrib import messages


def index(request):
    print('这是index view中执行的代码。。。')
    if request.front_user:
        print(request.front_user.username)
    return HttpResponse('index')


def my_list(request):
    if request.front_user:
        print(request.front_user.username)
    return HttpResponse('my list')


class SignView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password).first()
        if user:
            request.session['user_id'] = user.id
            return redirect(reverse('index'))
        else:
            messages.info(request, '用户名或密码错误')
            return redirect(reverse('login'))
