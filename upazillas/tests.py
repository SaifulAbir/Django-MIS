from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from django.utils import timezone
from .models import Division,District,Upazilla
from sknf.validators import check_valid_chars

class UpazillaTest(TestCase):

    def setUp(self):
        s1 = Division(name='Dhaka')
        s1.save()
        self.division = s1

        s2 = District(division=self.division, name='Gazipur')
        s2.save()
        self.district = s2

    def test__when_name_is_null__should_raise_error(self):
        s = Upazilla(division=self.division,district=self.district, created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_Division_is_null__should_raise_error(self):
        s = Upazilla(district=self.district, name='Doulotpur', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_District_is_null__should_raise_error(self):
        s = Upazilla(division=self.division, name='Doulotpur', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_name_is_empty__should_raise_error(self):
        s = Upazilla(division=self.division,district=self.district, name='', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_name_is_duplicate__should_raise_error(self):
        s = Upazilla(division=self.division,district=self.district, name='Doulotpur',created_date=timezone.now())
        s1 = Upazilla(division=self.division,district=self.district, name='Dulotpur',created_date=timezone.now())
        with self.assertRaises(IntegrityError):
            s.save()
            s1.save()

    def test__max_length_validation_is__added(self):
        max_length = Upazilla._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test__name_is_greater_then_100_character__should_raise_error(self):
        s = Upazilla(
            division=self.division,district=self.district,
            name="tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft"
                 " tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg"
                 " sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg"
                 " sdfgsdg sgddft sdfgsdg sgddft tesg"
                 " sdfgsdg sgddft sdfgsdg sgddft tesg"
                 " sdfgsdg sgddft ", created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()