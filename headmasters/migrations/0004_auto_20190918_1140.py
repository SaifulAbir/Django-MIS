# Generated by Django 2.2.4 on 2019-09-18 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('headmasters', '0003_auto_20190918_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headmasterdetails',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='headmasterdetails',
            name='to_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
