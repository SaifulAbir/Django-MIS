from django.db import models

from accounts.models import User
from school.models import School
from django.utils import timezone

class HeadmasterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='headmaster_profile')
    mobile = models.CharField(max_length=11)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/')
    joining_date = models.DateField(null=False, default=timezone.now)

    def __str__(self):
        return self.user.first_name

class HeadmasterDetails(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=False)
    headmaster = models.ForeignKey(HeadmasterProfile, on_delete=models.CASCADE, blank=False, null=False)
    from_date = models.DateField(null=False, default=timezone.now)
    to_date = models.DateField(blank=True, null=True,)
    created_date = models.DateTimeField(auto_now_add=True)



