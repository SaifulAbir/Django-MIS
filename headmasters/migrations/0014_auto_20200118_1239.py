# Generated by Django 2.2.4 on 2020-01-18 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('headmasters', '0013_auto_20200115_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headmasterprofile',
            name='mobile',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]