from django.db import models


# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=20, verbose_name="姓名")
    price = models.FloatField(verbose_name="价格")
    pub_date = models.DateField(verbose_name="发布日期")
    publish = models.ForeignKey('Publish', on_delete=models.CASCADE, verbose_name="出版社")
    authors = models.ManyToManyField('Author', verbose_name="作者")

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=32, verbose_name="姓名")
    age = models.IntegerField(default=20, verbose_name="年龄")

    def __str__(self):
        return self.name


class Publish(models.Model):
    name = models.CharField(max_length=32, verbose_name="出版社")
    city = models.CharField(max_length=32, verbose_name="城市")

    def __str__(self):
        return self.name
