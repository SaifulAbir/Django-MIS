# Generated by Django 2.2.4 on 2020-01-08 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club_meetings', '0007_auto_20191231_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubmeetings',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='school.School'),
        ),
        migrations.AlterField(
            model_name='clubmeetings',
            name='skleader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='skleaders.SkLeaderProfile'),
        ),
    ]
