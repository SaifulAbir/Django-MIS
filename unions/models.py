from django.db import models

# Create your models here.
from django.utils import timezone
from sknf.validators import check_valid_chars
from districts.models import District
from division.models import Division
from upazillas.models import Upazilla


class Union(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    upazilla = models.ForeignKey(Upazilla, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100,validators=[check_valid_chars])
    created_date = models.DateTimeField(default=timezone.now)

    objects = models.Manager

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_date']
        unique_together = ['division', 'district','upazilla', 'name']