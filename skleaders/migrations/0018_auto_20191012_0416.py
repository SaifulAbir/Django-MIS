# Generated by Django 2.2.4 on 2019-10-12 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skleaders', '0017_skleaderprofile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skleaderprofile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]
