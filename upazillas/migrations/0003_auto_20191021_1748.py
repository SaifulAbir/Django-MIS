# Generated by Django 2.2.4 on 2019-10-21 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0002_auto_20191021_1748'),
        ('division', '0003_auto_20191019_1124'),
        ('upazillas', '0002_auto_20190921_0323'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='upazilla',
            unique_together={('division', 'district', 'name')},
        ),
    ]