from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone
import class_orientation.strings as peer_education_strings
from school.models import School
from topics.models import Topics

place_choice=(
    ('1', 'Class'),
    ('2', 'Community'),
)

class PeerEducation(models.Model):
    created_date = models.DateField(default=timezone.now)
    place = models.CharField(max_length=10, choices=place_choice, default='')
    topic = models.ManyToManyField(Topics)
    school = models.ForeignKey(School, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.created_date

    def get_absolute_url(self):
        return reverse('peer_education:peer_education_list')

    class Meta:
        ordering = ['-created_date']
        verbose_name = peer_education_strings.PEER_EDUCATION_VERBOSE_NAME
        verbose_name_plural = peer_education_strings.PEER_EDUCATION_VERBOSE_NAME_PLURAL
        db_table = 'peer_educations'
