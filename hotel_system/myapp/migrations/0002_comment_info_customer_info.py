# Generated by Django 2.1.1 on 2018-12-05 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, verbose_name='顾客名字')),
                ('Email', models.EmailField(max_length=30, verbose_name='邮箱')),
                ('number', models.CharField(max_length=11, verbose_name='手机号')),
                ('Message', models.TextField(max_length=41, verbose_name='内容')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_info',
            fields=[
                ('name', models.CharField(max_length=100, verbose_name='顾客名字')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('id_card', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='证件号')),
            ],
        ),
    ]
