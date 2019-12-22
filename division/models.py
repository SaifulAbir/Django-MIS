from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone

from resources import strings
from sknf.validators import *


class Division(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False, validators=[check_valid_chars],)
    created_date = models.DateTimeField(default=timezone.now)
    objects = models.Manager

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super(Division, self).__init__(*args, **kwargs)
        self._meta.get_field('name').verbose_name = strings.DIVISION_NAME

    class Meta:
        ordering = ['-created_date']
        verbose_name = strings.DISTRICTS_VERBOSE_NAME
        verbose_name_plural = strings.DISTRICTS_VERBOSE_NAME_PLURAL
        db_table = 'divisions'