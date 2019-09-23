# Generated by Django 2.2.4 on 2019-09-23 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skleaders', '0009_merge_20190922_1141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skleaderdetails',
            old_name='skLeader',
            new_name='skleader',
        ),
        migrations.AlterField(
            model_name='skleaderprofile',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='skleaderprofile',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.School', unique=True),
        ),
    ]
