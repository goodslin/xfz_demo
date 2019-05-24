# Generated by Django 2.1.7 on 2019-04-06 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20190406_1838'),
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='SomeBody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=32)),
                ('par', models.ForeignKey(on_delete=True, to='app01.Part')),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_type',
            field=models.IntegerField(choices=[(0, '普通用户'), (1, '超级用户'), (2, 'VIP用户')], verbose_name='选项'),
        ),
        migrations.AddField(
            model_name='somebody',
            name='pking',
            field=models.ForeignKey(on_delete=True, related_name='b', to='app01.UserInfo'),
        ),
    ]
