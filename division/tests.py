from django.test import TestCase

# Create your tests here.
from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.utils import timezone
from .forms import DivisionForm
from .models import Division


class DivisionTest(TestCase):

    def create_division(self, name="Dhaka"):
        return Division.objects.create(name=name, created_date=timezone.now())

    # def create_division(self, division, name="Lakshmipur"):
    #     return District.objects.create(division=division, name=name, created_date=timezone.now())

    # models
    def testDivision_whenContentIsCorrect_shouldCreateObject(self):
        division = self.create_division()
        # division = self.create_division(division = division)
        actual = division.__str__()
        expected = division.name
        self.assertTrue(isinstance(division, Division))
        self.assertEqual(actual, expected)

    # views
    # Valid Data
    def testDivision_create_View_whenValidData_shouldResponse200(self):
        division = self.create_division()
        response = self.client.post(reverse('division:create_division'),
                                    {'division': division, 'name': "Dhaka", 'created_date': timezone.now()})
        actual = response.status_code
        expected = 200
        self.assertEqual(actual, expected)

    # Valid Form Data
    def testDivisionForm_whenValidData_shouldReturnTrue(self):
        division = self.create_division()
        form = DivisionForm(data={'division': str(division.id), 'name': "Dhaka"})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def testDivisionForm_whenInValidData_shouldReturnFalse(self):
        division = self.create_division()
        form = DivisionForm(data={'division': str(division.id), 'name': ""})
        self.assertFalse(form.is_valid())
