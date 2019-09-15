from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.



class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'student'),
        (2, 'teacher'),
        (3, 'secretary'),
        (4, 'supervisor'),
        (5, 'admin'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)

