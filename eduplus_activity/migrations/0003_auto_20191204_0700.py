# Generated by Django 2.2.6 on 2019-12-04 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduplus_activity', '0002_eduplusactivity_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eduplusactivity',
            name='description',
            field=models.TextField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
