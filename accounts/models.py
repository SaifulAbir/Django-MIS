
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'admin'),
        (2, 'headmaster'),
        (3, 'mentor'),
        (4, 'headmaster_mentor'),
        (5, 'skLeader'),
        (6, 'skMember'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=6)
    image = models.ImageField(upload_to='images/', default='')
    username = None
    email = models.EmailField(_('email address'), unique=True )  # changes email to unique and blank to false
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # removes email from REQUIRED_FIELDS

    objects = UserManager()


    @property
    def is_admin(self):
        if self.user_type == 1:
            return True
        else:
            return False

    @property
    def is_headmaster(self):
        if self.user_type == 2:
            return True
        else:
            return False

    @property
    def is_mentor(self):
        if self.user_type == 3:
            return True
        else:
            return False

    @property
    def is_skleader(self):
        if self.user_type == 5:
            return True
        else:
            return False

    @property
    def is_headmaster_or_mentor_or_skleader_or_both(self):
        if self.user_type == 2 or self.user_type == 3 or self.user_type == 4 or self.user_type == 5:
            return True
        else:
            return False


    def __str__(self):
        return self.first_name

