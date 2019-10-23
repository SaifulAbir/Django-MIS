from django.db import models
from django.utils import timezone

from accounts.models import User
from school.models import School
from topics.models import Topics
from skmembers.models import SkMemberProfile

# Create your models here.

class ClubMeetings(models.Model):
    date = models.DateField(default=timezone.now)
    class_room= models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    presence_guide_teacher = models.BooleanField(default=False)
    presence_skleader = models.BooleanField(default=False)
    attendance= models.ManyToManyField(User, related_name='a_profile')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    topics = models.ManyToManyField(Topics)

    def __str__(self):
        return self.class_room

    class Meta:
        ordering = ['-date']

    # class MeetingTopics(models.Model):
    #     club_meeting = models.ForeignKey(ClubMeetings, on_delete=models.CASCADE)
    #     topics = models.ManyToManyField(Topics)





