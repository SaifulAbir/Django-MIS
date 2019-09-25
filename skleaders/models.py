from django.db import models

# Create your models here.
from django.utils import timezone

from accounts.models import User
from school.models import School

class_choice=(
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ("10", '10'),

)
class SkLeaderProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='skleader_profile')
    mobile = models.CharField(max_length=11)
    student_class = models.CharField(max_length=128, choices=class_choice)
    roll = models.CharField(max_length=128)
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null=True)

    image = models.ImageField(upload_to='images/')
    joining_date = models.DateField(null=False, blank=False, default=timezone.now)

    def __str__(self):
        return self.user.first_name

class SkleaderDetails(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=False)
    skleader = models.ForeignKey(SkLeaderProfile, on_delete=models.CASCADE, blank=False, null=False)
    from_date = models.DateField(null=False, default=timezone.now)
    to_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)



