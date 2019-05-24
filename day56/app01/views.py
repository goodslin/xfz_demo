from django.shortcuts import render, redirect, HttpResponse
from app01 import models
import json


# Create your views here.


def students(request):
    stu_list = models.Students.objects.all()
    cls_list = models.Classes.objects.all()
    return render(request, 'students.html', {'stu_list': stu_list, 'cls_list': cls_list})


def add_student(request):
    response = {'status': True, 'message': None, 'data': None}
    try:
        username = request.POST.get('username')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        cls_id = request.POST.get('cls_id')
        obj = models.Students.objects.create(username=username, age=age, gender=gender, cs_id=cls_id)
        response['data'] = obj.id
    except Exception as e:
        response['status'] = False
        response['message'] = '用户输入错误'
    result = json.dumps(response, ensure_ascii=False)
    return HttpResponse(result)


def del_student(request):
    ret = {'status': True}
    try:
        nid = request.POST.get('nid')
        models.Students.objects.filter(id=nid).delete()
    except Exception as e:
        ret['status'] = False
    result = json.dumps(ret, ensure_ascii=False)
    return HttpResponse(result)


def edit_student(request):
    response = {'code': 1000, 'message': None}
    try:
        nid = request.POST.get('nid')
        user = request.POST.get('user')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        cls_id = request.POST.get('cls_id')
        models.Students.objects.filter(id=nid).update(
            username=user,
            age=age,
            gender=gender,
            cs_id=cls_id,
        )
        print(nid, user, age, gender, cls_id)
        # models.Students.objects.filter(id=nid).update(username='张三', age=17, gender=0, cs_id=3)
        # rec = models.Students.objects.filter(id=nid).all()
        # for item in rec:
        #     print(item.id, item.username, item.age, item.gender, item.cs_id)
    except Exception as e:
        response['status'] = 1001
        response['message'] = str(e)
    return HttpResponse(json.dumps(response))
