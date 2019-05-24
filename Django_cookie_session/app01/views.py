from django.shortcuts import render, redirect
import datetime
from django.views import View


# Create your views here.


def login(request):
    print("COOKIES", request.COOKIES)
    print("SESSION", request.session)
    if request.method == 'POST':
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if user == "goodslin" and pwd == "Jacklin012":
            ret = redirect("/index/")
            ret.set_cookie("username", user, max_age=12, expires=datetime.datetime.utcnow()+datetime.timedelta(hours=3))
            return ret

            # COOKIE and session
            # request.session["is_login"] = True
            # request.session["user"] = user
            # return redirect("/index/")
    return render(request, "login.html")


def index(request):

    # if request.COOKIES.get("username", None):
    #     name = "goodslin"
    #
    #     return render(request, "index.html", locals())
    # else:
    #
    #     return redirect("/login/")

    # COOKIE and session
    if request.session.get("is_login", None):
        request.session.set_expiry(expires=datetime.datetime.utcnow()+datetime.timedelta(hours=24))
        name = request.session.get("user", None)
        return render(request, "index.html", locals())

    else:
        return redirect("/login/")


class CBV(View):
    def dispatch(self, request, *args, **kwargs):
        result = super(CBC, self).dispatch(request, *args, **kwargs)
        return result