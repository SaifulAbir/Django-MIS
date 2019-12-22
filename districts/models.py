from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone

from division.models import Division
from resources import strings


class District(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='districts')
    name = models.CharField(max_length=128 )
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super(District, self).__init__(*args, **kwargs)
        self._meta.get_field('name').verbose_name = strings.DISTRICT_NAME
        self._meta.get_field('division').verbose_name = strings.DIVISION_NAME


    class Meta:
        ordering = ['-created_date']
        unique_together = ['division', 'name']

        verbose_name = strings.DISTRICTS_VERBOSE_NAME
        verbose_name_plural = strings.DISTRICTS_VERBOSE_NAME_PLURAL
        db_table = 'districts'


