# Generated by Django 2.2.4 on 2019-09-28 06:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubMeetings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('class_room', models.CharField(max_length=100)),
                ('presence_guide_teacher', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='MeetingTopics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club_meetings.ClubMeetings')),
                ('topics', models.ManyToManyField(to='topics.Topics')),
            ],
        ),
    ]
