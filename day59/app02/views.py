from django.shortcuts import render, HttpResponse, redirect
from django import forms
from django.forms import fields
from django.forms import widgets
from app01 import models
from django.forms.models import ModelChoiceField
import json
from django.forms.utils import ErrorDict

class TestForm(forms.Form):
    user = fields.CharField(
        required=True,  # 是否为空
        max_length=12,  # 最大长度
        min_length=3,  # 最小长度
        error_messages={},
        # widget=widgets.Select(),     # 定制HTML插件
        label='用户名',
        # initial='用户名',
        # disabled=True,
        label_suffix=':',
    )
    age = fields.IntegerField(
        required=True,
        label='年龄',
        max_value=12,
        min_value=1,
    )
    email = fields.EmailField(required=True, label='Email')
    image = fields.FileField()
    city = fields.TypedChoiceField(
        coerce=lambda x: int(x),
        choices=[(1, '上海',), (2, '北京',), (3, '武汉',)],
        initial=2,
    )
    hobby = fields.MultipleChoiceField(
        choices=[(1, '篮球'), (2, '足球'), (3, '乒乓球')],

    )
    # xdd = fields.CharField(
    #     # widget=widgets.Select(choices=[(1, '张三',), (2, '李四',), (3, '王五',)])
    #     widget=widgets.CheckboxInput()
    # )
    xdd = fields.MultipleChoiceField(
        initial=[2, ],
        choices=((1, '上海',), (2, '北京',), (3, '天津',)),
        widget=widgets.CheckboxSelectMultiple,
    )
    # 单radio，值为字符串
    address = fields.CharField(
        initial=2,
        widget=widgets.RadioSelect(choices=((1, '上海'), (2, '北京'),)),
    )


class AjaxForm(forms.Form):
    price = fields.IntegerField()
    user_id = fields.IntegerField(
        widget=widgets.Select()
    )
    user_id2 = ModelChoiceField(
        queryset=models.UserInfo.objects.all(),
        to_field_name='id',
    )

    def __init__(self, *args, **kwargs):
        # 拷贝所有的静态字段，赋值给self.fields
        super(AjaxForm, self).__init__(*args, **kwargs)
        self.fields['user_id'].widget.choices = models.UserInfo.objects.values_list('id', 'username')


def ajax(request):
    ret = {'status': 'SB', 'message': None}
    if request.method == 'GET':
        obj = AjaxForm()
        return render(request, 'ajax.html', {'obj': obj})
    else:
        obj = AjaxForm(request.POST)
        if obj.is_valid():
            ret['status'] = '钱'
            print(obj.cleaned_data)
            return HttpResponse(json.dumps(ret))
        else:
            print(type(obj.errors))
            print(obj.errors.as_ul())
            print(obj.errors.as_json())


def test(request):
    if request.method == 'GET':
        obj = TestForm()
        txt = "<input  type='text'/>"
        from django.utils.safestring import mark_safe
        txt = mark_safe(txt)
        return render(request, 'test.html', {'obj': obj, 'txt': txt})
    else:
        obj = TestForm(request.POST, request.FILES)
        obj.is_valid()
        print(obj.cleaned_data)
        return render(request, 'test.html', {'obj': obj})
