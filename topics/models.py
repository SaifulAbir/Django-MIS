from django.db import models
from django.utils import timezone
import topics.strings as topic_strings
# Create your models here.
class Topics(models.Model):
    name= models.CharField(max_length=128, unique=True)
    created_date = models.DateTimeField(default=timezone.now)
    objects = models.Manager

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_date']
        verbose_name = topic_strings.TOPICS_VERBOSE_NAME
        verbose_name_plural = topic_strings.TOPICS_VERBOSE_NAME_PLURAL
        db_table = 'topics'
