# Generated by Django 2.1.1 on 2018-12-17 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_customer_info_room_kind'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin_info',
            name='add_room',
        ),
    ]
