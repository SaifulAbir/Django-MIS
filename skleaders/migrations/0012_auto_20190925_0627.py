# Generated by Django 2.2.4 on 2019-09-25 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skleaders', '0011_auto_20190924_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skleaderprofile',
            name='student_class',
            field=models.PositiveIntegerField(choices=[(6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')]),
        ),
    ]
