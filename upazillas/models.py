from django.db import models

# Create your models here.
from django.utils import timezone
from sknf.validators import *
from districts.models import District
from division.models import Division
from resources import strings


class Upazilla(models.Model):
    division = models.ForeignKey(Division, on_delete=models.PROTECT, null=True)
    district = models.ForeignKey(District, on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=100, validators=[check_valid_chars])
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ['division','district','name']
        verbose_name = strings.UPAZILAS_VERBOSE_NAME
        verbose_name_plural = strings.UPAZILAS_VERBOSE_NAME_PLURAL
        db_table = 'upazilas'




