from django.db import models
from django.utils import timezone
# Create your models here.
from accounts.models import User
from school.models import School
from skleaders.models import GENDER_CHOICES

class_choice=(
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ("10", '10'),

)

class SkMemberProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='skmember_profile')
    mobile = models.CharField(max_length=11)
    student_class = models.CharField(max_length=10, choices=class_choice)
    roll = models.CharField(max_length=128)
    school = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    joining_date = models.DateField(null=False, blank=False, default=timezone.now)

    def __str__(self):
        return self.user.first_name
class SkmemberDetails(models.Model):
    school = models.ForeignKey(School, on_delete=models.PROTECT, blank=False, null=False)
    skmember = models.ForeignKey(SkMemberProfile, on_delete=models.PROTECT, blank=False, null=False)
    from_date = models.DateField(null=False, default=timezone.now)
    to_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)