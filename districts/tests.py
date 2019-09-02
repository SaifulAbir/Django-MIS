from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.utils import timezone
from .forms import DistrictForm
from .models import District, Division


class DistrictTest(TestCase):

    def create_division(self, name="Dhaka"):
        return Division.objects.create(name=name, created_date=timezone.now())

    def create_district(self, division, name="Lakshmipur"):
        return District.objects.create(division=division, name=name, created_date=timezone.now())

    # models
    def testDistrict_whenContentIsCorrect_shouldCreateObject(self):
        division = self.create_division()
        district = self.create_district(division = division)
        actual = district.__str__()
        expected = district.name
        self.assertTrue(isinstance(district, District))
        self.assertEqual(actual, expected)

    # views
    # Valid Data
    def testDistrict_create_View_whenValidData_shouldResponse200(self):
        division = self.create_division()
        response = self.client.post(reverse('districts:create_district'),
                                    {'division': division, 'name': "Lakshmipur", 'created_date': timezone.now()})
        actual = response.status_code
        expected = 200
        self.assertEqual(actual, expected)

    # Valid Form Data
    def testDistrictForm_whenValidData_shouldReturnTrue(self):
        division = self.create_division()
        form = DistrictForm(data={'division': str(division.id), 'name': "Lakshmipur"})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def testDistrictForm_whenInValidData_shouldReturnFalse(self):
        division = self.create_division()
        form = DistrictForm(data={'division': str(division.id), 'name': ""})
        self.assertFalse(form.is_valid())

