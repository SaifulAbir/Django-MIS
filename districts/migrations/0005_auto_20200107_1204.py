# Generated by Django 2.2.4 on 2020-01-07 12:04

from django.db import migrations, models
import sknf.validators


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0004_auto_20191222_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(max_length=128, validators=[sknf.validators.check_valid_chars]),
        ),
    ]