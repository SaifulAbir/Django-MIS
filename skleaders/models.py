from django.db import models

# Create your models here.
from django.utils import timezone
from . import strings
from accounts.models import User
from school.models import School

class_choice=(
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ("10", '10'),
)
GENDER_CHOICES = (
        ('', '--Select--'),
        ('M', strings.MALE),
        ('F', strings.FEMALE),
    )
class SkLeaderProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='skleader_profile')


    mobile = models.CharField(max_length=20, unique=True)

    student_class = models.CharField(max_length=10,choices=class_choice, blank=True, null=True)
    roll = models.CharField(max_length=128, blank=True, null=True)
    school = models.ForeignKey(School, on_delete=models.PROTECT, null=True)
    emergency_contact_person = models.CharField(max_length=200, blank=True, null=True)
    emergency_contact_number = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    joining_date = models.DateField(null=False, blank=False, default=timezone.now)

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = strings.SK_LEADER_VERBOSE_NAME
        verbose_name_plural = strings.SK_LEADER_VERBOSE_NAME_PLURAL
        db_table = 'skleader_profiles'

class SkleaderDetails(models.Model):
    school = models.ForeignKey(School, on_delete=models.PROTECT, blank=False, null=False)
    skleader = models.ForeignKey(SkLeaderProfile, on_delete=models.PROTECT, blank=False, null=False)
    from_date = models.DateField(null=False, default=timezone.now)
    to_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = strings.SK_LEADER_DETAILS_VERBOSE_NAME
        verbose_name_plural = strings.SK_LEADER_DETAILS_VERBOSE_NAME_PLURAL
        db_table = 'skleader_profile_details'



