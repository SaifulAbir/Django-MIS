# Generated by Django 2.2.4 on 2019-10-21 17:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_auto_20191019_1124'),
        ('skmembers', '0006_auto_20191013_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='skmemberprofile',
            name='joining_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='SkmemberDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField(default=django.utils.timezone.now)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School')),
                ('skmember', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skmembers.SkMemberProfile')),
            ],
        ),
    ]