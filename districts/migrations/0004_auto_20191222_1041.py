# Generated by Django 2.2.4 on 2019-12-22 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0003_merge_20191022_1058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='district',
            options={'ordering': ['-created_date'], 'verbose_name': 'District', 'verbose_name_plural': 'Districts'},
        ),
        migrations.AlterModelTable(
            name='district',
            table='districts',
        ),
    ]
