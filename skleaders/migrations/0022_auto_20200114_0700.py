# Generated by Django 2.2.6 on 2020-01-14 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skleaders', '0021_auto_20200114_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skleaderprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('', '--Select--'), ('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
    ]
