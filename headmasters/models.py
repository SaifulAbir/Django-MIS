from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import User
from school.models import School


class HeadmasterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='headmaster_profile')
    mobile = models.CharField(max_length=11)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.user.first_name


