from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.utils import timezone

from districts.models import District
from division.models import Division
from school.views import CreateSchool
from unions.models import Union
from upazillas.models import Upazilla
from .models import School


class DistrictTest(TestCase):

    def create_division(self, name="Dhaka"):
        return Division.objects.create(name=name, created_date=timezone.now())

    def create_district(self, division, name="Lakshmipur"):
        return District.objects.create(division=division, name=name, created_date=timezone.now())

    def create_upazilla(self, division, district, name="Kamalnagar"):
        return Upazilla.objects.create(division=division, district=district, name=name, created_date=timezone.now())

    def create_union(self, division, district, upazilla, name="Hazirhat"):
        return Union.objects.create(division=division, district=district, upazilla=upazilla, name=name, created_date=timezone.now())

    def create_school(self, division, district, upazilla, union, name = "New School", school_id = "45465676", address = "Dhaka, Bangladesh"):
        return School.objects.create(name=name, school_id=school_id, division=division, district=district, upazilla=upazilla, union=union, address=address)

    # models
    def testSchool_whenContentIsCorrect_shouldCreateObject(self):
        division = self.create_division()
        district = self.create_district(division = division)
        upazilla = self.create_upazilla(division = division, district = district)
        union = self.create_union(division = division, district = district, upazilla=upazilla)
        school = self.create_school(division = division, district = district, upazilla=upazilla, union = union)
        actual = school.__str__()
        expected = school.name
        self.assertTrue(isinstance(school, School))
        self.assertEqual(actual, expected)

    # views
    # Valid Data
    def testSchoolCreate_whenValidData_shouldCreateCorrect_object(self):
        school = School.objects.create()
        view = CreateSchool()
        view.kwargs = dict(pk=school.id)
        self.assertEqual(view.get_object(), school)




