# Generated by Django 2.2.6 on 2020-01-18 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eduplus_activity', '0011_auto_20200108_0851'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eduplusactivity',
            options={'ordering': ['-date'], 'verbose_name': 'Eduplus Activity', 'verbose_name_plural': 'Eduplus Activities'},
        ),
        migrations.AlterModelTable(
            name='eduplusactivity',
            table='eduplus_activities',
        ),
    ]
