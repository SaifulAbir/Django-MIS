from django.db import models
from . import strings as headmaster_strings
from accounts.models import User
from school.models import School
from django.utils import timezone

class HeadmasterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='headmaster_profile')
    mobile = models.CharField(max_length=15, unique=True)
    school = models.ForeignKey(School, on_delete=models.PROTECT, null=True)
    image = models.ImageField(upload_to='images/')
    joining_date = models.DateField(null=False, default=timezone.now)

    def __str__(self):
        return self.user.first_name
    class Meta:
        verbose_name = headmaster_strings.HEADMASTER_VERBOSE_NAME
        verbose_name_plural = headmaster_strings.HEADMASTER_VERBOSE_NAME_PLURAL
        db_table = 'headmaster_profiles'

class HeadmasterDetails(models.Model):
    school = models.ForeignKey(School, on_delete=models.PROTECT, blank=False, null=False)
    headmaster = models.ForeignKey(HeadmasterProfile, on_delete=models.PROTECT, blank=False, null=False)
    from_date = models.DateField(null=False, default=timezone.now)
    to_date = models.DateField(blank=True, null=True,)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = headmaster_strings.HEADMASTER_DETAIL_VERBOSE_NAME
        verbose_name_plural = headmaster_strings.HEADMASTER_DETAIL_VERBOSE_NAME_PLURAL
        db_table = 'headmaster_profile_details'



