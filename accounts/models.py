
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
import accounts.strings as account_strings


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, account_strings.USER_TYPE_ADMIN),
        (2, account_strings.USER_TYPE_HEADMASTER),
        (3, account_strings.USER_TYPE_MENTOR),
        (4, account_strings.USER_TYPE_HEADMASTER_MENTOR),
        (5, account_strings.USER_TYPE_SKLEADER),
        (6, account_strings.USER_TYPE_SKMEMBER),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=6)
    image = models.ImageField(upload_to=account_strings.USER_IMAGE_TEXT, default='')
    username = models.CharField(max_length=150, unique=True)
    email_verifiaction_code = models.CharField(max_length=100, null=True, blank=True, default='')
    email_verified = models.CharField(max_length=1, null=True, blank=True, default=0)
    email = models.CharField(_(account_strings.USER_EMAIL_TEXT), unique=True, max_length=254 )  # changes email to unique and blank to false
    first_name = models.CharField(_(account_strings.USER_FIRST_NAME_TEXT), max_length=40, blank=True)
    EMAIL_FIELD = account_strings.EMAIL_FIELD_TEXT
    USERNAME_FIELD = account_strings.USERNAME_FIELD_TEXT
    REQUIRED_FIELDS = ['email']  # removes email from REQUIRED_FIELDS

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

    class Meta:
        verbose_name = account_strings.USERS_VERBOSE_NAME
        verbose_name_plural = account_strings.USERS_VERBOSE_NAME_PLURAL
        db_table = 'users'

