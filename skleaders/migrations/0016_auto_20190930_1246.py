# Generated by Django 2.2.4 on 2019-09-30 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skleaders', '0015_auto_20190930_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skleaderprofile',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school.School'),
        ),
    ]
