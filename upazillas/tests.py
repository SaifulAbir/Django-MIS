from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.utils import timezone

from districts.models import District
from division.models import Division
from .forms import UpazillaForm
from .models import Upazilla


class UpazillaTest(TestCase):

    def create_division(self, name="Dhaka"):
        return Division.objects.create(name=name, created_date=timezone.now())

    def create_district(self, division, name="Lakshmipur"):
        return District.objects.create(division=division, name=name, created_date=timezone.now())

    def create_upazilla(self, division, district, name="Kamalnagar"):
        return Upazilla.objects.create(division=division, district = district, name=name, created_date=timezone.now())

    # models
    def testUpazilla_whenContentIsCorrect_shouldCreateObject(self):
        division = self.create_division()
        district = self.create_district(division = division)
        upazilla = self.create_upazilla(division = division, district = district)
        actual = upazilla.__str__()
        expected = upazilla.name
        self.assertTrue(isinstance(upazilla, Upazilla))
        self.assertEqual(actual, expected)

    # views
    # Valid Data
    def testUpazilla_create_View_whenValidData_shouldResponse200(self):
        division = self.create_division()
        district = self.create_district(division=division)
        response = self.client.post(reverse('upazillas:create_upazilla'),
                                    {'division': division, 'district':district, 'name': "Kamalnagar", 'created_date': timezone.now()})
        actual = response.status_code
        expected = 200
        self.assertEqual(actual, expected)

    # Valid Form Data
    def testUpazillaForm_whenValidData_shouldReturnTrue(self):
        division = self.create_division()
        district = self.create_district(division=division)
        form = UpazillaForm(data={'division': str(division.id), 'district': str(district.id), 'name': "Lakshmipur"})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def testUpazillaForm_whenInValidData_shouldReturnFalse(self):
        division = self.create_division()
        district = self.create_district(division=division)
        form = UpazillaForm(data={'division': str(division.id), 'district': str(district.id), 'name': ""})
        self.assertFalse(form.is_valid())


