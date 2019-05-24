from django.shortcuts import render


# Create your views here.


def backend(request):
    return render(request, "base.html")


def student(request):
    student_list = ["阿文", "阿超", "阿亮", "胖虎"]
    return render(request, "student.html", locals())
