from django.shortcuts import render, HttpResponse
from app01 import models
import json

# Create your views here.


def xuliehua(request):
    return render(request, 'xuliehua.html')


def get_data(request):
    from django.core import serializers

    ret = {'status': True, 'data': None}
    try:
        user_list = models.UserInfo.objects.all()
        ret['data'] = serializers.serialize("json", user_list)
    except Exception as e:
        ret['status'] = False
    result = json.dumps(ret)
    return HttpResponse(result)
