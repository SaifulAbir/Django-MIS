# Generated by Django 2.2.4 on 2019-09-28 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_school_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='image',
        ),
    ]