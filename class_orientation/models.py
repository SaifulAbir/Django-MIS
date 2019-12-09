from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone

from school.models import School
from topics.models import Topics

place_choice=(
    ('1', 'Class'),
    ('2', 'Community'),
)

class ClassOrientation(models.Model):
    created_date = models.DateField(default=timezone.now)
    place = models.CharField(max_length=10, choices=place_choice, default='')
    topic = models.ManyToManyField(Topics)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.topic.created_date

    def get_absolute_url(self):
        return reverse('class_orientation:class_orientation_list')

    class Meta:
        ordering = ['-created_date']
