# Generated by Django 2.2.4 on 2019-09-22 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skleaders', '0005_skleaderdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skleaderprofile',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
