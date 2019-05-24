from django.db import models


# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    pub_date = models.DateField()
    author = models.CharField(max_length=32, null=False)
    publish_id = models.ForeignKey('Publish')

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=32)


class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
