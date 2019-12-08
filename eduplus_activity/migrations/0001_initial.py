# Generated by Django 2.2.6 on 2019-12-04 05:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('topics', '0001_initial'),
        ('school', '0013_auto_20191102_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='EduPlusActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('presence_skleader', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('attendance', models.ManyToManyField(related_name='member_profile', to=settings.AUTH_USER_MODEL)),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school.School')),
                ('topics', models.ManyToManyField(to='topics.Topics')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]