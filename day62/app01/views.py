from django.shortcuts import render, HttpResponse
import json
import os
import uuid


# Create your views here.


def index(request):
    return render(request, 'index.html')


def ajax1(request):
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    return HttpResponse('...')


def upload_img(request):
    nid = str(uuid.uuid4())
    ret = {'status': True, 'message': None, 'data': None}
    obj = request.FILES.get('k3')
    file_path = os.path.join('static', nid+obj.name)
    f = open(file_path, 'wb')
    for line in obj.chunks():
        f.write(line)
    f.close()
    ret['data'] = file_path
    return HttpResponse(json.dumps(ret))


def jsonp(request):
    return render(request, 'jsonp.html')