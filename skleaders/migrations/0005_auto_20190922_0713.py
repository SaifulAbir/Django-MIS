# Generated by Django 2.2.4 on 2019-09-22 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skleaders', '0004_auto_20190921_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skleaderprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='skleaderprofile',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.School'),
        ),
    ]
