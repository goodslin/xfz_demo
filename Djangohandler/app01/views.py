from django.shortcuts import render, redirect, HttpResponse
from django.db import connection
from app01 import models


def get_cursor():
    return connection.cursor()


def index(request):
    books = models.Book.objects.all()
    return render(request, 'index.html', {'books': books})


def add_book(request):
    if request.method == 'GET':
        return render(request, 'add_book.html')
    else:
        name = request.POST.get('bookname')
        author = request.POST.get('author')
        # print(name, author)
        models.Book.objects.create(name=name, author=author)
        return render(request, 'add_book.html')


def book_detail(request):
    book_id = request.GET.get('id')
    row = models.Book.objects.filter(id=book_id)
    return render(request, 'book_detail.html', {'row': row})


def del_book_detail(request):
    book_id = request.GET.get('id')
    # print(book_id)
    models.Book.objects.filter(id=book_id).delete()
    return redirect('/')


def add_more_book(request):
    author_obj = models.Author.objects.first()
    book = models.Book(name="怎样打坦克")
    book.author = author_obj

    book.save()
    return HttpResponse("Success")


def author_get_book(request):
    author_obj = models.Author.objects.first()
    book_obj = author_obj.booklist.all()
    for i in book_obj:
        print(i)
    return HttpResponse('Get Book Success')


def book_get_author(request):
    book_obj = models.Book.objects.get(name='怎样打坦克')
    author = book_obj.author.name
    print(author)
    return HttpResponse("查询成功")


def author_add_authorinfo(request):
    author_obj = models.Author.objects.first()
    authorinfo_obj = models.AuthorInfo(frends='王五')
    authorinfo_obj.name = author_obj

    authorinfo_obj.save()
    return HttpResponse('增加成功')


def another_add(request):
    author_obj = models.Author.objects.first()
    book = models.Book(name="怎样打铁")
    # book.author = author_obj

    author_obj.booklist.add(book, bulk=False)
    return HttpResponse("增加成功啦！！！")


def add_tag(request):
    book_obj = models.Book.objects.get(pk=13)
    # tag_obj = models.Tag(name="文学")
    # tag_obj.save()
    tag_obj = models.Tag.objects.get(pk=3)
    book_obj.books.add(tag_obj)
    return HttpResponse("Add Success！")


def choose_tag(request):
    tag_obj = models.Tag.objects.get(pk=3)
    # book_obj = models.Book.objects.get(pk=10)
    # tag_obj.book.add(book_obj)
    book = tag_obj.book.all()
    for i in book:
        print(i)

    return HttpResponse("OK")
