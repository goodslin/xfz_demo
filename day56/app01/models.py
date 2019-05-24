from django.db import models

# Create your models here.


class Classes(models.Model):
    """
    班级表
    """
    title = models.CharField(max_length=32)
    m = models.ManyToManyField("Teachers", related_name='goodslin')

    def __str__(self):
        return self.title


class Teachers(models.Model):
    """
    老师表
    """
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Students(models.Model):
    """
    学生表
    """
    username = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.BooleanField()
    cs = models.ForeignKey(Classes, on_delete=models.CASCADE)

    def __str__(self):
        return self.username