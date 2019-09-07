from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.utils import timezone

from districts.models import District
from division.models import Division
from upazillas.models import Upazilla
from .forms import UnionForm
from .models import Union


class UpazillaTest(TestCase):

    def create_division(self, name="Dhaka"):
        return Division.objects.create(name=name, created_date=timezone.now())

    def create_district(self, division, name="Lakshmipur"):
        return District.objects.create(division=division, name=name, created_date=timezone.now())

    def create_upazilla(self, division, district, name="Kamalnagar"):
        return Upazilla.objects.create(division=division, district = district, name=name, created_date=timezone.now())

    def create_union(self, division, district, upazilla, name="Hazirhat"):
        return Union.objects.create(division=division, district=district, upazilla=upazilla, name=name,
                                    created_date=timezone.now())

    # models
    def testUpazilla_whenContentIsCorrect_shouldCreateObject(self):
        division = self.create_division()
        district = self.create_district(division = division)
        upazilla = self.create_upazilla(division = division, district = district)
        union = self.create_union(division=division, district=district, upazilla=upazilla)
        actual = union.__str__()
        expected = union.name
        self.assertTrue(isinstance(union, Union))
        self.assertEqual(actual, expected)

    # views
    # Valid Data
    def testUnion_create_View_whenValidData_shouldResponse200(self):
        division = self.create_division()
        district = self.create_district(division=division)
        upazilla = self.create_upazilla(division=division, district=district)

        response = self.client.post(reverse('uinons:create_union'),
                                    {'division': division, 'district':district, 'upazilla': upazilla,'name': "Hazirhat", 'created_date': timezone.now()})
        actual = response.status_code
        expected = 200
        self.assertEqual(actual, expected)

    # Valid Form Data
    def testUionForm_whenValidData_shouldReturnTrue(self):
        division = self.create_division()
        district = self.create_district(division=division)
        form = UpazillaForm(data={'division': str(division.id), 'district': str(district.id), 'name': "Lakshmipur"})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def testUnionForm_whenInValidData_shouldReturnFalse(self):
        division = self.create_division()
        district = self.create_district(division=division)
        form = UpazillaForm(data={'division': str(division.id), 'district': str(district.id), 'name': ""})
        self.assertFalse(form.is_valid())