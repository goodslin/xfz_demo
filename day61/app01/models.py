from django.db import models


# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(
        null=True,
        db_column='user',
        max_length=32,
        verbose_name='用户名',
        help_text='请输入用户名',
    )

    user_type_choices = [
        (0, '普通用户'),
        (1, '超级用户'),
        (2, 'VIP用户'),
    ]

    user_type = models.IntegerField(
        choices=user_type_choices,
        verbose_name='选项',
    )

    def __str__(self):
        return self.username


class SomeBody(models.Model):
    caption = models.CharField(max_length=32)
    pking = models.ForeignKey(
        to="UserInfo",
        to_field='id',
        related_name='b',
        # related_query_name='b',
        on_delete=True,
    )


class User(models.Model):
    username = models.CharField(max_length=32, db_index=True, verbose_name='姓名')
    par = models.ForeignKey(
        to='Part',
        to_field='id',
        on_delete=True,
        verbose_name='部门',
    )

    def __str__(self):
        return self.username


class Part(models.Model):
    caption = models.CharField(max_length=32, verbose_name='部门')

    def __str__(self):
        return self.caption


class Tag(models.Model):
    title = models.CharField(max_length=16)
    m = models.ManyToManyField(
        to='User',   # 默认和User表的主键进行关联

    )