from django.db import models


# Create your models here.
# 发布会表
class Event(models.Model):
    name = models.CharField(max_length=32, verbose_name='发布会标题')
    limit = models.IntegerField(verbose_name='参加人数')
    status = models.BooleanField(verbose_name='状态')
    address = models.CharField(max_length=200, verbose_name='地址')
    start_time = models.DateTimeField(verbose_name='发布会时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '发布会表'


# 嘉宾表
class Guest(models.Model):
    event = models.ForeignKey(to='Event', on_delete=models.CASCADE, verbose_name='发布会id')
    realname = models.CharField(max_length=32, verbose_name='姓名')
    phone = models.CharField(max_length=16, verbose_name='手机号')
    email = models.EmailField(verbose_name='邮箱')
    sign = models.BooleanField(verbose_name='签到状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name_plural = '嘉宾表'
        unique_together = ('event', 'phone')

    def __str__(self):
        return self.realname
