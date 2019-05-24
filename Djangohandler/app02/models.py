from django.db import models


class Student(models.Model):
    """学生表"""
    name = models.CharField(max_length=32)
    gender_choices = ((1, '男'), (2, '女'),)
    gender = models.SmallIntegerField(choices=gender_choices)

    def __str__(self):
        return self.name

    class Mete:
        db_table = 'student'


class Course(models.Model):
    """课程表"""
    name = models.CharField(max_length=32)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)

    def __str__(self):
        return "%s/%s" % (self.name, self.teacher.name)

    class Meta:
        db_table = 'course'


class Score(models.Model):
    """成绩表"""
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    course = models.ForeignKey("Course", on_delete=models.CASCADE)
    number = models.FloatField(null=True)

    def __str__(self):
        return "%s/%s" % (self.student.name, self.course.name)

    class Meta:
        db_table = 'score'


class Teacher(models.Model):
    """老师表"""
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'teacher'
