# Generated by Django 2.2.6 on 2019-10-19 11:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0010_auto_20191019_1124'),
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassOrientation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('student_class', models.CharField(choices=[('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=10)),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school.School')),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='topics.Topics')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
