
# Generated by Django 2.2.4 on 2019-09-16 13:05

# Generated by Django 2.2.4 on 2019-09-16 12:44


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0004_auto_20190915_0543'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0004_auto_20190915_0543'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeadmasterProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=11)),
                ('image', models.ImageField(upload_to='images/')),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.School')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='headmaster_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
