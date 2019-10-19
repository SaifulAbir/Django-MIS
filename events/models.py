from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from django.utils import timezone



class Event(models.Model):
    title = models.CharField(max_length=128, null=False)
    start_date = models.DateTimeField(default=timezone.now, null=False)
    end_date = models.DateTimeField(default=timezone.now, null=False)

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError("Dates are incorrect")

    def __str__(self):
        return self.title
