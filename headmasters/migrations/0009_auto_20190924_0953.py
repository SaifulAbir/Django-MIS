# Generated by Django 2.2.4 on 2019-09-24 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('headmasters', '0008_auto_20190923_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headmasterprofile',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.School'),
        ),
    ]