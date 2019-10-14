from django.test import TestCase

# Create your tests here.
from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.utils import timezone
from .forms import DivisionForm
from .models import Division


class DivisionTest(TestCase):

    def testDivision_whenNameIsNotGiven_shouldNotCreateObject(self):
        division = Division.objects.create()
        actual = division.__str__()
        expected = division.name
        self.assertTrue(isinstance(division, Division))
        self.assertEqual(actual, expected)

