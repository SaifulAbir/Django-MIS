from django.db import models
from django.utils import timezone
from topics.models import Topics
from skmembers.models import SkMemberProfile

# Create your models here.

class ClubMeetings(models.Model):
    date = models.DateField(default=timezone.now)
    class_room= models.CharField(max_length=100)
    presence_guide_teacher = models.BooleanField(default=False)
    #attendance= models.ForeignKey(SkMemberProfile,on_delete=models.CASCADE(), blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.class_room

    class Meta:
        ordering = ['-date']

class MeetingTopics(models.Model):
    club_meeting = models.ForeignKey(ClubMeetings, on_delete=models.CASCADE)
    topics = models.ManyToManyField(Topics)





