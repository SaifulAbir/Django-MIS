from django.db import models

# Create your models here.
from django.utils import timezone

from districts.models import District
from division.models import Division


class Upazilla(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


