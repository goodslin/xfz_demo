from django.shortcuts import render, HttpResponse


# Create your views here.


def session_view(request):
    request.session['username'] = 'goodslin'
    username = request.session.get('username')
    return HttpResponse('session view')
