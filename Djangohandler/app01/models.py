from django.db import models


# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=64, verbose_name='书名')
    author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True, related_name='booklist')

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=64, verbose_name='作者')
    age = models.IntegerField()
    addr = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class AuthorInfo(models.Model):
    name = models.OneToOneField("Author", on_delete=models.CASCADE)
    frends = models.CharField(max_length=32)


class Tag(models.Model):
    name = models.CharField(max_length=32)
    book = models.ManyToManyField("Book", related_name='books')
