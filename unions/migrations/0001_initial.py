# Generated by Django 2.2.4 on 2019-09-24 06:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('districts', '0001_initial'),
        ('division', '0001_initial'),
        ('upazillas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Union',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='districts.District')),
                ('division', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='division.Division')),
                ('upazilla', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='upazillas.Upazilla')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
