# Generated by Django 2.2.4 on 2019-09-21 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('headmasters', '0004_auto_20190918_0736'),
    ]

    operations = [
        migrations.AddField(
            model_name='headmasterdetails',
            name='headmaster',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='headmasters.HeadmasterProfile'),
            preserve_default=False,
        ),
    ]
