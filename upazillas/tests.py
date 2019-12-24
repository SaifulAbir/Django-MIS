from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from django.utils import timezone

from resources import strings
from .models import Division,District,Upazilla
from sknf.validators import check_valid_chars

class UpazillaTest(TestCase):

    def setUp(self):
        s1 = Division(name=strings.DIVISION_NAME_TEST)
        s1.save()
        self.division = s1

        s2 = District(division=self.division, name=strings.DISTRICT_NAME_TEST)
        s2.save()
        self.district = s2

    def test__when_name_is_null__should_raise_error(self):
        s = Upazilla(division=self.division,district=self.district, created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_Division_is_null__should_raise_error(self):
        s = Upazilla(district=self.district, name=strings.UPAZILA_NAME_TEST, created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_District_is_null__should_raise_error(self):
        s = Upazilla(division=self.division, name=strings.UPAZILA_NAME_TEST, created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_name_is_empty__should_raise_error(self):
        s = Upazilla(division=self.division,district=self.district, name='', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__Unique_together_validation_is__added(self):
        unique_together = Upazilla._meta.unique_together
        self.assertEquals(unique_together, (('division', 'district', 'name'),))

    def test__when__division_district_and_upazila_is_not_unique_together_should_raise_error(self):
        s = Upazilla(division=self.division, district=self.district,name=strings.UPAZILA_NAME_TEST, created_date=timezone.now())
        s1 = Upazilla(division=self.division, district=self.district,name=strings.UPAZILA_NAME_TEST, created_date=timezone.now())
        with self.assertRaises(IntegrityError):
            s.save()
            s1.save()

    def test__max_length_validation_is__added(self):
        max_length = Upazilla._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test__name_is_greater_then_100_character__should_raise_error(self):
        s = Upazilla(
            division=self.division,district=self.district,
            name=strings.EXCEEDING_LENGTH_TEST, created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()