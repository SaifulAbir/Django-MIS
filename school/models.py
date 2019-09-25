from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone

from districts.models import District
from division.models import Division
from unions.models import Union
from upazillas.models import Upazilla


class School(models.Model):
    name = models.CharField(max_length=264)
    school_id = models.CharField(max_length=255, unique=True, blank=True, null=True)
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    upazilla = models.ForeignKey(Upazilla, on_delete=models.SET_NULL, blank=True, null=True)
    union = models.ForeignKey(Union, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.TextField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('school:school_list')

    class Meta:
        ordering = ['-created_date']

