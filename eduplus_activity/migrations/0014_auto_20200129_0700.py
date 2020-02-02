# Generated by Django 2.2.4 on 2020-01-29 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skmembers', '0014_auto_20200120_0707'),
        ('eduplus_activity', '0013_auto_20200118_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eduplusactivity',
            name='attendance',
        ),
        migrations.AddField(
            model_name='eduplusactivity',
            name='student_attendance',
            field=models.ManyToManyField(related_name='member_profile', to='skmembers.SkMemberProfile'),
        ),
    ]
