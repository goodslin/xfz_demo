from django.shortcuts import render, HttpResponse, redirect
from django import forms
from django.forms import fields


class F1Form(forms.Form):
    user = fields.CharField(
        max_length=18,
        min_length=6,
        required=True,
        error_messages={
            'required': '用户名不能为空',
            'max_length': '太长了',
            'min_length': '太短了',
        }
    )
    pwd = fields.CharField(
        max_length=32,
        min_length=8,
        required=True,
        error_messages={
            'required': '密码不能为空',
            'max_length': '太长了',
            'min_length': '太短了',
        }
    )
    age = fields.IntegerField(
        required=True,
        error_messages={
            'required': '年龄不能为空',
            'invalid': '必须为数字',
        }
    )
    email = fields.EmailField(
        required=True,
        error_messages={
            'required': '邮箱不能为空',
            'invalid': '请输入正确的邮箱地址',
        }
    )


def f1(request):
    if request.method == 'GET':
        obj = F1Form()
        return render(request, 'f1.html', {'obj': obj})
    else:
        obj = F1Form(request.POST)
        # 是否全部验证成功
        if obj.is_valid():
            # 已经验证过的数据
            print('验证成功', obj.changed_data)
            return redirect('http://www.douban.com')
        else:
            print('验证失败', obj.errors)
            return render(request, 'f1.html', {'obj': obj})
