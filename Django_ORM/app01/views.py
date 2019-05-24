from django.shortcuts import render, HttpResponse
from app01.models import *


# Create your views here.

def index(request):
    return render(request, "index.html")


def addbook(request):
    # b = Book(name='python基础', price=99, author='阿力', pub_date='2019-01-01')
    # b.save()
    # Book.objects.create(name='Django从入门到精通', price=98, author='阿喜', pub_date='2018-03-01')
    # Book.objects.create(**{'name': 'PHP从入门到精通', 'price': 18, 'author': '大力', 'pub_date': '2017-01-10'})
    pub_obj = Publish.objects.filter(name='人民出版社')
    ret = Book.objects.filter(publish_id=pub_obj).values('name', 'price')
    print(ret)
    return HttpResponse("添加成功")


def update(request):
    Book.objects.filter(author='阿喜').update(price=198)
    return HttpResponse('修改成功')


def delete(request):
    Book.objects.filter(author='大力').delete()
    return HttpResponse('删除成功')


def select(request):
    # book_list=Book.objects.all()[:3]
    # print(book_list)
    # print(book_list[0])
    # book_list=Book.objects.filter(id=1)
    # book_list = Book.objects.get(id=2)  # 只能取出一条纪录的时候才不报错
    # book_list = Book.objects.exclude(author='鲁迅')
    # ret = Book.objects.filter(author='鲁迅').values("name", 'price')
    # ret2 = Book.objects.filter(author='鲁迅').values_list("name", 'price')
    # print(ret)
    # print(ret2)
    # book_list = Book.objects.all().values("name").distinct()    #按书名去重
    book_list = Book.objects.filter(name__icontains='d').values('name', 'price')
    return render(request, 'index.html', {"book_list": book_list})
