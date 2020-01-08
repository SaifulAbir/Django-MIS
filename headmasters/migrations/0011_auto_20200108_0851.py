# Generated by Django 2.2.4 on 2020-01-08 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('headmasters', '0010_remove_headmasterprofile_crop_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headmasterdetails',
            name='headmaster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='headmasters.HeadmasterProfile'),
        ),
        migrations.AlterField(
            model_name='headmasterdetails',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school.School'),
        ),
        migrations.AlterField(
            model_name='headmasterprofile',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='school.School'),
        ),
        migrations.AlterField(
            model_name='headmasterprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='headmaster_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]