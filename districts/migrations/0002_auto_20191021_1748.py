# Generated by Django 2.2.4 on 2019-10-21 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('division', '0003_auto_20191019_1124'),
        ('districts', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='district',
            unique_together={('division', 'name')},
        ),
    ]