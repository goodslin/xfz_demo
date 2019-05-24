from django.shortcuts import render, HttpResponse


# Create your views here.


def upload(request):
    if request.method == 'GET':
        return render(request, 'upload.html')
    else:
        img = request.FILES.get('img')
        print(request.POST)
        print(request.FILES)
        print(img.name)
        print(img.size)
        f = open(img.name, 'wb')
        for line in img.chunks():
            f.write(line)
        f.close()
        return HttpResponse('123')