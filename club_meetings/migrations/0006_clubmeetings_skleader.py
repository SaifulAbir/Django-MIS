# Generated by Django 2.2.6 on 2019-12-21 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skleaders', '0019_auto_20191015_0833'),
        ('club_meetings', '0005_auto_20191027_0621'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubmeetings',
            name='skleader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='skleaders.SkLeaderProfile'),
        ),
    ]
