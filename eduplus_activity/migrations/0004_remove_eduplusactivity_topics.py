# Generated by Django 2.2.6 on 2019-12-08 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eduplus_activity', '0003_auto_20191204_0700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eduplusactivity',
            name='topics',
        ),
    ]
