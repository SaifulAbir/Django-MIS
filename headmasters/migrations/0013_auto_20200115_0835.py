# Generated by Django 2.2.6 on 2020-01-15 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('headmasters', '0012_auto_20200115_0529'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='headmasterdetails',
            options={'verbose_name': 'Headmaster Detail', 'verbose_name_plural': 'Headmaster Details'},
        ),
        migrations.AlterModelOptions(
            name='headmasterprofile',
            options={'verbose_name': 'Headmaster', 'verbose_name_plural': 'Headmasters'},
        ),
        migrations.AlterModelTable(
            name='headmasterdetails',
            table='headmaster_profile_details',
        ),
        migrations.AlterModelTable(
            name='headmasterprofile',
            table='headmaster_profiles',
        ),
    ]
