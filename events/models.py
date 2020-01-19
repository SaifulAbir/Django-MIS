from django.core.exceptions import ValidationError
from django.db import models
import events.strings as event_strings
# Create your models here.
from django.utils import timezone



class Event(models.Model):
    title = models.CharField(max_length=128, null=False)
    start_date = models.DateTimeField(default=timezone.now, null=False)
    end_date = models.DateTimeField(default=timezone.now, null=False)

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError(event_strings.EVENT_DATE_ERROR_MSG)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = event_strings.EVENT_VERBOSE_NAME
        verbose_name_plural = event_strings.EVENT_VERBOSE_NAME_PLURAL
        db_table = 'events'
