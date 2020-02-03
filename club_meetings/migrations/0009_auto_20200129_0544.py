# Generated by Django 2.2.4 on 2020-01-29 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skmembers', '0014_auto_20200120_0707'),
        ('club_meetings', '0008_auto_20200108_0851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clubmeetings',
            name='attendance',
        ),
        migrations.AddField(
            model_name='clubmeetings',
            name='student_attendance',
            field=models.ManyToManyField(related_name='a_profile', to='skmembers.SkMemberProfile'),
        ),
    ]