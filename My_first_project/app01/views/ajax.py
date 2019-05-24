from django.shortcuts import render, redirect, HttpResponse
from app01 import models


def ajax1(request):
    nid = request.GET.get('nid')
    msg = "成功"
    try:
        models.Classes.objects.filter(id=nid).delete()
    except Exception as e:
        msg = str(e)
    return HttpResponse(msg)