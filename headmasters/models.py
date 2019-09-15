from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import User


class HeadmasterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='headmaster_profile')
    mobile = models.CharField(max_length=11)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	print('****', created)
	HeadmasterProfile.objects.get_or_create(user = instance)

