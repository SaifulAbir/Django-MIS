# Generated by Django 2.2.4 on 2019-11-02 11:12

from django.db import migrations, models
import sknf.validators


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0012_auto_20191027_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='club_establishment_date',
            field=models.DateField(blank=True, null=True, validators=[sknf.validators.no_future]),
        ),
    ]
