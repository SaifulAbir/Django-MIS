from django.db import models
from django.utils import timezone

# Create your models here.
class Topics(models.Model):
    name= models.CharField(max_length=128, unique=True)
    created_date = models.DateTimeField(default=timezone.now)
    objects = models.Manager

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_date']
