from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone
from sknf.validators import no_future
from districts.models import District
from division.models import Division
from unions.models import Union
from upazillas.models import Upazilla
import school.strings as school_strings

class School(models.Model):
    name = models.CharField(max_length=264 )
    school_id = models.CharField(max_length=255, unique=True, blank=False, null=False)
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    upazilla = models.ForeignKey(Upazilla, on_delete=models.SET_NULL, blank=True, null=True)
    union = models.ForeignKey(Union, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.TextField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    club_establishment_date = models.DateField(blank=True, null=True,validators=[no_future])
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return  self.name + ' (' +self.school_id + ')'

    def get_absolute_url(self):
        return reverse('school:school_list')

    class Meta:
        ordering = ['-created_date']
        verbose_name = school_strings.SCHOOL_VERBOSE_NAME
        verbose_name_plural = school_strings.SCHOOL_VERBOSE_NAME_PLURAL
        db_table = 'schools'



class SchoolPost(models.Model):
    school = models.ForeignKey(School, on_delete=models.PROTECT, blank=False, null=False)
    text = models.TextField(max_length=264)
    post_image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']
        verbose_name = school_strings.SCHOOL_POST_VERBOSE_NAME
        verbose_name_plural = school_strings.SCHOOL_POST_VERBOSE_NAME_PLURAL
        db_table = 'school_posts'

