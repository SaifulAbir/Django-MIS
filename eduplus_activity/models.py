from django.db import models

# Create your models here.
from django.utils import timezone

from accounts.models import User
from school.models import School
from skleaders.models import SkLeaderProfile
from topics.models import Topics

class EduplusTopics(models.Model):
    name= models.CharField(max_length=128, unique=True)
    created_date = models.DateTimeField(default=timezone.now)
    objects = models.Manager

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_date']

class EduPlusActivity(models.Model):
    date = models.DateField(default=timezone.now)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    presence_skleader = models.BooleanField(default=False)
    skleader = models.ForeignKey(SkLeaderProfile, on_delete=models.CASCADE, null=True)
    attendance= models.ManyToManyField(User, related_name='member_profile')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    topics = models.ManyToManyField(Topics)
    method = models.ForeignKey(EduplusTopics, on_delete=models.CASCADE)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.school + " on "+self.date

    class Meta:
        ordering = ['-date']
