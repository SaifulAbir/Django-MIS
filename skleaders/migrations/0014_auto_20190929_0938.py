# Generated by Django 2.2.4 on 2019-09-29 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skleaders', '0013_auto_20190929_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skleaderprofile',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.School'),
        ),
    ]
