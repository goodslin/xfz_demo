from django.shortcuts import render, redirect, HttpResponse
from app01 import models


def get_students(request):
    stu_list = models.Students.objects.all()
    # for row in stu_list:
    # print(row.id, row.username, row.age, row.gender, row.cs.id, row.cs.title)
    return render(request, 'get_students.html', {"stu_list": stu_list})


def add_students(request):
    if request.method == 'GET':
        cs_list = models.Classes.objects.all()
        return render(request, 'add_students.html', {'cs_list': cs_list})
    elif request.method == 'POST':
        u = request.POST.get('username')
        a = request.POST.get('age')
        g = request.POST.get('gender')
        c = request.POST.get('cs')
        models.Students.objects.create(
            username=u,
            age=a,
            gender=g,
            cs_id=c)
        return redirect('/students.html')


def del_students(request):
    nid = request.GET.get('nid')
    models.Students.objects.get(id=nid).delete()
    return redirect('/students.html')


def edit_students(request):
    if request.method == 'GET':
        cs_obj = models.Classes.objects.all().values("id", "title")
        nid = request.GET.get('nid')
        stu_obj = models.Students.objects.filter(id=nid).first()
        return render(request, 'edit_students.html', {'stu_obj': stu_obj, 'cs_obj': cs_obj})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        user = request.POST.get('username')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        class_id = request.POST.get('cs')
        models.Students.objects.filter(id=nid).update(
            username=user,
            age=age,
            gender=gender,
            cs_id=class_id)
        return redirect('/students.html')


def test(request):
    # stu_obj = models.Students.objects.all().values("username", "cs__title")
    # for row in stu_obj:
    #     print(row.username)
    #     print(row.cs.title)

    # stu_obj = models.Students.objects.filter(cs__title="python全栈3班").values('username', 'cs__title')
    # for row in stu_obj:
    #     print(row['username'], row['cs__title'])

    # cla_obj = models.Classes.objects.filter(title='python全栈3班').first()
    # print(cla_obj.ssss.all())

    # cls_list = models.Classes.objects.all()
    # for obj in cls_list:
    #     print(obj.id, obj.title, obj.m.all())
    #     for row in obj.m.all():
    #         print('--->', row.name)

    # obj = models.Teachers.objects.filter(id=3).first()
    # obj.ssssss.set([1])

    # obj = models.Classes.objects.all().values('id', 'title', 'm__name')
    # print(obj)

    obj = models.Teachers.objects.all().values('name', 'goodslin__title')
    print(obj)
    return HttpResponse('ok')
