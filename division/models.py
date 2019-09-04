from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class Division(models.Model):
    name = models.CharField(max_length=128)
    created_date = models.DateTimeField(default=timezone.now)

    objects = models.Manager

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_date']
