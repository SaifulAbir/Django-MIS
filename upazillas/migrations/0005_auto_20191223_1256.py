# Generated by Django 2.2.4 on 2019-12-23 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upazillas', '0004_merge_20191022_1058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='upazilla',
            options={'verbose_name': 'Upazila', 'verbose_name_plural': 'Upazilas'},
        ),
        migrations.AlterModelTable(
            name='upazilla',
            table='upazilas',
        ),
    ]
