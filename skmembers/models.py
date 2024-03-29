from django.db import models
from django.utils import timezone
# Create your models here.
from accounts.models import User
from school.models import School
from skleaders.models import GENDER_CHOICES
from . import strings as sk_strings
class_choice=(
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ("10", '10'),

)

class SkMemberProfile(models.Model):
    name = models.CharField((sk_strings.USER_NAME_TEXT), max_length=40)
    email = models.CharField((sk_strings.USER_EMAIL_TEXT), max_length=254, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    student_class = models.CharField(max_length=10, choices=class_choice, blank=True, null=True)
    roll = models.CharField(max_length=128, blank=True, null=True)
    school = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    joining_date = models.DateField(null=False, blank=False, default=timezone.now)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = sk_strings.SKMEMBER_VERBOSE_NAME
        verbose_name_plural = sk_strings.SKMEMBER_VERBOSE_NAME_PLURAL
        db_table = 'skmember_profiles'
class SkmemberDetails(models.Model):
    school = models.ForeignKey(School, on_delete=models.PROTECT, blank=False, null=False)
    skmember = models.ForeignKey(SkMemberProfile, on_delete=models.PROTECT, blank=False, null=False)
    from_date = models.DateField(null=False, default=timezone.now)
    to_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = sk_strings.SKMEMBER_DETAIL_VERBOSE_NAME
        verbose_name_plural = sk_strings.SKMEMBER_DETAIL_VERBOSE_NAME_PLURAL
        db_table = 'skmember_profile_details'