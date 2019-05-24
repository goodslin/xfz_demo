from django.db import models


# Create your models here.
# 增加
# models.Teachers.objects.create(name='root')
# obj = Teachers(name='root')
# obj.save()
# 查找
# Teachers.objects.all()
# Teachers.objects.filter(id=1)
# Teachers.objects.filter(id=1,name='root')
# result = Teachers.objects.filter(id__gt=1)
# [obj(id,name),obj(id,name)]
# result = Teachers.objects.filter(id__gt=1).first()
# 删除
# Teachers.objects.filter(id=1).delete()
# 改
# Teachers.objects.all().update(name='alex')
# Teachers.objects.filter(id=1).update(name='alex')

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
    cs = models.ForeignKey(Classes, on_delete=models.CASCADE, related_name='ssss')

    def __str__(self):
        return self.username

# 查找
# ret = Students.objects.all()
# [obj(1,)...]
# for item in ret:
#     print(item.id)
#     print(item.age)
#     print(item.gender)
#     print(item.cs_id)
#     print(item.cs.id)
#     print(item.cs.name)
#
# 删除
# Students.objects.filter(id=1).delete()
# Students.objects.filter(cs_id=1).delete()
#
# cid = input('请输入班级ID')
# Students.objects.filter(cs_id=cid).delete()
#
# cname = input('请输入班级名称')
# Students.objects.filter(cs__name=cname).delete()

# 增加
# obj = Classes.objects.filter(id=1).first()
# obj.m.add(1)
# 删除
# obj.m.remove(1)
# 清空
# obj.m.clear()
# 设置
# obj.m.set([2, 3, 4])

# obj.m.all()

# 1、类代表数据库表
# 2、类的对象代指数据库的一行纪录
# 3、FK字段代指关联表中的一行数据（类的对象）
# 4、- 正向：fk字段
#    - 反向：小写类名_set()  related_name='ssss' 可以对反向查询进行重构
# 5、谁是主表？就全部列出其数据
#     - models.Students.objects.all().values('username', 'cs__title')
#     - models.Classes.objects.all().values('title','ssss__username')
# 4、M2M字段，自动生成第三张表；依赖关联表对第三章表进行间接操作

# 示例
# - 所有学生的姓名以及其所在班级名称，QuerySet
#     stu_list = Students.objects.all()
#     select * from tb;
#     [obj1,obj2,obj3]
#
#     stu_list = Students.objects.all().values("id", "usename")
#     select id,username from tb;
#     [{"id":1,"username":'xx'},{..}]
#
#     stu_list = Students.objects.all().values_list("id",'username')
#     [(1,'root'),(2,'alex')]
#
# - 找到三班的所有学生
#     stu_obj = models.Students.objects.filter(cs__title="python全栈3班").values('username', 'cs__title')
#     for row in stu_obj:
#         print(row['username'],row[cs__title])
# - 通过三班反向查询三班所有的学生
#     cla_obj = models.Classes.objects.filter(title='python全栈3班').first()
#     print(cla_obj.students_set.all())