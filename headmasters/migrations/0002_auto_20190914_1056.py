# Generated by Django 2.2.4 on 2019-09-14 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('headmasters', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='headmasterprofile',
            old_name='Role',
            new_name='role',
        ),
    ]