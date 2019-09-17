from django.db import models

# Create your models here.
from accounts.models import User
from school.models import School


class SkLeaderProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='skleader_profile')
    mobile = models.CharField(max_length=11)
    student_class = models.CharField(max_length=128)
    roll = models.CharField(max_length=128)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.user.first_name
