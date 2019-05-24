from django.shortcuts import render
from datetime import datetime


# Create your views here.

def test(request):
    value = datetime(year=2017, month=4, day=24, hour=13, minute=7, second=0)
    return render(request, 'test.html', {'value': value})
