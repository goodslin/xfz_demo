from django.shortcuts import render, HttpResponse
from app01.models import *
from django.db.models import Avg, Min, Sum, Max, Count
from django.db.models import F, Q

# Create your views here.

def index(request):
    return render(request, 'index.html')


def addbook(request):
    # Book.objects.create(name='WindowsServer2012运维', price=9.9, pub_date='2017-12-01', publish_id=1)
    # publish_obj = Publish.objects.filter(name='人民出版社')[0]
    # Book.objects.create(name='锋利的jQuery', price=19.9, pub_date='2016-10-7', publish=publish_obj)
    # 正向查询，经过外键查询
    # ret = Book.objects.filter(publish__name="人民出版社")
    # print(ret)
    # ret2 = Publish.objects.filter(book__name='python从入门到精通').values("name")
    # print(ret2)
    # ret3 = Book.objects.filter(name='python从入门到精通').values("publish__name")
    # print(ret3)
    # ret4 = Book.objects.filter(publish__city="北京").values("name")
    # print(ret4)

    # book_obj = Book.objects.get(id=2)
    # author_objs = Author.objects.get(id=2)
    # book_obj.authors.add(author_objs)
    # book_obj.authors.remove(1)

    # Book_Author.objects.create(book_id=2, author_id=3)

    # obj = Book.objects.get(id=1)
    # print(obj.book_author_set.all()[0].author)

    # ret2=Book.objects.filter(authors__name='alex').values("name", "price")
    # print(ret2)
    # ret = Book.objects.all().aggregate(Avg("price"))
    # print(ret)
    # ret1 = Book.objects.filter(authors__name="alex").values("name", "price")
    # print(ret1)

    # ret2 = Publish.objects.values("name").annotate(Min("book__price"))
    # print(ret2)
    # Book.objects.all().update(price=F("price")+10)
    # ret3 = Book.objects.filter(Q(price=19.9) | Q(name="Linux运维"))
    # print(ret3)

    ret4 = Book.objects.filter(price=19.9)

    ret = ret4.iterator()
    print(next(ret))
    print(ret.__next__())

    return HttpResponse('success，添加成功！')


def update(): pass


def delete(): pass


def select(): pass
