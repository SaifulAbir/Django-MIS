# Generated by Django 2.2.6 on 2020-01-18 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eduplus_activity', '0012_auto_20200118_0931'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='method',
            options={'ordering': ['-created_date'], 'verbose_name': 'Method', 'verbose_name_plural': 'Methods'},
        ),
        migrations.AlterModelTable(
            name='method',
            table='methods',
        ),
    ]