from django.db import models

# Create your models here.
from django.utils import timezone
import eduplus_activity.strings as eduplus_activity_strings
from accounts.models import User
from school.models import School
from skleaders.models import SkLeaderProfile
from topics.models import Topics

class Method(models.Model):
    name= models.CharField(max_length=128, unique=True)
    created_date = models.DateTimeField(default=timezone.now)
    objects = models.Manager

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_date']
        verbose_name = eduplus_activity_strings.METHOD_VERBOSE_NAME
        verbose_name_plural = eduplus_activity_strings.METHOD_ACTIVITY_VERBOSE_NAME_PLURAL
        db_table = 'methods'

class EduPlusActivity(models.Model):
    date = models.DateField(default=timezone.now)
    school = models.ForeignKey(School, on_delete=models.PROTECT, null=True)
    presence_skleader = models.BooleanField(default=False)
    skleader = models.ForeignKey(SkLeaderProfile, on_delete=models.PROTECT, null=True)
    attendance= models.ManyToManyField(User, related_name='member_profile')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    topics = models.ManyToManyField(Topics)
    method = models.ForeignKey(Method, on_delete=models.PROTECT)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.school

    class Meta:
        ordering = ['-date']
        verbose_name = eduplus_activity_strings.EDUPLUS_ACTIVITY_VERBOSE_NAME
        verbose_name_plural = eduplus_activity_strings.EDUPLUS_ACTIVITY_VERBOSE_NAME_PLURAL
        db_table = 'eduplus_activities'
