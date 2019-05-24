from django.db import models
from django.core import validators


class Article(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    username = models.CharField(max_length=32)
    telephone = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=16)


class Book(models.Model):
    title = models.CharField(max_length=64)
    page = models.IntegerField()
    price = models.FloatField(validators=[validators.MaxValueValidator(limit_value=1000)])
