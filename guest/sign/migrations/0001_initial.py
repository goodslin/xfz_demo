# Generated by Django 2.1.7 on 2019-04-12 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('limit', models.IntegerField()),
                ('status', models.BooleanField()),
                ('address', models.CharField(max_length=200)),
                ('start_time', models.DateTimeField(verbose_name='events time')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realname', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=16)),
                ('emai', models.EmailField(max_length=254)),
                ('sign', models.BooleanField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sign.Event')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='guest',
            unique_together={('event', 'phone')},
        ),
    ]
