# Generated by Django 2.2.4 on 2020-01-20 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skleaders', '0025_auto_20200118_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skleaderprofile',
            name='mobile',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]