from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class Class_Orientation(models.Model):
    topic = models.CharField(max_length=128)
    class_name =models.CharField(max_length=128)
    from_date = models.DateField(null=False, default=timezone.now)
    created_date = models.DateTimeField(default=timezone.now)

    objects = models.Manager

    def __str__(self):
        return self.topic

    class Meta:
        ordering = ['-created_date']