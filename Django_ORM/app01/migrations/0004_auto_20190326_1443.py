# Generated by Django 2.1.7 on 2019-03-26 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20190326_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='user_group',
        ),
        migrations.AlterField(
            model_name='book',
            name='publish_id',
            field=models.ForeignKey(on_delete='CASCADE', to='app01.Publish'),
        ),
    ]
