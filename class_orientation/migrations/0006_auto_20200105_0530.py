# Generated by Django 2.2.6 on 2020-01-05 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('class_orientation', '0005_auto_20200101_1110'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='peereducation',
            options={'ordering': ['-created_date'], 'verbose_name': 'Peer Education', 'verbose_name_plural': 'Peer Educations'},
        ),
        migrations.AlterModelTable(
            name='peereducation',
            table='peer_educations',
        ),
    ]
