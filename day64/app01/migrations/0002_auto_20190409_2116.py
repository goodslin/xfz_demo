# Generated by Django 2.1.7 on 2019-04-09 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classification',
            options={'verbose_name_plural': '分类（视频分类）'},
        ),
        migrations.AlterModelTable(
            name='classification',
            table='Classification',
        ),
    ]
