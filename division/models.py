from django.db import models

class Division_name(models.Model):
    Division = models.CharField(max_length = 150)


    objects  = models.Manager

    def __str__(self):
        return self.Division