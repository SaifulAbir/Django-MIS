from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from django.utils import timezone
from .models import User

class UserTest(TestCase):
    def test__when_Every_field_is_valid___should_pass(self):
        time = timezone.now()
        s = User(image='1.jpg', email='A@g.com', password=123)
        try:
            s.full_clean()
        except:
            self.fail()

    def test__when_Email_field_is_null_will_raise__validation_error(self):
        s= User(image='1.jpg', password=123)

        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_Email_field_is_empty_will_raise__validation_error(self):
        s= User(image='1.jpg',email='', password=123)

        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_Password_field_is_null_will_raise__validation_error(self):
        s= User(image='1.jpg',email='a@g.com')

        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_Password_field_is_empty_will_raise__validation_error(self):
        s= User(image='1.jpg',email='a@g.com',password='')

        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_email_is_not_unique_should_raise__integrity_error(self):
        s1=User(image='1.jpg', email='A@g.com', password=123)
        s2=User(image='1.jpg', email='A@g.com', password=124)

        with self.assertRaises(IntegrityError):
            s1.save()
            s2.save()