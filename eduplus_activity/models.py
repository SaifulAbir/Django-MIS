from django.db import models

# Create your models here.
from django.utils import timezone

from accounts.models import User
from school.models import School
from topics.models import Topics


class EduPlusActivity(models.Model):
    date = models.DateField(default=timezone.now)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    presence_skleader = models.BooleanField(default=False)
    attendance= models.ManyToManyField(User, related_name='member_profile')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    topics = models.ManyToManyField(Topics)
    description = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.school + " on "+self.date

    class Meta:
        ordering = ['-date']
