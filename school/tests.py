from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from django.utils import timezone
from.models import School, Division, District , Upazilla, Union

class SchoolTest(TestCase):
    def setUp(self):
        s1 = Division(name='Dhaka')
        s1.save()
        self.division = s1

        s2 = District(division=self.division, name='Gazipur')
        s2.save()
        self.district = s2

        s3 = Upazilla(division=self.division, district=self.district, name='Sripur')
        s3.save()
        self.upazilla = s3

        s4 = Union(division=self.division, district=self.district,upazilla=self.upazilla, name= 'Dholapur')
        s4.save()
        self.union = s4

    def test__when_school_name_is_null__should_raise_error(self):
        s = School(school_id = 123)
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_school_name_is_empty__should_raise_error(self):
        s = School( name='', school_id = 123)
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_school_id_is_null__should_raise_error(self):
        s = School(name = 'Mirpur School')
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_school_id_is_empty__should_raise_error(self):
        s = School( name='Mirpur School', school_id = '')
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_school_name_is_duplicate__should_raise_error(self):
        sl1 = School( name='Mirpur School', school_id = 123)
        sl2 = School( name='Mirpur School', school_id = 12)
        with self.assertRaises(IntegrityError):
            sl1.save()
            sl2.save()









