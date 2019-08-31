from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class Division(models.Model):
    name = models.CharField(max_length=128)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class District(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='districts')
    name = models.CharField(max_length=128)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('districts:district_list')

    class Meta:
        ordering = ['-created_date']


