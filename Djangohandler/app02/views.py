from django.shortcuts import render, HttpResponse
from app02 import models
from django.db.models import Avg, Sum, Q, Count, Max, Min, F
from django.db import connection


# 平均成绩大于60分的学生的id和成绩
def index01(request):
    students = models.Student.objects. \
        annotate(score_avg=Avg("score__number")).filter(score_avg__gt=60).values('id', 'score_avg')
    for student in students:
        print(student)

    print(connection.queries)
    return HttpResponse("NB")


def index02(request):
    """查询所有同学的id，姓名，选课数量，总成绩"""
    students = models.Student.objects. \
        annotate(score_nums=Count("score"), total=Sum("score__number")).values('id', 'name', 'score_nums', 'total')
    for student in students:
        print(student)
    return HttpResponse("NB")


def index03(request):
    """查询姓仓的老师的个数"""
    teachers = models.Teacher.objects.filter(name__startswith="苍").count()
    print(teachers)
    return HttpResponse("NB")


def index04(request):
    """查询所有没学过苍老师课程的姓名和id"""
    students = models.Student.objects.exclude(score__course__teacher__name="苍老师")
    for student in students:
        print(student.id, student.name)
    return HttpResponse("NB")


def index05(request):
    """查询学过id为1和2课程的所有同学的id和姓名"""
    students = models.Student.objects.filter(score__course__in=(1, 2)).values('id', 'name').distinct()
    for student in students:
        print(student)
    return HttpResponse("NB")


def index06(request):
    """查询所有学过苍老师所教的所有课的同学学号和姓名
    1、找到每一位学生学习黄老师课程的数量
    2、黄老师教的课程数量
    3、二者对比如果相等，就输出
    """
    # students = models.Student.objects.filter(score__course__teacher__name="波多老师").values('id', 'name').distinct()
    # for student in students:
    #     print(student)
    students = models.Student.objects.annotate(nums=Count("score__course", filter=Q(score__course__teacher__name="波多老师"))) \
        .filter(nums=models.Course.objects.filter(teacher__name="波多老师").count()).values('id', 'name')
    for student in students:
        print(student)
    return HttpResponse("NB")


def index07(request):
    """查询所有课程成绩小于60分的同学的id、姓名"""
    students = models.Student.objects.filter(score__number__lt=60).values('id', 'name').distinct()
    for student in students:
        print(student)
    return HttpResponse("NB")


def index08(request):
    """查询所有没有学全所有课程的同学id和姓名"""
    students = models.Student.objects.filter(score__course__exact=(1, 2, 3, 4)).values('id', 'name')
    for student in students:
        print(student)
    return HttpResponse("NB")


def index09(request):
    """查询各科成绩的最高和最低分，以如下形式显示：课程ID，课程名称，最高分，最低分"""
    courses = models.Course.objects.annotate(max=Max("score__number"), min=Min("score__number"))
    for course in courses:
        print(course.id, course.name, course.max, course.min)
    return HttpResponse("NB")


def index10(request):
    """查询所有学生的姓名、平均分、并且按照平均分从高到低排序"""
    students = models.Student.objects.annotate(score_avg=Avg("score__number")) \
        .order_by('score_avg').values('id', 'name', 'score_avg')
    for student in students:
        print(student)
    return HttpResponse("NB")


def index11(request):
    """查询每门课程的平均成绩，按照平均成绩进行排序"""
    courses = models.Course.objects.annotate(score_avg=Avg("score__number")).order_by("score_avg")
    for course in courses:
        print(course.name, course.score_avg)


def index12(request):
    """统计总共有多少男生，多少女生"""
    students = models.Student.objects.values('gender').annotate(gender_count=Count('gender'))
    for student in students:
        print(student)
    return HttpResponse("NB")


def index13(request):
    """将苍老师的课程成绩在原来的基础上都加5分"""
    models.Score.objects.filter(course__teacher__name="苍老师").update(number=F("number") + 5)
    return HttpResponse("NB")


def index14(request):
    """查询两门以上不及格的同学的id、姓名、以及不及格的课程数
    1、查询所有不及格的学生
    2、统计每个学生不及格的课程的数量判断是否大于2
    """
    students = models.Student.objects.filter(score__number__lt=60).annotate(student_count=Count("score__number"))
    return HttpResponse("NB")


def index15(request):
    """查询每门课的选课人数
    1、按课程分类
    2、计算课程人数
    """
    courses = models.Course.objects.annotate(sutdent_nums=Count("score__student"))
    for course in courses:
        print(course.name, course.sutdent_nums)
    return HttpResponse("NB")
