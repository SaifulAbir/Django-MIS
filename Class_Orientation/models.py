from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone



class Class_Orientation(models.Model):
    name = models.CharField(max_length=128 )
    class_no= models.CharField(max_length=128)
    from_date = models.DateField(null=False, default=timezone.now)
    to_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_date']
