from django.shortcuts import render, redirect
from app01 import models
from app01.forms import UserForm
from app02 import views as v2


def users(request):
    user_list = models.UserInfo.objects.all()
    return render(request, 'user.html', {'user_list': user_list})


def add_user(request):
    if request.method == 'GET':
        obj = UserForm()
        return render(request, 'add_user.html', {'obj': obj})
    else:
        obj = UserForm(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
            models.UserInfo.objects.create(**obj.cleaned_data)
            return redirect('/users/')
        else:
            return render(request, 'add_user.html', {'obj': obj})


def edit_user(request, nid):
    if request.method == 'GET':
        data = models.UserInfo.objects.filter(id=nid).first()
        obj = UserForm({'username': data.username, 'email': data.email})
        return render(request, 'edit_user.html', {'nid': nid, 'obj': obj})
    else:
        obj = UserForm(request.POST)
        if obj.is_valid():
            models.UserInfo.objects.filter(id=nid).update(**obj.cleaned_data)
            return redirect('/users/')
        else:
            return render(request, 'edit_user.html', {'obj': obj, 'nid': nid})


