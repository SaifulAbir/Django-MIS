# Generated by Django 2.2.6 on 2019-11-02 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20191027_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=40, verbose_name='first name'),
        ),
    ]
