from django.db import models
from django.utils import timezone

from accounts.models import User
from school.models import School
from skleaders.models import SkLeaderProfile
from topics.models import Topics
from skmembers.models import SkMemberProfile
import club_meetings.strings as club_meeting_strings
# Create your models here.

class ClubMeetings(models.Model):
    date = models.DateField(default=timezone.now)
    class_room= models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.PROTECT, null=True)
    presence_guide_teacher = models.BooleanField(default=False)
    presence_skleader = models.BooleanField(default=False)
    skleader = models.ForeignKey(SkLeaderProfile, on_delete=models.PROTECT, null=True)
    attendance= models.ManyToManyField(User, related_name='a_profile')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    topics = models.ManyToManyField(Topics)

    def __str__(self):
        return self.class_room

    class Meta:
        ordering = ['-date']
        verbose_name = club_meeting_strings.CLUB_MEETING_VERBOSE_NAME
        verbose_name_plural = club_meeting_strings.CLUB_MEETING_VERBOSE_NAME_PLURAL
        db_table = 'club_meetings'





