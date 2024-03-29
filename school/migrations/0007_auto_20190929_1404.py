# Generated by Django 2.2.4 on 2019-09-29 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_remove_school_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='school',
            name='school_id',
            field=models.CharField(default='', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
