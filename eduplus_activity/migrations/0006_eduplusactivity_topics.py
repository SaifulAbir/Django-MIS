# Generated by Django 2.2.6 on 2019-12-08 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduplus_activity', '0005_eduplustopics'),
    ]

    operations = [
        migrations.AddField(
            model_name='eduplusactivity',
            name='topics',
            field=models.ManyToManyField(to='eduplus_activity.EduplusTopics'),
        ),
    ]
