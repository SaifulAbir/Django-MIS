# Generated by Django 2.2.6 on 2020-01-14 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skleaders', '0020_auto_20200108_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skleaderprofile',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='skleaderprofile',
            name='roll',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='skleaderprofile',
            name='student_class',
            field=models.CharField(blank=True, choices=[('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=10, null=True),
        ),
    ]
