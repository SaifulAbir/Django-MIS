# Generated by Django 2.2.6 on 2019-10-22 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('division', '0003_auto_20191019_1124'),
        ('districts', '0002_auto_20191022_0232'),
        ('upazillas', '0002_auto_20190921_0323'),
        ('unions', '0003_auto_20190921_0323'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='union',
            unique_together={('division', 'district', 'upazilla', 'name')},
        ),
    ]
