from django.db import models

# Create your models here.
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=128, null=False)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
