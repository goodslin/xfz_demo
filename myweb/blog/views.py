from django.shortcuts import render, HttpResponse, redirect
import time


# Create your views here.
class Animal():
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex


def show_time(req):
    t = time.ctime()
    # return render(req, "index.html", locals())
    return render(req, "show_time.html", {"time": t})


def article_year(request, year, month):
    return HttpResponse("year:%s month:%s" % (year, month))


def register(request):
    if request.method == "POST":
        user = request.POST.get("user")
        if user == "lin":
            print(request.POST.get("user"))
            return redirect('/login/')
        return HttpResponse("success!")
    return render(request, "register.html")


def login(req):
    name = 'lin'
    return render(req, "login.html", locals())


def query(request):
    l = ["苍老师", "吉泽老师", "波多老师"]
    d = {'name': "欧阳霸天", 'age': 19}
    c = Animal("alex", "公")
    return render(request, "index.html", locals())


def xxxx(req):
    return HttpResponse('ok')
